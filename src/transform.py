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
    sparta_day_sql = id_txts.drop(columns=['psychometric_score','presentation_score','id'])
    sparta_day_sql = sparta_day_sql.rename(columns={"date": "day_Date", "location":"day_location"})
    #add sparta day to final dict
    newDictTxt = {"sparta_day":sparta_day_sql}
    finalDict.update(newDictTxt)

    #transform jsons

    ## Strengths
    strengthDf = transform_strengths(dict_of_dfs["json"].copy(deep=True))

    #set strengths to have a person id and remove the names and dates
    id_strengths = set_person_id(strengthDf,mapping_df,names_freq,course=False)
    id_strengths = id_strengths.drop(columns=['name'])
    id_strengths = id_strengths.drop(columns=['date'])
    id_strengths = pd.merge(id_strengths, id_txts.copy(), on=["id"])
    id_strengths = id_strengths.drop(columns=['date'])
    id_strengths = id_strengths.rename(columns={"id": "person_id", "strength":"strength_name"})
    id_strengths = id_strengths.drop(columns=['location','psychometric_score','presentation_score'])
    newDictStrengths = {"strengths": id_strengths}

    #add strengths to final dict
    finalDict.update(newDictStrengths)


    ## Weaknesses
    weaknessesDf = transform_weaknesses(dict_of_dfs["json"].copy(deep=True))

    #set Weaknesses to have a person id and remove the names and dates
    id_weaknesses = set_person_id(weaknessesDf,mapping_df,names_freq,course=False)
    id_weaknesses = id_weaknesses.drop(columns=['name'])
    id_weaknesses = id_weaknesses.drop(columns=['date'])
    id_weaknesses = pd.merge(id_weaknesses, id_txts.copy(), on=["id"])
    id_weaknesses = id_weaknesses.drop(columns=['date'])
    id_weaknesses = id_weaknesses.rename(columns={"id": "person_id", "weakness":"weaknesses_name"})
    id_weaknesses = id_weaknesses.drop(columns=['location','psychometric_score','presentation_score'])
    newDictWeaknesses = {"weaknesses": id_weaknesses}

    #add Weaknesses to final dict
    finalDict.update(newDictWeaknesses)


    ## TechSkills
    techSkillsDf = get_tech_skills_frame(dict_of_dfs["json"].copy(deep=True))

    #set TechSkills to have a person id and remove the names and dates
    id_techSkills = set_person_id(techSkillsDf,mapping_df,names_freq,course=False)
    id_techSkills = id_techSkills.drop(columns=['name'])
    id_techSkills = id_techSkills.drop(columns=['date'])
    id_techSkills = pd.merge(id_techSkills, id_txts.copy(), on=["id"])
    id_techSkills = id_techSkills.drop(columns=['date'])
    id_techSkills = id_techSkills.rename(columns={"id": "person_id"})
    id_techSkills = id_techSkills.drop(columns=['location','psychometric_score','presentation_score'])
    newDictTechSkills = {"tech_skills": id_techSkills}

    #add TechSkills to final dict
    finalDict.update(newDictTechSkills)


    #SpartaDayResults + txt SpartaDayResults
    json_data_results = get_json_sparta_day_results(dict_of_dfs["json"].copy(deep=True))
    json_data_results_id = set_person_id(json_data_results,mapping_df,names_freq,course=False)
    big_sparta_day_table = pd.merge(json_data_results_id, id_txts.copy(), on=["id"])


    #transform course behaviour csv

    

    #Assemble dfs that match tables in ERD

    return finalDict
