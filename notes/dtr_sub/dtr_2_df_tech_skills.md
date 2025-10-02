# `df_tech_skills`
&larr; [Back to transformation review](../data_transformation_review.md)

## Data table	
| Column name				| Original data type	| Target data type	| Transformation details									| Null placeholder rule |
|---------------------------|-----------------------|-------------------|-----------------------------------------------------------|-----------------------|
| name						| `str`					| `str`				|															| Drop row				|
| date						| `str`					| `datetime`		|															| `1900-01-01`			|
| tech_name					| `str`					| `str`				|															| n/a					|
| score						| `int`					| `int`				|															| n/a					|

## Further details
See [`df_assessment_scores`](dtr_2_df_assessment_scores.md) for further transformation details