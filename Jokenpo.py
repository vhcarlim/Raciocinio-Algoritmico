import random
import time

RESET   ="\033{0m"
BOLD    ="\033{1m"
GREEN   ="\033[91m"
YELLOW  ="\033[93m"
CYAN    ="\033[96m"
MAGENTA ="\033[95m"

print(CYAN + "=" * 50 + RESET)
print(BOLD + MAGENTA + " ✊ JOKENPÔ - Pedra, Papel ou Tesoura! ✂️" + RESET)
print(CYAN + "=" * 50 + RESET)
print()
print(BOLD + "  Bem-vindo ao Jokenpô!\n" + RESET)
print("  Escolha a modalidade:")
print("  1 - 👤 Humano x Humano")
print("  2 - 👤 Humano x 🤖 Computador")
print("  3 - 🤖 Computador x 🤖 Computador")

modalidade = int(input(BOLD + " Digite 1, 2 ou 3: " + RESET))
while modalidade < 1 or modalidade > 3:
    print(RED + "  Modalidade inválida!" + RESET)
    modalidade = int(input(BOLD + "  Digite 1, 2 ou 3: " + RESET))
  
if modalidade == 1:
    nome1 = input(CYAN + "\n Nome do Jogador 1: " + RESET)
    nome2 = input(CYAN + " Nome do Jogador 2: " + RESET)
elif modalidade == 2:
    nome1 = input(CYAN + "\n Nome do Jogador 2: " + RESET)
    nome2 = "🤖 Computador"
else:
    nome1= "🤖 Computador 1"
    nome2= "🤖 Computador 2"

vitorias1 = 0
vitorias2 = 0
empates =0
continuar = "S"
