"""
Tests for the AI extraction agent.
Validates the LLM's ability to accurately extract structured financial data 
from raw document text using a predefined golden dataset.
"""
import pytest

from src.agent import FinancialExtractor

# Golden Dataset: Expected output for the Alphabet Q4 2024 earnings release
EXPECTED_ALPHABET = {
    "media_email": "press@abc.xyz",
    "dividends": {
        "distributions": {
            "class_a": 1200000000,
            "class_b": 172000000,
            "class_c": 1100000000
        },
        "total": 2400000000
    },
    "revenues": {
        "distributions": {
            "google_cloud": 11955000000,
            "google_services": 84094000000,
            "other_bets": 400000000
        }
    },    
    "total_employee_count": 183323,
    "total_assets": 450256000000
}


@pytest.mark.parametrize("run_number", range(1, 6))
def test_alphabet_extraction(run_number):
    """
    Runs the LLM extraction process multiple times to ensure consistency and accuracy.
    Compares the generated Pydantic model against the golden dataset.
    
    Args:
        run_number (int): The current iteration number (injected by pytest).
    """
    print(f"\n--- Launching LLM extraction test (Iteration {run_number}/5) ---")
    
    url = "https://s206.q4cdn.com/479360582/files/doc_financials/2024/q4/2024q4-alphabet-earnings-release.pdf"

    extractor = FinancialExtractor()
    
    # The '_' ignores the returned filename as it is not needed for this test
    result, _ = extractor.process_from_source(url)
    
    assert result.media_email == EXPECTED_ALPHABET["media_email"], f"Email mismatch on iteration {run_number}"
    assert result.total_employee_count == EXPECTED_ALPHABET["total_employee_count"], f"Employee count mismatch on iteration {run_number}"
    assert result.total_assets == EXPECTED_ALPHABET["total_assets"], f"Total assets mismatch on iteration {run_number}"
    
    assert result.dividends.distributions == EXPECTED_ALPHABET["dividends"]["distributions"], f"Dividends mismatch on iteration {run_number}"
    assert result.revenues.distributions == EXPECTED_ALPHABET["revenues"]["distributions"], f"Revenues mismatch on iteration {run_number}"