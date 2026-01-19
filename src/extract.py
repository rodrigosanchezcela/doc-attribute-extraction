from pydantic_ai import Agent
from src.config import  MODEL_NAME, get_config, OUTPUT_DIR
from src.schema import InvoiceModel
from pathlib import Path


cfg = get_config()

class InvoiceExtractionAgent:
    """Agent for extracting invoice data using Pydantic schema."""

    def __init__(self):

        self.agent = Agent(
            model=str(MODEL_NAME),
            output_type=InvoiceModel,
            system_prompt=cfg.system_prompt,

        )

    
    def extract_attributes(self, text_file: str) -> InvoiceModel:
        """Extract attributes from the given PDF invoice."""
        ""
        with Path(text_file).open("r", encoding="utf-8") as f:
            invoice_text = f.read()
        
        result = self.agent.run_sync(invoice_text, output_type=InvoiceModel)
        
        #store result in directory
        output_dir = OUTPUT_DIR / "extracted_attributes"
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / Path(text_file).stem.replace(".txt", "_attributes.json")
        with open(output_file, "w", encoding="utf-8") as out:
            out.write(result.output.model_dump_json(indent=4))
        
        return result.output
