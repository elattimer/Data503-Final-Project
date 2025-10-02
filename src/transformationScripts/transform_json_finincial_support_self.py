import json
import pandas as pd

def transform_financial_support_self(df: pd.DataFrame) -> pd.DataFrame:
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
    if "financial_support_self" in df.columns:
        df["financial_support_self"] = df["financial_support_self"].apply(to_bool)
    else:
        # If column doesn't exist, create it with default True
        df["financial_support_self"] = True

    return df

# # Transform the DataFrame
# df_cleaned = transform_financial_support_self(df)

# # Inspect result
# print(df_cleaned[["financial_support_self"]])