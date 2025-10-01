# Data Transformation Log

## Raw data exploration
There are 4 unique raw data structures that require transformation. The naming convention and internal structure of each file is consistent with its respective 'type'.

| Data													| Documentation shorthand	| File name example              
|
| Applications to Sparta Global							| `applicants.csv`			| `April2019Applicants.csv`		 
| Overview of Sparta Global assessment day results		| `sparta_day.txt`			| `Sparta Day 1 August 2019.txt` 
| Breakdowns of each applicant's assessment day results | `assessment_scores.json`	| `13480.json`					 
| Progress data for Academy courses						| `course.csv`				| `Business_20_2019-02-11.csv`	 

## Transformation plan
### Overview
|	| Step										| Description																					
|
| 1 | Raw data to DataFrames					| Parse all raw data into initial DataFrames	
| 2 | Data cleaning								| Fix identified errors and ensure consistent data types and formatting across all DataFrames 
| 3 | Create DataFrames for DB schema tables	| Restructure into DataFrames that describe the SQL database schema tables                    

### 1. Raw data to DataFrames
`applicants.csv` -> `df_applicants`

`sparta_day.csv` -> `df_sparta_day`, `df_strengths`, `df_weaknesses`, `df_tech_skills`

`assessment_scores.json` -> `df_assessment_scores`

`course.csv` -> `df_course`

### 2. Cleaning DataFrame data
Click through to see data cleaning details for each DataFrame:
- [df_applicants](dtl_sub/dtl_2_df_applicants.md)
- [df_sparta_day](dtl_sub/dtl_2_df_sparta_day.md)
- [df_strengths](dtl_sub/dtl_2_df_sparta_day.md)
- [df_weaknesses](dtl_sub/dtl_2_df_sparta_day.md)
- [df_tech_skills](dtl_sub/dtl_2_df_sparta_day.md)
- [df_assessment_scores](dtl_sub/dtl_2_df_assessment_scores.md)
- [df_course](dtl_sub/dtl_2_df_course.md)

### 3. Create DataFrames for DB schema tables
