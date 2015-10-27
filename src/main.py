import re

#Funciones
def dec_bin(numero):
	binario = "{0:b}".format(numero)
	long_actual = len(binario)
	if(long_actual < 5):
		binario = (5-long_actual)*"0" + binario
	return binario

def parse_r(line):
	pass

def parse_i(line):
	pass

def parse_j(line):
	pass
#Diccionarios
instrucciones_tipo_r = {
	"SLL":	"000000",
	"SRL":	"000010",
	"SRA":	"000011",
	"SRLV":	"000110",
	"SRAV":	"000111",
	"ADD":	"100000",
	"SLLV": "000100",
	"SUB":	"100010",
	"AND":	"100100",
	"OR":	"100101",
	"XOR":	"100110",
	"NOR":	"100111",
	"SLT":	"101010",
}

instrucciones_tipo_i = {
	"LB":	"100000",
	"LH":	"100001",
	"LW":	"100011",
	"LWU":	"100111",
	"LBU":	"100100",
	"LHU":	"100101",
	"SB":	"101000",
	"SH":	"101001",
	"SW":	"101011",
	"ADDI":	"001000",
	"ANDI":	"001100",
	"ORI":	"001101",
	"XORI":	"001110",
	"LUI":	"001111",
	"SLTI":	"001010",
	"BEQ":	"000100",
	"BNE":	"000101",
	"J":	"000010",
	"JAL":	"000011",
}

instrucciones_tipo_j = {
	"JR":	"001000",
	"JALR":	"001001",
}


#Logica
test_file = open("assembler.txt", "r")
assembler = test_file.readlines()

for line in assembler:
	line = line.strip()

	line_data = filter(None, re.split(r' |,' , line))
	instruction = line_data[0]
	if(instruction in instrucciones_tipo_r.keys()):
		parse_r(line_data)
	elif(instruction in instrucciones_tipo_i.keys()):
		parse_i(line_data)
	elif(instruction in instrucciones_tipo_j.keys()):
		parse_j(line_data)
	else:
		print("Instruccion no existe")

