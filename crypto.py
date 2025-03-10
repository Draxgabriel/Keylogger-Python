def encryption(msg):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    msg = msg.lower()

    crypto = []

    for char in msg:
        if char in alfabeto:
            index = alfabeto.index(char) + 1
            crypto.append(str(index))

    arr = '-'.join(crypto)
    return arr

palavra = str(input("Coloque o texto para ser cryptografado: "))
if not palavra:
    print("Sem valor!!!")
    exit(-1)
resul = encryption(palavra)
print(f"Criptografado com sucesso: {resul}")
