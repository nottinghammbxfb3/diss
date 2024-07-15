import pandas as pd
lnldic={}

with open('scripts/lnl_values.txt','r')as f:
    for line in f.readlines():
        parts = line.split()
        if len(parts) > 1:
            gene = parts[0]
            val = parts[1]
            lnldic[gene] = [val]

for k,v in lnldic.items():
    if 'n'+k in lnldic:
        lnldic[k].append(lnldic['n'+k][0])

lnldic = {k: v for k, v in lnldic.items() if len(v) >= 2}

df_data = {'branch': [], 'test': [], 'null': []}
for gene, values in lnldic.items():
    df_data['branch'].append(gene)
    df_data['test'].append(values[0])
    df_data['null'].append(values[1])

# Create DataFrame
df = pd.DataFrame(df_data)

df['test'] = pd.to_numeric(df['test'])
df['null'] = pd.to_numeric(df['null'])

# Calculate diff as 2 * test - null
df['diff'] = 2 * (df['test'] - df['null'])

from scipy.stats import chi2

df['p_value'] = chi2.sf(df['diff'], df=1)
df['sig'] = df['p_value'] < 0.05

significant_df = df[df['sig'] == True]
significant_df['p_value'] = significant_df['p_value'].round(6)

significant_df=significant_df.rename(columns={'sig':'*'})
significant_df['**']=significant_df['p_value'] <0.01

significant_df.to_csv('scripts/sig_diffs.csv',index=False)