from transformationScripts.transform_json import *
from transformationScripts.person_id_mapping import *
def transform(dict_of_dfs):
    finalDict = {}
    #transform applicants csv
    #transform jsons

    ## Strengths
    strengthDf = transform_strengths(dict_of_dfs["json"].copy(deep=True))
    #set strengths to have a person id and remove the names and dates

    newDictStrengths = {"strengths": strengthDf}

    #add strengths to final dict
    finalDict.update(newDictStrengths)


    ## Weaknesses
    weeknessDf = transform_strengths(dict_of_dfs["json"].copy(deep=True))
    #set strengths to have a person id and remove the names and dates

    newDictStrengths = {"strengths": strengthDf}

    #add strengths to final dict
    finalDict.update(newDictStrengths)

    #transform course behaviour csv

    #Set personID for applicants_df
    applicants_df = set_person_id_for_applicants(transformed_applicants)

    #Create mapping df
    mapping_df = make_person_id_mapping_df(applicants_df)

    #Create frequency dictionary
    names_freq = get_name_frequency_dict(mapping_df['name'])

    #Set person ids   (mappingdf,dictionary,df)
    #For each transformed dataframe
    #Need name column 'name'and date column 'date'
    id_df = set_person_id(data,mapping_df,names_freq,course=False)

    #Assemble dfs that match tables in ERD

    return finalDict
