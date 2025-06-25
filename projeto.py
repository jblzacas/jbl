import datetime
gastos = []
tipos_gasto = []

CINZA = '\033[90m'
MAGENTA = '\033[35m'
VERMELHO = '\033[31m'
AMARELO = '\033[33m'
BRANCO = "\033[97m"
RESET = '\033[0m'
AZUL = '\033[34m'
CIANO = '\033[36m'
VERDE = '\033[92m'

def cadastrartipogasto():
    print(f"{AZUL}=== cadastro de tipos de gasto ={RESET}")
    while True:
        tipo = input(f"{VERDE}digite um tipo de gasto, (aperta enter se ja terminou): {RESET}")
        if tipo == "":
            print(f"{VERMELHO}fechando cadastro de tipos.{RESET}")
            break #se n tiver nada, encerrar o codigo
        elif tipo in tipos_gasto:
            print(f"{VERDE}tipo de gasto cadastrado✅.{RESET}")
        else:
            tipos_gasto.append(tipo)#adiciona um tipo de gasto
            print(f"{VERDE}tipo '{tipo}' cadastrado com sucesso✅{RESET}")# sucesso no cadastro do tipo
def cadastrargasto():
    if len(tipos_gasto) == 0:
        print(F"{VERMELHO}nenhum tipo de gasto cadastrado❌.{RESET}")
        return
    print(F"{AZUL}tipos de gasto disponíveis:{RESET}")
    i = 0
    while i < len(tipos_gasto):
        print(f"{i + 1}. {tipos_gasto[i]}")
        i += 1 #adiciona numeros aos tipos pra ficar mais facil a seleção
    try:
        escolha = int(input(F"{AZUL}escolha o número do tipo de gasto: {RESET}"))
        if escolha < 1 or escolha > len(tipos_gasto):
            print(F"{VERMELHO}opção errada❌.{RESET}")
            return# escolher tipo de acordo com o numero designado
        tipo_escolhido = tipos_gasto[escolha - 1]
    except ValueError:
        print(F"{VERMELHO}entrada errada❌. digite um número{RESET}.")
        return
    dia = input(F"{BRANCO}digite o dia do mês (1-31): {RESET}")
    valor = input(F"{CIANO}digite o valor do gasto: {RESET}")
    gasto = {
        "tipo": tipo_escolhido,
        "dia": dia,
        "valor": valor
    }
    gastos.append(gasto)
    print(F"{VERDE}gasto cadastrado com sucesso✅{RESET}")
def consultargastos():
    if len(gastos) == 0:
        print(F"{VERMELHO}nenhum gasto cadastrado.{RESET}")
        return
    print(F"{BRANCO}=== lista de gastos ==={RESET}")
    i = 0
    while i < len(gastos):
        gasto = gastos[i]
        try:
            valor = float(gasto["valor"])
            print(f"{i + 1}. Tipo: {gasto['tipo']} | Dia: {gasto['dia']} | Valor: R$ {valor:}")
        except ValueError:
            print(f"{i + 1}. Tipo: {gasto['tipo']} | Dia: {gasto['dia']} | Valor: [valor inválido]")
        i += 1 #adiciona numeros aos gastos para seleção
    print()
def buscargastos():
    if len(tipos_gasto) == 0:
        print(F"{VERMELHO}nenhum tipo de gasto cadastrado para buscar.{RESET}")
        return
    print(F"{BRANCO}tipos de gasto disponíveis:{RESET}")
    i = 0
    while i < len(tipos_gasto):
        print(f"{i + 1}. {tipos_gasto[i]}")
        i += 1
    try:
        escolha = int(input(F"{BRANCO}escolha o número do tipo de gasto: {RESET}"))
        if escolha < 1 or escolha > len(tipos_gasto):
            print("opção invalida.")
            return
        tipoescolhido = tipos_gasto[escolha - 1]
    except ValueError:
        print(F"{VERMELHO}entrada errada. digite um número.{RESET}")
        return
    encontrados = []
    i = 0
    while i < len(gastos):
        gasto = gastos[i]
        if gasto["tipo"] == tipoescolhido:
            encontrados.append(gasto)
        i += 1
    if len(encontrados) == 0:
        print(f"{VERMELHO}nenhum gasto encontrado para o tipo '{tipoescolhido}'.{RESET}")
        return
    print(f"{BRANCO}=== Gastos do tipo '{tipoescolhido}' ==={RESET}")
    i = 0
    while i < len(encontrados):
        gasto = encontrados[i]
        print(f"{i + 1}. Dia: {gasto['dia']} | Valor: {gasto['valor']}")
        i += 1
    print()
def totalgastos():
    if len(gastos) == 0:
        print(F"{VERMELHO}nenhum gasto cadastrado.{RESET}")
        return
    mesatual = datetime.datetime.now().strftime("%B")
    total = 0.0
    i = 0
    while i < len(gastos):
        gasto = gastos[i]
        try:
            total += float(gasto["valor"])
        except ValueError:
            print(f"{VERMELHO}Valor incorreto no gasto: {gasto}.{RESET}")
        i += 1
    print(f"total de gastos cadastrados em {mesatual}: R$ {total:}")
def mostramenu():
    while True:
        print(f"{BRANCO}=== sistema de controle de gastos ==={RESET}")
        print(F"{AZUL}1. cadastrar tipos de gastos{RESET}")
        print(F"{AZUL}2. cadastrar gastos{RESET}")
        print(F"{AZUL}3. ver todos os gastos{RESET}")
        print(f"{AZUL}4. buscar por tipo{RESET}")
        print(f"{AZUL}5. total do mês{RESET}")
        print(f"{VERMELHO}6. Sair{RESET}")
        escolha = input(f"{BRANCO}escolha uma opção: {RESET}")
        if escolha == "1":
            cadastrartipogasto()
        elif escolha == "2":
            cadastrargasto()
        elif escolha == "3":
            consultargastos()
        elif escolha == "4":
            buscargastos()
        elif escolha == "5":
            totalgastos()
        elif escolha == "6":
            print(f"{BRANCO}saindo do melhor sistema do mundo👻{RESET}")
            break
        else:
            print(f"{VERMELHO}Opção não existe, tente de novo{RESET}")
mostramenu()
