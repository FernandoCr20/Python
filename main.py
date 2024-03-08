# arquivo = open("texto.txt", "r")
# print(arquivo.read())
# #print(arquivo.seek(0))
# print(arquivo.tell())
# #print(arquivo.read(8))
# arquivo.close()
# print(arquivo.closed)

# arquivo = open("novo.txt", "w")
# arquivo.write("Arquivo de escrita")
# arquivo.close()
# print(arquivo.closed)

# arquivo = open("frutas.txt", "w")
# arquivo.write("banana \n")
# arquivo.write("uva \n")
# arquivo.write("mamao \n")
# arquivo.close()
# print(arquivo.closed)

# precos = [20, 100, 500, 600]
# with open("precos_roupas.txt", "w") as arquivo:
#     for preco in precos:
#         arquivo.write(str(preco) + '\n')
# print(arquivo.closed)

# precos = [80000]
# with open("precos_roupas.txt", "a") as arquivo:
#     for preco in precos:
#         arquivo.write(str(preco) + '\n')
# print(arquivo.closed)

# precos = [10000]
# with open("precos_roupas.txt", "w") as arquivo:
#     for preco in precos:
#         arquivo.write(str(preco) + '\n')
# print(arquivo.closed)

# disciplinas = ["RAD \n", "Introdução a C \n", "Segurança da informação \n"]
# with open("disciplinas.txt", "w") as file:
#     file.write("Relação de disciplinas \n")
#     file.writelines(disciplinas)
# with open("disciplinas.txt", "r") as file:
#     print(file.read())
# print(file.closed)

# with open("texto.txt", "r") as arquivo:
#     print("conteudo da linha")
#     for linha in arquivo:
#         print(repr(linha))

# with open("texto.txt", "r") as arquivo:
#     print("Conteudo da linha")
#     for linha in arquivo:
#         linha_ = linha.strip()
#         print(repr(linha_))

''' Tratamento de exceções '''

# try:
#     with open("arquivo_teste.txt", "r") as arquivo:
#         print(arquivo.read())
# except FileNotFoundError:
#     print("arquivo não existe")

# import os
# try:
#     os.remove("teste2.txt")
#     print("Arquivo foi removido")
# except FileNotFoundError as error:
#     print("Descrição", error)
    
# try:
#     f = open("novo.txt", "r")
#     f.write("Hello")
# except IOError as erro:
#     print("O erro foi:", erro)

