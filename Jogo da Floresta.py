# Jogo da Floresta
print("Você está em uma simulação de uma floresta e precisa escolher um caminho para o seu personagem.")
print("Você pode escolher: esquerda ou direita")

caminho = input("Qual caminho você escolhe? ")

if caminho == "esquerda":
    print("Você encontrou um rio!")
    print("Você pode: atravessar ou voltar")
    decisao_esquerda = input("O que você decide? ")

    if decisao_esquerda == "atravessar":
        print("Você chegou a uma vila segura!")
    elif decisao_esquerda == "voltar":
        print("Você permanece perdido na floresta.")
    else:
        print("Opção inválida!")

elif caminho == "direita":
    print("Você encontrou uma montanha!")
    print("Você pode: subir ou voltar")
    decisao_direita = input("O que você decide? ")

    if decisao_direita == "subir":
        print("Você encontrou um tesouro no topo!")
    elif decisao_direita == "voltar":
        print("Você permanece perdido na floresta.")
    else:
        print("Opção inválida!")

else:
    print("Opção inválida!")
