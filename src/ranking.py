import pandas as pd

def generate_ranking(df: pd.DataFrame) -> pd.DataFrame:
    """Generate ranking sorted by score (descending)."""
    df_ranked = df.sort_values(
        by="Nota Objetiva",
        ascending=False
    ).reset_index(drop=True)

    df_ranked["Ranking"] = df_ranked.index + 1

    return df_ranked
