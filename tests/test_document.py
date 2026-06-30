"""
Tests for the PDF processing module.
Verifies the ability to download, read, and extract text from financial documents.
"""
from src.document import PDFProcessor


def test_pdf_extraction_success():
    """
    Tests the full extraction pipeline for a valid remote PDF URL.
    Ensures the extracted text is not empty and contains expected keywords 
    to validate the parsing logic.
    """
    url = "https://s206.q4cdn.com/479360582/files/doc_financials/2024/q4/2024q4-alphabet-earnings-release.pdf"
    processor = PDFProcessor(source=url)

    text = processor.extract_content()

    assert len(text) > 0, "The extracted text should not be empty."
    assert "Alphabet" in text, "The extracted text should contain the company name."