import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv('gasolina.csv')
grafico = sns.lineplot(data = df, x = 'dia', y = 'venda', color='b')
plt.title('Valor da gasolina por dia')
plt.xticks()
plt.xlabel('Dia')
plt.ylabel('Valor')
plt.legend(['Valor da gasolina'])
plt.savefig('gasolina.png', format='png')
plt.show()