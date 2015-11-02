from funciones import dec_bin, bin_hex


class AssemblerParser:
    # Definicion de Tipos
    TIPO_R = 0
    TIPO_I = 1
    TIPO_J = 2

    # Definicion de Subtipos
    SUBTIPO_1 = 3
    SUBTIPO_2 = 4
    SUBTIPO_3 = 5
    SUBTIPO_4 = 6
    SUBTIPO_5 = 7
    SUBTIPO_6 = 8

    # Diccionarios
    lista_instrucciones = {
        # Tipo R
        "SLL":  ["000000", TIPO_R, SUBTIPO_1],
        "SRL":  ["000010", TIPO_R, SUBTIPO_1],
        "SRA":  ["000011", TIPO_R, SUBTIPO_1],
        "SRLV": ["000110", TIPO_R, SUBTIPO_2],
        "SRAV": ["000111", TIPO_R, SUBTIPO_2],
        "ADD":  ["100000", TIPO_R, SUBTIPO_3],
        "SLLV": ["000100", TIPO_R, SUBTIPO_2],
        "SUB":  ["100010", TIPO_R, SUBTIPO_3],
        "AND":  ["100100", TIPO_R, SUBTIPO_3],
        "OR":   ["100101", TIPO_R, SUBTIPO_3],
        "XOR":  ["100110", TIPO_R, SUBTIPO_3],
        "NOR":  ["100111", TIPO_R, SUBTIPO_3],
        "SLT":  ["101010", TIPO_R, SUBTIPO_3],

        # Tipo I
        "LB":   ["100000", TIPO_I, SUBTIPO_1],
        "LH":   ["100001", TIPO_I, SUBTIPO_1],
        "LW":   ["100011", TIPO_I, SUBTIPO_1],
        "LWU":  ["100111", TIPO_I, SUBTIPO_1],
        "LBU":  ["100100", TIPO_I, SUBTIPO_1],
        "LHU":  ["100101", TIPO_I, SUBTIPO_1],
        "SB":   ["101000", TIPO_I, SUBTIPO_1],
        "SH":   ["101001", TIPO_I, SUBTIPO_1],
        "SW":   ["101011", TIPO_I, SUBTIPO_1],
        "ADDI": ["001000", TIPO_I, SUBTIPO_2],
        "ANDI": ["001100", TIPO_I, SUBTIPO_2],
        "ORI":  ["001101", TIPO_I, SUBTIPO_3],
        "XORI": ["001110", TIPO_I, SUBTIPO_2],
        "LUI":  ["001111", TIPO_I, SUBTIPO_4],
        "SLTI": ["001010", TIPO_I, SUBTIPO_3],
        "BEQ":  ["000100", TIPO_I, SUBTIPO_5],
        "BNE":  ["000101", TIPO_I, SUBTIPO_5],
        "J":    ["000010", TIPO_I, SUBTIPO_6],
        "JAL":  ["000011", TIPO_I, SUBTIPO_6],

        # Tipo J
        "JR":   ["001000", TIPO_J, SUBTIPO_1],
        "JALR": ["001001", TIPO_J, SUBTIPO_2],
    }

    def parsear_assembler(self, asm_file, coe_file):
        # Logica
        test_file = open(asm_file, "r")
        assembler = test_file.readlines()

        lista_instrucciones_hexa = []

        for linea in assembler:
            linea = linea.strip()
            linea = self.eliminar_comentarios(linea)

            if linea:
                instruccion, operandos = self.parsear_instruccion(linea)

                if self.lista_instrucciones[instruccion][1] == self.TIPO_I:
                    instruccion_binaria = self.parse_i(instruccion, operandos)
                elif self.lista_instrucciones[instruccion][1] == self.TIPO_J:
                    instruccion_binaria = self.parse_j(instruccion, operandos)
                elif self.lista_instrucciones[instruccion][1] == self.TIPO_R:
                    instruccion_binaria = self.parse_r(instruccion, operandos)

                instruccion_hexa = bin_hex(instruccion_binaria)

                lista_instrucciones_hexa.append(instruccion_hexa)

        coe_text = self.crear_coe(lista_instrucciones_hexa)

        test_file = open(coe_file, "w")
        test_file.write(coe_text)

    def parsear_instruccion(self, linea):
        linea = linea.replace(",", "")
        data = linea.split()
        instruccion = data[0]
        operandos = data[1:]
        return instruccion, operandos

    def parse_r(self, instruccion, operandos):
        subtipo = self.lista_instrucciones[instruccion][2]
        codigo_operacion = self.lista_instrucciones[instruccion][0]

        instruccion_binaria = "0" * 6

        if subtipo == self.SUBTIPO_1:
            instruccion_binaria += "0" * 5
            instruccion_binaria += dec_bin(int(operandos[1]))
            instruccion_binaria += dec_bin(int(operandos[0]))
            instruccion_binaria += dec_bin(int(operandos[2]))
        elif subtipo == self.SUBTIPO_2:
            instruccion_binaria += dec_bin(int(operandos[2]))
            instruccion_binaria += dec_bin(int(operandos[1]))
            instruccion_binaria += dec_bin(int(operandos[0]))
            instruccion_binaria += "0" * 5
        elif subtipo == self.SUBTIPO_3:
            instruccion_binaria += dec_bin(int(operandos[1]))
            instruccion_binaria += dec_bin(int(operandos[2]))
            instruccion_binaria += dec_bin(int(operandos[0]))
            instruccion_binaria += "0" * 5

        instruccion_binaria += codigo_operacion

        return instruccion_binaria

    def parse_i(self, instruccion, operandos):
        subtipo = self.lista_instrucciones[instruccion][2]
        codigo_operacion = self.lista_instrucciones[instruccion][0]

        instruccion_binaria = codigo_operacion

        if subtipo == self.SUBTIPO_1:
            # Quito los parentesis y lo pongo como un tercer argumento
            operandos[1] = operandos[1].replace("(", " ")
            operandos[1] = operandos[1].replace(")", "")
            operandos.append(operandos[1].split()[1])
            operandos[1] = operandos[1][0]

            instruccion_binaria += dec_bin(int(operandos[2]))
            instruccion_binaria += dec_bin(int(operandos[0]))
            instruccion_binaria += dec_bin(int(operandos[1]), digitos=16)
        elif subtipo == self.SUBTIPO_2 or subtipo == self.SUBTIPO_3:
            instruccion_binaria += dec_bin(int(operandos[1]))
            instruccion_binaria += dec_bin(int(operandos[0]))
            instruccion_binaria += dec_bin(int(operandos[2]), digitos=16)
        elif subtipo == self.SUBTIPO_4:
            instruccion_binaria += "0" * 5
            instruccion_binaria += dec_bin(int(operandos[0]))
            instruccion_binaria += dec_bin(int(operandos[1]), digitos=16)
        elif subtipo == self.SUBTIPO_5:
            instruccion_binaria += dec_bin(int(operandos[0]))
            instruccion_binaria += dec_bin(int(operandos[1]))
            instruccion_binaria += dec_bin(int(operandos[2]), digitos=16)
        elif subtipo == self.SUBTIPO_6:
            instruccion_binaria += dec_bin(int(operandos[0]), digitos=26)

        return instruccion_binaria

    def parse_j(self, instruccion, operandos):
        subtipo = self.lista_instrucciones[instruccion][2]
        codigo_operacion = self.lista_instrucciones[instruccion][0]

        instruccion_binaria = "0" * 6

        if subtipo == self.SUBTIPO_1:
            instruccion_binaria += dec_bin(int(operandos[0]))
            instruccion_binaria += "0" * 15
        elif subtipo == self.SUBTIPO_2:
            instruccion_binaria += dec_bin(int(operandos[0]))
            instruccion_binaria += "0" * 5

            # Veo si hay mas de un operando (es decir, existe "rd")
            if len(operandos) > 1:
                instruccion_binaria += dec_bin(int(operandos[1]))
            else:
                instruccion_binaria += "0" * 5

        instruccion_binaria += codigo_operacion

        return instruccion_binaria

    def eliminar_comentarios(self, linea):
        linea = linea.split(";")
        instruccion = linea[0]
        return instruccion

    def crear_coe(self, lista):
        MEMORY_INITIALIZATION_RADIX = "memory_initialization_radix"
        MEMORY_INITIALIZATION_RADIX_VALUE = "16"

        MEMORY_INITIALIZATION_VECTOR = "memory_initialization_vector"

        texto_archivo = MEMORY_INITIALIZATION_RADIX + "="
        texto_archivo += MEMORY_INITIALIZATION_RADIX_VALUE + ";" + "\n"

        texto_archivo += MEMORY_INITIALIZATION_VECTOR + "=" + "\n"

        for item in lista:
            texto_archivo += item + ",\n"

        texto_archivo = texto_archivo[:-2] + ";"

        return texto_archivo

# Main
parser = AssemblerParser()
parser.parsear_assembler("files/assembler.txt", "files/salida.coe")
