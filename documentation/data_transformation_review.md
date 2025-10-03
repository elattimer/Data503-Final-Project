# Data Transformation Review
&larr; [Back to README](../README.md)

## Raw data exploration
There are 4 unique raw data structures that require transformation. The naming convention and internal structure of each file is consistent with its respective 'type'.

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
During this step, convert the data to correct data types and ensure consistent formatting across DataFrames. In dealing with potenital null values, placeholder values matching the target data type are agreed upon. These rules will not always need to be applied.

In anticipation of generating unique IDs for each applicant, applicant names and assessment day/course start dates are duplicated across DataFrames, as these will be required for mapping the correct IDs.

Click through to see data cleaning details for each DataFrame:
- [df_applicants](dtr_sub/dtr_2_df_applicants.md)
- [df_sparta_day](dtr_sub/dtr_2_df_sparta_day.md)
- [df_assessment_scores](dtr_sub/dtr_2_df_assessment_scores.md)
- [df_strengths](dtr_sub/dtr_2_df_strengths.md)
- [df_weaknesses](dtr_sub/dtr_2_df_weaknesses.md)
- [df_tech_skills](dtr_sub/dtr_2_df_tech_skills.md)
- [df_course](dtr_sub/dtr_2_df_course.md)
- [df_behaviour_scores](dtr_sub/dtr_2_df_behaviour_scores.md)

### 3. Structure DataFrames to match DB schema tables
#### Generate and map person ID for each applicant
Pass the clean DataFrames through a function that uses a person's name and assessment day/course start dates to map the correct person ID to each record.

#### Restructure DataFrames to match database schema
Referring to the ERD, merge existing DataFrames to create new ones that match the structure of each entity table in the database.

#### Everything is now ready to load into the SQL database
Store all schema DataFrames in a dictionary that can be passed to the load function.