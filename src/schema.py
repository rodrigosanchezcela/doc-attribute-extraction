"""Schema definitions for invoice data extraction using Pydantic."""

from pydantic import BaseModel, field_validator
from pydantic.types import Decimal


class InvoiceModel(BaseModel):
    """Pydantic schema for invoice data extraction."""
    customer: str
    date: str
    total: Decimal
    invoice_number: str
    address_line: str

    @field_validator('total')
    def validate_total(cls, value):
        if value < 0:
            raise ValueError('Total amount must be non-negative')
        return value
    
