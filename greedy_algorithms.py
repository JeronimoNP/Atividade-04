"""
Implementação de Algoritmos Gulosos (Greedy Algorithms)

1. Troco Mínimo (Minimum Change)
2. Atividades Compatíveis (Compatible Activities)
"""


def troco_minimo(valor, denominacoes=None):
    """
    Calcula o número mínimo de moedas necessárias para fornecer o troco.
    
    Args:
        valor (int): O valor do troco a ser fornecido
        denominacoes (list): Lista de denominações de moedas disponíveis.
                           Padrão: [100, 50, 25, 10, 5, 1]
    
    Returns:
        int: O número mínimo de moedas necessárias
    
    Exemplo:
        >>> troco_minimo(289)
        9
        >>> troco_minimo(11)
        2
    """
    if denominacoes is None:
        denominacoes = [100, 50, 25, 10, 5, 1]
    
    # Ordena as denominações em ordem decrescente para algoritmo guloso
    denominacoes_ordenadas = sorted(denominacoes, reverse=True)
    
    num_moedas = 0
    valor_restante = valor
    
    for moeda in denominacoes_ordenadas:
        if valor_restante >= moeda:
            quantidade = valor_restante // moeda
            num_moedas += quantidade
            valor_restante -= quantidade * moeda
    
    return num_moedas


def atividades_compativeis(atividades):
    """
    Seleciona o máximo número de atividades que podem ser realizadas 
    sem sobreposição de tempo.
    
    Args:
        atividades (list): Lista de tuplas/listas contendo (nome, inicio, fim)
                          onde inicio e fim são tempos (int ou float)
    
    Returns:
        int: O número máximo de atividades que podem ser selecionadas
    
    Exemplo:
        >>> atividades = [
        ...     ("A1", 1, 3),
        ...     ("A2", 2, 5),
        ...     ("A3", 4, 7),
        ...     ("A4", 1, 8),
        ...     ("A5", 6, 9)
        ... ]
        >>> atividades_compativeis(atividades)
        2
    """
    if not atividades:
        return 0
    
    # Ordena as atividades por horário de término (estratégia gulosa)
    atividades_ordenadas = sorted(atividades, key=lambda x: x[2])
    
    # Seleciona a primeira atividade
    num_atividades = 1
    ultima_atividade_fim = atividades_ordenadas[0][2]
    
    # Percorre as atividades restantes
    for i in range(1, len(atividades_ordenadas)):
        nome, inicio, fim = atividades_ordenadas[i]
        
        # Se a atividade começa após o término da última atividade selecionada
        if inicio >= ultima_atividade_fim:
            num_atividades += 1
            ultima_atividade_fim = fim
    
    return num_atividades


def main():
    """
    Função principal para demonstrar o uso dos algoritmos.
    """
    print("=" * 60)
    print("Algoritmos Gulosos - Demonstração")
    print("=" * 60)
    
    # Demonstração: Troco Mínimo
    print("\n1. TROCO MÍNIMO")
    print("-" * 60)
    
    valores_teste = [289, 11, 63, 1, 100, 156]
    denominacoes = [100, 50, 25, 10, 5, 1]
    
    print(f"Denominações disponíveis: {denominacoes}")
    print()
    
    for valor in valores_teste:
        num_moedas = troco_minimo(valor, denominacoes)
        print(f"Valor: {valor:3d} → Número mínimo de moedas: {num_moedas}")
    
    # Demonstração: Atividades Compatíveis
    print("\n\n2. ATIVIDADES COMPATÍVEIS")
    print("-" * 60)
    
    atividades = [
        ("A1", 1, 3),
        ("A2", 2, 5),
        ("A3", 4, 7),
        ("A4", 1, 8),
        ("A5", 6, 9),
        ("A6", 8, 10)
    ]
    
    print("Lista de atividades:")
    for nome, inicio, fim in atividades:
        print(f"  {nome}: [{inicio}, {fim}]")
    
    max_atividades = atividades_compativeis(atividades)
    print(f"\nNúmero máximo de atividades compatíveis: {max_atividades}")
    
    # Exemplo adicional
    print("\n" + "-" * 60)
    atividades2 = [
        ("Reunião 1", 9, 10),
        ("Reunião 2", 9, 11),
        ("Reunião 3", 10, 11),
        ("Reunião 4", 11, 12),
        ("Reunião 5", 11, 13)
    ]
    
    print("\nLista de atividades (exemplo 2):")
    for nome, inicio, fim in atividades2:
        print(f"  {nome}: [{inicio}h, {fim}h]")
    
    max_atividades2 = atividades_compativeis(atividades2)
    print(f"\nNúmero máximo de atividades compatíveis: {max_atividades2}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
