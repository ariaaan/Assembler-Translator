import re


# Funciones
def dec_bin(numero, digitos=5):
    binario = "{0:b}".format(numero)
    longitud_actual = len(binario)
    if longitud_actual < digitos:
        binario = (digitos - longitud_actual) * "0" + binario
    return binario


def bin_hex(numero, digitos=8):
    hexa = hex(int(numero, 2))
    hexa = hexa[2:]
    longitud_actual = len(hexa)
    if longitud_actual < digitos:
        hexa = (digitos - longitud_actual) * "0" + hexa
    return hexa


def parse_r(instruccion, operandos):
    instruccion_binaria = "0" * 6
    instruccion_binaria += dec_bin(int(operandos[0]))
    instruccion_binaria += dec_bin(int(operandos[1]))
    instruccion_binaria += dec_bin(int(operandos[2]))
    instruccion_binaria += "0" * 5
    instruccion_binaria += instrucciones_tipo_r[instruccion]

    return instruccion_binaria


def parse_i(instruccion, operandos):
    if len(operandos) == 2:
        # Quito los parentesis y lo pongo como un tercer argumento
        operandos[1] = operandos[1].replace("(", " ")
        operandos[1] = operandos[1].replace(")", "")
        operandos.append(operandos[1].split()[1])
        operandos[1] = operandos[1][0]

    instruccion_binaria = instrucciones_tipo_i[instruccion]
    instruccion_binaria += dec_bin(int(operandos[0]))
    instruccion_binaria += dec_bin(int(operandos[1]))
    instruccion_binaria += dec_bin(int(operandos[2]), digitos=16)

    return instruccion_binaria


def parse_j(instruccion, operandos):
    instruccion_binaria = ""

    return instruccion_binaria


def eliminar_comentarios(linea):
    linea = linea.split(";")
    instruccion = linea[0]
    return instruccion


def parse_instruccion(linea):
    linea = linea.replace(",", "")
    data = linea.split()
    instruccion = data[0]
    operandos = data[1:]
    return instruccion, operandos


# Diccionarios
instrucciones_tipo_r = {
    "SLL": "000000",
    "SRL": "000010",
    "SRA": "000011",
    "SRLV": "000110",
    "SRAV": "000111",
    "ADD": "100000",
    "SLLV": "000100",
    "SUB": "100010",
    "AND": "100100",
    "OR": "100101",
    "XOR": "100110",
    "NOR": "100111",
    "SLT": "101010",
}

instrucciones_tipo_i = {
    "LB": "100000",
    "LH": "100001",
    "LW": "100011",
    "LWU": "100111",
    "LBU": "100100",
    "LHU": "100101",
    "SB": "101000",
    "SH": "101001",
    "SW": "101011",
    "ADDI": "001000",
    "ANDI": "001100",
    "ORI": "001101",
    "XORI": "001110",
    "LUI": "001111",
    "SLTI": "001010",
    "BEQ": "000100",
    "BNE": "000101",
    "J": "000010",
    "JAL": "000011",
}

instrucciones_tipo_j = {
    "JR": "001000",
    "JALR": "001001",
}


def main():
    # Logica
    test_file = open("assembler.txt", "r")
    assembler = test_file.readlines()

    for linea in assembler:
        linea = linea.strip()
        linea = eliminar_comentarios(linea)

        if linea:
            instruccion, operandos = parse_instruccion(linea)

            print("ASM:", instruccion, ", ".join(operandos))

            if instruccion in instrucciones_tipo_i.keys():
                instruccion_binaria = parse_i(instruccion, operandos)
            elif instruccion in instrucciones_tipo_j.keys():
                instruccion_binaria = parse_j(instruccion, operandos)
            elif instruccion in instrucciones_tipo_r.keys():
                instruccion_binaria = parse_r(instruccion, operandos)

            print("BIN:", instruccion_binaria)

            instruccion_hexa = bin_hex(instruccion_binaria)
            print("HEX:", instruccion_hexa)
            print()


main()
