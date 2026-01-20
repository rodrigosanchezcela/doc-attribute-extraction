"""running script for document ingestion."""

from src.ingest import Ingestor
from src.extract import InvoiceExtractionAgent
from src.pipeline import Pipeline
from src.config import OUTPUT_DIR
from pathlib import Path


if __name__ == "__main__":

    #ingestor = Ingestor()
    #extractor = InvoiceExtractionAgent()

    #file to ingest
    pdf_path = Path("data/raw/invoice_Aaron Bergman_36258.pdf")

    #ingestor.ingest(str(pdf_path))

    text_file = OUTPUT_DIR / "extracted_text" / "invoice_Aaron Bergman_36258.txt"
    #invoice = extractor.extract_attributes(text_file)
    #print(invoice)


    pipeline = Pipeline()
    invoice_state = pipeline.process_document(str(pdf_path))
    print(invoice_state["invoice_model"].model_dump())
    print(invoice_state)