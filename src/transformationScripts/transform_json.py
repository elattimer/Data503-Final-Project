from extract_json import extract_json
from transform_json_lists import *
from transform_json_tech_self_score import get_tech_self_score
from transform_json_course_interest import transform_course_interest
from transform_json_finincial_support_self import transform_financial_support_self
from transform_json_geo_flex import transform_geo_flex
from transform_json_result import transform_result
from transform_json_self_development import transform_self_development
from transform_json_date_fix import fix_date


from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from warnings import filterwarnings


subscription_id = "cd36dfff-6e85-4164-b64e-b4078a773259"
resource_group = "data503"
location = "uksouth"
storage_account_name = "data503paulastorage"
account_url = f"https://{storage_account_name}.blob.core.windows.net"

# az login in bash
credential = DefaultAzureCredential()

# Create instance of blob service client class for the specific account and user credentials
blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

# Get the client for the container from blob_service_client
container_talent = blob_service_client.get_container_client("talent")

filterwarnings("ignore", category=FutureWarning)

container_talent = blob_service_client.get_container_client("talent")

def get_strengths_frame(data : pd.DataFrame) -> pd.DataFrame:
    return transform_strengths(data)

def get_weaknesses_frame(data : pd.DataFrame) -> pd.DataFrame:
    return transform_weaknesses(data)

def get_tech_skills_frame(data : pd.DataFrame) -> pd.DataFrame:
    return get_tech_self_score(data)

def get_json_sparta_day_results(data: pd.DataFrame) -> pd.DataFrame:
    dataEnd = transform_self_development(data)
    dataEnd = transform_course_interest(dataEnd)
    dataEnd = transform_financial_support_self(dataEnd)
    dataEnd = transform_geo_flex(dataEnd)
    dataEnd = transform_result(dataEnd)
    dataEnd = fix_date(dataEnd)
    dataEnd = dataEnd.drop(columns=['tech_self_score', 'strengths', 'weaknesses'])
    dataEnd = dataEnd.drop_duplicates()
    return dataEnd



# # Testing area
# dataOrig = extract_json(container_client=container_talent)
# dataSpartaDay = get_json_sparta_day_results(dataOrig.copy(deep=True))
# print(dataSpartaDay)

# print(get_strengths_frame(dataOrig.copy(deep=True)).drop_duplicates().isnull().sum())
# print(get_weaknesses_frame(dataOrig.copy(deep=True)).drop_duplicates().isnull().sum())
# print(get_tech_skills_frame(dataOrig.copy(deep=True)).drop_duplicates().isnull().sum())