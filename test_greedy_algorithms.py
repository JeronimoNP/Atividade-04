"""
Testes para os Algoritmos Gulosos
"""

import unittest
from greedy_algorithms import troco_minimo, atividades_compativeis


class TestTrocoMinimo(unittest.TestCase):
    """Testes para o algoritmo de Troco Mínimo"""
    
    def test_valor_simples(self):
        """Testa valores simples que são uma única moeda"""
        self.assertEqual(troco_minimo(1), 1)
        self.assertEqual(troco_minimo(5), 1)
        self.assertEqual(troco_minimo(10), 1)
        self.assertEqual(troco_minimo(25), 1)
        self.assertEqual(troco_minimo(50), 1)
        self.assertEqual(troco_minimo(100), 1)
    
    def test_valor_multiplo(self):
        """Testa valores que são múltiplos de moedas"""
        self.assertEqual(troco_minimo(200), 2)  # 2x100
        self.assertEqual(troco_minimo(150), 2)  # 100 + 50
        self.assertEqual(troco_minimo(30), 2)   # 25 + 5
    
    def test_valor_complexo(self):
        """Testa valores que requerem combinação de várias moedas"""
        self.assertEqual(troco_minimo(289), 9)  # 100+100+50+25+10+1+1+1+1
        self.assertEqual(troco_minimo(11), 2)   # 10 + 1
        self.assertEqual(troco_minimo(63), 5)   # 50 + 10 + 1 + 1 + 1
    
    def test_valor_exato(self):
        """Testa valores que podem ser feitos com poucas moedas"""
        self.assertEqual(troco_minimo(156), 4)  # 100 + 50 + 5 + 1
    
    def test_denominacoes_customizadas(self):
        """Testa com denominações customizadas"""
        denominacoes = [1, 5, 10]
        self.assertEqual(troco_minimo(15, denominacoes), 2)  # 10 + 5
        self.assertEqual(troco_minimo(27, denominacoes), 5)  # 10 + 10 + 5 + 1 + 1
    
    def test_valor_zero(self):
        """Testa com valor zero"""
        self.assertEqual(troco_minimo(0), 0)
    
    def test_valor_negativo(self):
        """Testa que valor negativo gera erro"""
        with self.assertRaises(ValueError):
            troco_minimo(-1)


class TestAtividadesCompativeis(unittest.TestCase):
    """Testes para o algoritmo de Atividades Compatíveis"""
    
    def test_lista_vazia(self):
        """Testa com lista vazia de atividades"""
        self.assertEqual(atividades_compativeis([]), 0)
    
    def test_uma_atividade(self):
        """Testa com apenas uma atividade"""
        atividades = [("A1", 1, 3)]
        self.assertEqual(atividades_compativeis(atividades), 1)
    
    def test_atividades_sem_sobreposicao(self):
        """Testa atividades que não se sobrepõem"""
        atividades = [
            ("A1", 1, 2),
            ("A2", 2, 3),
            ("A3", 3, 4),
            ("A4", 4, 5)
        ]
        self.assertEqual(atividades_compativeis(atividades), 4)
    
    def test_atividades_com_sobreposicao(self):
        """Testa atividades com sobreposição"""
        atividades = [
            ("A1", 1, 3),
            ("A2", 2, 5),
            ("A3", 4, 7),
            ("A4", 1, 8),
            ("A5", 6, 9)
        ]
        self.assertEqual(atividades_compativeis(atividades), 2)  # A1 e A3
    
    def test_todas_atividades_sobrepostas(self):
        """Testa quando todas as atividades se sobrepõem"""
        atividades = [
            ("A1", 1, 10),
            ("A2", 2, 8),
            ("A3", 3, 6),
            ("A4", 4, 5)
        ]
        self.assertEqual(atividades_compativeis(atividades), 1)
    
    def test_atividades_reunioes(self):
        """Testa exemplo de reuniões"""
        atividades = [
            ("Reunião 1", 9, 10),
            ("Reunião 2", 9, 11),
            ("Reunião 3", 10, 11),
            ("Reunião 4", 11, 12),
            ("Reunião 5", 11, 13)
        ]
        self.assertEqual(atividades_compativeis(atividades), 3)
    
    def test_atividades_adjacentes(self):
        """Testa atividades adjacentes (uma termina quando outra começa)"""
        atividades = [
            ("A1", 1, 2),
            ("A2", 2, 3),
            ("A3", 3, 4)
        ]
        self.assertEqual(atividades_compativeis(atividades), 3)


if __name__ == "__main__":
    unittest.main()
