# adobe25-challenge-1a-bingpot
# PDF Outline Extractor (adobe25-challenge-1a-bingpot)

This project provides tools to extract structured outlines (headings, sections) from PDF documents using PyMuPDF (fitz). It includes two scripts:

- `challenge-1a.py`: Processes all PDFs in a directory, extracting outlines and saving them as JSON files.
- `get_text.py`: Extracts and cleans text from a single PDF, merging fragmented lines.

## Features
- Detects headings and classifies them by level (H1, H2, H3) based on heuristics.
- Outputs a JSON file per PDF with the document title and outline.
- Handles line fragment merging for cleaner text extraction.

## Requirements
- Python 3.7+
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd adobe25-challenge-1a-bingpot-main
   ```
2. **Install dependencies:**
   ```bash
   pip install pymupdf
   ```

## Usage

### 1. Batch Outline Extraction
Edit the `INPUT_DIR` and `OUTPUT_DIR` variables in `challenge-1a.py` to point to your PDF folder and desired output location.

Run:
```bash
python challenge-1a.py
```
This will process all PDFs in the input directory and save JSON outlines in the output directory.

### 2. Single PDF Text Extraction
Edit the `pdf_path` variable in `get_text.py` to point to your PDF file.

Run:
```bash
python get_text.py
```
This will print the cleaned, merged text from the PDF.

## Docker
A `Dockerfile` is provided for containerized execution.

### Build the image
```bash
docker build -t pdf-outline-extractor .
```

### Run the container
Mount your data directory and run the script:
```bash
docker run --rm -v /path/to/your/pdfs:/data pdf-outline-extractor
```
Edit the script(s) to use `/data` as the input/output directory inside the container.

## Notes
- Update the input/output paths in the scripts as needed for your environment or Docker usage.
- Only PDFs are processed; other file types are ignored.


