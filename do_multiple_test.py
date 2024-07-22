import pandas as pd

df=pd.read_csv('scripts/sig_diffs.csv')
pvals=df[['branch','p_value']]

pvals=pvals.sort_values(by='p_value', ascending=True)

pvals['rank'] = pvals['p_value'].rank(method='min').astype(int)
pvals['padj'] = (pvals['rank']/213) * 0.05 
pvals['significant'] = pvals['p_value'] < pvals['padj']

pvals.to_csv('scripts/adjusted_p_values.csv',index=False)

