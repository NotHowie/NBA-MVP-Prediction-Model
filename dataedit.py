import pandas as pd
from scipy.stats import zscore

excel = pd.read_excel("dataset.xlsx") 
df = pd.DataFrame(excel)
df['3P%'] = df['3P%'].fillna(0)


df['Consecutive MVP'] = 0
df['Total MVP'] = 0


consecutive_mvp_count = {}
total_mvp_count = {}

for index, row in df.iterrows():
    player = row['Player']
    mvp_won = row['MVP_Won']
    

    if player not in consecutive_mvp_count:
        consecutive_mvp_count[player] = 0
        total_mvp_count[player] = 0
    

    if mvp_won == 1:
        consecutive_mvp_count[player] += 1
        total_mvp_count[player] += 1
    else:
        consecutive_mvp_count[player] = 0
    

    df.at[index, 'Consecutive MVP'] = consecutive_mvp_count[player]
    df.at[index, 'Total MVP'] = total_mvp_count[player]

df.to_excel("updated_dataset.xlsx", index=False)


