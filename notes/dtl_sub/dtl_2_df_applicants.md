# `df_applicants`
<- [Back to transformation review](../data_transformation_review.md)

## Data table
| Column name  | Original data type | Target data type	| Transformation details														| Null placeholder rule							|
|--------------|--------------------|-------------------|-------------------------------------------------------------------------------|-----------------------------------------------|
| name		   | `str`              | `str`				| Set to upper case and remove punctuation										| Drop row										|
| gender	   | `str`				| `str`				| Title case																	| `"Undisclosed"`								|
| dob		   | `str`				| `datetime`		| Japanese format: `yyyy-mm-dd`													| `1900-01-01`									|
| email        | `str`              | `str`				| Set to lower case																| `example@example.com`							|
| city         | `str`              | `str`				| Title case																	| `"Unknown"`									|
| address      | `str`              | `str`				|																				| `"Unknown"`									|
| postcode     | `str`              | `str`				| Set to upper case																| `"Unknown"`									|
| university   | `str`              | `str`				| Title case																	| `"Did not attend"`							|
| degree       | `str`              | `str`				| Reformat to `"1:1"`, `"2:1"`, `"2:2"` and `"3:1"`								| `"Did not attend"` if null with `university`	|
| invited_date | `float`            | `datetime`		| Japanese format: `yyyy-mm-dd` <br>Combine `invited_date` and `month` columns	| `1900-01-01`									|
| invited_by   | `str`              | `str`				| Title case and correct misspelled names										| `"Not invited"`								|

## Further details
### Dropped columns
- `month` -> combined into `invited_date`
- `phone_number` -> not required for PowerBI analysis
