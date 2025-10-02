# `df_sparta_day`
<- [Back to transformation review](../data_transformation_review.md)

## Data table	
| Field name			| Original data type	| Target data type	| Transformation details									| Null placeholder  |	
|-----------------------|-----------------------|-------------------|-----------------------------------------------------------|-------------------|
| sparta_day_id			| `int`					| `int`				| `int` incrementation through each record, beginning at 1	|					|
| date					| `str`					| `datetime`		| Japanese format: `yyyy-mm-dd`								|					|
| location				| `str`					| `str`				| Capitalise												|					|
| psychometric_score	| `str`					| `int`				| Remove `"/100"`, convert to `int`							|					|
| presentation_score	| `str`					| `int`				| Remove `"/32"`, convert to `int`							|					|

## Further details
### Dropped rows
Duplicate rows are dropped to account for copies of the same JSON in the raw data