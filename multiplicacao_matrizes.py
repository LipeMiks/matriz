def ler_matrizes_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        linhas = f.readlines()

    matrizes = []
    matriz = []

    for linha in linhas:
        linha = linha.strip()
        if not linha or linha.startswith('#'):
            if matriz:
                matrizes.append(matriz)
                matriz = []
        else:
            numeros = list(map(int, linha.split()))
            matriz.append(numeros)

    if matriz:
        matrizes.append(matriz)

    return matrizes


def verificar_matriz_quadrada(matriz):
    return all(len(linha) == len(matriz) for linha in matriz)


def somar(a, b):
    return a + b


def multiplicar(a, b):
    return a * b


def multiplicar_matrizes(A, B):
    n = len(A)
    resultado = [[0] * n for _ in range(n)]

    print("\nPasso a passo da multiplicacao:")
    for i in range(n):
        for j in range(n):
            soma = 0
            for k in range(n):
                mult = multiplicar(A[i][k], B[k][j])
                soma = somar(soma, mult)
                print(f"resultado[{i}][{j}] += {A[i][k]} * {B[k][j]} = {mult} -> soma parcial = {soma}")
            resultado[i][j] = soma

    return resultado


def imprimir_matriz(matriz, nome):
    print(f"\nMatriz {nome}:")
    for linha in matriz:
        print(' '.join(map(str, linha)))


# --- Execução principal ---

arquivo = 'matrizes.txt'  # Altere se necessário

matrizes = ler_matrizes_do_arquivo(arquivo)

if len(matrizes) != 2:
    print("Erro: O arquivo deve conter exatamente duas matrizes.")
    exit()

A, B = matrizes

if not verificar_matriz_quadrada(A) or not verificar_matriz_quadrada(B):
    print("Erro: As matrizes devem ser quadradas.")
    exit()

if len(A) != len(B):
    print("Erro: As matrizes devem ter o mesmo tamanho.")
    exit()

imprimir_matriz(A, "A")
imprimir_matriz(B, "B")

resultado = multiplicar_matrizes(A, B)

imprimir_matriz(resultado, "Resultado")
