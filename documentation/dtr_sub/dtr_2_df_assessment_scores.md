# `df_assessment_scores`
&larr; [Back to transformation review](../data_transformation_review.md)

## Data table	
| Column name				| Original data type	| Target data type	| Transformation details															| Null placeholder rule		|
|---------------------------|-----------------------|-------------------|-----------------------------------------------------------------------------------|---------------------------|
| name						| `str`					| `str`				| `int` incrementation through each record, beginning at 1							| Drop row					|
| date						| `str`					| `datetime`		| Remove extraneous `/`s, align incorrect dates, Japanese format: `yyyy-mm-dd`		| `1900-01-01`				|
| self_development			| `str`					| `bool`			| Covert to true/false from yes/no or 1/0 strs										| `False`					|
| geo_flex					| `str`					| `bool`			| Covert to true/false from yes/no or 1/0 strs										| `False`					|
| financial_support_self	| `str`					| `bool`			| Covert to true/false from yes/no or 1/0 strs										| `True`					|
| result					| `str`					| `bool`			| Covert to true/false from yes/no or 1/0 strs										| `False`					|
| course_interest			| `str`					| `str`				| Set to uppercase																	| `"No interest"`			|

## Further details
### Incorrect dates
Raw JSON data has incorrect dates - assessment days in June have been incorrectly entered as taking place in July. This requires a function to map the correct dates onto the `df_assessment_scores` DataFrame, using `df_sparta_day` as the authoritative date source.

### Dropped rows
Duplicate rows are dropped to account for copies of the same JSON in the raw data

### Lists and dictionaries
Raw JSON data contains `strengths` and `weaknesses` lists, and a `tech_self_score`, dictionary. As each JSON is processed, we iterate through each list/dictionary to create:
- [df_strengths](dtr_2_df_strengths.md)
- [df_weaknesses](dtr_2_df_weaknesses.md)
- [df_tech_skills](dtr_2_df_tech_skills.md)