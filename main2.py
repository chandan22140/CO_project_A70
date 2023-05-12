import sys
from functions_tomain import *
from OPcodes_final import *
from registers_types import *
from sys import stdin
from parsers import *
from check_validity import *


ls_inputs2 = []
while True:
    try:
        input_line = input()
        ls_inputs2.append(input_line)
    except EOFError:
        break

ls_inputs = []
for i in range(len(ls_inputs2)):
    if (ls_inputs2[i] == ''):
        continue
    else:
        ls_inputs.append(ls_inputs2[i])

VALID = True
HLT_COUNT = 0
error_tracker = []
LINE_COUNT = 0
LINE_COUNT2 = 1
LINE_COUNT3 = 1
var_given = []
var_given2 = []
var_called = []
var_called2 = []
lbl_given = []
lbl_given2 = []
lbl_called = []
lbl_called2 = []
lbl_instf = []

count_ls_1 = 0
consterr = 0

for line in ls_inputs:
    line = line.strip()
    line_comp = list(map(str, line.split()))
    first_entry_of_instruction = line_comp[0]
    no_of_line_comp = len(line_comp)
    if first_entry_of_instruction[-1::] == ":":
        lbl_inst = []
        for i in range(1,no_of_line_comp):
            element_of_line_comp = line_comp[i]
            lbl_inst.append(element_of_line_comp)
        if len(lbl_inst)==0:
            consterr = count_ls_1
        if len(lbl_inst)!=0:
            lbl_instf.append(lbl_inst)
        label_name = first_entry_of_instruction[:-1:]
        line_no = count_ls_1
        label_name_and_line_tuple = (label_name,line_no)
        lbl_given2.append(label_name)
        lbl_given.append(label_name_and_line_tuple)
    count_ls_1+=1  
count_ls_2 = 0

for line in ls_inputs:
    line = line.strip()
    line_comp = list(map(str, line.split()))
    first_entry_of_instruction = line_comp[0]
    if first_entry_of_instruction[-1::] == ":":
        if len(line_comp)>1:
            if line_comp[1]=='ld' or line_comp[1]=='st':
                var_in_line = line_comp[-1]
                var_called.append(var_in_line)
                var_called2.append([var_in_line,count_ls_2])
            if line_comp[1]=='jmp' or line_comp[1]=='jlt' or line_comp[1]=='jgt' or line_comp[1]=='je':
                label_in_line = line_comp[-1]
                lbl_called.append(label_in_line)
                lbl_called2.append([label_in_line,count_ls_2])
    if line_comp[0]=='ld' or line_comp[0]=='st':
        var_in_line = line_comp[-1]
        var_called.append(var_in_line)
        var_called2.append([var_in_line,count_ls_2])
    if line_comp[0]=='jmp' or line_comp[0]=='jlt' or line_comp[0]=='jgt' or line_comp[0]=='je': 
        label_in_line = line_comp[-1]
        lbl_called.append(label_in_line)
        lbl_called2.append([label_in_line,count_ls_2])
    count_ls_2+=1

for i in range(len(ls_inputs)):
    line = ls_inputs[i]
    line = line.strip()
    line_comp = list(map(str, line.split()))
    if line_comp[0] == 'movi' or line_comp[0] == 'movr':
        error_tracker.append(f'ERROR: No Such Instruction Found as {line_comp[0]} for instruction {i+1}')
    if line_comp[0] == 'mov':
        if len(line_comp) < 2:
            error_tracker.append(f'ERROR: Invalid Instruction size for mov on line number {i+1}')
            break
        if line_comp[1] == 'FLAGS':
            error_tracker.append(f'ERROR: Invalid Use of FLAGS on line number {i+1}')
        if line_comp[-1][0] == '$':
            line_comp[0] = 'movi'
        else:
            line_comp[0] = 'movr'
    line = ' '.join(line_comp)
    ls_inputs[i] = line

for line in ls_inputs:
    line = line.strip()
    line_comp = list(map(str, line.split()))
    if line_comp[0] == "var":
        if len(line_comp)==2:
            b = line_comp[-1]
            c = (b,LINE_COUNT3)
            var_given.append(c)
            var_given2.append(b)
            LINE_COUNT3-=1
        else:
            error_tracker.append(f'ERROR (Variable): Illegal declaration of variables (Length 2 was expected, Length found was {len(line_comp)}) for instruction {LINE_COUNT3}')
    LINE_COUNT3+=1

    
validvar = isVarValid(var_given,var_called,AN,instructions3)

if validvar[0] == -1:
    error_tracker.append(f'ERROR (Variable): Illegal declaration of variables for instruction {validvar[1]}')
    VALID = False 

if validvar[0] == -2:
    lenarr = len(var_given2)
    index = 0
    for i in range(0,lenarr):
        if var_given2[i] == validvar[1]:
            index = i
            break
    error_tracker.append(f'ERROR (Variable): Variable name incorrect for instruction {index+1}')
    VALID = False  

if validvar[0] == -3:
    index = 0
    for i in range(0,len(var_called2)):
        if var_called2[i][0]==validvar[1]:
            index = var_called2[i][1]
            break
    error_tracker.append(f'ERROR (Variable): Variable called was never given in instruction {index+1}')
    VALID = False 

if validvar[0] == -4:
    lenarr = len(var_given2)
    index = 0
    for i in range(0,lenarr):
        if var_given2[i] == validvar[1]:
            index = i
            break
    error_tracker.append(f'ERROR (Variable): Variable has the same name as an ISA instruction for instruction {index+1}')
    VALID = False
if validvar[0] == -5:
    lenarr = len(var_given2)
    index = 0
    for i in range(0,lenarr):
        if var_given2[i] == validvar[1]:
            index = i
            break
    error_tracker.append(f'ERROR (Variable): Variable name incorrect (only numeric) for instruction {index+1}')
    VALID = False     
    
validlbl = isLabelValid(lbl_called,lbl_given,lbl_instf,instructions3,AN,lbl_given2,var_given2)

if validlbl[0] == -1:
    error_tracker.append(f'ERROR (Label): Invalid label name for instruction {validlbl[1]+1}')
    VALID = False

if validlbl[0] == -2:
    error_tracker.append(f'ERROR (Label): Invalid label instruction for instruction {validlbl[1]+1}')
    VALID = False

if validlbl[0] == -3:
    lenarr = len(lbl_called2)
    index = 0
    for i in range(0,lenarr):
        if lbl_called2[i][0]==validlbl[1]:
            index = lbl_called2[i][1]
    error_tracker.append(f'ERROR (Label): Invalid label called for instruction {index+1}')
    VALID = False

if validlbl[0] == -4:
    lenarr = len(lbl_given)
    index = 0
    for i in range(0,lenarr):
        if lbl_given[i][0]==validlbl[1]:
            index = lbl_given[i][1] 
    error_tracker.append(f'ERROR (Label): Label name is the same as an instruction for instruction {index+1}')
    VALID = False

if validlbl[0] == -5:
    error_tracker.append(f'ERROR (Label): Label instruction not given for instruction {consterr+1}')
    VALID = False

if validlbl[0] == -6:
    error_tracker.append(f'ERROR (Label): Invalid label name (only numeric or empty) for instruction {validlbl[1]+1}')
    VALID = False    
    
duptuple = Duplication(lbl_given,var_given,lbl_given2,var_given2)

if duptuple[0]==-1:
    lenarr = len(var_given2)
    index = 0
    for i in range(0,lenarr):
        if var_given2[i] == duptuple[1]:
            index = i
            break
    error_tracker.append(f'ERROR (Label/Var): Label name is the same as a variable for instruction {index+1}')
    VALID = False

if duptuple[0]==-2:
    lenarr = len(lbl_given2)
    index = 0
    for i in range(0,lenarr):
        if lbl_given[i][0] == duptuple[1]:
            index = lbl_given[i][1]
            break
    error_tracker.append(f'ERROR (Label): A label was given more than once for instruction {index+1}')
    VALID = False

if duptuple[0]==-3:
    error_tracker.append(f'ERROR (Var): A variable was given more than once for instruction {duptuple[1]+1}')
    VALID = False
 
for line in ls_inputs:
    line = line.strip()
    line_comp = list(map(str, line.split()))
    a = line_comp[0]

    if a[-1::]==':':
        b =line_comp[-1]
        if b=='hlt':
            HLT_COUNT+=1
        LINE_COUNT+=1
        continue

    if line_comp[0]=="var":
        LINE_COUNT+=1
        continue

    if isLineValid(line_comp) == -1:
        error_tracker.append(f'ERROR: No Such Instruction Found as {line_comp[0]} for instruction {LINE_COUNT+1}')
        VALID = False
        break

    if isLineValid(line_comp) == -2:
        error_tracker.append(f'ERROR: Wrong Syntax used at line number {LINE_COUNT+1}, please note it is a Type {opcode[line_comp[0]]} which requires {type_space[opcode[line_comp[0]][-1]]} arguments including the instruction')
        VALID = False
        break

    if lineTypesMatch(line_comp,lbl_given2,var_given2) == -1:
        if (line_comp[0] == 'movr' or line_comp[0] == 'movi'):
            error_tracker.append(f'ERROR (Invalid Register (No such Register Found) at line number {LINE_COUNT+1}): Wrong Syntax used for Instruction mov, kindly use acceptable argument(s) only, which in case of mov is/are {type_syntaxconstituents[opcode[line_comp[0]][-1]]}')
        else:
            error_tracker.append(f'ERROR (Invalid Register (No such Register Found) at line number {LINE_COUNT+1}): Wrong Syntax used for Instruction {line_comp[0]}, kindly use acceptable argument(s) only, which in case of {line_comp[0]} is/are {type_syntaxconstituents[opcode[line_comp[0]][-1]]}')
        VALID = False
        break

    if lineTypesMatch(line_comp,lbl_given2,var_given2) == -2:
        error_tracker.append(f'ERROR (Illegal Immediate Value used at line number {LINE_COUNT+1})')
        VALID = False
        break

    if lineTypesMatch(line_comp,lbl_given2,var_given2) == -3:
        error_tracker.append(f'ERROR (Illegal Immediate Value used at line number {LINE_COUNT+1})')
        VALID = False
        break

    if lineTypesMatch(line_comp,lbl_given2,var_given2) == -4:
        error_tracker.append(f'ERROR Invalid use of FLAGS register at line number {LINE_COUNT+1}')
        VALID = False
        break

    if lineTypesMatch(line_comp,lbl_given2,var_given2) == -5 or lineTypesMatch(line_comp,lbl_given2,var_given2) == -8:
        error_tracker.append(f'ERROR Invalid use of label at line number {LINE_COUNT+1}')
        VALID = False
        break

    if lineTypesMatch(line_comp,lbl_given2,var_given2) == -6 or lineTypesMatch(line_comp,lbl_given2,var_given2) == -7:
        error_tracker.append(f'ERROR Invalid use of variable at line number {LINE_COUNT+1}')
        VALID = False
        break
    
    if 'hlt' in line_comp:
        HLT_COUNT += 1
    
    LINE_COUNT+=1

if HLT_COUNT == 0:
    error_tracker.append(f'ERROR (hlt) for line number {LINE_COUNT}: No hlt instruction present')
    VALID = False

if HLT_COUNT > 1:
    error_tracker.append(f'ERROR (hlt) for line number {LINE_COUNT}: Multiple hlt instruction present')
    VALID = False
checkdiv = list(map(str, ls_inputs[-1].split()))
if HLT_COUNT == 1 and checkdiv[-1] != 'hlt':
    error_tracker.append(f'ERROR (hlt) for line number {LINE_COUNT}: hlt not present as last instruction')
    VALID = False
if HLT_COUNT == 1 and checkdiv[-1] == 'hlt':
    a = checkdiv[0]
    b = a[-1::]
    if b==":":
        c = a[:-1:]
        if c not in lbl_called:
            error_tracker.append(f'ERROR (hlt) for line number {LINE_COUNT}: hlt not present as last instruction, label with hlt was never called')
            VALID = False
            
if len(error_tracker) > 0:
    print(error_tracker[0])
else:
    len_without_vars_and_labels = 0
    for inst in ls_inputs:
        inst_comps = list(map(str, inst.strip().split()))
        if (inst_comps[0] == 'var'):
            continue
        else:
            len_without_vars_and_labels += 1

    ls_vars = []
    ls_labels = []

    for i, inst in enumerate(ls_inputs):
        if 'var' in inst:
            ls_vars.append([i, list(map(str, inst.split()))[-1]])
        if ':' in inst:
            ls_labels.append([i, list(map(str, inst.split()))[0][:-1]])

    no_of_vars = len(ls_vars)

    for i in range(len(ls_inputs)):
        output_string = ''
        inst_comps = list(map(str, ls_inputs[i].strip().split()))

        if inst_comps[0] == 'var':
            continue

        if inst_comps[0][-1] == ":":
            inst_comps = inst_comps[1:]

        temp = ""
        if inst_comps[0]=="mov":
            if "$" in inst_comps[-1]:
                temp = "movi"
            else:
                temp = "movr"
        else:
            temp = inst_comps[0]

        inst_type = opcode[temp][-1]
        output_string += opcodes_parser(temp)
        output_string += '0' * type_unused_bit[inst_type]

        for i in range(type_register[inst_type]):
            output_string += reg_parser(inst_comps[i+1])

        if inst_type == 'B':
            output_string += imm_parser(inst_comps[-1])

        if inst_type == 'D':
            location = len_without_vars_and_labels
            for i in ls_vars:
                if i[-1] == inst_comps[-1]:
                    location += i[0]
            output_string += imm_parser(location)

        if inst_type == 'E':
            location = 0
            for i in ls_labels:
                if i[-1] == inst_comps[1]:
                    location += i[0] - no_of_vars
            output_string +=mem_add_parser(location)
            
        print(output_string)