import os
from pathlib import Path
from urllib.parse import urlparse
import requests

class PDFProcessor:
    def __init__(self, source: str):
        """
        Initializes the processor with the document source (URL or local file path).
        """
        self.source = source

    def _is_url(self) -> bool:
        """
        Private method to determine if self.source is a valid URL.
        """

        return self.source.startswith(('http://', 'https://'))

    def _download(self) -> str:
        """
        Downloads the file from the URL and saves it in the data/downloads/ directory.
        Returns the absolute or relative local file path.
        """

        response = requests.get(self.source)
        response.raise_for_status()

        # Define the directory and create it if it doesn't exist
        download_dir = Path("data/downloads")
        download_dir.mkdir(parents=True, exist_ok=True)

        # Extract the filename from the URL
        # urlparse breaks down the URL, and os.path.basename gets the last part of the path
        parsed_url = urlparse(self.source)
        filename = os.path.basename(parsed_url.path)

        if not filename:
            filename = "default_document.pdf"
    
        file_path = download_dir / filename

        with open(file_path, "wb") as f:
            f.write(response.content)

        return str(file_path)

    def extract_content(self) -> str:
        """
        Main method:
        1. Handles file retrieval (calls _download if it's a URL).
        2. Extracts text from the PDF (e.g., using PyMuPDF / pymupdf4llm).
        3. Returns the extracted content.
        """
        pass

if __name__ == "__main__":
    # 1. The URL provided in your assignment
    test_url = "https://s206.q4cdn.com/479360582/files/doc_financials/2024/q4/2024q4-alphabet-earnings-release.pdf"
    
    # 2. Instantiate the class
    processor = PDFProcessor(source=test_url)
    
    print(f"Testing URL detection: {processor._is_url()}")
    
    # 3. Test the download method
    if processor._is_url():
        print("Starting download...")
        try:
            saved_path = processor._download()
            print(f"Success! The file was saved at: {saved_path}")
        except Exception as e:
            print(f"An error occurred during download: {e}")
    else:
        print("The provided source is not a valid URL.")