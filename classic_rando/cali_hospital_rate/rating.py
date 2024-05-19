import pandas as pd

df_1 = pd.read_excel('classic_rando/cali_hospital_rate/Hospital_Survey_Data_Alcohol_Drug_Abuse.xlsx', skiprows=1)
df_2 = pd.read_csv('classic_rando/cali_hospital_rate/Hospital_Survey_Data_Speticemia.csv', skiprows=1)

filtered_df_1 = df_1[
    (df_1['DRG Definition'] == '001 - ALCOHOL/DRUG ABUSE OR DEPENDENCE, LEFT AMA') &
    (df_1['Provider State'] == 'CA')
]

filtered_df_2 = df_2[
    (df_2['DRG Definition'].str.contains('LEFT AMA')) &
    (df_2['Provider State'] == 'CA')
]

average_1 = filtered_df_1['Hospital Rating'].mean()
average_2 = filtered_df_2['Hospital Rating'].mean()

print(f'{average_1}, {average_2}')