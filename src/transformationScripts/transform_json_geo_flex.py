import json
import pandas as pd


def transform_geo_flex(df: pd.DataFrame) -> pd.DataFrame:
    def to_bool(val):
        if pd.isnull(val):
            return False
        if isinstance(val, str):
            val_lower = val.strip().lower()
            if val_lower in ("yes", "true", "1"):
                return True
            elif val_lower in ("no", "false", "0"):
                return False
        return bool(val)  # fallback for numbers or already boolean

    # Apply transformation directly to the column
    if "geo_flex" in df.columns:
        df["geo_flex"] = df["geo_flex"].apply(to_bool)
    else:
        # If column doesn't exist, create it with default False
        df["geo_flex"] = False

    return df

