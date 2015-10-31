# Tipo de Instrucciones

---

## Tipo "R" (3 Subtipos)

### Subtipo 1
#### Instrucciones:
- SLL
- SRL
- SRA

#### Formato de la Instrucción en assembler:

```
INSTRUCCION rd, rt, rs
```   

#### Formato de la Instrucción en binario:

```
000000 - 00000 - rt - rd - sa - INSTCODE
```

### Subtipo 2
#### Instrucciones:
- SRLV
- SRAV
- SLLV

#### Formato de la Instrucción en assembler:

```
INSTRUCCION rd, rt, rs
```

#### Formato de la Instrucción en binario:

```
000000 - rs - rt - rd - 00000 - (INSTCODE)
```

### Subtipo 3
#### Instrucciones:
- ADD
- SUB
- AND
- OR
- XOR
- NOR
- SLT

#### Formato de la Instrucción en assembler:

```
INSTRUCCION rd, rs, rt
```

#### Formato de la Instrucción en binario:

```
000000 - rs - rt - rd - 00000 - INSTCODE
```

---

## Tipo "I" (6 Subtipos)

### Subtipo 1
#### Instrucciones:
- LB
- LH
- LW
- LWU
- LBU
- LHU
- SB
- SH
- SW

#### Formato de la Instrucción en assembler:

```
INSTRUCCION rt, offset(base)     -->     INSTRUCCION rt, offset, base
```

#### Formato de la Instrucción en binario:

```
INSTCODE - base - rt - offset
```

### Subtipo 2
#### Instrucciones:
- ADDI
- ANDI
- XORI

#### Formato de la Instrucción en assembler:

````
INSTRUCCION rt, rs, immediate
````

#### Formato de la Instrucción en binario:

````
INSTCODE - rs - rt - immediate
````

### Subtipo 3
> Se podría unir con el Subtipo 2

#### Instrucciones:
- ORI
- SLTI

#### Formato de la Instrucción en assembler:

```
INSTRUCCION rs, rt, immediate
```

#### Formato de la Instrucción en binario:

```
INSTCODE - rt - rs - immediate
```

### Subtipo 4
#### Instrucciones:
- LUI

#### Formato de la Instrucción en assembler:

```
INSTRUCCION rt, immediate
```

#### Formato de la Instrucción en binario:

```
INSTCODE - 00000 - rt - immediate
```

### Subtipo 5
#### Instrucciones:
- BEQ
- BNE

#### Formato de la Instrucción en assembler:

```
INSTRUCCION rs, rt, offset
```

#### Formato de la Instrucción en binario:

```
INSTCODE - rs - rt - offset
```


### Subtipo 6
#### Instrucciones:
- J
- JAL

#### Formato de la Instrucción en assembler:

```
INSTRUCCION instr_index
```

#### Formato de la Instrucción en binario:

```
INSTCODE - instr_index (26 bits)
```

---

## Tipo "J" (2 Subtipos)

### Subtipo 1
#### Instrucciones:
- JR

#### Formato de la Instrucción en assembler:

```
INSTRUCCION rs    ->    JR rs
```

#### Formato de la Instrucción en binario:

```
000000 - rs - 000000000000000 - INSTCODE
```

### Subtipo 2
#### Instrucciones:
- JALR

#### Formato de la Instrucción en assembler:

```
INSTRUCCION rs        ->    JALR rs
INSTRUCCION rd, rs    ->    JALR rd, rs
```

#### Formato de la Instrucción en binario:

```
000000 - rs - 00000 - rd - 00000 - INSTCODE
```
