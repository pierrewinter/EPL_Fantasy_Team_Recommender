import pandas as pd

epl_season = '2018-19'
data_to_import = './data/' + epl_season + '/gws/merged_gw.csv'
df = pd.read_csv(data_to_import, encoding='cp1252')
