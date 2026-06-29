import os
from pathlib import Path
from urllib.parse import urlparse
import requests
import pymupdf4llm

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

        if self._is_url():
            file_path = self._download()
        else:
            file_path = self.source
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"The local file was not found: {file_path}")
        
        return pymupdf4llm.to_markdown(file_path)
