from constants_1 import *
from reg_type_consts import *
from func_to_main2 import *
def getRegcode(register):
    return reg_encode[register]
def getRegCount(type):
    return type_regno[type]
def ifValidVar(var_declared,var_called,alphanumeric,inst):
    num_array = ['0','1','2','3','4','5','6','7','8','9']
    inst2 = inst.copy()
    inst2.append('var')
    len1 = len(var_declared)
    for i in var_declared:
        if i[1]!=1:
            return (-1,i[1])
        if i[1]==1:
            a = i[0]
            b = len(a)
            count = 0
            count2 = 0
            for j in a:
                if j in alphanumeric:
                    count+=1
                if j in num_array:
                    count2+=1
            if count!=b:
                return (-2,i[0])
            if b==count2:
                return (-5,i[0])
    b2 = len(var_called)
    var2 = []
    for i in var_declared:
        var2.append(i[0])
    for i in var2:
        if i in inst2:
            return (-4,i)
    
    for i in var_called:
        if i not in var2:
            return (-3,i)
            
    return (0,0)


def ifValidLabel(lbl_called,lbl_declared,lbl_inst,inst,alphanumeric,lbl_declared2,var_declared2): 
    
    num_array = ['0','1','2','3','4','5','6','7','8','9']
    inst2 = inst.copy()
    inst2.append('var')
    l1 = len(lbl_declared)
    l2 = len(lbl_inst)
    if l1!=l2:
        return (-5,0)
    count2 = 0
    for i in lbl_declared:
        a = i[0]
        b = len(a)
        count = 0
        count4 = 0
        for j in a:
            if j in alphanumeric:
                count+=1
            if j in num_array:
                count4+=1
        if count!=b:
            return (-1,i[1])
        if b==count4:
            return (-6,i[1])
        else:
            c = lbl_inst[count2]
            if ifValidLine2(c)!=0 or ifMatchLines(c,lbl_declared2,var_declared2)!=0:
                return (-2,i[1])
        count2+=1
    count3 = 0
    b2 = len(lbl_called)
    lbl2 = []
    for i in lbl_declared:
        lbl2.append(i[0])
    for i in lbl_called:
        if i not in lbl2:
            return (-3,i)     
    for i in lbl2:
        if i in inst2:
            return (-4,i)
    return (0,0)


def ifVarLabdupli(lbl_declared,var_declared,lbl_declared2,var_declared2): 
    
    a = len(lbl_declared)
    b = len(var_declared)
    for i in var_declared2:
        if i in lbl_declared2:
            return (-1,i)
    for i in range(0,a):
        a2 = lbl_declared[i][0]
        for j in range(i+1,a):
            if a2==lbl_declared[j][0]:
                return (-2,a2)
    for i in range(0,b):
        b2 = var_declared[i][0]
        for j in range(i+1,b):
            if b2==var_declared[j][0]:
                return (-3,var_declared[j][1])
    return (0,0)

    
def ifValidLine(line_comp):
    if ifInstValid1(line_comp[0]) == False:
        return -1
    if ifSizeValid(line_comp[0], line_comp) == False:
        return -2
    return 0

def ifValidLine2(line_comp):
    if ifInstValid2(line_comp[0]) == False:
        return -1
    if ifSizeValid(line_comp[0], line_comp) == False:
        return -2
    return 0

def ifMatchLines(line_comp,lbl_declared2,var_declared2):

    temp = ""
    if line_comp[0]=="mov":
        if "$" in line_comp[-1]:
            temp = "movi"
        else:
            temp = "movr"
    else:
        temp = line_comp[0]
    ls_type_order = type_syntaxconst[OPcodes[temp][-1]]
    for i in range(1, len(line_comp)):
        if ls_type_order[i] == 'Register':
            if ifRegValid(line_comp[i]) is False:
                return -1
            if ifRegValid(line_comp[i])==-1:
                if line_comp[0]!="movr":
                    return -4
        if ls_type_order[i] == 'Immediate':
            if ifImmValid(line_comp[i]) is False:
                return -2
            if ifImmRanValid(line_comp[i]) is False:
                return -3
        if ls_type_order[i] == 'Memory Address': 
            if line_comp[0]=='ld' or line_comp[0]=='st':
                if line_comp[-1] not in var_declared2:
                    if line_comp[-1] in lbl_declared2: 
                        return -5
                    else:
                        return -6      
            if line_comp[0]=='jmp' or line_comp[0]=='jlt' or line_comp[0]=='jgt' or line_comp[0]=='je': 
                if line_comp[-1] not in lbl_declared2:
                    if line_comp[-1] in var_declared2: 
                        return -7
                    else:
                        return -8
    return 0