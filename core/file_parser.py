from PyPDF2 import PdfReader
from docx import Document


def extract_text_from_pdf(uploaded_file):

    text = ""

    reader = PdfReader(uploaded_file)

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_text_from_docx(uploaded_file):

    document = Document(uploaded_file)

    text = "\n".join(
        [paragraph.text for paragraph in document.paragraphs]
    )

    return text


def extract_text_from_txt(uploaded_file):

    return uploaded_file.read().decode("utf-8")


def parse_uploaded_file(uploaded_file):

    extension = uploaded_file.name.split(".")[-1].lower()

    if extension == "pdf":
        return extract_text_from_pdf(uploaded_file)

    elif extension == "docx":
        return extract_text_from_docx(uploaded_file)

    elif extension == "txt":
        return extract_text_from_txt(uploaded_file)

    else:
        raise ValueError(
            "Unsupported file format"
        )