from pathlib import Path

import pytest

from app.ingestion.pdf import PDFExtractionError, extract_pdf

FIXTURE = Path(__file__).parent / "fixtures" / "sample.pdf"


def test_extracts_text_with_page_metadata():
    blocks = extract_pdf(FIXTURE)
    assert len(blocks) >= 2
    joined = " ".join(b["content"] for b in blocks)
    assert "Overfitting ocorre" in joined
    assert "regularizacao" in joined.lower() or "Regularizacao" in joined
    for block in blocks:
        assert block["metadata"]["page"] in (1, 2)
        assert block["content"].strip()


def test_pages_are_preserved_not_flattened():
    blocks = extract_pdf(FIXTURE)
    pages = {b["metadata"]["page"] for b in blocks}
    assert 1 in pages


def test_missing_file_raises_specific_error(tmp_path):
    with pytest.raises(PDFExtractionError):
        extract_pdf(tmp_path / "inexistente.pdf")


def test_corrupted_pdf_raises_specific_error(tmp_path):
    bad = tmp_path / "corrompido.pdf"
    bad.write_bytes(b"isto nao e um pdf")
    with pytest.raises(PDFExtractionError):
        extract_pdf(bad)
