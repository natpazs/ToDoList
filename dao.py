from random import *

Arquivo = "ToDo.txt"


class DaoAdicionarTarefa():
    def __init__(self, tarefa):
        self.tarefa = tarefa
        self.status = "A"

    def adicionar(self, x):
        with open(Arquivo, "a") as arquivo:
            tarefa_formatada = f"{self.status}\t\t\t{x}\t{self.tarefa}"
            
            with open(Arquivo, "r") as arquivo:
                ler = arquivo.read()

            with open(Arquivo, "a") as arquivo:
                if "STATUS: \tID: \tTAREFA:" not in ler:
                    arquivo.write(f"STATUS: \tID: \tTAREFA:\n")
                arquivo.write(f"{tarefa_formatada}\n")
                return True


class DaoListarTarefa():
    def listar(self):
        with open(Arquivo,"r") as arquivo:
            linhas = arquivo.readlines()
        return linhas
    
class DaoAlterar():
    def alterarTarefa(self, antigo, novo):
        with open(Arquivo, "r") as arquivo:
            texto = arquivo.read()

            textoNovo = texto.replace(antigo, novo)

            with open(Arquivo, "w") as arquivo:
                arquivo.write(textoNovo)
                return True
            