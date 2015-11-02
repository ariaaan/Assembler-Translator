# Convertir de Decimal a Binario
def dec_bin(numero, digitos=5):
    binario = "{0:b}".format(numero)
    longitud_actual = len(binario)
    if longitud_actual < digitos:
        binario = (digitos - longitud_actual) * "0" + binario
    return binario


# Convertir de Binario a Hexadecimal
def bin_hex(numero, digitos=8):
    hexa = hex(int(numero, 2))
    hexa = hexa[2:]
    longitud_actual = len(hexa)
    if longitud_actual < digitos:
        hexa = (digitos - longitud_actual) * "0" + hexa
    return hexa
