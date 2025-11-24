# Atividade-04

Implementação de Algoritmos Gulosos (Greedy Algorithms) em Python.

## Algoritmos Implementados

### 1. Troco Mínimo (Minimum Change)

Dado um valor de troco e um conjunto de denominações de moedas, determina o menor número de moedas necessárias para fornecer o troco.

**Entrada:**
- Valor inteiro V
- Conjunto de denominações de moedas {1, 5, 10, 25, 50, 100}

**Saída:**
- O número mínimo de moedas necessárias

**Exemplo:**
```python
from greedy_algorithms import troco_minimo

# Valor: 289 → Moedas: 2×100 + 1×50 + 1×25 + 1×10 + 4×1 = 9 moedas
resultado = troco_minimo(289)  # Retorna 9
```

### 2. Atividades Compatíveis (Compatible Activities)

Dado um conjunto de atividades, cada uma com um horário de início e de término, seleciona o máximo número de atividades que podem ser realizadas sem sobreposição de tempo.

**Entrada:**
- Lista de atividades com nome, horário de início e de término

**Saída:**
- O número máximo de atividades que podem ser selecionadas sem que nenhuma delas tenha sobreposição

**Exemplo:**
```python
from greedy_algorithms import atividades_compativeis

atividades = [
    ("A1", 1, 3),
    ("A2", 2, 5),
    ("A3", 4, 7),
    ("A4", 1, 8),
    ("A5", 6, 9)
]
resultado = atividades_compativeis(atividades)  # Retorna 2 (A1 e A3)
```

## Como Usar

### Executar a demonstração

```bash
python3 greedy_algorithms.py
```

Este comando executará exemplos de ambos os algoritmos e mostrará os resultados.

### Executar os testes

```bash
python3 -m unittest test_greedy_algorithms.py -v
```

Este comando executará todos os testes unitários para validar a implementação dos algoritmos.

## Estrutura do Projeto

```
.
├── README.md                      # Este arquivo
├── greedy_algorithms.py           # Implementação dos algoritmos
└── test_greedy_algorithms.py      # Testes unitários
```

## Complexidade dos Algoritmos

### Troco Mínimo
- **Complexidade de Tempo:** O(n), onde n é o número de denominações
- **Complexidade de Espaço:** O(1)

### Atividades Compatíveis
- **Complexidade de Tempo:** O(n log n), devido à ordenação das atividades
- **Complexidade de Espaço:** O(n), para armazenar as atividades ordenadas

## Estratégia Gulosa

Ambos os algoritmos utilizam a estratégia gulosa (greedy):

1. **Troco Mínimo:** Sempre escolhe a maior moeda possível que não excede o valor restante
2. **Atividades Compatíveis:** Ordena as atividades por tempo de término e sempre escolhe a próxima atividade que começa após o término da última atividade selecionada