# `df_sparta_day`
&larr; [Back to transformation review](../data_transformation_review.md)

## Data table	
| Column name			| Original data type	| Target data type	| Transformation details									| Null placeholder rule  |	
|-----------------------|-----------------------|-------------------|-----------------------------------------------------------|------------------------|
| sparta_day_id			| `int`					| `int`				| `int` incrementation through each record, beginning at 1	| n/a					 |
| date					| `str`					| `datetime`		| Japanese format: `yyyy-mm-dd`								| `1900-01-01`			 |
| location				| `str`					| `str`				|															| `"Unknown"`			 |
| name					| `str`					| `str`				| Set to uppercase											| Drop row				 |
| psychometric_score	| `str`					| `int`				| Remove `"/100"`, convert to `int`							| n/a					 |
| presentation_score	| `str`					| `int`				| Remove `"/32"`, convert to `int`							| n/a					 |

## Further details
### Parsing
Assessment day data is contained in .txt files, which requires parsing the data and assigning it to variables before loading everything into the DataFrame. The formatting of each .txt was consistent, meaning the same logic can be applied across all files.