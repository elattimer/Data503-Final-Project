# `df_behaviour_scores`
&larr; [Back to transformation review](../data_transformation_review.md)

## Data table	
| Column name				| Original data type	| Target data type	| Transformation details									 | Null placeholder rule |
|---------------------------|-----------------------|-------------------|------------------------------------------------------------|-----------------------|
| course_id					| n/a					| `int`				| Matched from df_course dictionary                          | n/a					 |
| start_date				| `str`					| `datetime`		| Split file name string, convert to datetime                | n/a					 |
| name						| `str`					| `str`				| Set to uppercase                                           | n/a					 |
| week						| `str`					| `int`				| Melt and pivot, extract week number, convert to int		 | n/a				     |
| analytical				| `str`					| `int`				| Melt and pivot, match to week, convert to int				 | `0`					 |
| independence				| `str`					| `int`				| Melt and pivot, match to week, convert to int				 | `0`	                 |
| determination				| `str`					| `int`				| Melt and pivot, match to week, convert to int		 		 | `0`					 |
| professionalism			| `str`					| `int`				| Melt and pivot, match to week, convert to int	         	 | `0`					 |
| studious					| `str`					| `int`				| Melt and pivot, match to week, convert to int	             | `0`					 |
| imaginative				| `str`					| `int`				| Melt and pivot, match to week, convert to int	             | `0`	   				 |

## Further details
### Data contained in column headers
Data for the specific course week is contained in the column header for each behaviour (e.g. `Studious_W4`). This requires melting the DataFrame in order to access the column headers as string values, splitting them to access the respective week number, and finally assigning that number to a DataFrame and matching with the correct behaviour scores.