from transformationScripts.transform_json import *
from transformationScripts.person_id_mapping import *
from transformationScripts.transform_csv_applicants import *
from transformationScripts.transform_csv_course_behaviours import *

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

    applicant_sparta_day_merge = applicants_df[['invited_by','person_id']]
    applicant_sql_table = applicants_df.copy().drop(columns=['id','city','address','postcode','invited_by','invited_date'])
    
    applicant_sql_table = applicant_sql_table.rename(columns={"name":"person_name","dob":"date_of_birth","uni":"university","degree":"university_grade"})
    ## add applicants
    newDictApp = {"applicants":applicant_sql_table}
    finalDict.update(newDictApp)

    ## postcode table
    postcodeDf = applicants_df[['postcode','city']].copy()
    postcodeDf = postcodeDf.drop_duplicates()
    postcodeDf["post_code_id"] = range(1, len(postcodeDf) + 1)
    postcodeDf = postcodeDf.rename(columns={"postcode":"post_code"})
    newDictPost = {"postcode":postcodeDf}
    finalDict.update(newDictPost)

    ## address table
    addressDf = applicants_df[['address','postcode']].copy()
    addressDf = addressDf.rename(columns={"postcode":"post_code"})
    addressDf = pd.merge(addressDf,postcodeDf, on=["post_code"])
    addressDf = addressDf.drop(columns=["post_code","city"])
    addressDf = addressDf.drop_duplicates()
    addressDf = addressDf.rename(columns={"address":"address_line"})
    addressDf["address_id"] = range(1, len(addressDf) + 1)
    newDictAddress = {"address":addressDf}
    finalDict.update(newDictAddress)

    ## person-address

    addressDf_forPerson = applicants_df[['address','id']].copy()
    addressDf_forPerson = addressDf_forPerson.rename(columns={"address":"address_line"})
    addressDf_forPerson = pd.merge(addressDf_forPerson,addressDf, on=["address_line"])
    addressDf_forPerson = addressDf_forPerson.drop(columns=["address_line","post_code_id"])
    addressDf_forPerson = addressDf_forPerson.rename(columns={"id":"person_id"})
    addressDf_forPerson = addressDf_forPerson.drop_duplicates()
    newDictAddressPerson = {"address_person":addressDf_forPerson}
    finalDict.update(newDictAddressPerson)



    print("applicants.csv Transformed")

    #transformed txt
    txts = dict_of_dfs["txt"]
    id_txts = set_person_id(txts,mapping_df,names_freq,course=False)
    id_txts = id_txts.drop(["name"],axis=1)
    sparta_day_sql = id_txts.drop(columns=['psychometric_score','presentation_score','id'])
    sparta_day_sql = sparta_day_sql.rename(columns={"date": "day_Date", "location":"day_location"})
    sparta_day_sql = sparta_day_sql.drop_duplicates()
    #add sparta day to final dict
    newDictTxt = {"sparta_day":sparta_day_sql}
    finalDict.update(newDictTxt)


    print("txt`s Transformed")

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
    print("Json-strengths Transformed")

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
    print("Json-weaknesses Transformed")

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
    print("Json-techSkills Transformed")

    #SpartaDayResults + txt SpartaDayResults
    json_data_results = get_json_sparta_day_results(dict_of_dfs["json"].copy(deep=True))
    json_data_results_id = set_person_id(json_data_results,mapping_df,names_freq,course=False)
    json_data_results_id = json_data_results_id.drop(columns=['date'])    
    big_sparta_day_table = pd.merge(json_data_results_id, id_txts.copy(), on=["id"])
    big_sparta_day_table = big_sparta_day_table.drop(columns=['date','name','location'])
    big_sparta_day_table = big_sparta_day_table.rename(columns={
        "id": "person_id",
        "presentation_score":"presentation",
        "psychometric_score":"psychometric",
        "financial_support_self":"financial_support"
        })
    big_sparta_day_table = pd.merge(big_sparta_day_table, applicant_sparta_day_merge, on=["person_id"])
    
    newDictSpartaDay = {"sparta_day_results": big_sparta_day_table}
    finalDict.update(newDictSpartaDay)
    print("Json-SpartaDayResults Transformed")

    print("Json's Transformed")


    #transform course behaviour csv

    csv_course = transform_csv_course_behaviours_course(dict_of_dfs["course_behaviours_csv"].copy(deep=True))
    newDictCsv_course = {"courses": csv_course}
    finalDict.update(newDictCsv_course)
    


    csv_behaviours = transform_csv_course_behaviours_behaviour_scores(dict_of_dfs["course_behaviours_csv"].copy(deep=True))
    csv_behaviours = csv_behaviours.rename(columns={"start_date":"date"})
    id_behaviours = set_person_id(csv_behaviours,mapping_df,names_freq,course=False)
    id_behaviours = id_behaviours.drop(columns=['date','name'])
    id_behaviours = id_behaviours.rename(columns={"professionalism":"professionalisum","independence":"independance","id":"person_id"})
    newDictCsv_scores = {"behaviours":id_behaviours}
    finalDict.update(newDictCsv_scores)

    print("CourseBehaviours.csv Transformed")

    return finalDict
