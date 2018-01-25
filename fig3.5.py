from matplotlib import pyplot as plt

from matplotlib import pyplot as plt

mentions = [500, 505]
years = [2013, 2014]

plt.bar([2013, 2014], mentions, 0.8)    # Desnecessário .6, troca valores para 
                                        # as datas corretas 2013, 2014 ao invéz
                                        # de 2012.6, 2013.6
plt.xticks(years)
plt.ylabel('# de vezes que ouvimos alguém dizer "data science"')

# se você não fizer isso, matplotlib nomeará o eixo x de 0, 1
# e então adiciona a +2.013e3 para fora do canto (matplotlib feito!)
# plt.ticklabel_format(useOffset=False) # código desnecessário

# engana o eixo y mostra apenas a parte acima de 500
plt.axis([2012.5, 2014.5, 0, 550])
plt.title('Não tão Grande Agora.') # correção nas apas de dupla para simples
plt.show()