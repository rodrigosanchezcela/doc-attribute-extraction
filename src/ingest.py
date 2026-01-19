"""Ingest class for document ingestion and processing."""

from pathlib import Path
import pymupdf

from src.config import ROOT_DIR, OUTPUT_DIR

class Ingestor:
    """Class for ingesting and processing Invoices."""

    def ingest(self, file_path: str):
        """Ingest and process the document.
        
        Args:
            file_path: Path to the PDF file (relative to project root or absolute)
            
        Returns:
            Extracted text from the document
        """

        file_path = Path(file_path)
        pdf_name = file_path.stem # For later caching alredy ingested files.
        print(f"pdf name is {pdf_name}")

        if not file_path.is_absolute():
            file_path = ROOT_DIR / file_path
            
        if not file_path.exists():
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        output_dir = OUTPUT_DIR / "extracted_text"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / f"{pdf_name}.txt"
        if output_file.exists():
            print(f"Extracted text for {pdf_name} already exists. Skipping ingestion.")
            

        else:
            print(f"Ingesting and extracting text from {file_path}...")

            doc = pymupdf.open(str(file_path))
            
            with open(output_file, "w", encoding="utf-8") as out:
                for page in doc:
                    text = page.get_text()
                    out.write(text)
            print(f"Extracted text saved to {output_file}")
        
        return str(output_file)
            

            