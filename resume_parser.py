# resume_parser.py

import fitz  # PyMuPDF

def extract_resume_text(pdf_file):
    """
    Extracts and returns text from a PDF file.
    Args:
        pdf_file: file-like object (from Streamlit uploader)
    Returns:
        str: extracted plain text
    """
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()
