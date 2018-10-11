def sin_vocales(palabra):
    vocales = ["a", "e", "i", "o", "u"]
    for vocal in vocales:
        palabra = palabra.replace(vocal, "")
    return palabra

def scramble(palabra):
    """
    Esta función te regresa
    el las letras de la palabra invertidas
    cada par
    """
    n_palabra = ""
    if len(palabra) % 2 != 0:
        palabra = palabra[:-1]
    seq_impar = palabra[1::2]
    seq_par = palabra[::2]

    for ei, ep in zip(seq_impar, seq_par):
        n_palabra = n_palabra + ei + ep

    return n_palabra
    

# Solo se corre si, el código se ejecuta
# dentro de la línea de comandos
if __name__ == "__main__":
    print(scramble("carro"))
