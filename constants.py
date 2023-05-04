import string
opcode_bits = 5
rgstr_bits = 3
memryaddr_bits = 8
imm_bits = 8
instructions1 = ['add','sub','movi','movr','ld','st','mul','div','rs','ls','xor','or',
'and','not','cmp','jmp','jlt','jgt','je','hlt']
#movi,movr and mov causing Bullshit
instructions2 = ['add','sub','mov','ld','st','mul','div','rs','ls','xor','or',
'and','not','cmp','jmp','jlt','jgt','je','hlt']
instructions3 =  ['add','sub','mov','ld','st','mul','div','rs','ls','xor','or',
'and','not','cmp','jmp','jlt','jgt','je','hlt','R0','R1','R2','R3','R4','R5','R6','FLAGS']#for instructions without load and store action
registers = ['R0','R1','R2','R3','R4','R5','R6','FLAGS']
nums = ['0','1','2','3','4','5','6','7','8','9']
AN=list(string.ascii_lowercase + string.ascii_uppercase + string.digits + "_") #AN is list with all letter from a to Z and 0 to 9 and _ 
print(AN)