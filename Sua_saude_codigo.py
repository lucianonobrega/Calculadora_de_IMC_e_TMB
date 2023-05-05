from time import sleep

def apresentacao():
    print("*" * 13)
    print("* Sua Saúde *")
    print("*" * 13)

def tela_opcoes():
    print("[1]Calcular IMC.\n[2]Calcular Taxa Metabólica Basal (TMB).\n[3]Explicações."
          "\n[4]Sair.")

def taxa_atividade_tabela():
    print("Taxa de atividade:\n-Sedentários = 1.2.\n-Levemente ativo (exercício leve 1 a 3 dias "
          "por semana) = 1.375.\n-Moderadamente ativo (exercício moderado 3 a 5 dias por  semana) = 1.55."
          "\n-Altamente ativo (exercício pesado 5 a 6 dias por semana) = 1.725.\n-Extremamente ativo ("
          "exercício pesado diariamente e até 2 vezes por dia) = 1.9. ")

def imc_tabela():
    print("-" * 31)
    print("Abaixo do peso: Abaixo de 18.5.\nPeso ideal: Entre 18.6 e 24.9.\nLevemente acima do peso: "
          "Entre 25.0 e 29.9.\nObesidade grau I: Entre 30.0 e 34.9.\nObesidade grau II: Entre 35.0 e 39.9.\n"
          "Obesidade III: Acima de 40.")
    print("-" * 31)

def calculo_imc(peso,altura):
    imc = peso/(altura)**2
    return imc

def tmb_homem(peso,altura,idade,taxa_atividade):
    tmb = taxa_atividade * (66 + (13.7 * peso) + (5 * altura) - (6.8 * idade))
    return tmb

def tmb_mulher(peso,altura,idade,taxa_atividade):
    tmb = taxa_atividade * (655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade))
    return tmb

def condicionais(opcao):
    sleep(2)
    if opcao == 1:
        try:
            peso = float(input("Digite o seu peso em Kg: "))
            altura = float(input("Digite a sua altura em metros (ex: 1.80): "))
            sleep(1)
            print(f"O seu IMC é de {calculo_imc(peso,altura):.2f}.")
            sleep(2)
            imc_tabela()
            sleep(5)
        except:
            print("Peso ou altura inválido.")
            sleep(1)
    elif opcao == 2:
        try:
            peso = float(input("Digite o seu peso em Kg: "))
            altura = float(input("Digite a sua altura em cm (ex: 180): "))
            idade = int(input("Digite a sua idade: "))
            sleep(1)
            taxa_atividade_tabela()
            sleep(2)
            taxa_atividade = float(input("Digite a sua taxa de atividade: "))
            sexo = str(input("Digite 'h' se você for homem ou 'm' se você for mulher: ")).lower()
            if sexo == "h":
                print(f"A sua taxa metabólica basal é de aproximadamente {tmb_homem(peso,altura,idade,taxa_atividade):.2f} kcal.")
                sleep(2)
            elif sexo == "m":
                print(f"A sua taxa metabólica basal é de aproximadamente {tmb_mulher(peso,altura,idade,taxa_atividade):.2f} kcal.")
                sleep(2)
        except:
            print("Você digitou algo errado em algum campo. Tente novamente.")
            sleep(2)
    elif opcao == 3:
        print("-O Índice de Massa Corporal, conhecido pela sigla IMC, é um cálculo simples que permite medir se alguém está ou não com o peso ideal.\n"
              "Ele aponta se o peso está adequado ou se está abaixo ou acima do peso.")
        sleep(6)
        print("-Metabolismo basal ou Taxa metabólica basal é um método matemático, inexato, de calcular a quantidade calórica que o corpo necessita,\n"
              "em vinte e quatro horas, para manter-se nutrido durante o decorrer das atividades diárias, e/ou fazendo um jejum de pelo\nmenos doze horas em repouso,"
              " sem prejudicar o funcionamento dos principais órgãos.")
        sleep(6)
    elif opcao == 4:
        print("Encerrando...")
        sleep(2)
        global a
        a = 0
    else:
        print("Opção inválida. Por favor, tente novamente.")
        sleep(2)

apresentacao()
sleep(2)
a = 1
while a == 1:
    try:
        tela_opcoes()
        sleep(2)
        opcao = int(input("Escolha a sua opção: "))
        condicionais(opcao)
    except:
        print("Opção inválida.")
        continue