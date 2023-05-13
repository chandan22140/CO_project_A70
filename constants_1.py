import string
code_size = 5
reg_size = 3
mem_add_size = 8
imm_size = 8
instructions1 = ['add','sub','movi','movr','ld','st','mul','div','rs','ls','xor','or',
'and','not','cmp','jmp','jlt','jgt','je','hlt']
instructions2 = ['add','sub','mov','ld','st','mul','div','rs','ls','xor','or',
'and','not','cmp','jmp','jlt','jgt','je','hlt']
instructions3 =  ['add','sub','mov','ld','st','mul','div','rs','ls','xor','or',
'and','not','cmp','jmp','jlt','jgt','je','hlt','R0','R1','R2','R3','R4','R5','R6','FLAGS']
registers = ['R0','R1','R2','R3','R4','R5','R6','FLAGS']
num_array = ['0','1','2','3','4','5','6','7','8','9']
alphanumeric= list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
alphanumeric.append('_')
