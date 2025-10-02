import json
import pandas as pd


def transform_result(df: pd.DataFrame) -> pd.DataFrame:
    def to_bool(val):
        if pd.isnull(val):
            return False
        if isinstance(val, str):
            val_lower = val.strip().lower()
            if val_lower in ("yes", "true", "1","pass"):
                return True
            elif val_lower in ("no", "false", "0","fail"):
                return False
        return bool(val)  # fallback for numbers or already boolean

    # Apply transformation directly to the column
    if "result" in df.columns:
        df["result"] = df["result"].apply(to_bool)
    else:
        # If column doesn't exist, create it with default False
        df["result"] = False

    return df

