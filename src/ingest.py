"""Ingest class for document ingestion and processing."""

from pathlib import Path
import pymupdf

from src.config import ROOT_DIR, OUTPUT_DIR
from typing import Dict, Any
import time

class Ingestor:
    """Class for ingesting and processing Invoices."""

    def ingest(self, state_dict : Dict[str, Any]):
        """Ingest and process the document.
        
        Args:
            file_path: Path to the PDF file (relative to project root or absolute)
            
        Returns:
            Extracted text from the document
        """
        print("starting ingestion...")
        t1 = time.time()
        pdf_path = Path(state_dict["pdf_path"])
        pdf_name = pdf_path.stem # For later caching alredy ingested files.
        print(f"pdf name is {pdf_name}")

        if not pdf_path.is_absolute():
            pdf_path = ROOT_DIR / pdf_path
            
        if not pdf_path.exists():
            raise FileNotFoundError(f"The file {pdf_path} does not exist.")
        
        output_dir = OUTPUT_DIR / "extracted_text"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / f"{pdf_name}.txt"
        if output_file.exists():
            print(f"Extracted text for {pdf_name} already exists. Skipping ingestion.")
            state_dict["cache_hit"] = True
            

        else:
            print(f"Ingesting and extracting text from {pdf_path}...")

            doc = pymupdf.open(str(pdf_path))
            
            with open(output_file, "w", encoding="utf-8") as out:
                for page in doc:
                    text = page.get_text()
                    out.write(text)

            print(f"Extracted text saved to {output_file}")
        t2 = time.time()
        state_dict["text_file"] = str(output_file)
        state_dict["timings"]["ingestion_time_ms"] = (t2 - t1)*1000 # in milliseconds
        print("Finished ingestion.")
        return state_dict
            

            