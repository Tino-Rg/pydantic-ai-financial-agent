from typing import Dict

from pydantic import BaseModel, Field


class Dividends(BaseModel):
    """
    Represents the dividend distribution details extracted from the financial report.
    """
    
    distributions: Dict[str, int] = Field(
        description=(
            "Dictionary of dividends distributed by share class. "
            "RULE 1 (Key format): Strictly use 'snake_case' (e.g., 'class_a', 'class_b'). "
            "RULE 2 (Values): Amounts must be absolute values. If the document states "
            "values are 'in millions', you MUST multiply the extracted number by 1,000,000."
        )
    )
    
    total: int = Field(
        description=(
            "Total dividends distributed. Absolute value (multiply by 1,000,000 "
            "if the document indicates 'in millions')."
        )
    )


class Revenues(BaseModel):
    """
    Represents the revenue breakdown by top-level operating segments.
    """
    
    distributions: Dict[str, int] = Field(
        description=(
            "Dictionary of consolidated revenues by segment. "
            "RULE 1 (Key format): Strictly use 'snake_case' (e.g., 'google_services', 'intelligent_cloud'). "
            "RULE 2 (Depth): Extract ONLY the top-level operating segments. Do NOT include sub-segments or individual products. "
            "RULE 3 (Values): Amounts must be absolute values. Multiply by 1,000,000 if the document specifies figures are 'in millions'."
        )
    )


class FinancialReport(BaseModel):
    """
    The master data schema for the financial report extraction.
    Aggregates all specific financial metrics, structures, and contact information
    expected to be extracted by the LLM.
    """
    
    media_email: str = Field(
        description="Main press contact email address (e.g., press@abc.xyz)."
    )
    
    dividends: Dividends = Field(
        description=(
            "Details of dividends. If the company does not pay dividends, "
            "return an empty dictionary and 0 for the total."
        )
    )
    
    revenues: Revenues = Field(
        description="Revenues by main operating segment of the company."
    )
    
    total_employee_count: int = Field(
        description=(
            "Total number of employees at the end of the period. "
            "WARNING: this figure is ALWAYS an absolute raw value in financial documents, "
            "do NOT multiply it by one million."
        )
    )
    
    total_assets: int = Field(
        description=(
            "Total assets at the end of the year. Absolute value "
            "(multiply by 1,000,000 if the document indicates 'in millions')."
        )
    )