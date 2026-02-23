def extract_tables(pdf_path):
    # extract logic
    return tables

def process_tables(tables):
    # cleaning logic
    return df_clean

def generate_ranking(df):
    # sorting and ranking logic
    return df_ranked

def main():
    pdf_path = "input.pdf"
    tables = extract_tables(pdf_path)
    df_clean = process_tables(tables)
    df_ranked = generate_ranking(df_clean)

    df_ranked.to_csv("ranking_output.csv", index=False)

if __name__ == "__main__":
    main()
