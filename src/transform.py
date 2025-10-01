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


    #transformed txt
    txts = dict_of_dfs["txt"]
    id_txts = set_person_id(txts,mapping_df,names_freq,course=False)
    id_txts = id_txts.drop(["name"],axis=1)
    #transform jsons

    ## Strengths
    strengthDf = transform_strengths(dict_of_dfs["json"].copy(deep=True))

    #set strengths to have a person id and remove the names and dates
    id_strengths = set_person_id(strengthDf,mapping_df,names_freq,course=False)
    id_strengths = id_strengths.drop(['name'],axis=1)
    id_strengths = id_strengths.drop(['date'],axis=1)
    id_strengths= pd.merge(strengthDf, id_txts, on=["id"])
    id_strengths = id_strengths.drop(['date'],axis=1)
    id_strengths = id_strengths.rename(columns={"id": "person_id"})
    id_strengths = id_strengths.drop(['location','psychometric_score','presentation_score'],axis=1)
    newDictStrengths = {"strengths": id_strengths}

    #add strengths to final dict
    finalDict.update(newDictStrengths)


    ## Weaknesses
    weeknessDf = transform_weaknesses(dict_of_dfs["json"].copy(deep=True))
    weeknessDf= pd.merge(weeknessDf, txts, on="date")

    #set strengths to have a person id and remove the names and dates
    id_weaknesses = set_person_id(weeknessDf,mapping_df,names_freq,course=False)
    id_weaknesses = id_weaknesses.rename(columns={"id": "person_id"})
    id_weaknesses = id_weaknesses.drop(['name','date'],axis=1)
    newDictWeaknesses = {"weaknesses": id_weaknesses}

    #add strengths to final dict
    finalDict.update(newDictWeaknesses)


    #transform course behaviour csv

    

    #Assemble dfs that match tables in ERD

    return finalDict
