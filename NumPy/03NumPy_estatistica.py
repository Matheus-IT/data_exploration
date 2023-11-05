import numpy as np

# Criando um array
A = np.array([15, 23, 63, 94, 75])

# Em estatística a média é o valor que aponta para onde mais se concentram os dados de uma distribuição.
print('mean', np.mean(A))

# O desvio padrão mostra o quanto de variação ou "dispersão" existe em 
# relação à média (ou valor esperado). 
# Um baixo desvio padrão indica que os dados tendem a estar próximos da média.
# Um desvio padrão alto indica que os dados estão espalhados por uma gama de valores.
print('standard deviation', np.std(A))

# Variância de uma variável aleatória é uma medida da sua dispersão 
# estatística, indicando "o quão longe" em geral os seus valores se 
# encontram do valor esperado
print('variance', np.var(A))
