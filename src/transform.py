from transformationScripts.transform_json import *

def transform(data:dict):
    finalDict = {}
    newDictStrengths = {"strengths":transform_strengths(data["json"].copy(deep=True))}
    finalDict.update(newDictStrengths)
    print(finalDict)
    return finalDict