# `df_course`
<- [Back to transformation review](../data_transformation_review.md)

## Data table	
| Column name				| Original data type	| Target data type	| Transformation details									| Null placeholder rule |
|---------------------------|-----------------------|-------------------|-----------------------------------------------------------|-----------------------|
| course_id					| n/a					| `int`				| Range function to generate int							| n/a					|
| subject_name				| `str`					| `str`				| Split file name string									| n/a					|
| trainer					| `str`					| `str`				| Set to uppercase											| n/a					|
| start_date				| `str`					| `datetime`		| Split file name string, convert to datetime				| n/a					|
| class_number				| `str`					| `int`				| Split file name string, convert to int					| n/a					|

## Further details
### Data contained in file name
Data for `subject_name`, `class_number_` and `start_date` was contained in the file name rather than the file itself. This required splitting the string by the appropriate delimiter and converting to the correct data type before assigning to the DataFrame.