import pandas as pd
import numpy as np

def preprocess(data):
    df =pd.DataFrame([data])

    kitchen_mapping = {
        'Not installed': 0,
        'Installed': 1,
        'Semi equipped': 2,
        'Hyper equipped': 3,
        'USA uninstalled' :0,
        'USA installed': 1,
        'USA semi equipped': 2,
        'USA hyper equipped' :3}     
    
# Replace values in the "Kitchen type" column with corresponding numbers and create a new column called "Kitchen values"
    df['Kitchen_values'] = df['Kitchen_values'].map(kitchen_mapping)

    building_cond_mapping = {
        
        'To restore': 0,
        'To be done up': 2,
        'Just renovated': 3,
        'To renovate': 1,
        'Good': 3,
        'As new' :4
    }

    df['Building_cond_values'] = df['Building_cond_values'].map(building_cond_mapping)


    #New column with energy classes 
    conditions = [
        (df['Primary_energy_consumption']>=1)&(df['Primary_energy_consumption']<100),
        (df['Primary_energy_consumption']>=100)&(df['Primary_energy_consumption']<200),
        (df['Primary_energy_consumption']>=200)&(df['Primary_energy_consumption']<300),
        (df['Primary_energy_consumption']>=300)&(df['Primary_energy_consumption']<400),
        (df['Primary_energy_consumption']>=400)&(df['Primary_energy_consumption']<500),
        (df['Primary_energy_consumption']>=500)&(df['Primary_energy_consumption']<600),
        (df['Primary_energy_consumption']>=600)
    ]

    values = [ 7, 6, 5, 4, 3, 2, 1]

    df['Energy_efficiency'] = np.select(conditions, values)

    return df



