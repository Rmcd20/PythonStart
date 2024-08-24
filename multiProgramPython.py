from datetime import datetime

def calcular_imc(peso, altura):
    """Calcula (IMC)."""
    return peso / (altura ** 2)

def classificar_imc(imc):
    """Classifica categ."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif imc >= 30:
        return "Obesidade"
    else:
        return "Valor de IMC inválido"

def verificar_data(dia, mes, ano):
    """Verifica se a data é válida."""
    try:
        datetime(ano, mes, dia)
        return True
    except ValueError:
        return False

def calcular_fase_lua(data_atual):
    """ fase da Lua para uma data específica."""
    data_lua_nova = datetime(2000, 1, 6)
    dias_passados = (data_atual - data_lua_nova).days
    fase = (dias_passados % 29.53) / 29.53
    
    if 0 <= fase < 0.25:
        return "Lua Nova"
    elif 0.25 <= fase < 0.5:
        return "Lua Crescente"
    elif 0.5 <= fase < 0.75:
        return "Lua Cheia"
    else:
        return "Lua Minguante"

def coletar_temperaturas():
    """ temperaturas diárias da semana."""
    temperaturas = []
    dias = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
    
    for dia in dias:
        while True:
            try:
                temperatura = float(input(f"Digite a temperatura para {dia}: "))
                if temperatura < -100 or temperatura > 60:
                    print("Temperatura fora do intervalo válido. Por favor, insira um valor entre -100 e 60 graus Celsius.")
                else:
                    temperaturas.append(temperatura)
                    break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
    
    return temperaturas

def calcular_estatisticas(temperaturas):
    """Calcula e retorna  temperatura média, máxima e mínima."""
    temperatura_media = sum(temperaturas) / len(temperaturas)
    temperatura_maxima = max(temperaturas)
    temperatura_minima = min(temperaturas)
    
    return temperatura_media, temperatura_maxima, temperatura_minima

def exibir_estatisticas(temperatura_media, temperatura_maxima, temperatura_minima):
    """Exibe as estatísticas de temperatura calculadas."""
    print(f"\nTemperatura média da semana: {temperatura_media:.2f}°C")
    print(f"Temperatura máxima da semana: {temperatura_maxima:.2f}°C")
    print(f"Temperatura mínima da semana: {temperatura_minima:.2f}°C")

def menu():
    """MENU."""
    while True:
        print("\nMenu:")
        print("1. Calcular IMC")
        print("2. Determinar Fase da Lua")
        print("3. Analisar Temperaturas Semanal")
        print("4. Sair")
        opcao = input("Escolha uma opção (1/2/3/4): ")
        
        if opcao == '1':
            try:
                peso = float(input('Digite seu peso (em kg): '))
                altura = float(input('Digite sua altura (em metros): '))
                if altura <= 0 or peso <= 0:
                    print("Peso e altura devem ser positivos. Tente novamente.")
                    continue
                imc = calcular_imc(peso, altura)
                categoria = classificar_imc(imc)
                print(f'Seu IMC é: {imc:.2f}')
                print(f'Classificação: {categoria}')
            except ValueError:
                print("Entrada inválida. Por favor, insira números válidos para peso e altura.")
        
        elif opcao == '2':
            while True:
                try:
                    dia = int(input("Digite o dia (ex: 24): "))
                    mes = int(input("Digite o mês (ex: 8): "))
                    ano = int(input("Digite o ano (ex: 2024): "))
                    
                    if verificar_data(dia, mes, ano):
                        data_atual = datetime(ano, mes, dia)
                        fase_lua = calcular_fase_lua(data_atual)
                        print(f"A fase da Lua em {data_atual.strftime('%d/%m/%Y')} é: {fase_lua}")
                        break
                    else:
                        print("Data inválida. Por favor, insira uma data válida.")
                except ValueError:
                    print("Entrada inválida. Por favor, insira números inteiros válidos para dia, mês e ano.")
        
        elif opcao == '3':
            temperaturas = coletar_temperaturas()
            temperatura_media, temperatura_maxima, temperatura_minima = calcular_estatisticas(temperaturas)
            exibir_estatisticas(temperatura_media, temperatura_maxima, temperatura_minima)
        
        elif opcao == '4':
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida! Por favor, escolha 1, 2, 3 ou 4.")

if __name__ == "__main__":
    menu()
