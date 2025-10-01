# `df_assessment_scores`
<- [Back to transformation log](../data_transformation_log.md)

## Data table	
| Field name				| Original data type	| Target data type	| Transformation details									| Null placeholder |
|---------------------------|-----------------------|-------------------|-----------------------------------------------------------|------------------|
| name						| `str`					| `str`				| `int` incrementation through each record, beginning at 1  |                  |
| date						| `str`					| `datetime`		| Remove extraneous `/`s, Japanese format: `yyyy-mm-dd`		|                  |
| self_development			| `str`					| `bool`			| Covert to true/false from yes/no or 1/0 strs				| False            |
| geo_flex					| `str`					| `bool`			| Covert to true/false from yes/no or 1/0 strs				| False            |
| financial_support_self	| `str`					| `bool`			| Covert to true/false from yes/no or 1/0 strs				| True             |
| result					| `str`					| `bool`			| Covert to true/false from yes/no or 1/0 strs				| False            |
| course_interest			| `str`					| `str`				| Set to uppercase											| "NO INTEREST"    |

## Additional details