import pdfplumber
import docx2txt


def extract_text(file_path):
    """
    Extract text from PDF or DOCX resume
    """
    if file_path.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text()
        return text

    elif file_path.endswith(".docx"):
        return docx2txt.process(file_path)

    else:
        return ""
