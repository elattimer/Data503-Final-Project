# Data503-Final-Project

## Contents
1. [Project Brief](#project-brief)
2. [Contribution Rules](#contribution-rules)
x. [Additional Documentation](#additional-documentation)

## Project Brief
### Overview
We have been tasked with answering the following business questions regarding the Sparta Academy:

    1. Which members of the Talent Team are performing best?
    2. How many trainees are removed at each stage of the course? What factors influence removals?
    3. Which factors at interview stage predict high performance on the course?  
    4. How are courses performing on any given date?

The raw data tracks a candidate's journey from the application process to their enrolment and performance on an Academy training course. It is stored on Azure in two containers:
- `Academy` - course performance data
- `Talent` - applicant and assessment day data


### Project Steps
1. ERD for an SQL database in 3NF and providing a single person view
2. ETL pipeline from Azure to database
3. PowerBI dashboard to visualise data
4. Presentation to answer business questions and describe our project workflow

### Deliverables
- Trello board 
- GitHub repo with documentation and code for ETL pipeline
- Power BI dashboard
- Presentation 

## Contribution Rules 
### Repo Organisation
- Branch name = feature, not author
- Pull requests to be approved by a colleage, not yourself!

### Commits
- Commit at least twice a day &rarr; before lunch and before EOD
- Descriptive message that summarises the changes made

### Codebase
- Pythonic formatting please!
- Add to `requirements.txt` when you push: `pip freeze >> Requirements.txt `
- **Functions:** descriptive names, doc strings, type hints
- One process per file
- Ensure test coverage
- Remember testing file format: `test_<file_name>.py`



## Tech Stack 

## Instructions for Installation 

## Operating Instructions 

## Authors and Acknowledgements 




## Additional Documentation
- [ERD](documentation/erd.md)
- [Data Dictionary](documentation/data_dictionary.md)
- [Data Transformation Review](documentation/data_transformation_review.md)
- [Development Notes](documentation/dev_notes.md)

### External links
- [Project Overview - Google Docs](https://docs.google.com/document/d/16dbxWPakB2JyXFFWVX_WuNCb8eEJxZH-aQjVm09Ec84/edit?usp=sharing)
- [Product Backlog - Google Docs](https://docs.google.com/document/d/1_DXbBCsMrntUOGPmtWWk9bz7DS5yMR1-4RLiHH21pWw/edit?usp=sharing)
- [ERD - LucidChart](https://lucid.app/lucidchart/3c2c3539-f808-4dc6-ab6e-0989cc190aa9/edit?invitationId=inv_9cd65a09-b610-4e94-8768-9d397872cc4d&page=0_0#)