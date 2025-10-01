from transformationScripts.transform_json import *
from transformationScripts.person_id_mapping import *
from transformationScripts.transform_csv_applicants import *

def transform(dict_of_dfs):
    finalDict = {}


    #get applicants csv data
    transformed_applicants = transform_applicants(dict_of_dfs["applicants_csv"])

    #Set personID for applicants_df
    #transformed_applicants needs name, date in datetime 
    applicants_df = set_person_id_for_applicants(transformed_applicants)

    #Create mapping df
    mapping_df = make_person_id_mapping_df(applicants_df)

    #Create frequency dictionary
    names_freq = get_name_frequency_dict(mapping_df['name'])

    '''
    #Set person ids   (mappingdf,dictionary,df)
    #For each transformed dataframe
    #Need name column 'name'and date column 'date' (replace data with transformed data)
    #id_df = set_person_id('data',mapping_df,names_freq,course=False)
    '''

    #transform applicants csv
    #transform jsons

    ## Strengths
    strengthDf = transform_strengths(dict_of_dfs["json"].copy(deep=True))
    #set strengths to have a person id and remove the names and dates
    id_strengths = id_df = set_person_id(strengthDf,mapping_df,names_freq,course=False)
    id_strengths.drop(['name','date'],axis=1)
    newDictStrengths = {"strengths": id_strengths}

    #add strengths to final dict
    finalDict.update(newDictStrengths)


    ## Weaknesses
    weeknessDf = transform_weaknesses(dict_of_dfs["json"].copy(deep=True))
    #set strengths to have a person id and remove the names and dates
    id_weaknesses = id_df = set_person_id(weeknessDf,mapping_df,names_freq,course=False)
    newDictWeaknesses = {"weaknesses": id_weaknesses}

    #add strengths to final dict
    finalDict.update(newDictWeaknesses)


    #transform course behaviour csv

    

    #Assemble dfs that match tables in ERD

    return finalDict
