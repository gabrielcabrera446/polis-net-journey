import math
def es_primo(n):
    if n>3:
        for i in range (2, math.isqrt(n)+1):
            if n % i == 0:
                return False
        return True
    elif n == 2 or n == 3:
        return True
    else:
        raise ValueError("El numero debe ser mayor o igual a 2")

def weighted_av (values, weights):
    mean = 0
    divisor = 0
    if (len(values) != 0 and len(weights) != 0 and len(values) == len(weights)):
        for i in range (0, len(values)):
            mean = mean + values[i]*weights[i]
            divisor = divisor + weights[i]
        if divisor != 0:
            return mean/divisor
        else:
            raise ValueError("Los pesos deben sumar algo distinto a 0")
    else:
        raise ValueError("Las listas no pueden ser vacias o tener distintas cantidades")
