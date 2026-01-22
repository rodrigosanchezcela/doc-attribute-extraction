import time
from pydantic_ai import Agent
from src.config import  MODEL_NAME, get_config, OUTPUT_DIR
from src.schema import InvoiceModel
from pathlib import Path
from typing import Dict, Any


cfg = get_config()

class InvoiceExtractionAgent:
    """Agent for extracting invoice data using Pydantic schema."""

    def __init__(self):

        self.agent = Agent(
            model=str(MODEL_NAME),
            output_type=InvoiceModel,
            system_prompt=cfg.system_prompt,
        )

    def extract_attributes(self,  state : Dict[str, Any]) -> Dict[str, Any]:
        """Extract attributes from the given PDF invoice."""
        ""
        print("starting extraction...")
        t1 = time.time()
        with Path(state["text_file"]).open("r", encoding="utf-8") as f:
            invoice_text = f.read()
        
        result =  self.agent.run_sync(invoice_text)
        t2 = time.time()
        state["model"] = self.agent.model
        state["model_name"] = self.agent.model.model_name

        
        #store result in directory
        output_dir = OUTPUT_DIR / "extracted_attributes"
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / Path(state["text_file"]).stem.replace(".txt", "_attributes.json")
        with open(output_file, "w", encoding="utf-8") as out:
            out.write(result.output.model_dump_json(indent=4))
        
        state["invoice_model"] = result.output.model_dump()
        state["input_tokens"] = result.usage().input_tokens
        state["output_tokens"] = result.usage().output_tokens
        state["requests"] = result.usage().requests
        state["timings"]["extraction_time"] = (t2 - t1)*1000  # in milliseconds
        print("Finised extraction.")
        return state

    async def extract_attributes_async(self,  state : Dict[str, Any]) -> Dict[str, Any]:
            """Extract attributes from the given PDF invoice."""
            ""
            print("starting extraction...")
            t1 = time.time()
            with Path(state["text_file"]).open("r", encoding="utf-8") as f:
                invoice_text = f.read()
            
            result =  await self.agent.run(invoice_text)
            t2 = time.time()
            state["model"] = self.agent.model
            state["model_name"] = self.agent.model.model_name

            
            #store result in directory
            output_dir = OUTPUT_DIR / "extracted_attributes"
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = output_dir / Path(state["text_file"]).stem.replace(".txt", "_attributes.json")
            with open(output_file, "w", encoding="utf-8") as out:
                out.write(result.output.model_dump_json(indent=4))
            
            state["invoice_model"] = result.output.model_dump()
            state["input_tokens"] = result.usage().input_tokens
            state["output_tokens"] = result.usage().output_tokens
            state["requests"] = result.usage().requests
            state["timings"]["extraction_time_ms"] = (t2 - t1)*1000  # in milliseconds
            print("Finished extraction.")

            
            return state
