# Ordenando normas en python

import pandas as pd
df = pd.read_csv ('prueba2.csv')
print(df)

df['norma'].tolist()

df['numero'].tolist()

df['texto'].tolist()

from collections import defaultdict

def sorted_by(res, listanor, key=None):
    if key is None:
        key = lambda x: x

    # group the elements by their key
    grouped_items = defaultdict(list)
    for item in res:
        k = key(item)
        grouped_items[k].append(item)

    # flatten the dict of groups to a list
    return [item for key in listanor for item in grouped_items[key]]
    
    
a = zipped
b = ['Ley','Decreto de urgencia', 'Decreto Legislativo','Decreto Supremo','Resolución Suprema','Resolución Ministerial','Resolución vice ministerial','Resolución Presidencial','Resolución Directoral'];
result = sorted_by(a, b, lambda tup: tup[0])
print(result) 

columns = ["normas","numero","texto"]

df = pd.DataFrame(data=result,columns=columns)
df.head()

df.to_excel('final.xlsx')
