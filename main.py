from src.extractor import extract_tables
from src.processor import process_tables
from src.ranking import generate_ranking

def main():
    pdf_path = "input.pdf"
    tables = extract_tables(pdf_path)
    df_clean = process_tables(tables)
    df_ranked = generate_ranking(df_clean)

    df_ranked.to_csv("ranking_output.csv", index=False)

if __name__ == "__main__":
    main()
