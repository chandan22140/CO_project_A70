from constants import *
from registers_types import *
from check_validity import *
from OPcodes_final import *

def getRegisterEncoding(register):
    return reg_encoded[register]

def getRegisterCount(type):
    """Returns Register Count"""
    return type_register[type]

def isVarValid(var_given,var_called,AN,inst):
    """Checks if Variables are Valid"""
    numarr = ['0','1','2','3','4','5','6','7','8','9']
    inst2 = inst.copy()
    inst2.append('var')
    len1 = len(var_given)
    for i in var_given:
        if i[1]!=1:
            return (-1,i[1])
        if i[1]==1:
            a = i[0]
            b = len(a)
            count = 0
            count2 = 0
            for j in a:
                if j in alphanum:
                    count+=1
                if j in numarr:
                    count2+=1
            if count!=b:
                return (-2,i[0])
            if b==count2:
                return (-5,i[0])
    b2 = len(var_called)
    var2 = []
    for i in var_given:
        var2.append(i[0])
    for i in var2:
        if i in inst2:
            return (-4,i)
    
    for i in var_called:
        if i not in var2:
            return (-3,i)
            
    return (0,0) #no issues all variables declared and called are valid


def isLabelValid(lbl_called,lbl_given,lbl_inst,inst,alphanum,lbl_given2,var_given2): #add in main
    """Checks if Labels validity"""
    numarr = ['0','1','2','3','4','5','6','7','8','9']
    inst2 = inst.copy()
    inst2.append('var')
    l1 = len(lbl_given)
    l2 = len(lbl_inst)
    if l1!=l2:
        return (-5,0)
    count2 = 0
    for i in lbl_given:
        a = i[0]
        b = len(a)
        count = 0
        count4 = 0
        for j in a:
            if j in alphanum:
                count+=1
            if j in numarr:
                count4+=1
        if count!=b:
            return (-1,i[1])
        if b==count4:
            return (-6,i[1])
        else:
            c = lbl_inst[count2]
            if isLineValid2(c)!=0 or lineTypesMatch(c,lbl_given2,var_given2)!=0:
                return (-2,i[1])
        count2+=1
    count3 = 0
    b2 = len(lbl_called)
    lbl2 = []
    for i in lbl_given:
        lbl2.append(i[0])
    for i in lbl_called:
        if i not in lbl2:
            return (-3,i)     
    for i in lbl2:
        if i in inst2:
            return (-4,i)
    return (0,0)


def Duplication(lbl_given,var_given,lbl_given2,var_given2): #add to main.py
    """Checks for duplicates"""
    a = len(lbl_given)
    b = len(var_given)
    for i in var_given2:
        if i in lbl_given2:
            return (-1,i)
    for i in range(0,a):
        a2 = lbl_given[i][0]
        for j in range(i+1,a):
            if a2==lbl_given[j][0]:
                return (-2,a2)
    for i in range(0,b):
        b2 = var_given[i][0]
        for j in range(i+1,b):
            if b2==var_given[j][0]:
                return (-3,var_given[j][1])
    return (0,0)

    
def isLineValid(line_comp):
    """Checks validity for each line and instructions within
    """
    if isInstructValid1(line_comp[0]) == False:
        return -1
    if isSizeRight(line_comp[0], line_comp) == False:
        return -2
    return 0

def isLineValid2(line_comp):
    if isInstructValid2(line_comp[0]) == False:
        return -1
    if isSizeRight(line_comp[0], line_comp) == False:
        return -2
    return 0

def lineTypesMatch(line_comp,lbl_given2,var_given2):
    """It verifies whether the objects specified in the instruction line match their intended types,
    such as ensuring that registers are used where registers are expected in the syntax, and so on."""
    temp = ""
    if line_comp[0]=="mov":
        if "$" in line_comp[-1]:
            temp = "movi"
        else:
            temp = "movr"
    else:
        temp = line_comp[0]
    ls_type_order = type_to_syntaxconstituents[opcode[temp][-1]]
    for i in range(1, len(line_comp)):
        if ls_type_order[i] == 'Register':
            if isRegValid(line_comp[i]) is False:
                return -1
            if isRegValid(line_comp[i])==-1:
                if line_comp[0]!="movr":
                    return -4
        if ls_type_order[i] == 'Immediate':
            if isImmValid(line_comp[i]) is False:
                return -2
            if isImmRangeValid(line_comp[i]) is False:
                return -3
        if ls_type_order[i] == 'Memory Address': #start from here
            if line_comp[0]=='ld' or line_comp[0]=='st':
                if line_comp[-1] not in var_given2:
                    if line_comp[-1] in lbl_given2: #illegal use
                        return -5
                    else:
                        return -6      
            if line_comp[0]=='jmp' or line_comp[0]=='jlt' or line_comp[0]=='jgt' or line_comp[0]=='je': 
                if line_comp[-1] not in lbl_given2:
                    if line_comp[-1] in var_given2: #illegal use
                        return -7
                    else:
                        return -8
                
                
    return 0
