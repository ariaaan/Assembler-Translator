# Assembler-Translator
Converts MIPS Assembler to a ".coe" file

## Example
For example, if we have the next assembler code.
```
;Example ".asm" file
LW 1, 0(20)        
XOR 2, 2, 2         
ADD 3, 1, 2       

XORI 3, 2, 25916    
```

The output ".coe" file will look like this.

```
memory_initialization_radix=16;
memory_initialization_vector=
8e810000,
00421026,
00221820,
3843653c;
```
