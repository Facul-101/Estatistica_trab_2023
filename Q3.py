import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics as st
import scipy

df = pd.read_csv("Q3.csv", delimiter=';')

vals = []

for line in df.index:
    df.loc[line, 'fi'] = (df.loc[line, 'Fi'])/(df['Fi'].sum())

    if line == 0:
        df.loc[line, 'fac'] = (df.loc[line, 'Fi'])/(df['Fi'].sum())
    else:
        df.loc[line, 'fac'] = df.loc[line - 1, 'fac'] + (df.loc[line, 'Fi'])/(df['Fi'].sum())

    init, end = df.loc[line, 'Class'].split(':')
    med = (float(init) + float(end))/2

    for _ in range(df.loc[line, 'Fi']):
        vals.append(med)

Qs = np.quantile(vals, [0.25, 0.5, 0.75])

print(df)

print(f'{"Média":<25}-> {np.mean(vals)}')
print(f'{"Moda":<25}-> {st.mode(vals)}')
print(f'{"Mediana":<25}-> {np.median(vals)}')
print(f'{"Desvio-padrão":<25}-> {np.std(vals)}')
print(f'{"Coeficiente de varição":<25}-> {np.std(vals)/np.mean(vals)}')
print(f'{"Assimetria":<25}-> {scipy.stats.skew(vals)}')
print(f'{"Curtose":<25}-> {scipy.stats.kurtosis(vals)}')
print(f'{"Quartil 1":<25}-> {Qs[0]}')
print(f'{"Quartil 2":<25}-> {Qs[1]}')
print(f'{"Quartil 3":<25}-> {Qs[2]}')

plt.hist(vals, 5, range=(4, 24), alpha=0.7)
plt.xticks([x*2 for x in range(2, 13)])
plt.plot([Qs[0], Qs[0]], [vals.count(Qs[0]), 0], 'r:', label="Q1")
plt.plot([Qs[1], Qs[1]], [vals.count(Qs[1]), 0], 'm:', label="Q2")
plt.plot([Qs[2], Qs[2]], [vals.count(Qs[2]), 0], 'k:', label="Q3")
plt.legend()
plt.show()
