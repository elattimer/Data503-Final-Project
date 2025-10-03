# Data503-Final-Project

## Contents
1. [Project Brief](#project-brief)
2. [Contribution Rules](#contribution-rules)
3. [Installation Instructions](#installation-instructions)
4. [Operating Instructions](#operating-instructions)
5. [Additional Documentation](#additional-documentation)

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
- Pull requests to be approved by a colleague, not yourself!

### Commits and Pushes
- Commit after a significant working change
- Include a descriptive message that summarises the changes made
- Push at least twice a day &rarr; before lunch and before EOD

### Codebase
- Pythonic formatting please!
- Add to `requirements.txt` when you push: `pip freeze >> Requirements.txt `
- **Functions:** descriptive names, doc strings, type hints
- One process per file
- Ensure test coverage
- Remember testing file format: `test_<file_name>.py`

## Tech Stack 
- Azure
- Python
- MSSQL on Ubuntu server
- SQL management tools - MS SQL Management Studio, VS 2022
- PowerBI

## Installation and set-up Instructions 
### Clone repo 
    git clone https://github.com/elattimer/Data503-Final-Project.git

### Install libraries via requirements.txt
    pip install -r requirements.txt

### Create Azure VM (on Ubuntu server)
1. Create a new resource and select the Ubuntu OS of your choice
2. (Optional) Set up [history logging](https://www.digitalocean.com/community/tutorials/how-to-use-bash-history-commands-and-expansions-on-a-linux-vps)

### Install MSSQL
```
curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
curl -fsSL https://packages.microsoft.com/config/ubuntu/24.04/mssql-server-preview.list | sudo tee /etc/apt/sources.list.d/mssql-server-preview.list
sudo apt-get update
sudo apt-get install -y mssql-server

# Set password
sudo /opt/mssql/bin/mssql-conf setup

# Check the SQL server is running
systemctl status mssql-server --no-pager
```

### Connect to VM
    ssh -i <ssh-key-path> <vm-username>@<vm-ip-address>

### Firewall and SSH tunnelling
```
# Open VM for tunneling
sudo ufw allow 1433/tcp
sudo ufw reload
sudo ss -tlnp | grep 1433

# Start tunnel (exit current terminal) in a new terminal window
eval "$(ssh-agent -s)"
ssh-add data-503-project-key.pem

# Set 127.0.0.1 port 1433 as your new connection
ssh -L 1433:127.0.0.1:1433 <azure-username>@<azure-vm-ip-address>
```

### Define SQL tables
Run the [table_creation.sql](src/sql_commands/table_creation.sql) queries with your software of choice


## Operating Instructions 
- `python src/main.py` to run the ETL pipeline
- Access the SQL database with your SQL management tool of choice

## Additional Documentation
- [ERD](documentation/erd.md)
- [Data Dictionary](documentation/data_dictionary.md)
- [Data Transformation Review](documentation/data_transformation_review.md)
- [Development Notes](documentation/dev_notes.md)

### External links
- [Project Overview - Google Docs](https://docs.google.com/document/d/16dbxWPakB2JyXFFWVX_WuNCb8eEJxZH-aQjVm09Ec84/edit?usp=sharing)
- [Product Backlog - Google Docs](https://docs.google.com/document/d/1_DXbBCsMrntUOGPmtWWk9bz7DS5yMR1-4RLiHH21pWw/edit?usp=sharing)
- [ERD - LucidChart](https://lucid.app/lucidchart/3c2c3539-f808-4dc6-ab6e-0989cc190aa9/edit?invitationId=inv_9cd65a09-b610-4e94-8768-9d397872cc4d&page=0_0#)