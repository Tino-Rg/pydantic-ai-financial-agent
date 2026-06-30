import os

from pydantic_ai import Agent

from .config import settings
from .document import PDFProcessor
from .models import FinancialReport
from .utils import load_prompt

# Set the Google API key in the environment variables before initializing the agent
os.environ["GOOGLE_API_KEY"] = settings.gemini_api_key

class FinancialExtractor:
    """
    A class responsible for orchestrating the extraction of financial data 
    from documents using an AI model.
    """

    def __init__(self, model_name: str = 'google:gemini-3.1-flash-lite'):
        """
        Initializes the FinancialExtractor with a specified AI model.

        Args:
            model_name (str): The name of the LLM model to use for extraction. 
                              Defaults to 'google:gemini-3.1-flash-lite'.
        """
        self.agent = Agent(
            model=model_name,
            model_settings={'temperature': 0.0}, # Limit creativity, useless to extract informations from a doc
            output_type=FinancialReport,
            system_prompt=load_prompt("system_prompt.txt")
        )

    def extract_financial_data(self, content: str) -> FinancialReport:
        """
        Executes the AI agent synchronously to extract structured financial data 
        from the provided text content.

        Args:
            content (str): The raw text or Markdown content of the document.

        Returns:
            FinancialReport: A Pydantic model containing the extracted structured data.
        """
        result = self.agent.run_sync(content)
        return result.output
    
    def process_from_source(self, source: str) -> tuple[FinancialReport, str]:
        """
        Manages the complete pipeline: downloads or reads the PDF, extracts the text, 
        and processes it through the AI agent.

        Args:
            source (str): The URL or local file path of the source document.

        Returns:
            tuple[FinancialReport, str]: A tuple containing the structured financial 
                                         report and the extracted filename.
        """
        processor = PDFProcessor(source=source)
        document_text = processor.extract_content()
        
        report = self.extract_financial_data(document_text)
        
        return report, processor.filename