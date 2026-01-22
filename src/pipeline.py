# pdf document -> ingest.py -> text file -> extract.py -> InvoiceModel


from langchain_core.runnables import RunnableLambda
from src.ingest import Ingestor
from src.extract import InvoiceExtractionAgent
from pydantic_ai import RunUsage

from typing import Dict, Any

class Pipeline:
    """Pipeline class for document ingestion and attribute extraction."""
    
    def __init__(self):
        
        self.ingestor = Ingestor()
        self.extractor = InvoiceExtractionAgent()

    async def process_document(self, pdf_path: str):
        """Process the document from ingestion to structured attribute extraction.
        
        Args:
            pdf_path: Path to the PDF file (relative to project root or absolute)
        """
        if not pdf_path:
            raise ValueError("PDF path must be provided.")
        
        state : Dict[str, Any]  = {"pdf_path": None,
                                    "text_file": None,
                                    "model": None,
                                    "model_name": None,
                                    "invoice_model": None,
                                    "input_tokens": int,
                                    "output_tokens": int,
                                    "requests": int,
                                    "timings": {},
                                    "cache_hit": False,
                                    }
        
        state["pdf_path"] = pdf_path
        ingest_runnable = RunnableLambda(self.ingestor.ingest) # ingest function returns str
        extract_runnable = RunnableLambda(self.extractor.extract_attributes_async)

        pipeline = ingest_runnable | extract_runnable

        result = await pipeline.ainvoke(state)
        return result



        



        
