def transform_location_line(location_line: str) -> str:
    '''
    takes in <LOCATION> ACADEMY
    returns LOCATION
    '''
    list_of_words = location_line.split(" ")
    return list_of_words[0]