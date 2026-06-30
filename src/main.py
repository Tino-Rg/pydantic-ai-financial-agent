import os
from pathlib import Path
from src.agent import FinancialExtractor


def main():
    """
    Main entry point of the application.
    Initializes the AI agent, processes a target financial report PDF,
    and saves the extracted structured data as a local JSON file.
    """
    # Target document (can be replaced by a local path or another URL)
    url = "https://s206.q4cdn.com/479360582/files/doc_financials/2024/q4/2024q4-alphabet-earnings-release.pdf"
    
    print("--- Starting extraction process ---")
    print(f"Targeting: {url}\n")
    
    # Initialize the AI extractor
    extractor = FinancialExtractor()
    
    print("Analyzing financial data with AI... (This may take a few seconds)")
    
    # Process the document and extract data
    financial_report, filename = extractor.process_from_source(url)
    
    print("\n--- Data extracted successfully ---")
    
    # Prepare the output directory
    output_dir = Path("data/output")
    os.makedirs(output_dir, exist_ok=True)
    
    # Construct the output JSON filename based on the original PDF name
    json_filename = f"{Path(filename).stem}_extracted.json"
    file_path = output_dir / json_filename
    
    file_path = os.path.join(output_dir, json_filename)
    
    # Serialize the Pydantic model to a JSON string
    json_content = financial_report.model_dump_json(indent=2)
    
    # Save the JSON file securely
    with open(file_path, "w", encoding="utf-8") as json_file:
        json_file.write(json_content)
        
    print(f"Result saved successfully to: {file_path}")


if __name__ == "__main__":
    main()