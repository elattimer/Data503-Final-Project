from extract_json import extract_json
import pandas as pd

df = extract_json()
def transform_course_interest(df: pd.DataFrame) -> pd.DataFrame:

    def clean_string(val):
        if pd.isnull(val) or str(val).strip() == "":
            return "No interest"
        return str(val).strip().title()

    if "course_interest" not in df.columns:
        df["course_interest"] = "No interest"
    else:
        df["course_interest"] = df["course_interest"].apply(clean_string)

    return df

# Call the function 
df_cleaned = transform_course_interest(df)

# Inspect results (uncomment to see if its working as expected)
#print(df_cleaned[["course_interest"]].head(10))
