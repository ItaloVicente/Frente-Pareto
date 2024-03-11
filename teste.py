from paretoset import paretoset
import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo Excel
caminho_arquivo_excel = 'metadata/bayesian_search_result_03_07_seed_18.xlsx'  # Substitua pelo caminho real do seu arquivo

# Carregar os dados do Excel
dados_excel = pd.read_excel(caminho_arquivo_excel)

# Especificar as colunas relevantes
coluna_mrr = 'MRR'  # Substitua pelo nome real da coluna MRR
coluna_mop = 'MOP'  # Substitua pelo nome real da coluna MOP

# Pegar os dados das colunas
mrr = dados_excel[coluna_mrr].tolist()
mop = dados_excel[coluna_mop].tolist()

metrics = pd.DataFrame({"mrr": mrr,
                       "mop": mop})
mask = paretoset(metrics, sense=["max", "max"])
paretoset_metrics = metrics[mask]
print(paretoset_metrics)
paretoset_metrics.reset_index(drop=True, inplace=True)
plt.scatter(mrr, mop, label='Dados')
plt.plot(*zip(*paretoset_metrics), color='red', label='Frente de Pareto')
plt.title('Frente de Pareto')
plt.xlabel('MRR')
plt.ylabel('MOP')
plt.legend()
plt.grid(True)
plt.savefig("teste1")