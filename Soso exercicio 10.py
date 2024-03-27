def soma_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return soma, media

def substituir_palavra(lista, palavra_procurada, nova_palavra):
    return [nova_palavra if palavra == palavra_procurada else palavra for palavra in lista]

def gerar_triangulo(num_linhas):
    for i in range(1, num_linhas + 1):
        print('*' * i)

# Exemplos de uso das funções
if __name__ == "__main__":
    lista_numeros = [1, 2, 3, 4]
    soma, media = soma_media(lista_numeros)
    print("Soma:", soma)
    print("Média:", media)

    lista_palavras = ["banana", "morango", "limão"]
    nova_lista = substituir_palavra(lista_palavras, "morango", "maçã")
    print("Lista alterada:", nova_lista)

    num_linhas = 4
    gerar_triangulo(num_linhas)

 
