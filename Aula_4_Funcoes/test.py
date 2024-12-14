import unittest
from unittest.mock import patch, MagicMock

# Supondo que as funções estão em um arquivo chamado sistema_vendas.py
from sistema_vendas import cadastrar_usuarios, login, menu_administrador, menu_usuario, calcular_total, resumo_compra

class TestSistemaVendas(unittest.TestCase):

    @patch('builtins.input', side_effect=['João', 'joao123', 'senha123', 'Sair'])
    def test_cadastrar_usuarios(self, mock_input):
        usuarios = cadastrar_usuarios()
        self.assertEqual(len(usuarios), 1)
        self.assertEqual(usuarios[0]['nome'], 'João')
        self.assertEqual(usuarios[0]['login'], 'joao123')
        self.assertEqual(usuarios[0]['senha'], 'senha123')

    @patch('builtins.input', side_effect=['joao123', 'senha123'])
    def test_login_success(self, mock_input):
        usuarios = [{'nome': 'João', 'login': 'joao123', 'senha': 'senha123'}]
        usuario = login(usuarios)
        self.assertEqual(usuario['nome'], 'João')

    @patch('builtins.input', side_effect=['joao123', 'senha_errada'])
    def test_login_failure(self, mock_input):
        usuarios = [{'nome': 'João', 'login': 'joao123', 'senha': 'senha123'}]
        usuario = login(usuarios)
        self.assertIsNone(usuario)

    @patch('builtins.input', side_effect=['1', 'Produto A', '10.0', 'Sair'])
    def test_menu_administrador(self, mock_input):
        produtos = []
        menu_administrador(produtos)
        self.assertEqual(len(produtos), 1)
        self.assertEqual(produtos[0]['nome'], 'Produto A')
        self.assertEqual(produtos[0]['preco'], 10.0)

    @patch('builtins.input', side_effect=['1', '2', 'Sair'])
    def test_menu_usuario(self, mock_input):
        produtos = [{'nome': 'Produto A', 'preco': 10.0}, {'nome': 'Produto B', 'preco': 20.0}]
        carrinho = menu_usuario(produtos)
        self.assertEqual(len(carrinho), 1)
        self.assertEqual(carrinho[0]['produto']['nome'], 'Produto A')
        self.assertEqual(carrinho[0]['quantidade'], 2)

    def test_calcular_total(self):
        carrinho = [{'produto': {'nome': 'Produto A', 'preco': 10.0}, 'quantidade': 3}]
        subtotal, imposto, total = calcular_total(carrinho)
        self.assertEqual(subtotal, 30.0)
        self.assertEqual(imposto, 0.05)
        self.assertEqual(total, 31.5)

    @patch('builtins.print')
    def test_resumo_compra(self, mock_print):
        carrinho = [{'produto': {'nome': 'Produto A', 'preco': 10.0}, 'quantidade': 2}]
        subtotal, imposto, total = 20.0, 0.05, 21.0
        resumo_compra(carrinho, subtotal, imposto, total)
        mock_print.assert_any_call("Subtotal: R$20.00")
        mock_print.assert_any_call("Imposto: 5.00%")
        mock_print.assert_any_call("Total: R$21.00")
