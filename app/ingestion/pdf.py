import logging
from pathlib import Path

from docling.datamodel.base_models import InputFormat
from docling.datamodel.document import ConversionResult
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.settings import settings as docling_settings

logger = logging.getLogger(__name__)


class PDFExtractionError(Exception):
    pass


def _build_converter(fast: bool = True) -> DocumentConverter:
    """Cria um DocumentConverter com opções de performance configuráveis.

    Args:
        fast: quando True, desabilita OCR e análise de tabelas, extraindo apenas
              o texto nativo do PDF. Isso é muito mais rápido para PDFs com
              texto selecionável.
    """
    if not fast:
        return DocumentConverter()

    # Importação tardia para não falhar se as classes mudarem de lugar.
    try:
        from docling.pipeline.standard_pdf_pipeline import StandardPdfPipeline
        from docling.datamodel.pipeline_options import PdfPipelineOptions

        pipeline_options = PdfPipelineOptions()
        pipeline_options.do_ocr = False
        pipeline_options.do_table_structure = False

        return DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_cls=StandardPdfPipeline,
                    pipeline_options=pipeline_options,
                )
            }
        )
    except Exception:
        logger.warning("Não foi possível configurar extração rápida; usando padrão.")
        return DocumentConverter()


def extract_pdf(path: str | Path, fast: bool = True) -> list[dict]:
    """Extrai blocos de texto de um PDF com página e título como metadados.

    Retorna lista de blocos no formato:
      {"content": str, "metadata": {"page": int, "heading": str | None}}

    Args:
        path: caminho do PDF.
        fast: se True, usa extração de texto nativo sem OCR/tabelas.
    """
    source = Path(path)
    if not source.is_file():
        raise PDFExtractionError(f"arquivo não encontrado: {source}")

    try:
        converter = _build_converter(fast=fast)
        result = converter.convert(source)
    except Exception as exc:
        logger.exception("falha ao extrair PDF %s", source)
        raise PDFExtractionError(f"falha na extração de {source.name}") from exc

    blocks: list[dict] = []
    current_heading: str | None = None
    for entry in result.document.iterate_items():
        item = entry[0] if isinstance(entry, tuple) else entry
        text = (getattr(item, "text", "") or "").strip()
        if not text:
            continue
        prov = getattr(item, "prov", None) or []
        page = getattr(prov[0], "page_no", None) if prov else None

        if type(item).__name__ == "SectionHeaderItem":
            current_heading = text

        blocks.append(
            {
                "content": text,
                "metadata": {"page": page, "heading": current_heading},
            }
        )
    return blocks


if __name__ == "__main__":
    import sys

    logging.basicConfig(level=logging.WARNING)
    for block in extract_pdf(sys.argv[1]):
        heading = block["metadata"]["heading"]
        prefix = f"[{heading}] " if heading else ""
        print(f"p.{block['metadata']['page']} {prefix}{block['content'][:100]}")
