from matplotlib import pyplot as plt
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x for x in histogram.keys()],      # move cada barra para a esquerda 
                                            # (removido -4 para centralizar)
        histogram.values(),                 # dá para cada barra sua altura correta
        8)                                  # dá para cada barra largura de 8

plt.axis([-5, 105, 0, 5])                   # eixo x de -5 até 105
                                            # eixo y de 0 até 5

plt.xticks([10 * i for i in range(11)])     # rótulos do eixo x em 0, 10, ..., 100
plt.xlabel('Decil')
plt.ylabel('# de Alunos')
plt.title('Distribuiução das Notas do Teste 1')
plt.show()