import os
from pathlib import Path
from urllib.parse import urlparse

import pymupdf4llm
import requests


class PDFProcessor:
    """
    A utility class to handle the retrieval and text extraction of PDF documents 
    from both local file paths and remote URLs.
    """

    def __init__(self, source: str):
        """
        Initializes the PDFProcessor with the document source.

        Args:
            source (str): The URL or local file path of the PDF document.
        """
        self.source = source
        self.filename = self._determine_filename()

    def _is_url(self) -> bool:
        """
        Determines if the provided source is a valid HTTP/HTTPS URL.

        Returns:
            bool: True if the source is a URL, False otherwise.
        """
        return self.source.startswith(('http://', 'https://'))
    
    def _determine_filename(self) -> str:
        """
        Extracts the filename from the source URL or local path.

        Returns:
            str: The extracted filename, or a default name if extraction fails.
        """
        if self._is_url():
            parsed_url = urlparse(self.source)
            filename = os.path.basename(parsed_url.path)
            return filename if filename else "default_document.pdf"
        
        return os.path.basename(self.source)

    def _download(self) -> str:
        """
        Downloads the PDF file from the remote URL and saves it locally.

        Returns:
            str: The absolute or relative path to the downloaded local file.

        Raises:
            requests.exceptions.RequestException: If the download request fails.
        """
        # Best practice: always set a timeout for external requests to prevent hanging
        response = requests.get(self.source, timeout=30)
        response.raise_for_status()

        # Define the directory and create it if it doesn't exist
        download_dir = Path("data/downloads")
        download_dir.mkdir(parents=True, exist_ok=True)
    
        file_path = download_dir / self.filename

        with open(file_path, "wb") as f:
            f.write(response.content)

        return str(file_path)

    def extract_content(self) -> str:
        """
        Retrieves the file (downloading it if necessary) and extracts its text 
        content into Markdown format suitable for LLM processing.

        Returns:
            str: The extracted text content formatted as Markdown.

        Raises:
            FileNotFoundError: If the provided local file path does not exist.
        """
        if self._is_url():
            file_path = self._download()
        else:
            file_path = self.source
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"The local file was not found: {file_path}")
        
        return pymupdf4llm.to_markdown(file_path)
