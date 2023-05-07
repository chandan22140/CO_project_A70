'''
type_register type of data to registor number
'''
type_register = {
    'A':3,
    'B':1,
    'C':2,
    'D':1,
    'E':0,
    'F':0
}
'''
type_space for giving no of space separated items 
'''
type_space = {
    'A':4,
    'B':3,
    'C':3,
    'D':3,
    'E':2,
    'F':1
}
'''
type_imm tells us no of immediate commands after type
'''
type_imm= {
    'A':0,
    'B':1,
    'C':0,
    'D':0,
    'E':0,
    'F':0
}
'''
type_unused_bit tells us no of unused bits per type
'''
type_unused_bit = {
    'A':2,
    'B':0,
    'C':5,
    'D':0,
    'E':3,
    'F':11
}
'''
type_memadd This statement provides information on the number of memory addresses per type and how it functions
 as a Boolean dictionary. It indicates that each instruction type can have a maximum of one memory address and serves as
 a means of determining whether a particular instruction type supports memory addresses or not.
'''
type_memadd = {
    'A':0,
    'B':0,
    'C':0,
    'D':1,
    'E':1,
    'F':0
}
'''
reg_encoded gives us the encoding of the specified register
'''
reg_encoded = {
    'R0': '000',
    'R1': '001',
    'R2': '010',
    'R3': '011',
    'R4': '100',
    'R5': '101',
    'R6': '110',
    'FLAGS': '111',
}
'''
type_syntaxtype type_syntaxconstituents This statement informs us about the various components present in the syntax and their sequence,
such as registers, immediates, and so on. It provides details on the specific type of elements that 
comprise the syntax and their respective positions within the sequence.
'''
type_syntaxtype = {
    'A':['Instruction','Register','Register','Register'],
    'B':['Instruction','Register','Immediate'],
    'C':['Instruction','Register','Register'],
    'D':['Instruction','Register','Memory Address'],
    'E':['Instruction','Memory Address'],
    'F':['Instruction']
}