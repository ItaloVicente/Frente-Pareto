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

# Ordenar os dados por MRR (do menor para o maior)
sorted_indices = sorted(range(len(mrr)), key=lambda k: mrr[k])
mrr = [mrr[i] for i in sorted_indices]
mop = [mop[i] for i in sorted_indices]

# Inverter a ordem dos dados
mrr.reverse()
mop.reverse()

# Calcular a frente de Pareto
pareto_front = []
current_max_mop = float('-inf')
for i in range(len(mop)):
    if mop[i] > current_max_mop:
        pareto_front.append((mrr[i], mop[i]))
        current_max_mop = mop[i]

# Plotar a frente de Pareto
plt.scatter(mrr, mop, label='Dados')
plt.plot(*zip(*pareto_front), color='red', label='Frente de Pareto')
plt.title('Frente de Pareto')
plt.xlabel('MRR')
plt.ylabel('MOP')
plt.legend()
plt.grid(True)
plt.savefig("figure_teste")
