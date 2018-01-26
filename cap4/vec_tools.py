"""Ferramenta de simulação de vetor para lista python

Esta ferramenta é uma implementação do capítulo 4, do livro Data Science do Zero
em python 3 para meus estudos. O nome de algumas funções foi renomeado para 
simplificar.

Lembrando que não deve ser utilizado para fins produtivos, pois utiliza listas
do python que não são as melhores alternativas em performance. O melhor seria 
utilizar numpy para trabalhar com vetores.

Exemplo:
    from vec_tool import vec_sum
    vec_sum([1, 2, 3])
    6
"""

from typing import List # import para hint de listas
from math import sqrt   # utilizado na função de magnitude de uma lista de vetores

def vec_add(v: List[int], w: List[int]) -> List[int]:
    """Soma de vetores.

    Adição entre dois vetores. Utilização de `zip` e compreensão de listas para 
    adicionar os elementos de cada vetor e criar um novo vetor das somas.

    Docstest:
        >>> vec_add([1, 2, 3], [3, 2, 1])
        [4, 4, 4]
    
    Args:
        v (List[int]): Primeiro vetor a ser somado.
        w (List[int]): Segundo vetor a ser somado.
    
    Return:
        List[int]: Novo vetor somado.
    """
    return [v_i + v_w for v_i, v_w in zip(v, w)]

def vec_sub(v: List[int], w: List[int]) -> List[int]:
    """Subtração de vetores.

    Subtração entre dois vetores. Utilização de `zip` e compreensão de listas 
    para subtrair os elementos de cada vetor e criar um novo vetor das 
    subtrações.

    Doctest:
        >>> vec_sub([1, 2, 3], [3, 2, 1])
        [-2, 0, 2]
    
    Args:
        v (List[int]): Primeiro vetor a ser subtração.
        w (List[int]): Segundo vetor a ser subtração.
    
    Return:
        List[int]: Novo vetor subtraído.
    """
    return [v_i - v_w for v_i, v_w in zip(v, w)]

def vec_sum(v: List[int]) -> int:
    """Soma uma lista de vetores.

    Utilizando-se de `reduce()` para simplificar a função, temos a soma de cada 
    elemento. Através de uma função passada como argumento, `reduce()` computa uma 
    lista e retorna o resultado ao final.

    Para melhorar utilizei função built-in (sum) do próprio python.

    Doctest:
        >>> vec_sum([1, 2, 3])
        6
    
    Args:
        v: List[int]: Lista de vetores para soma.
    Return:
        int: Resultado da soma dos vetores contidos na lista.
    """
    # return reduce(vec_add, v)
    return sum(v)   # Simplifica a soma utilizando funções já construídas do 
                    # python.

def vec_smult(s: int, v: List[int]) -> List[int]:
    """Multiplicação de escalar por uma lista de vetores.

    Cada vetor da lista é multiplicado pelo escalar passado.

    Doctest:
        >>> vec_smult(2, [1, 2, 3])
        [2, 4, 6]
    
    Args:
        s: int: Escalar (scale) de multiplicação.
        v: List[int]: Lista de vetores para multiplicação.
    Return:
        int: Lista de vetores multiplicados pelo escalar.
    """
    return [s * v_i for v_i in v]

def vec_mean(v: List[int]) -> float:
    """Computar média de uma lista de vetores.

    Utilizando da função de soma de vetores e divide pelo seu tamanho para se 
    obter a média.

    Nesta função preferi fazer a chamada da função sum do que utilizar vec_sum()
    e realizar um calculo direto a ter de usar a função de multiplicação.

    Doctest:
        >>> vec_mean([1, 2, 3])
        2.0
    
    Args:
        v: List[int]: Lista de vetores a ser calculada a média.
    Return:
        float: Média da lista de vetores.
    """
    # n = len(v)
    # return vect_smult(1/n, vec_sum(v))
    return sum(v) / len(v) # menor custo computacional e mesmo resultado

def vec_dot(v: List[int], w: List[int]) -> int:
    """Produto escalar entre dois vetores.

    Este exemplo já se encontra bem simplificado, apenas alterei em primeiro 
    gerar. Multiplica-se cada elemento de ambos os vetores depois somam a lista 
    gerada realizando uma única chamada a `sum()`.

    Docstring:
        >>> vec_dot([1, 2, 3], [3, 2, 1])
        10
    
    Args:
        v: List[int]: Primeira lista de vetor para cálculo do escalar.
        w: List[int]: Segunda lista de vetor para cálculo do escalar.
    Return:
        int: Produto escalar dos dois vetores passados no argumento.
    """
    # return sum(v_i * v_w for v_i, v_w in zip(v, w))
    return  sum([v_i * v_w for v_i, v_w in zip(v, w)])  # gera a lista depois 
                                                        # depois realiza a soma
def vec_sum_squares(v: List[int]) -> int:
    """Comnputar a soma dos quadrados de uma lista de vetores.

    Utiliza-se da função `vec_dot()` para calcular a soma dos quadrados de um vetor.

    Docstring:
        >>> vec_sum_squares([1, 2, 3])
        14
    
    Args:
        v: List[int]: Lista de vetor.
    Return:
        int: Soma dos quadrados do vetor.
    """
    return vec_dot(v, v)

def vec_magnitude(v: List[int]) -> float:
    """Computar a magnitude de uma lista de vetores.
    
    Calcula o tamanho do comprimento de um vetor. A magnitude é dada pela 
    fórmula ||v|| = raiz(x1²+x2²+...+xi²).

    Docstring:
        >>> vec_magnitude([1, 2, 3])
        3.7416573867739413

    Args:
        v: List[int]: Lista de vetores para se calcular a magnitude.
    Return:
        float: Retorna o comprimento do vetor.
    """
    return sqrt(vec_sum_squares(v))

def vec_distance(v: List[int],w: List[int]) -> float:
    """Computar a distância entre dois vetores.

    Esta função subtrai os vetores antes de calcular seu comprimento, resultando
    na distância entre os dois vetores passados por argumento.

    (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2

    Docstring:
        >>> vec_distance([1, 2, 3], [3, 2, 1])
        2.8284271247461903
    
    Args:
        v: List[int]: Primeira lista de vetores.
        w: List[int]: Segunda lista de vetores.
    Return:
        float: Distancia entre os dois vetores passados por argumento.
    """
    return vec_magnitude(vec_sub(v, w))

# inicia doctest quando execultado como python vec_tools.py.
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True) # mostra os resultados em uma forma verbosa.