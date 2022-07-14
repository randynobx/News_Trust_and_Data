'''Data Wrangling Module'''

# Imports
import pandas as pd

###############################
###     Survey Encoding     ###
###############################

# Response Code -> Response Description
col_names = {
    'A1':'Very Conservative',
    'A2':'Conservative',
    'A3':'Moderate',
    'A4':'Liberal',
    'A5':'Very Liberal',
    'A6':'Great amount',
    'A7':'Fair amount',
    'A8':'Not very much',
    'A9':'None at all',
    'A10':'NYT',
    'A11':'WSJ',
    'A12':'USA_TODAY',
    'A13':'WaPo',
    'A14':'FoxNews',
    'A15':'Breitbart',
    'A16':'CNN',
    'A17':'BuzzFeed_News',
    'A18':'HuffPo',
    'A19':'Time',
    'A20':'USNWR',
    'A21':'Other',
    'A22':'Yes',
    'A23':'No',
    'A24':'Decrease Trust',
    'A25':'Increase Trust',
    'A26':'No Change',
    'A27':'Strongly approve',
    'A28':'Somewhat approve',
    'A29':'Somewhat disapprove',
    'A30':'Strongly disapprove',
    'A31':'18-29',
    'A32':'30-44',
    'A33':'45-59',
    'A34':'60+',
    'A35':'Female',
    'A36':'Male',
    'A37':'0-9,999',
    'A38':'10,000-24,999',
    'A39':'25,000-49,999',
    'A40':'50,000-74,999',
    'A41':'75,000-99,999',
    'A42':'100,000-124,999',
    'A43':'125,000-149,999',
    'A44':'150,000-174,999',
    'A45':'175,000-199,999',
    'A46':'200,000+',
    'A47':'Prefer not to answer',
    'A48':'New England',
    'A49':'Middle Atlantic',
    'A50':'East North Central',
    'A51':'West North Central',
    'A52':'South Atlantic',
    'A53':'East South Central',
    'A54':'West South Central',
    'A55':'Mountain',
    'A56':'Pacific',
    'A57':'iOS Phone/Tablet',
    'A58':'Android Phone/Tablet',
    'A59':'Other Phone/Tablet',
    'A60':'Windows Desktop/Laptop',
    'A61':'MacOS Desktop/Laptop',
    'A62':'Other Desktop/Laptop'
}

# Response -> Question
questions = {
    'Data_Access':['Decrease Trust', 'No Change', 'Increase Trust'],
    'General_Trust':['None at all', 'Not very much', 'Fair amount',
                     'Great amount'],
    'Income':['0-9,999', '10,000-24,999', '25,000-49,999', '50,000-74,999',
              '75,000-99,999', '100,000-124,999', '125,000-149,999',
              '150,000-174,999', '175,000-199,999', '200,000+',
              'Prefer not to answer'],
    'Trump_Approval':['Strongly disapprove', 'Somewhat disapprove',
                      'Somewhat approve', 'Strongly approve'],
    'Political_View':['Very Liberal', 'Liberal', 'Moderate', 'Conservative',
                      'Very Conservative'],
    'Pay_For_News':['Yes', 'No'],
    'Age':['18-29','30-44','45-59','60+'],
    'Gender':['Male', 'Female'],
    'Region':['New England','Middle Atlantic','East North Central',
              'West North Central','South Atlantic','East South Central',
              'West South Central','Mountain','Pacific'],
    'Device':['iOS Phone/Tablet','Android Phone/Tablet','Other Phone/Tablet',
              'Windows Desktop/Laptop','MacOS Desktop/Laptop',
              'Other Desktop/Laptop']
}


###############################
###   Wrangling Functions   ###
###############################

def set_categories(surveys):
    '''Set columns to 'Categorical' in DataFrame

    Args: surveys (list): list of DataFrames to set categories
    '''

    # Preferred order of categories
    order = {}
    order['Data_Access'] = ['Decrease Trust', 'No change', 'Increase Trust']
    order['General_Trust'] = ['None at all', 'Not very much', 'Fair amount', 'Great amount']
    order['Income'] = ['0-9,999', '10,000-24,999', '25,000-49,999',
                       '50,000-74,999', '75,000-99,999', '100,000-124,999',
                       '125,000-149,999', '150,000-174,999', '175,000-199,999',
                       '200,000+', 'Prefer not to answer']
    order['Trump_Approval'] = ['Strongly disapprove', 'Somewhat disapprove',
                               'Somewhat approve', 'Strongly approve']
    order['Political_View'] = ['Very Liberal', 'Liberal', 'Moderate',
                               'Conservative', 'Very Conservative']

    # Set order for specified categories
    for col, val  in order.items():
        for survey in surveys:
            if col in survey.columns:
                survey[col] = pd.Categorical(survey[col], val)
