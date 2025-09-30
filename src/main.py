import extract
import transform
import load
import copy

# extract
dataRaw = extract.extract()

# transform
dataTransformed = transform.transform(dataRaw.copy())


# load 
load.load(dataTransformed)