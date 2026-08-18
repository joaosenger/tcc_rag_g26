from pathlib import Path

import pytest

from app.ingestion.markdown import MarkdownExtractionError, extract_markdown


def write(tmp_path: Path, content: str) -> Path:
    path = tmp_path / "doc.md"
    path.write_text(content, encoding="utf-8")
    return path


def test_sections_hierarchy(tmp_path):
    path = write(
        tmp_path,
        """# Machine Learning

Intro geral.

## Supervised Learning

Conteúdo supervisionado.

### Classification

Conteúdo de classificação.
""",
    )
    blocks = extract_markdown(path)
    sections = [b["metadata"]["section"] for b in blocks]
    assert sections == [
        "Machine Learning",
        "Machine Learning > Supervised Learning",
        "Machine Learning > Supervised Learning > Classification",
    ]
    assert blocks[0]["content"] == "Intro geral."
    assert blocks[2]["content"] == "Conteúdo de classificação."


def test_no_headings_single_root_block(tmp_path):
    path = write(tmp_path, "Texto solto sem estrutura.\nSegunda linha.\n")
    blocks = extract_markdown(path)
    assert len(blocks) == 1
    assert blocks[0]["metadata"]["section"] == "raiz"


def test_frontmatter_title_preserved(tmp_path):
    path = write(
        tmp_path,
        """---
title: Configurando o ambiente
description: Instalação de dependências
---

# Seção

Conteúdo.
""",
    )
    blocks = extract_markdown(path)
    assert blocks[0]["metadata"]["title"] == "Configurando o ambiente"
    assert "title:" not in blocks[0]["content"]
    assert "Configurando o ambiente" not in blocks[0]["content"]


def test_jinja_syntax_removed(tmp_path):
    path = write(
        tmp_path,
        """# Aula

{% set aula = "01" %}
{% include "templates/cabecalho.md" %}

Conteúdo real {{ variavel }} da aula.
""",
    )
    blocks = extract_markdown(path)
    joined = " ".join(b["content"] for b in blocks)
    assert "{%" not in joined
    assert "{{" not in joined
    assert "Conteúdo real" in joined and "da aula." in joined


def test_section_stack_resets_on_higher_level(tmp_path):
    path = write(
        tmp_path,
        """# A

a

## B

b

# C

c
""",
    )
    blocks = extract_markdown(path)
    sections = [b["metadata"]["section"] for b in blocks]
    assert sections == ["A", "A > B", "C"]


def test_missing_file_raises(tmp_path):
    with pytest.raises(MarkdownExtractionError):
        extract_markdown(tmp_path / "inexistente.md")
