from constants import *
from registers_types import *
from OPcodes_final import *

def isInstructValid1(instruction):
    if instruction in instructions1:
        return True
    else:
        return False

def isInstructValid2(instruction):
    if instruction in instructions2:
        return True
    else:
        return False
    
def isRegValid(register):
    if register in registers:
        if register == 'FLAGS':
            return -1
        else:
            return True
    else:
        return False


def isImmValid(immediate):
    try:
        int(immediate[1:])
    except:
        return False
    if immediate[0] != '$':
        return False
    else:
        return True

def isImmRangeValid(immediate):
    if int(immediate[1:]) >= 0 and int(immediate[1:]) <= 255:
        return True
    else:
        return False

def isSizeRight(instruction, ls):
    if instruction=='mov':
        if len(ls)==3:
            return True
    else:
        type_instruction = OPcodes_final[instruction][-1]
        if len(ls) == type_to_input_len[type_instruction]:
            return True
    return False