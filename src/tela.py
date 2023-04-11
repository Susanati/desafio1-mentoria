from PyQt5 import uic, QtWidgets


def funcao_principal():
    linha1 = cadastro.codigo_lineEdit.text()
    linha2 = cadastro.descricao_lineEdit.text()
    linha3 = cadastro.preco_lineEdit.text()

    if cadastro.informatica_Button.isChecked():
        print("Categoria Informatica foi selecionado")
    else:
        print("Categoria Eletronico foi selecionado")

    print("Codigo:", linha1)
    print("Descricao:", linha2)
    print("Preço:", linha3)


app = QtWidgets.QApplication([])
cadastro = uic.loadUi("cadastro.ui")
cadastro.pushButton.clicked.connect(funcao_principal)

cadastro.show()
app.exec()
