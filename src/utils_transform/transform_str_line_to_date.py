from datetime import datetime

def transform_str_line_to_date(date_string: str):
    ''''
    input is format Thursday 1 August 2019 as a string
    output is 2019-8-1 00:00:00 as a datetime object
    '''
    space_position = date_string.index(" ")
    stripped_date_string = date_string[space_position:]
    date_object = datetime.strptime(stripped_date_string, "%d %B %Y")
    print(date_object)
    return date_object