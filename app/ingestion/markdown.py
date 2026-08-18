import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


class MarkdownExtractionError(Exception):
    pass


def _strip_frontmatter(text: str) -> tuple[str, dict]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return text, {}
    metadata: dict = {"title": None, "description": None}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep and key.strip() in metadata:
            metadata[key.strip()] = value.strip()
    return text[match.end() :], metadata


def _strip_jinja(text: str) -> str:
    cleaned = re.sub(r"\{%[+-]?.*?[+-]?%\}", "", text, flags=re.DOTALL)
    cleaned = re.sub(r"\{\{.*?\}\}", "", cleaned, flags=re.DOTALL)
    return cleaned


def extract_markdown(path: str | Path) -> list[dict]:
    """Extrai blocos de texto de um Markdown com caminho de seção hierárquico.

    Retorna lista de blocos no formato:
      {"content": str, "metadata": {"section": str, "title": str | None}}
    """
    source = Path(path)
    if not source.is_file():
        raise MarkdownExtractionError(f"arquivo não encontrado: {source}")

    try:
        raw = source.read_text(encoding="utf-8")
    except OSError as exc:
        raise MarkdownExtractionError(f"falha ao ler {source.name}") from exc

    body, frontmatter = _strip_frontmatter(raw)
    body = _strip_jinja(body)

    blocks: list[dict] = []
    section_stack: list[str] = []
    buffer: list[str] = []

    def flush():
        content = "\n".join(buffer).strip()
        buffer.clear()
        content = "\n".join(
            line for line in content.splitlines() if line.strip() != "---"
        ).strip()
        if content:
            blocks.append(
                {
                    "content": content,
                    "metadata": {
                        "section": " > ".join(section_stack) or "raiz",
                        "title": frontmatter.get("title"),
                    },
                }
            )

    for line in body.splitlines():
        heading = HEADING_RE.match(line)
        if heading:
            flush()
            level = len(heading.group(1))
            title = heading.group(2).strip()
            del section_stack[level - 1 :]
            section_stack.append(title)
        else:
            buffer.append(line)
    flush()
    return blocks


if __name__ == "__main__":
    import sys

    logging.basicConfig(level=logging.WARNING)
    for block in extract_markdown(sys.argv[1]):
        print(f"[{block['metadata']['section']}] {block['content'][:100]}")
