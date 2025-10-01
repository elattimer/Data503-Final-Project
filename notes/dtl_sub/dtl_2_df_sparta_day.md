# `df_sparta_day`
<- [Back to transformation log](../data_transformation_log.md)

## Data table	
| Field name			| Original data type	| Target data type	| Transformation details									| Null placeholder	
|
| sparta_day_id			| `int`					| `int`				| `int` incrementation through each record, beginning at 1 
| date					| `str`					| `datetime`		| Japanese format: `yyyy-mm-dd`		
| location				| `str`					| `str`				| Capitalise
| psychometric_score	| `str`					| `int`				| Remove `"/100"`, convert to `int`
| presentation_score	| `str`					| `int`				| Remove `"/32"`, convert to `int`

## Additional details