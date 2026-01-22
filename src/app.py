
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from typing import Literal
from src.pipeline import Pipeline
from src.config import get_config, OUTPUT_DIR
from pathlib import Path
import os

app = FastAPI()
cfg = get_config()

@app.get("/")
async def root():
    return "Welcome to the Document Attribute Extraction API!"


@app.post("/uploadPDF/")
async def create_upload_pdf(file: UploadFile):
    print(f"Received file: {file.filename}")
    if file.filename.split(".")[-1].lower() not in cfg.supported_files:
        raise HTTPException(status_code=400, detail="Only PDF or image files are accepted.")

    print("file uploaded succesfully!")
    #writing file to disk
    upload_dir = OUTPUT_DIR / "uploads"
    upload_dir.mkdir(parents=True, exist_ok=True)
    file_path = upload_dir / file.filename
    with open(file_path, "wb") as f:
        content =await file.read()
        f.write(content)
    
    print("file saved to disk.")
    
    print("Starting pipeline...")
    pipeline = Pipeline()
    invoice_state = await pipeline.process_document(str(file_path))

    print(invoice_state)
    response_data = invoice_state.copy()
    response_data.pop("model")
    
    
    return {"message": "PDF uploaded successfully!",
            "state": response_data,
            }