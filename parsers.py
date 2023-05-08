from OPcodes_final import *
from registers_types import *
def opcodes_parser(instruction):
    return OPcodes_final[instruction][0]
def imm_parser(immediate):
    imm = int(immediate[1:])
    return '{0:08b}'.format(imm)
def mem_add_parser(location):
    return '{0:08b}'.format(location)
def reg_parser(register):
    return reg_encoded[register]