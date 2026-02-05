import math

def sumaCplx(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])

def restaCplx(c1, c2):
    return (c1[0] - c2[0], c1[1] - c2[1])

def prodCplx(c1, c2):
    a1, b1 = c1
    a2, b2 = c2
    return (a1*a2 - b1*b2, a1*b2 + a2*b1)

def divisionCplx(c1, c2):
    a1, b1 = c1
    a2, b2 = c2
    denominador = a2**2 + b2**2
    real = (a1*a2 + b1*b2) / denominador
    imag = (a2*b1 - a1*b2) / denominador
    return (round(real, 2), round(imag, 2))

def moduloClpx(c):
    return round(math.sqrt(c[0]**2 + c[1]**2), 2)

def conjugadoClpx(c):
    return (c[0], -c[1])

def conversionPolarCartesianoClpx(c):
    r, theta = c
    real = r * math.cos(theta)
    imag = r * math.sin(theta)
    return (round(real, 2), round(imag, 2))

def conversionCartesianoPolarClpx(c):
    a, b = c
    r = math.sqrt(a**2 + b**2)
    theta = math.atan2(b, a)
    return (round(r, 2), round(theta, 2))

def faseClpx(c):
    return round(math.atan2(c[1], c[0]), 2)
