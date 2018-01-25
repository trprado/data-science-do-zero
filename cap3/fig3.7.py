from matplotlib import pyplot as plt

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# cria o gráfico de dispersão
plt.scatter(friends, minutes)

# nomeia cada posição, função de anotação do gráfocp de dispersão.
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                xy=(friend_count, minute_count),# coloca o rótulo com sua
                xytext=(5, -5),                 # posição e compensa os valores
                                                # x, u da posição do texto.
                textcoords='offset points')

# correção de eixos para ficar igual exemplo do livro.
plt.axis([58, 74, 80, 240])
plt.title('Minutos Diários vs Número de Amigos')
plt.xlabel('# de amigos')
plt.ylabel('minutos diários passados no site')
plt.show()