# LJOtoAnki
Framework for converting PDFs of the LJO learning words to txt for importing into Anki

Example use:
```bash
uv run main.py gemini Unit11.pdf Unit11.txt
```

## Project Structure
```bash
LJOtoAnki
├── config.py                  # Configuration settings
├── .env.example               # Environment variables
├── .gitignore                 # Git ignore configuration
├── llm_clients.py             # LLM client implementations
├── main.py                    # Main
├── pdf_processor.py           # PDF processing utilities
├── pyproject.toml             # Project metadata and dependencies
├── .python-version            # Python version specification
├── README.md                  # README (this file)
└── uv.lock                    # Dependency lock file (uv package manager)
```


### File Descriptions
- **config.py** - Configuration settings
- **llm_clients.py** - LLM client implementations
- **main.py** - Main entry point of the application
- **pdf_processor.py** - PDF processing utilities for extracting content from LJO learning words PDFs
- **pyproject.toml** - Project metadata and dependency specifications
- **uv.lock** - Lock file for reproducible dependency installation using uv package manager
