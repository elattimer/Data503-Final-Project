from transformationScripts.transform_json import *
def transform(dict_of_dfs):
    finalDict = {}
    #transform applicants csv
    #transform jsons
    newDictStrengths = {"strengths":transform_strengths(dict_of_dfs["json"].copy(deep=True))}
    finalDict.update(newDictStrengths)
    #transform course behaviour csv

    #Set personID for applicants_df

    #Create mapping df

    #Create frequency dictionary

    #Set person ids   (mappingdf,dictionary,df)

    #Assemble dfs that match tables in ERD

    return finalDict
