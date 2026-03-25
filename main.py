from src.extractor import extract_tables
from src.processor import process_datas
from src.ranking import generate_ranking

def main():
    pdf_path = "analisar.pdf" # Path to the PDF file you want to analyze
    pages = "180-642"         # Range of pages to extract; can be adjusted as needed
    start_index = 35          # Starting index for processing tables; change if necessary
    tables = extract_tables(pdf_path, pages)
    df_clean = process_data(tables, start_index)
    df_ranked = generate_ranking(df_clean)

    df_ranked.to_csv("ranking_output.csv", index=False) # Save the ranked output to a CSV file

if __name__ == "__main__":
    main()
