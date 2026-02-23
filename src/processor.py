def process_data(tables: list, start_index: int) -> pd.DataFrame:
    """Concatenate tables and clean dataset."""
    df = pd.concat(tables, ignore_index=True)

    df = df[start_index:]
    df = df[[0, 8]]
    df = df.rename(columns={0: "NOME", 8: "Nota Objetiva"})

    df["Nota Objetiva"] = pd.to_numeric(
        df["Nota Objetiva"], errors="coerce"
    )

    df = df.dropna(subset=["Nota Objetiva"])

    return df
