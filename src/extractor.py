import tabula

def extract_tables(pdf_path: str, pages: str) -> list:
    """Extract tables from PDF using tabula."""
    tables = tabula.read_pdf(
        pdf_path,
        pages=pages,
        multiple_tables=True,
        stream=True,
        pandas_options={"header": None},
        encoding="latin-1"
    )
    return tables
