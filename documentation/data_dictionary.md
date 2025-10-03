# Data Dictionary
&larr; [Back to README](../README.md)

## behaviour_scores
| Variable			| Data Type |
|-------------------|-----------|
|person_id			| `INTEGER`	|
|course_id			| `INTEGER`	|
|week				| `INTEGER`	|
|analytical			| `INTEGER`	|
|independence		| `INTEGER`	|
|determination		| `INTEGER`	|
|professionalism	| `INTEGER`	|
|studious			| `INTEGER`	|
|imaginative		| `INTEGER`	|

## course
| Variable		|	Data Type	|
|---------------|---------------|
|course_id		| `INTEGER`		|
|subject_name	| `VARCHAR`		|		
|trainer_name	| `VARCHAR`		| 
|start_date		| `DATE`		|
|course_number	| `INT`			|		

## person
| Variable			| Data Type |
|-------------------|-----------|
|person_id			| `INTEGER`	|
|name 				| `VARCHAR`	| 
|gender				| `VARCHAR`	|	 
|date_of_birth		| `DATE`	|
|email				| `VARCHAR`	|	 
|university 		| `VARCHAR`	| 
|university_grade	| `VARCHAR`	| 
|application_date	| `DATE`	|

 
## person_address
| Variable -|	Data Type | 
|-----------|-----------|
person_id	| `INTEGER` |
address_id	| `INTEGER` | 

## address
| Variable		| Data Type | 
|---------------|-----------|
| address_id	| `INTEGER` |
| post_code_id	| `INTEGER` |
| address_line	| `VARCHAR` | 

## post_code
| Variable		|Data Type	| 
|---------------|-----------|
|post_code_id	| `INTEGER` |
|post_code		| `VARCHAR` | 
|city			| `VARCHAR` | 

## sparta_days
| Variable		| Data Type | 
|---------------|-----------|
|sparta_day_id	| `INTEGER` |
|date			| `DATE`	|
|location		| `VARCHAR` | 

## sparta_day_results
| Variable			| Data Type | 
|-------------------|-----------|
|person_id			| `INTEGER` |
|sparta_day_id		| `INTEGER` |
|psychometrics		| `INTEGER` |
|presentation		| `INTEGER` |
|self_development	| `BIT`		|
|geo_flex			| `BIT`		|
|financial_support	| `BIT`		|
|result				| `BIT`		|
|course_interest	| `VARCHAR` | 
|invited_by			| `VARCHAR` | 
|invited_date		| `DATE`	|

## sparta_day_results_tech_self_score
| Variable		| Data Type |
|---------------|-----------|
|tech_name		| `VARCHAR` | 
|person_id		| `INTEGER` |
|sparta_day_id	| `INTEGER` |
|score			| `INTEGER` |

## sparta_day_results_strengths
| Variable		| Data Type |
|---------------|-----------|
|strength_name	| `VARCHAR` | 
|person_id		| `INTEGER` |
|sparta_day_id	| `INTEGER` |

## sparta_day_results_weaknesses
| Variable			| Data Type |
|-------------------|-----------|
|weaknesses_name	| `VARCHAR` | 
|person_id			| `INTEGER` |
|sparta_day_id		| `INTEGER` |
