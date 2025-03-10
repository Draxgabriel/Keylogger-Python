def descriptografar(dig):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    numeros = dig.split('-') 

    decrypto = [alfabeto[int(num) - 1] for num in numeros]
    arr = ''.join(decrypto)
    return arr

resul = descriptografar("15-16-1")
print(f"Decriptografado com sucesso: {resul}")
