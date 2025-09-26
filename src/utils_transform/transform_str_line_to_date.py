from datetime import datetime

def transform_str_line_to_date(date_string: str):
    ''''
    input is format Thursday 1 August 2019 as a string
    output is 2019-08-10 as a date object
    '''
    space_position = date_string.index(" ")
    stripped_date_string = date_string[space_position:]
    datetime_object = datetime.strptime(stripped_date_string, "%d %B %Y")
    date_object = datetime_object.date()
    return date_object