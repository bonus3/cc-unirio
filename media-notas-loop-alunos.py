#programa que recebe nome de vários alunos e suas quatro notas e calcula a média de cada um

#Não sabemos quantos alunos o usuário irá informar, então precisamos que o trecho repita atá uma condição ser atingida
#Vamos fazer o programa repetir até o usuário informar a palavra "sair"
#A estrutura de repetição para quando não sabemos quantas vezes um trecho de código deve repetir é o "while"
while (True): #Repare que apenas informamos o valor boleano True. Assim vai repetir até usarmos um "break", que força parar uma repetição
    #Dentro desse while haverá o programa que criamos em media-notas-loop-notas.py, apenas adicionaremos a condição para sair
    

    #Receber o nome do aluno
    print("Escreva 'sair' para finalizar o programa.")
    nome_aluno = input("Informe o nome do aluno: ")
    
    #Verificamos se o usuário informou o valor "sair" e, se sim, saímos do loop
    if (nome_aluno == "sair") :
        print("Obrigado!")
        break # esse comando força o loop finalizar, sem executar os comandos seguintes. Funciona também com "for"

    #A varipavel "soma_notas" armazenará a soma das notas informadas
    #inicializamos com o valor zero e somaremos cada nota informada
    soma_notas = 0

    for x in range(1, 5):
        nota_digitada = float(input("Informe a nota " + str(x) + " de " + nome_aluno + ": "))
        soma_notas = soma_notas + nota_digitada #Adiciona o valor da nota digitada ao valor que estiver em "soma_notas"

    #cálculo da média: soma das notas dividido pelo número de notas
    media = soma_notas / 4

    #A variável "status_aluno" receberá o valor "aprovado" se a média for maior que 5. Caso contrário, receberá o valor "reprovado"
    if (media > 5) :
        status_aluno = "aprovado"
    else :
        status_aluno = "reprovado"
        
    #A mesma atribuição condicional de valor pra variável 'status_aluno' poderia ser feita de outra forma mais simplificada:
    status_aluno = "aprovado" if media > 5 else "reprovado" #Essa linha tem o mesmo resultado do if else anterior

    print("O(A) aluno(a) " + nome_aluno + " tem média " + str(media) + " e está " + status_aluno)
