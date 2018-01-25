from matplotlib import pyplot as plt

# os valores não ficam os mesmos quando rodo, mas a visualização é próxima,
# isso depende muito do matplotlib e talvez do sistema que se esta executando.
test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.axis('equal')   # inclusão dos eixos do exemplo, no livro esta como "equals"
                    # o correto é "equal"
plt.title('Os eixos não são compatíveis')
plt.xlabel('nota do teste 2')
plt.ylabel('nota do teste 1')
plt.show()