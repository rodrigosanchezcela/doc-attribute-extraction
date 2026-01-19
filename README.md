# Document Attribute Extraction

An intelligent document processing system that extracts structured invoice data from PDF documents using AI-powered agents. Built with Pydantic AI and PyMuPDF for accurate, schema-validated data extraction.

## 🚀 Features

- **PDF Text Extraction**: Automatically extracts text content from PDF invoices using PyMuPDF
- **AI-Powered Attribute Extraction**: Uses Pydantic AI with GPT models to intelligently extract structured invoice data
- **Schema Validation**: Ensures extracted data conforms to predefined Pydantic models
- **Caching System**: Avoids re-processing already extracted documents
- **JSON Output**: Saves extracted attributes in structured JSON format
- **Modular Architecture**: Clean separation of concerns with dedicated modules for ingestion, extraction, and configuration

## 📋 Prerequisites

- Python 3.13 or higher
- OpenAI API key
- [uv](https://github.com/astral-sh/uv) package manager (recommended) or pip

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd doc-attribute-extraction
   ```

2. **Install dependencies**
   ```bash
   uv pip install -e .
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_KEY=your-openai-api-key-here
   MODEL_NAME=gpt-4o-mini  # Optional, defaults to gpt-4o-mini
   ```

## 🎯 Usage

### Command Line

Process a single invoice:

```bash
uv run python main.py
```


### Programmatic Usage

```python
from src.ingest import Ingestor
from src.extract import InvoiceExtractionAgent
from pathlib import Path

# Initialize components
ingestor = Ingestor()
extractor = InvoiceExtractionAgent()

# Process a PDF invoice
pdf_path = "data/raw/invoice_example.pdf"
ingestor.ingest(pdf_path)

# Extract structured attributes
text_file = "outputs/extracted_text/invoice_example.txt"
invoice_data = extractor.extract_attributes(text_file)

print(invoice_data)
# Output: InvoiceModel(customer='...', date='...', total=Decimal('...'), ...)
```

## 📁 Project Structure

```
doc-attribute-extraction/
├── data/
│   ├── raw/              # Input PDF invoices
│   └── processed/        # Processed data
├── outputs/
│   ├── extracted_text/   # Extracted raw text from PDFs
│   └── extracted_attributes/  # Structured JSON output
├── src/
│   ├── __init__.py       # Package exports
│   ├── config.py         # Project configuration and settings
│   ├── ingest.py         # PDF text extraction module
│   ├── extract.py        # AI-powered attribute extraction
│   └── schema.py         # Pydantic data models
├── tests/                # Unit tests
├── main.py              # CLI entry point
├── pyproject.toml       # Project dependencies and config
└── README.md
```

## 🔍 How It Works

1. **Ingestion**: The `Ingestor` class processes PDF files and extracts raw text using PyMuPDF
2. **Text Storage**: Extracted text is saved to `outputs/extracted_text/` for caching
3. **AI Extraction**: The `InvoiceExtractionAgent` uses Pydantic AI to parse text and extract structured data
4. **Validation**: Extracted data is validated against the `InvoiceModel` schema
5. **Output**: Validated invoice data is saved as JSON in `outputs/extracted_attributes/`

## 📊 Extracted Data Schema

```python
class InvoiceModel(BaseModel):
    customer: str           # Customer name
    date: str              # Invoice date
    total: Decimal         # Total amount (validated as non-negative)
    invoice_number: str    # Invoice ID
    address_line: str      # Customer address
```

## 🛠️ Development

### Running Tests

```bash
uv run pytest
```

### Code Formatting

```bash
uv run ruff format .
```

### Type Checking

```bash
uv run ruff check .
```

## 🧰 Technologies

- **[Pydantic AI](https://ai.pydantic.dev/)**: AI agent framework with structured output
- **[PyMuPDF](https://pymupdf.readthedocs.io/)**: Fast PDF text extraction
- **[OpenAI GPT](https://openai.com/)**: Large language models for intelligent extraction
- **[Pydantic](https://pydantic.dev/)**: Data validation and settings management
- **[Python 3.13+](https://www.python.org/)**: Modern Python with latest features

## 📝 Configuration

Key configuration variables in `src/config.py`:

- `ROOT_DIR`: Project root directory
- `DATA_DIR`: Data storage directory
- `OUTPUT_DIR`: Output files directory
- `OPENAI_KEY`: OpenAI API key (from environment)
- `MODEL_NAME`: LLM model to use (from environment, defaults to gpt-4o-mini)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Pydantic AI](https://ai.pydantic.dev/) for reliable AI agent development
- PDF processing powered by [PyMuPDF](https://pymupdf.readthedocs.io/)

---

**Note**: This project is part of an AI Engineering learning initiative focused on building production-ready document processing systems. README.md has been AI generated, the rest of the code is mine.