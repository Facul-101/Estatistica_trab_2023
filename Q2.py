import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Q2.csv", delimiter=';')
print(df)

plt.boxplot(df)
plt.xticks([1, 2], ["Homens", "Mulheres"])
plt.ylabel("Altura (m)")
plt.show()
