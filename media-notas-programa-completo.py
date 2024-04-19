#Programa completo que faz operações com alunos e suas notas. Tendo menu de opções para o usuário ter uma melhor experiência.
#Vamos também fazer um código organizado, separando funcionalidades em funções
#(funções são um tipo de sub programa dentro do programa principal)

#Repare que teremos uma lista de alunos e cada aluno tem suas informações (propriedades) e ações (métodos).
#Para esse cenário, o uso de orientação a objetos é uma solução mais apropriada.

#Classes e funções tem que ser declaradas antes de serem usadas

#Vamos criar a classe "Aluno"
class Aluno:
    
    def __init__(self, nome): #um método especial, chamado de "contrutor". É chamada automaticamente em cada novo objeto
        self.nome = nome #iniciando a propriedade nome com o valor informado pelo usuário
        self.notas = [] #iniciando a variável que armazenará as notas. Iniciamos com uma lista vazia
        
    def receber_notas(self) :
        while (True) :
            try :
                notas_cadastradas = len(self.notas)
                proxima_nota = notas_cadastradas + 1
                nota = input("informe a nota " + str(proxima_nota) + " ou aperte ENTER pra continuar: ")
                if (nota == '' and notas_cadastradas == 0) :
                    raise Exception("Informe ao menos uma nota")
                if (nota == '') :
                    break
                self.notas.append(float(nota))
            except :
                print("Informe uma nota válida no formato 12.24")
                
    def calcular_media(self) :
        soma_notas = 0
        for nota in self.notas :
            soma_notas += nota
        return soma_notas / len(self.notas)
                
#variavel "alunos" que armazenará todos os alunos inseridos
alunos = []
                
def listar_alunos():
    print("")
    print("Listando alunos...")
    for index in range(len(alunos)):
        aluno_media = alunos[index].calcular_media();
        aluno_status = "aprovado" if aluno_media > 5 else "reprovado"
        print("O(a) aluno(a) " + alunos[index].nome + " de Index " + str(index + 1) + ", possui média de " + str(aluno_media) + " e está " + aluno_status)


#Não sabemos quantas vezes o programa vai se repetir. Assim usaremos o "while true"
while (True) :
    print("")
    print("Escolha uma das opções e informe o número correspondente:")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos e suas médias")
    print("3 - Apagar aluno")
    print("0 - Sair")
    opcao_escolhida = input()
    match opcao_escolhida:
        case "0":
            print("Obrigado!")
            break
        case "1":
            novo_aluno = Aluno(input("Informe o nome do aluno: "))
            novo_aluno.receber_notas()
            alunos.append(novo_aluno)
        case "2":
            listar_alunos()
        case "3":
            index = input("Informe o Index (informado na listagem de alunos) do aluno pque será apagado: ")
            try:
                index = int(index) - 1
                if (index < 0 or index > len(alunos) - 1):
                    raise Exception("Index inválido")
                alunos.pop(index)
            except Exception as e:
                print(str(e))
        case _:
            print("Opção inválida")