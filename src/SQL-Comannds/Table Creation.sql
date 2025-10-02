IF NOT EXISTS (
    SELECT 1 
    FROM sys.tables 
    WHERE name = 'person'
)
BEGIN
    CREATE TABLE person (
        person_id INT PRIMARY KEY,
        person_name VARCHAR(50),
        gender VARCHAR(50),
        date_of_birth DATE,
        email VARCHAR(100),
        university VARCHAR(150),
        university_grade VARCHAR(50)
    );
END
IF NOT EXISTS (
    SELECT 1 
    FROM sys.tables 
    WHERE name = 'courses'
)
BEGIN
    CREATE TABLE courses (
        course_id INT PRIMARY KEY,
        subject_name VARCHAR(50),
        trainer_name VARCHAR(50),
        start_date DATE,
        class_number INT
    );
END

IF NOT EXISTS (
    SELECT 1 
    FROM sys.tables 
    WHERE name = 'behavioursScore'
)
BEGIN
    CREATE TABLE behavioursScore (
        person_id INT,
        week INT,
        course_id INT,
        analytical INT,
        independance INT,
        determination INT,
        professionalisum INT,
        studious INT,
        imaginative INT,
        PRIMARY KEY(person_id, course_id, week),
        FOREIGN KEY (person_id) REFERENCES person(person_id),
        FOREIGN KEY (course_id) REFERENCES course(course_id),
    );
END

IF NOT EXISTS (
    SELECT 1 
    FROM sys.tables 
    WHERE name = 'post_codes'
)
BEGIN
    CREATE TABLE post_codes(
        post_code_id INT PRIMARY KEY,
        post_code VARCHAR(50),
        city VARCHAR(50),
    );
END

IF NOT EXISTS (
    SELECT 1 
    FROM sys.tables 
    WHERE name = 'addresses'
)
BEGIN
    CREATE TABLE addresses (
        address_id INT PRIMARY KEY,
        post_code_id INT,
        address_line VARCHAR(50),
        FOREIGN KEY (post_code_id) REFERENCES post_codes(post_code_id),
    );
END

IF NOT EXISTS (
    SELECT 1 
    FROM sys.tables 
    WHERE name = 'person_addresses'
)
BEGIN
    CREATE TABLE person_addresses (
        person_id INT,
        address_id INT,
        PRIMARY KEY(person_id,address_id),
        FOREIGN KEY (person_id) REFERENCES person(person_id),
        FOREIGN KEY (address_id) REFERENCES addresses(address_id),
    );
END

IF NOT EXISTS (
    SELECT 1 
    FROM sys.tables 
    WHERE name = 'sparta_day'
)
BEGIN
    CREATE TABLE sparta_day (
        sparta_day_id INT PRIMARY KEY,
        day_Date date,
        day_location VARCHAR(50)
    );
END

IF NOT EXISTS (
    SELECT 1 
    FROM sys.tables 
    WHERE name = 'sparta_day_results'
)
BEGIN
    CREATE TABLE sparta_day_results (
        person_id INT,
        sparta_day_id INT,
        psychometric INT,
        presentation INT,
        self_development BIT,
        geo_flex BIT,
        financial_support BIT,
        result BIT,
        course_interest VARCHAR(50),
        invited_by VARCHAR(50),
        PRIMARY KEY(person_id, sparta_day_id),
        FOREIGN KEY (person_id) REFERENCES person(person_id),
        FOREIGN KEY(sparta_day_id) REFERENCES sparta_day(sparta_day_id),
    );
END

IF NOT EXISTS (
    SELECT 1 
    FROM sys.tables 
    WHERE name = 'sparta_day_strengths_results'
)
BEGIN
    CREATE TABLE sparta_day_strengths_results (
        strength_name VARCHAR(50),
        person_id INT,
        sparta_day_id INT,
        PRIMARY KEY (strength_name, person_id, sparta_day_id),
        FOREIGN KEY (person_id) REFERENCES person(person_id),
        FOREIGN KEY (sparta_day_id) REFERENCES sparta_day(sparta_day_id)    
    );
END

IF NOT EXISTS (
    SELECT 1 
    FROM sys.tables 
    WHERE name = 'sparta_day_weaknesses_results'
)
BEGIN
    CREATE TABLE sparta_day_weaknesses_results (
        weaknesses_name VARCHAR(50),
        person_id INT,
        sparta_day_id INT,
        PRIMARY KEY (weaknesses_name, person_id, sparta_day_id),
        FOREIGN KEY (person_id) REFERENCES person(person_id),
        FOREIGN KEY (sparta_day_id) REFERENCES sparta_day(sparta_day_id)    
    );
END

IF NOT EXISTS (
    SELECT 1 
    FROM sys.tables 
    WHERE name = 'sparta_day_tech_results'
)
BEGIN
    CREATE TABLE sparta_day_tech_results (
        tech_name VARCHAR(50),  
        score INT,
        person_id INT,
        sparta_day_id INT,
        PRIMARY KEY (tech_name, person_id, sparta_day_id),
        FOREIGN KEY (person_id) REFERENCES person(person_id),
        FOREIGN KEY (sparta_day_id) REFERENCES sparta_day(sparta_day_id),
    );
END