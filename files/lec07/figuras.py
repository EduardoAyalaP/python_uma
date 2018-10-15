import pdb

def diamond(rows):
    total_diamond = ""
    mid_row = rows / 2 - 0.5
    if rows % 2 == 0:
        raise ValueError("Poner número impar")
    for i in range(rows):
        if i <= mid_row:
            nelemen = 2 * i + 1
        else:
            row_factor = 2 * (i - mid_row ) 
            nelemen = rows - row_factor

        row = ("*" * int(nelemen)).center(rows, " ")
        # total_diamond += row + "\n"
        print(row)


def is_amstrong(n):
    """
    Función para validar si un número entero positivo
    es un número de Amstrong
    
    parameters
    ----------
    n: int
        número a validar si es Amstrong
       
    Returns
    -------
    Bool:
        True si 'n' es Amstrong. Falso de otra manera
    """
    numbers = []
    total_sum = 0
    # Obtenemos cada dígito del número
    for ni in str(n):
        numbers.append(ni)

    len_numbers = len(numbers)
    
    for ni in numbers:
        total_sum = total_sum + int(ni) ** len_numbers 

    validation = True if total_sum == n else False
    return validation
    
def amstrong_between(a, b):
    """
    Función para encontrar todos los números
    amstrong entre un rango a, ..., b
    
    Parameters
    ----------
    a: int
        cota inferior a evaluar
    b: int
        cota superior a evaluar
    
    Returns
    -------
    list:
        elementos entre a, ... ,b que sean número de Amstrong
    """
    amstrong_numbers = []
    for i in range(a, b + 1):
        if is_amstrong(i):
            amstrong_numbers.append(i)
    
    return amstrong_numbers

if __name__ == "__main__":
    diamond(10)
