# Data503-Final-Project

### Contents

- Intro
  - Tech Stack 
  - Instructions for Installation
  - Operating Instructions
  - Authors and Acknowledgements 

### Intro 

Project Overview: 

1. ETL Timeline based on fictionalised version of Sparta Global 
   - Candidates apply and invited to Sparta Day (Assessment day) : .csv file, .txt file
   - After, each candidate is interviewed for strengths, 	weaknesses, capabilities --> Pass, 	Fail, Career interest : .json file per candidate
   - Join Academy; Candidates assessed on 6 behaviours, on a score out of 8 : .csv file
2. Data is stored on Azure in two containers:
   - Academy (all files are there)
   - Talent  (majority of files are there, not all .json files per candidate tho)

Should include an fully normalised SQL database with all of the data, and provide a single person of view at the end of it (i.e track a single person from Talent to Academy).

Actual Deliverables:
        - Trello board 
        - GitHub Repo with code to ETL
        - Power BI dashboard
        - Presentation 

#### Contribution rules 

- Functions should have doc strings
- Functions also include type hints ?
- Passes some kind of test please
- Function name should make sense (is a doing thing)
- Commit at least twice a day (Before Lunch, before EOD, maybe before 16:00?)
- Commit with some kind of useful message that will describe what you did 
  - Potential format??: 
  - Sign off : Name and Time (use git thing that aurora said)
- Potentially use a formatting tool to make code all consistent 
- Add to requirements when you push
  - pip freeze >> Requirements.txt 
- Title your test functions with the following format:
  - test_<function>.py
- Variables are lowercase uppercase 
- Functions are lowercase and underscores
- One function per file (acc one process)

#### Tech Stack 

#### Instructions for Installation 

#### Operating Instructions 

#### Authors and Acknowledgements 

### Repo Rules

#### Branch Naming Conventions

Branches should be named by their features, not by the Authors 

#### Pull Requests

Pulls will have to be requested and approved by Edward before they will be committed to the main branch.

#### Further Documentation
[Data Transformation Log](notes/data_transformation_log.md)