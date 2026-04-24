import random # jogadas aleatórias do computador
import time # contagem regressiva e pausas

# cabeçalho inicial do programa
print("  Trabalho acadêmico de Raciocínio Algorítmico - JOKENPÔ ")
time.sleep(1.5)
print("  Bem-vindo! ")
print("  Por favor, escolha a modalidade: ")
time.sleep(1.5)
print("  1 - Humano x Humano ")
print("  2 - Humano x Computador ")
print("  3 - Computador x Computador ")

# validação da modalidade escolhida
modalidade = int(input("  Digite 1, 2 ou 3: "))
while modalidade < 1 or modalidade > 3:
    print("  Modalidade inválida!")
    modalidade = int(input("  Digite exatamente 1, 2 ou 3: "))
# definição dos nomes dos jogadores
if modalidade == 1:
    nome1 = input("  Nome do Jogador 1: ")
    nome2 = input("  Nome do Jogador 2: ")
elif modalidade == 2:
    nome1 = input("  Nome do Jogador: ")
    nome2 = "Computador"
else:
    nome1 = "Computador 1"
    nome2 = "Computador 2"

# inicialização das variáveis de contagem de vitórias e empates
vitorias1 = 0
vitorias2 = 0
empates   = 0
continuar = "S"
# loop principal do jogo
while continuar == "S":
# início de cada partida com contagem regressiva para criar suspense
    print("  Nova partida comecando...")
    print("  3...")
    time.sleep(0.5)
    print("  2...")
    time.sleep(0.5)
    print("  1...")
    time.sleep(0.5)
# para a modalidade Humano x Humano, as jogadas de ambos os jogadores são solicitadas via input
    if modalidade == 1:
        print(f"\n  {nome1}, escolha sua jogada:")
        print("  1 - Pedra")
        print("  2 - Papel")
        print("  3 - Tesoura")
        jogada1 = int(input("  Digite 1, 2 ou 3: "))
        while jogada1 < 1 or jogada1 > 3:
            print("  Jogada inválida!")
            jogada1 = int(input("  Digite 1, 2 ou 3: "))
        print(f"\n  {nome2}, escolha sua jogada:")
        print("  1 - Pedra")
        print("  2 - Papel")
        print("  3 - Tesoura")
        jogada2 = int(input("  Digite 1, 2 ou 3: "))
        while jogada2 < 1 or jogada2 > 3:
            print("  Jogada invalida!")
            jogada2 = int(input("  Digite 1, 2 ou 3: "))
# para a modalidade Humano x Computador, a jogada do jogador é solicitada via input, enquanto a jogada do computador é gerada aleatoriamente com o random
    elif modalidade == 2:
        print(f"\n  {nome1}, escolha sua jogada:")
        print("  1 - Pedra")
        print("  2 - Papel")
        print("  3 - Tesoura")
        jogada1 = int(input("  Digite 1, 2 ou 3: "))
        while jogada1 < 1 or jogada1 > 3:
            print("  Jogada invalida!")
            jogada1 = int(input("  Digite 1, 2 ou 3: "))
        jogada2 = random.randint(1, 3)
# para a modalidade Computador x Computador, as jogadas de ambos os jogadores são geradas aleatoriamente
    else:
        jogada1 = random.randint(1, 3)
        jogada2 = random.randint(1, 3)
# determinação do nome da jogada do primeiro jogador para exibição posterior
    if jogada1 == 1:
        nome_jogada1 = "Pedra"
    elif jogada1 == 2:
        nome_jogada1 = "Papel"
    else:
        nome_jogada1 = "Tesoura"
# determinação do nome da jogada do segundo jogador para exibição posterior
    if jogada2 == 1:
        nome_jogada2 = "Pedra"
    elif jogada2 == 2:
        nome_jogada2 = "Papel"
    else:
        nome_jogada2 = "Tesoura"
# exibição das jogadas de cada jogador
    print(f"  {nome1} jogou: {nome_jogada1}")
    time.sleep(1.5)
    print(f"  {nome2} jogou: {nome_jogada2}")
    time.sleep(1.5)
# determinação do vencedor da partida e atualização do placar
    if jogada1 == jogada2:
        print("  Empate!")
        empates = empates + 1
    elif (jogada1 == 1 and jogada2 == 3) or (jogada1 == 2 and jogada2 == 1) or (jogada1 == 3 and jogada2 == 2):
        print(f"  {nome1} venceu essa partida!")
        vitorias1 = vitorias1 + 1
    else:
        print(f"  {nome2} venceu essa partida!")
        vitorias2 = vitorias2 + 1
# print do placar atualizado após cada partida
    print("  Placar atual:")
    print(f"  {nome1}: {vitorias1} vitoria(s)")
    print(f"  {nome2}: {vitorias2} vitoria(s)")
    print(f"  Empates: {empates}")
# opção para continuar jogando ou encerrar o jog
    print()
    continuar = input("  Deseja continuar? (S para sim / N para sair): ").strip().upper()
    while continuar != "S" and continuar != "N":
        print("  Opção inválida! Digite S ou N.")
        continuar = input("  Deseja continuar? (S/N): ").strip().upper()

# fim do jogo e exibição do placar final

print("  Fim de jogo! Placar final:")
print(f"  {nome1}: {vitorias1} vitoria(s)")
print(f"  {nome2}: {vitorias2} vitoria(s)")
print(f"  Empates: {empates}")
if vitorias1 > vitorias2:
    print(f"  Grande vencedor: {nome1}! Parabens!")
elif vitorias2 > vitorias1:
    print(f"  Grande vencedor: {nome2}! Parabens!")
else:
    print("  O jogo terminou empatado!")

print("  Código desenvolvido por: Felipe, Pedro e Victor")
print("  Game Over! Até a próxima!")
