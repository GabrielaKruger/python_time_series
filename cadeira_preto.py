# ----------------------------------------------------------------------------
# script: exercicios_vendas.py
# autor: gabriela krüger
# data de criação: 01/09/2025
# versão: 1.0
# ----------------------------------------------------------------------------


# cabeçalho do arquivo:
# as primeiras linhas do script geralmente contêm informações sobre o arquivo,
# como o autor, data, versão, e para que ele serve. 
# isso não afeta a execução do código, mas ajuda na organização
# e para outros desenvolvedores entenderem rapidamente o que o script faz.

"""
docstring:
é uma forma de documentação que o python reconhece. 
pode ser usada logo após a criação de funções, classes ou módulos.
serve para explicar o que o código faz, quais parâmetros recebe, 
o que retorna e outras informações importantes.
ela pode ser acessada em tempo de execução usando help() ou .__doc__.
"""# ----------------------------------------------------------------------------

def e_par(n: int) -> bool:
    """
    verifica se um número é par

    args:
        n (int): número inteiro a ser verificado

    returns:
        bool: verdadeiro se o número for par, falso caso contrário

    exemplo:
        >>> e_par(2)
        true
        >>> e_par(3)
        false
    """
    return n % 2 == 0


def limpa_texto(s: str) -> str:
    """
    converte texto para minúsculo e remove pontuações comuns

    args:
        s (str): texto de entrada

    returns:
        str: texto limpo e em minúsculas

    exemplo:
        >>> limpa_texto("olá, mundo!")
        'ola mundo'
    """
    import re
    texto = s.lower()
    texto = re.sub(r"[,\.;:!?\'\"()\-_\[\]]", "", texto)
    return texto


def total_por_vendedor(vendas: list[tuple[str, float]]) -> dict:
    """
    calcula o total de vendas por vendedor

    args:
        vendas (list[tuple[str, float]]): lista de tuplas (nome, valor)

    returns:
        dict: dicionário {nome: soma_valores} com total de vendas por vendedor

    exemplo:
        >>> total_por_vendedor([('ana', 100), ('bia', 50), ('ana', 200)])
        {'ana': 300, 'bia': 50}
    """
    totais = {}
    for nome, valor in vendas:
        if nome in totais:
            totais[nome] += valor
        else:
            totais[nome] = valor
    return totais


# testes rápidos
if __name__ == "__main__":
    print("2 é par?", e_par(2))
    print("3 é par?", e_par(3))
    print("texto limpo:", limpa_texto("olá, mundo!"))
    vendas = [('ana', 100), ('bia', 50), ('ana', 200)]
    print("totais por vendedor:", total_por_vendedor(vendas))
