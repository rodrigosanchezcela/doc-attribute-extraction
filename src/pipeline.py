# pdf document -> ingest.py -> text file -> extract.py -> InvoiceModel

import langchain
from langchain_core.runnables import RunnableLambda
from src.ingest import Ingestor
from src.extract import InvoiceExtractionAgent
from src.config import OUTPUT_DIR
from pathlib import Path

class Pipeline:
    """Pipeline class for document ingestion and attribute extraction."""
    
    def __init__(self):
        
        self.ingestor = Ingestor()
        self.extractor = InvoiceExtractionAgent()
        self.history = {}

    def process_document(self, pdf_path: str):
        """Process the document from ingestion to structured attribute extraction.
        
        Args:
            pdf_path: Path to the PDF file (relative to project root or absolute)
        """
        if not pdf_path:
            raise ValueError("PDF path must be provided.")
        
        ingest_runnable = RunnableLambda(self.ingestor.ingest) # ingest function returns str
        extract_runnable = RunnableLambda(self.extractor.extract_attributes)

        pipeline = ingest_runnable | extract_runnable

        result = pipeline.invoke(pdf_path)
        return result



        



        
