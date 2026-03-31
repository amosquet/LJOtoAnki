import PyPDF2


def extract_text(file_path: str) -> str:
    """
    Reads a PDF file and extracts all available text.
    """
    extracted_text = ""
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                extracted_text += page.extract_text() + "\n"
        return extracted_text
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return ""
