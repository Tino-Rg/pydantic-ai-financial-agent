from src.document import PDFProcessor

def test_pdf_extraction_success():

    url = "https://s206.q4cdn.com/479360582/files/doc_financials/2024/q4/2024q4-alphabet-earnings-release.pdf"
    processor = PDFProcessor(source=url)

    text = processor.extract_content()

    assert len(text) > 0, "The extracted text should not be empty."
    assert "Alphabet" in text, "The extracted text should contain the company name."