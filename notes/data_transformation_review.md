# Data Transformation Review
&larr; [Back to README](../README.md)

## Raw data exploration
There were 4 unique raw data structures that required transformation. The naming convention and internal structure of each file was consistent with its respective 'type'.

| Data													| Documentation shorthand	| File name example              |
|-------------------------------------------------------|---------------------------|--------------------------------|	
| Applications to Sparta Global							| `applicants.csv`			| `April2019Applicants.csv`		 |
| Overview of Sparta Global assessment day results		| `sparta_day.txt`			| `Sparta Day 1 August 2019.txt` |
| Breakdowns of each applicant's assessment day results | `assessment_scores.json`	| `13480.json`					 |
| Progress data for Academy courses						| `course.csv`				| `Business_20_2019-02-11.csv`	 |

## Transformation plan
### Overview
|   | Step												| Description																				    |
|---|---------------------------------------------------|-----------------------------------------------------------------------------------------------|
| 1 | Raw data to DataFrames							| Parse all raw data into initial DataFrames													|
| 2 | Data cleaning										| Fix identified errors and ensure consistent data types and formatting across all DataFrames	|
| 3 | Structure DataFrames to match DB schema tables	| Restructure into DataFrames that describe the SQL database schema tables						|   

### 1. Raw data to DataFrames
`applicants.csv` &rarr; `df_applicants`

`sparta_day.csv` &rarr; `df_sparta_day`

`assessment_scores.json` &rarr; `df_assessment_scores`, `df_strengths`, `df_weaknesses`, `df_tech_skills`

`course.csv` &rarr; `df_course`, `df_behaviour_scores`

### 2. Cleaning DataFrame data
This step of the process involved converting the data to correct data types and ensuring consistent formatting across DataFrames. In dealing with potenital null values, placeholder values matching the target data type were agreed upon. These rules did not always need to be applied.

In anticipation of generating unique IDs for each applicant, applicant names and assessment day/course start dates were duplicated across DataFrames, as these were required for mapping the correct IDs.

Click through to see data cleaning details for each DataFrame:
- [df_applicants](dtl_sub/dtl_2_df_applicants.md)
- [df_sparta_day](dtl_sub/dtl_2_df_sparta_day.md)
- [df_assessment_scores](dtl_sub/dtl_2_df_assessment_scores.md)
- [df_strengths](dtl_sub/dtl_2_df_strengths.md)
- [df_weaknesses](dtl_sub/dtl_2_df_weaknesses.md)
- [df_tech_skills](dtl_sub/dtl_2_df_tech_skills.md)
- [df_course](dtl_sub/dtl_2_df_course.md)
- [df_behaviour_scores](dtl_sub/dtl_2_df_behaviour_scores.md)

### 3. Structure DataFrames to match DB schema tables
