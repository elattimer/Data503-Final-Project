import pytest
import pandas as pd
from datetime import datetime
from src.transformationScripts.extract_txt import extract_txt_to_df

def test_extract_txt():
    raw_text = """Tuesday 9 April 2019
London Academy

DELILA GARRET -  Psychometrics: 51/100, Presentation: 23/32
HOMER HYMER -  Psychometrics: 64/100, Presentation: 23/32
WOLFY DINZEY -  Psychometrics: 58/100, Presentation: 13/32
LEAH EARNEY -  Psychometrics: 57/100, Presentation: 16/32
REGAN RAWLINS -  Psychometrics: 53/100, Presentation: 16/32
GAN SUERMEIER -  Psychometrics: 48/100, Presentation: 19/32
COR BY ADNETT -  Psychometrics: 57/100, Presentation: 16/32
NARA BAG-GER -  Psychometrics: 57/100, Presentation: 23/32
AUGUSTIN WINTERS -  Psychometrics: 53/100, Presentation: 23/32
FRANCISKA KEZOR -  Psychometrics: 60/100, Presentation: 20/32
MIMI BEAMAND -  Psychometrics: 53/100, Presentation: 18/32
MORGANA MCDARMID -  Psychometrics: 70/100, Presentation: 19/32
LY;NNELL SAMBER -  Psychometrics: 58/100, Presentation: 21/32
AXEL SCATCHAR -  Psychometrics: 59/100, Presentation: 16/32
MIGUEL BO'dfWEN -  Psychometrics: 58/100, Presentation: 21/32

"""

    expected = pd.DataFrame({
        'date':[
            datetime(2019,4,9),datetime(2019,4,9),datetime(2019,4,9),
            datetime(2019,4,9),datetime(2019,4,9),datetime(2019,4,9),
            datetime(2019,4,9),datetime(2019,4,9),datetime(2019,4,9),
            datetime(2019,4,9),datetime(2019,4,9),datetime(2019,4,9),
            datetime(2019,4,9),datetime(2019,4,9),datetime(2019,4,9)
        ],
        'location':[
            'London','London','London','London','London',
            'London','London','London','London','London',
            'London','London','London','London','London'
        ],
        'name':[
            'DELILA GARRET','HOMER HYMER','WOLFY DINZEY','LEAH EARNEY',
            'REGAN RAWLINS','GAN SUERMEIER','COR BY ADNETT','NARA BAG-GER',
            'AUGUSTIN WINTERS','FRANCISKA KEZOR','MIMI BEAMAND',
            'MORGANA MCDARMID','LY;NNELL SAMBER','AXEL SCATCHAR','MIGUEL BO\'DFWEN'
        ],
        'psychometric_score':[51,64,58,57,53,48,57,57,53,60,53,70,58,59,58],
        'presentation_score':[23,23,13,16,16,19,16,23,23,20,18,19,21,16,21],
        'sparta_day_id':[None]*15
    })

    result = extract_txt_to_df(test=True,test_data=raw_text)
    print(expected['name'])
    print(result['name'])
    pd.testing.assert_frame_equal(
        result.reset_index(drop=True),
        expected.reset_index(drop=True)
    )
