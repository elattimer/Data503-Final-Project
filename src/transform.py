from transformationScripts.transform_json import *
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

    #Create mapping df

    #Create frequency dictionary

    #Set person ids   (mappingdf,dictionary,df)

    #Assemble dfs that match tables in ERD

    return finalDict
