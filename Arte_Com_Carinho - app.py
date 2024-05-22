import os
import sys
import time
import mysql.connector
import datetime
import openpyxl.drawing.image

from tkinter.filedialog import askdirectory
from tkinter import Tk

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from View.PY.FrmLogin import Ui_login
from View.PY.FrmAdmin import Ui_FrmAdmin
from View.PY.FrmFuncionario import Ui_FrmFuncionario
from openpyxl import *

banco_dados = mysql.connector.connect(
    host='localhost',
    port='3307',
    user='root',
    passwd='admin',
    database='banco_arte_com_carinho'
)
cursor = banco_dados.cursor()


class FrmLogin(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_login()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(lambda: self.logar())

    def logar(self):

        global window, UserLogado

        cursor.execute("SELECT * FROM login")
        logins = cursor.fetchall()

        usuario = self.ui.lineEdit.text()
        senha = self.ui.lineEdit_2.text()

        for login in logins:

            if usuario != login[0]:
                self.ui.lineEdit.setStyleSheet(
                    'background-color: rgba(0, 0 , 0, 0);border: 2px solid rgba(0,0,0,0);'
                    'border-bottom-color: rgb(255, 17, 49);color: rgb(0,0,0);padding-bottom: 8px;'
                    'border-radius: 0px;font: 10pt "Montserrat";')

            if senha != login[1]:
                self.ui.lineEdit_2.setStyleSheet(
                    'background-color: rgba(0, 0 , 0, 0);border: 2px solid rgba(0,0,0,0);'
                    'border-bottom-color: rgb(255, 17, 49);color: rgb(0,0,0);padding-bottom: 8px;'
                    'border-radius: 0px;font: 10pt "Montserrat";')

            if usuario == login[0] and senha == login[1]:

                UserLogado = login[3]

                self.ui.lineEdit.setStyleSheet(
                    'background-color: rgba(0, 0 , 0, 0);border: 2px solid rgba(0,0,0,0);'
                    'border-bottom-color: rgb(255, 17, 49);color: rgb(0,0,0);padding-bottom: 8px;'
                    'border-radius: 0px;font: 10pt "Montserrat";')

                self.ui.lineEdit_2.setStyleSheet(
                    'background-color: rgba(0, 0 , 0, 0);border: 2px solid rgba(0,0,0,0);'
                    'border-bottom-color: rgb(255, 17, 49);color: rgb(0,0,0);padding-bottom: 8px;'
                    'border-radius: 0px;font: 10pt "Montserrat";')

                if login[2] == 'admin':
                    window.close()
                    window = FrmAdmin()
                    window.show()

                if login[2] == 'funcionario':
                    window.close()
                    window = Frmfuncionario()
                    window.show()
                break


class FrmAdmin(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_FrmAdmin()
        self.ui.setupUi(self)

        self.ui.lbl_seja_bem_vindo.setText(f'Seja Bem vindo(a) - {UserLogado}')
        self.ui.lbl_titulo_vendas.setText(f'Vendedor(a) - {UserLogado}')
        self.ui.lbl_seja_bem_vindo.setFixedWidth(500)

        self.ui.btn_home.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_home))

        self.ui.btn_funcionarios.clicked.connect(
            lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_funcionarios))
        self.ui.btn_cadastrar_funcionarios.clicked.connect(
            lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_cadastro_funcionarios))
        self.ui.btn_alterar_funcionarios.clicked.connect(
            lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.alterar_funcionarios))

        self.ui.btn_cadastro.clicked.connect(self.CadastroFuncionarios)
        self.ui.btn_finalizar_alterar_funcionarios.clicked.connect(self.AlterarFuncionarios)

        self.ui.line_senha_alterar_funcionarios.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.btn_excluir_funcionarios.clicked.connect(self.ExcluirFuncionarios)
        self.ui.tabela_alterar_funcionarios.doubleClicked.connect(self.setTextAlterarFuncionarios)

        self.ui.btn_ver_senha.clicked.connect(self.VerSenhaCadastroFuncionarios)
        self.ui.btn_ver_senha_alterar.clicked.connect(self.VerSenhaAlterarFuncionarios)

        self.ui.tabela_funcionarios.setColumnWidth(0, 260)
        self.ui.tabela_funcionarios.setColumnWidth(1, 260)
        self.ui.tabela_funcionarios.setColumnWidth(2, 260)

        self.ui.btn_monitoramento.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.monitoramento))

        self.ui.tabela_monitoramento.setColumnWidth(0, 156)
        self.ui.tabela_monitoramento.setColumnWidth(1, 156)
        self.ui.tabela_monitoramento.setColumnWidth(2, 156)
        self.ui.tabela_monitoramento.setColumnWidth(3, 156)
        self.ui.tabela_monitoramento.setColumnWidth(4, 156)

        self.ui.btn_clietes.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_clientes))
        self.ui.btn_cadastrar_clientes.clicked.connect(
            lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_cadastrar_clientes))
        self.ui.btn_alterar_clientes.clicked.connect(
            lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_alterar_clientes))
        self.ui.btn_finalizar_cadastro_clientes.clicked.connect(self.CadatrarClientes)
        self.ui.btn_exclui_fornecedores.clicked.connect(self.ExcluirClientes)
        self.ui.tabela_alterar_clientes.doubleClicked.connect(self.setTextAlterarClientes)
        self.ui.btn_finalizar_alteracao_fornecedores_clicked.connect(self.AlterarClientes)

        self.ui.tabela_clientes.setColumnWidth(0, 192)
        self.ui.tabela_clientes.setColumnWidth(1, 192)
        self.ui.tabela_clientes.setColumnWidth(2, 192)
        self.ui.tabela_clientes.setColumnWidth(3, 194)

        self.ui.tabela_cadastrar_clientes.setColumnWidth(0, 247)
        self.ui.tabela_cadastrar_clientes.setColumnWidth(1, 247)
        self.ui.tabela_cadastrar_clientes.setColumnWidth(2, 247)
        self.ui.tabela_cadastrar_clientes.setColumnWidth(3, 249)

        self.ui.tabela_alterar_clientes.setColumnWidth(0, 247)
        self.ui.tabela_alterar_clientes.setColumnWidth(1, 247)
        self.ui.tabela_alterar_clientes.setColumnWidth(2, 247)
        self.ui.tabela_alterar_clientes.setColumnWidth(3, 249)

        self.ui.btn_Vendas.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_vendas))

        self.ui.tabela_vendas.setColumnWidth(0, 50)
        self.ui.tabela_vendas.setColumnWidth(1, 131)
        self.ui.tabela_vendas.setColumnWidth(2, 250)
        self.ui.tabela_vendas.setColumnWidth(3, 131)
        self.ui.tabela_vendas.setColumnWidth(4, 75)
        self.ui.tabela_vendas.setColumnWidth(5, 155)

        self.ui.btn_fornecedores.clidked.connect(
            lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_fornecedores))
        self.ui.btn_adicionar_fornecedores.clicked.connect(
            lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_cadastrar_fornecedores))
        self.ui.btn_editar_fornecedores.clicked.connect(
            lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_alterar_fornecedores))
        self.ui.btn_cadastrar_fornecedores.clicked.connect(self.CadastrarFornecedores)
        self.ui.tabela_alterar_fornecedores.doubleClicked.connect(self.setTextAlterarFornecedores)
        self.ui.btn_excluir_fornecedores.clicked.connect(self.ExcluirFornecedores)

        self.ui.tabela_fornecedores.setColumnWidth(0, 257)
        self.ui.tabela_fornecedores.setColumnWidth(1, 257)
        self.ui.tabela_fornecedores.setColumnWidth(2, 257)

        self.ui.tabela_cadastrar_fornecedores.setColumnWidth(0, 330)
        self.ui.tabela_cadastrar_fornecedores.setColumnWidth(1, 330)
        self.ui.tabela_cadastrar_fornecedores.setColumnWidth(2, 330)

        self.ui.tabela_alterar_fornecedores.setColumnWidth(0, 330)
        self.ui.tabela_alterar_fornecedores.setColumnWidth(1, 330)
        self.ui.tabela_alterar_fornecedores.setColumnWidth(2, 330)

        #produtos

        self.ui.btn_produtos.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_produtos))
        self.ui.btn_cadastrar_produto.clicked.connect(
            lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_cadastrar_produtos))
        self.ui.btn_alterar_clientes.clicked.connect(
            lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_alterar_produtos))
        self.ui.btn_finalizar_cadastro_produtos.clicked.connect(self.CadatrarProdutos)
        self.ui.btn_exclui_produto.clicked.connect(self.ExcluirProdutos)
        self.ui.tabela_alterar_produto.doubleClicked.connect(self.setTextAlterarProdutos)
        self.ui.btn_finalizar_alteracao_produto_clicked.connect(self.AlterarProdutos)

        self.ui.tabela_produto.setColumnWidth(0, 50)
        self.ui.tabela_produto.setColumnWidth(1, 131)
        self.ui.tabela_produto.setColumnWidth(2, 250)
        self.ui.tabela_produto.setColumnWidth(3, 131)
        self.ui.tabela_produto.setColumnWidth(4, 75)
        self.ui.tabela_produto.setColumnWidth(5, 155)

        self.ui.tabela_cadastro_produto.setColumnWidth(0, 50)
        self.ui.tabela_cadastro_produto.setColumnWidth(1, 165)
        self.ui.tabela_cadastro_produto.setColumnWidth(2, 300)
        self.ui.tabela_cadastro_produto.setColumnWidth(3, 165)
        self.ui.tabela_cadastro_produto.setColumnWidth(4, 75)
        self.ui.tabela_cadastro_produto.setColumnWidth(5, 250)

        self.ui.tabela_alterar_produto.setColumnWidth(0, 50)
        self.ui.tabela_alterar_produto.setColumnWidth(1, 165)
        self.ui.tabela_alterar_produto.setColumnWidth(2, 300)
        self.ui.tabela_alterar_produto.setColumnWidth(3, 165)
        self.ui.tabela_alterar_produto.setColumnWidth(4, 75)
        self.ui.tabela_alterar_produto.setColumnWidth(5, 250)

        self.ui.btn_configs.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_configuracaoes))

        self.ui.btn_voltar.clicked.connect(self.Voltar)

        self.AtualizaTabelasLogin()
        self.AtualizaTabelaClientes()
        self.AtualizaTabelaFornecedores()
        self.AtualizaTabelaProdutos()
        self.AtualizaTabelaVendas()

        temp = QTimer(self)
        temp.timeout.connect(self.HoraData)
        temp.timeout.connect(self.Sair)
        temp.start(1000)

        self.AtualizaCompleterSearchFornecedores()
        self.AtualizaCompleterSearchProdutos()
        self.AtualizaCompleterSearchFuncionarios()
        self.AtualizaCompleterSearchClientes()
        self.AtualizaCompleterSearchVendas()

        #Busca Produtos:

        self.ui.btn_pesquisar_produtos.clicked.connect(lambda: self.SearchProdutos(pg='Produtos'))
        self.ui.line_search_Bar_produtos.returnPressed.connect(lambda: self.SearchProdutos(pg='Produtos'))

        self.ui.btn_pesquisar_produtos.clicked.connect(lambda: self.SearchProdutos(pg='Alterar'))
        self.ui.line_search_Bar_produtos.returnPressed.connect(lambda: self.SearchProdutos(pg='Alterar'))

        self.ui.btn_pesquisar_produtos.clicked.connect(lambda: self.SearchProdutos(pg='Cadastrar'))
        self.ui.line_search_Bar_produtos.returnPressed.connect(lambda: self.SearchProdutos(pg='Cadastrar'))


        #fornecedores:

        self.ui.btn_pesquisar_fornecedores.clicked.connect(lambda: self.SearchFornecedores(pg='Fornecedores'))
        self.ui.line_search_Bar_fornecedores.returnPressed.connect(lambda: self.SearchFornecedores(pg='Fornecedores'))

        self.ui.btn_pesquisar_fornecedores.clicked.connect(lambda: self.SearchFornecedores(pg='Alterar'))
        self.ui.line_search_Bar_fornecedores.returnPressed.connect(lambda: self.SearchFornecedores(pg='Alterar'))

        self.ui.btn_pesquisar_fornecedores.clicked.connect(lambda: self.SearchFornecedores(pg='Cadastrar'))
        self.ui.line_search_Bar_fornecedores.returnPressed.connect(lambda: self.SearchFornecedores(pg='Cadastrar'))


        #Funcionarios

        self.ui.btn_pesquisar_funcionarios.clicked.connect(lambda: self.SearchFuncionarios(pg='Funcionarios'))
        self.ui.line_search_Bar_funcionarios.returnPressed.connect(lambda: self.SearchFuncionarios(pg='Funcionarios'))

        self.ui.btn_pesquisar_funcionarios.clicked.connect(lambda: self.SearchFuncionarios(pg='Alterar'))
        self.ui.line_search_Bar_funcionarios.returnPressed.connect(lambda: self.SearchFuncionarios(pg='Alterar'))

        self.ui.btn_pesquisar_funcionarios.clicked.connect(lambda: self.SearchFuncionarios(pg='Cadastrar'))
        self.ui.line_search_Bar_funcionarios.returnPressed.connect(lambda: self.SearchFuncionarios(pg='Cadastrar'))

        #Clientes

        self.ui.btn_pesquisar_clientes.clicked.connect(lambda: self.SearchClientes(pg='Clientes'))
        self.ui.line_search_Bar_clientes.returnPressed.connect(lambda: self.SearchClientes(pg='Clientes'))

        self.ui.btn_pesquisar_clientes.clicked.connect(lambda: self.SearchClientes(pg='Alterar'))
        self.ui.line_search_Bar_clientes.returnPressed.connect(lambda: self.SearchClientes(pg='Alterar'))

        self.ui.btn_pesquisar_clientes.clicked.connect(lambda: self.SearchClientes(pg='Cadastrar'))
        self.ui.line_search_Bar_clientes.returnPressed.connect(lambda: self.SearchClientes(pg='Cadastrar'))

        self.ui.line_cadastrar_contato_fornecedores.textChanged.connect(
            lambda: self.FormataNumeroContato(pg='CadastrarFornecedores'))
        self.ui.line_cadastrar_contato_fornecedores.textChanged.connect(
            lambda: self.FormataNumeroContato(pg='AlterarFornecedores'))

        self.ui.line_contato_cadastrar_clientes.textChanged.connect(
            lambda: self.FormataNumeroContato(pg='CadastrarClientes'))
        self.ui.line_contato_cadastrar_clientes.textChanged.connect(
            lambda: self.FormataNumeroContato(pg='AlterarClientes'))

        self.ui.line_cpf_cadastrar_clientes.textChanged.connect(
            lambda: self.FormataCPFClientes(pg='Cadastrar'))
        self.ui.line_alterar_cpf_clientes.textChanged.connect(
            lambda: self.FormataCPFClientes(pg='Alterar'))
        self.ui.line_cliente.textChanged.connect(lambda: self.FormataCPFClientes(pg='Vendas'))

        self.ui.line_codigo_produto.returnPressed.connect(self.PesquisandoProdutoPeloCodigo)
        self.ui.btn_confirmar_codigo.clicked.connect(self.PesquisandoProdutoPeloCodigo)
        self.ui.line_search_Bar_vendas.returnPressed.connect(self.CodProdutoVendas)

        self.ui.line_cliente.returnPressed.connect(self.ConfirmarCliente)
        self.ui.btn_confirmar_cliente.clicked.connect(self.ConfirmarCliente)

        self.ui.btn_adicionar_compra.clicked.connect(self.CadastrandoVendas)
        self.ui.btn_excluir_item.clicked.connect(self.ExcluirVenda)

        self.ui.lbl_total_venda.move(670, 20)
        self.ui.lbl_total_valor.move(910,20)
        self.ui.line_troco.move(680, 80)
        self.ui.btn_confirmar_troco.move(860, 80)
        self.ui.lbl_devolver_troco.move(680, 130)
        self.ui.lbl_troco.move(830, 130)

        self.ui.line_troco.returnPressed.connect(self.Troco)
        self.ui.btn_confirmar_troco.clicked.connect(self.Troco)

        self.AtualizaTotal()

        self.ui.btn_finalizar_compra.clicked.connect(self.FinalizarVendas)
        self.AtualizaTabelaMonitoramentoVendas()

        self.ui.btn_limpar_tabela.clicked.connect(self.LimparTabelaMonitoramento)

        self.ui.line_search_bar_monitoramentoto.returnPressed.connect(self.SearchMonitoramentoVendas)
        self.ui.btn_filtrar_monitoramento.clicked.connect(self.SearchMonitoramentoVendas)

        self.ui.btn_gerar_xls.clicked.connect(self.GerarXls)

        self.ui.btn_salvar.clicked.connect(self.Futuro)
        self.ui.btn_salvar.clicked.connect(self.Sair)

def Voltar(self):
    global window

    window.close()
    window = FrmLogin()
    window.show()


def HoraData(self):
    tempoAtual = QTime.currentTime()
    tempoTexto = tempoAtual.toString('hh:mm:ss')
    data_atual = datetime.date.today()
    dataTexto = data_atual.srtftime('%d/%m/%Y')

    self.ui.lbl_hora_data_funcionarios.setText(f'{dataTexto} {tempoTexto}')
    self.ui.lbl_hora_data_alterar_funcionarios.setText(f'{dataTexto} {tempoTexto}')

    self.ui.lbl_hora_data_monitoramento.setText(f'{dataTexto} {tempoTexto}')

    self.ui.lbl_hora_data.setText(f'{dataTexto} {tempoTexto}')

    self.ui.lbl_hora_data_produtos.setText(f'{dataTexto} {tempoTexto}')
    self.ui.lbl_hora_data_alterar_produto.setText(f'{dataTexto} {tempoTexto}')
    self.ui.lbl_hora_data_cadastrar_produto.setText(f'{dataTexto} {tempoTexto}')

    self.ui.lbl_hora_data_fornecedores.setText(f'{dataTexto} {tempoTexto}')
    self.ui.lbl_hora_data_alterar_fornecedores.setText(f'{dataTexto} {tempoTexto}')
    self.ui.lbl_hora_data_cadastrar_fornecedores.setText(f'{dataTexto} {tempoTexto}')

    self.ui.lbl_hora_data_clientes.setText(f'{dataTexto} {tempoTexto}')
    self.ui.lbl_hora_data_cadastrar_clientes.setText(f'{dataTexto} {tempoTexto}')
    self.ui.lbl_hora_data_alterar_clientes.setText(f'{dataTexto} {tempoTexto}')

def PesquisandoProdutosPeloCodigo(self):
    produtos = list()

    cod_inserido = self.ui.line_codigo_produto

    cursor.execute('SELECT * FROM produtos')
    banco_produtos = cursor.fetchall()

    produtos.clear()
    tabela = self.ui.tabela_produto

    for produto in banco_produtos:
        produtos.append(produto[0])

    items = tabela.findItems(cod_inserido.text(), Qt.MatchExactly)

    if items:
        item = items [0]
        tabela.SetCurrentItem(item)

        cod_inserido.setStyleSheet(StyleNormal)

    else:
        cod_inserido.setStyleSheet(StyleError)

def codProdutoVendas(self):
        cursor.execute('SELECT * FROM produtos')
        banco_produtos = cursor.fetchall()

        produto_inserido = self.ui.line_search_bar_vendas

        for pos, produto in enumerate(banco_produtos):
            if produto[1] == produto_inserido.text():
                self.ui.line_codigo_vendas.setText(produto[0])
                break
   def ConfirmarCliente(self):
        global search_clientes

        cliente = self.ui.line_cliente

        if cliente.text() in search_clientes:
            cliente.setStyleSheet('''
                background-color: rgba(0, 0 , 0, 0);
                border: 2px solid rgba(0,0,0,0);
                border-bottom-color: rgb(15, 168, 103);
                color: rgb(0,0,0);
                padding-bottom: 8px;
                border-radius: 0px;
                font: 10pt "Montserrat";''')
        else:
            cliente.setStyleSheet(StyleError)

def FinalizarVendas(self):
    cursor.execute('SELECT * FROM vendas')
    banco_vendas = cursor.fetchall()

    cursor.execute('SELECT * FROM quem_vendeu_mais')
    banco_quem_mais_vendeu = cursor.fetchall()

    if len(banco_vendas) > 0:
        tempoAtual = QTime.currentTime()
        tempoTexto = tempoAtual.toString('hh:mm:ss')
        data_atual = datetime.date.today()
        dataTexto = data_atual.strftime('%d/%m/%Y')

        qtde_vendido = list()
        totalVenda = list()
        vendedor = UserLogado
        clienteInserido = self.ui.line_cliente
        cliente = ''
        data_hora = f'{dataTexto} / {tempoTexto}'

        if clienteInserido.text() in search_clientes:
            cliente = clienteInserido.text()
        else:
            cliente = 'Não Informado'

        for venda in banco_vendas:
            qtde_vendido.append(int(venda[3]))
            totalVenda.append(int(venda[4]))

        comando_SQL = 'INSERT INTO monitoramento_vendas VALUES (%s,%s,%s,%s,%s)'
        dados = f'{vendedor}', f'{cliente}', f'{sum(qtde_vendido)}', f'{sum(totalVenda)}', f'{data_hora}'
        cursor.execute(comando_SQL, dados)

        funcionarios = list()
        for funcionario in banco_quem_mais_vendeu:
            funcionarios.append(funcionario[0])

            if funcionario[0] == vendedor:
                cursor.execute(f'UPDATE quem_vendeu_mais set total_qtde = {int(funcionario[1]) + int(sum(qtde_vendido))} WHERE nome = "{vendedor}"')

            if vendedor not in funcionarios:
                comando_SQL = 'INSERT INTO quem_vendeu_mais VALUES (%s,%s)'
                dados = f'{vendedor}', f'{sum(qtde_vendido)}'
                cursor.execute(comando_SQL, dados)

        cursor.execute('DELETE FROM vendas')
        self.AtualizaTabelaVendas()
        self.AtualizaTotal()
        self.AtualizaTabelaMonitoramentoVendas()
        self.AtualizaCompleterSearchVendas()

        self.ui.line_codigo_vendas.clear()
        self.ui.line_cliente.clear()
        self.ui.line_quantidade_vendas.clear()
        self.ui.line_desconto_vendas.clear()
        self.ui.lbl_troco.setText('0,00')
        self.ui.line_cliente.setStyleSheet(StyleNormal)
        self.ui.line_search_bar_vendas.clear()
        self.ui.line_troco.clear()
        self.ui.line_desconto_vendas.setStyleSheet(StyleNormal)
        self.ui.line_codigo_vendas.setStyleSheet(StyleNormal)
        self.ui.line_quantidade_vendas.setStyleSheet(StyleNormal)

def Troco(self):
    cursor.execute('SELECT * FROM vendas')
    banco_vendas = cursor.fetchall()

    troco_desejado = self.ui.line_troco.text()
    if troco_desejado.isnumeric() == True:
        vendas = list()
        vendas.clear()

        for venda in banco_vendas:
            vendas.append(int(venda[4]))

        troco = int(troco_desejado) - sum(vendas)
        self.ui.lbl_troco.setText(f'{lang.toString(int(troco) * 0.01, "f", 2)}')

def AtualizaTotal(self):

        cursor.execute('SELECT * FROM vendas')
        banco_vendas = cursor.fetchall()

        vendas = list()

        for pos, venda in enumerate(banco_vendas):
            vendas.append(int(venda[4]))

        total = lang.toString(sum(vendas) * 0.01, 'f', 2)
        self.ui.lbl_total_valor.setText(f'{total}')
        self.Troco()

def Futuro(self):
    global futuroTexto
    atual = datetime.datetime.now()

    futuro = atual + datetime.timedelta(minutes=20)
    futuroTexto = futuro.time().strftime('%H:%M:%S')

def Sair(self):
    global futuroTexto
    tempoAtual = QTime.currentTime()
    tempoTexto = tempoAtual.toString('hh:mm:ss')

    if self.ui.checkBox_finalizar_app.isChecked() == True:
        if tempoTexto == futuroTexto:
            sys.exit()

def LimparTabelaMonitoramento(self):
    cursor.execute('DELETE FROM monitoramento_vendas')
    cursor.execute('DELETE FROM quem_vendeu_mais')
    self.AtualizaTabelaMonitoramentoVendas()
    self.AtualizaCompleterSearchVendas()

    # Popups
def Popup(self):
    msg = QMessageBox()
    msg.setWindowTitle("Erro - Cadastro do Funcionario")
    msg.setText('Selecione um Nível de Usuário!')

    icon = QIcon()
    icon.addPixmap(QPixmap("View/Imagens/Logo Ico.ico"), QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    x = msg.exec_()

def PopupXlsDiretorio(self):
    msg = QMessageBox()
    msg.setWindowTitle("Erro - Gerar Excel")
    msg.setText('Selecione um diretório válido!')

    icon = QIcon()
    icon.addPixmap(QPixmap("View/Imagens/Logo Ico.ico"), QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    x = msg.exec_()

def PopupXls(self):
    msg = QMessageBox()
    msg.setWindowTitle("Erro - Gerar Excel")
    msg.setText('Verifique se não há um ARQUIVO com o mesmo nome aberto!')

    icon = QIcon()
    icon.addPixmap(QPixmap("View/Imagens/Logo Ico.ico"), QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    x = msg.exec_()

def PoupXlsBancoVazio(self):
    msg = QMessageBox()
    msg.setWindowTitle("Erro - Gerar Excel")
    msg.setText('Nenhuma venda informada!')

    icon = QIcon()
    icon.addPixmap(QPixmap("View/Imagens/Logo Ico.ico"), QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    x = msg.exec_()

    # Função que gera um arquivo xlsx para melhor monitoramento das vendas
def GerarXls(self):
    global wb

    cursor.execute('SELECT * FROM monitoramento_vendas')
    banco_monitoramento = cursor.fetchall()

    if len(banco_monitoramento) > 0:
            Tk().withdraw()
            diretorio = askdirectory()

            if diretorio != '':
                try:
                    wb.save(filename=r'{}\Relatório.xlsx'.format(diretorio))
                except:
                    self.PopupXls()
                else:

                    cursor.execute('SELECT * FROM quem_vendeu_mais')
                    banco_quem_vendeu_mais = cursor.fetchall()

                    total_vendido = 0
                    total_faturado = 0
                    total_clientes_cadastrados = 0
                    total_clientes_não_cadastrados = 0
                    quem_vendeu_mais = list()
                    funcionario = ''

                    planilha = wb['Relatório']

                    c = 18
                    for vendas in banco_monitoramento:
                        total_vendido += int(vendas[2])
                        total_faturado += int(vendas[3])
                        if vendas[1] == 'Não Informado':
                            total_clientes_não_cadastrados += 1
                        else:
                            total_clientes_cadastrados += 1
                        c += 1
                        conv = lang.toString(int(vendas[3]) * 0.01, "f", 2)
                        planilha[f'A{c}'] = vendas[0]
                        planilha[f'E{c}'] = vendas[1]
                        planilha[f'I{c}'] = int(vendas[2])
                        planilha[f'M{c}'] = 'RS ' + conv
                        planilha[f'R{c}'] = vendas[4]

                    for funcionarios in banco_quem_vendeu_mais:
                        quem_vendeu_mais.append(funcionarios[1])

                    for funcionarios in banco_quem_vendeu_mais:
                        if funcionarios[1] == max(quem_vendeu_mais, key=int):
                            funcionario = funcionarios[0]
                    conv = lang.toString(int(total_faturado) * 0.01, "f", 2)

                    planilha['F12'] = total_vendido
                    planilha['F13'] = 'RS ' + conv
                    planilha['F14'] = funcionario
                    planilha['F15'] = total_clientes_cadastrados
                    planilha['F16'] = total_clientes_não_cadastrados

                    wb.save(filename=r'{}\Relatório.xlsx'.format(diretorio))

                    for c in range(19, 19 + len(banco_monitoramento)):
                        planilha[f'A{c}'] = None
                        planilha[f'E{c}'] = None
                        planilha[f'I{c}'] = None
                        planilha[f'M{c}'] = None
                        planilha[f'R{c}'] = None
            else:
                self.PopupXlsDiretorio()
    else:
        self.PoupXlsBancoVazio()
