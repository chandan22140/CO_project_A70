import sys
from func_to_main import *
from OPcodes import *
from reg_type_consts import *
from sys import stdin
from ToBinary import *
ls_inputs2 = []
with open('input.txt', 'r') as f:
    for line in f:
        ls_inputs2.append(line.strip())

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
var_declared = []
var_declared2 = []
var_called = []
var_called2 = []
lbl_declared = []
lbl_declared2 = []
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
        lbl_declared2.append(label_name)
        lbl_declared.append(label_name_and_line_tuple)
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
        error_tracker.append(f'ERROR: Incorrect Instruction as No Instruction as -- {line_comp[0]} for {i+1}')
    if line_comp[0] == 'mov':
        if len(line_comp) < 2:
            error_tracker.append(f'ERROR: Incorrect size for mov on line number {i+1}')
            break
        if line_comp[1] == 'FLAGS':
            error_tracker.append(f'ERROR: Incorrect flag used at line number {i+1}')
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
            var_declared.append(c)
            var_declared2.append(b)
            LINE_COUNT3-=1
        else:
            error_tracker.append(f'ERROR (Variable): Incorrect variable used (Length 2 was expected, Length found was {len(line_comp)}) for {LINE_COUNT3}')
    LINE_COUNT3+=1
validvar = ifValidVar(var_declared,var_called,alphanumeric,instructions3)
if validvar[0] == -1:
    error_tracker.append(f'ERROR (Variable): Incorrect variable declaration for  {validvar[1]}')
    VALID = False 
if validvar[0] == -2:
    lenarr = len(var_declared2)
    index = 0
    for i in range(0,lenarr):
        if var_declared2[i] == validvar[1]:
            index = i
            break
    error_tracker.append(f'ERROR (Variable): Incorrect variable name for {index+1}')
    VALID = False  
if validvar[0] == -3:
    index = 0
    for i in range(0,len(var_called2)):
        if var_called2[i][0]==validvar[1]:
            index = var_called2[i][1]
            break
    error_tracker.append(f'ERROR (Variable): variable called but not declared {index+1}')
    VALID = False 
if validvar[0] == -4:
    lenarr = len(var_declared2)
    index = 0
    for i in range(0,lenarr):
        if var_declared2[i] == validvar[1]:
            index = i
            break
    error_tracker.append(f'ERROR (Variable): Variable and ISA instruction name same for : {index+1}')
    VALID = False
if validvar[0] == -5:
    lenarr = len(var_declared2)
    index = 0
    for i in range(0,lenarr):
        if var_declared2[i] == validvar[1]:
            index = i
            break
    error_tracker.append(f'ERROR (Variable): Incorrect Variable used (only numeric) for {index+1}')
    VALID = False       
validlbl = ifValidLabel(lbl_called,lbl_declared,lbl_instf,instructions3,alphanumeric,lbl_declared2,var_declared2)
if validlbl[0] == -1:
    error_tracker.append(f'ERROR (Label): Invalid label for instruction {validlbl[1]+1}')
    VALID = False
if validlbl[0] == -2:
    error_tracker.append(f'ERROR (Label): Invalid label for instruction {validlbl[1]+1}')
    VALID = False
if validlbl[0] == -3:
    lenarr = len(lbl_called2)
    index = 0
    for i in range(0,lenarr):
        if lbl_called2[i][0]==validlbl[1]:
            index = lbl_called2[i][1]
    error_tracker.append(f'ERROR (Label): Incorrect Label for instruction {index+1}')
    VALID = False
if validlbl[0] == -4:
    lenarr = len(lbl_declared)
    index = 0
    for i in range(0,lenarr):
        if lbl_declared[i][0]==validlbl[1]:
            index = lbl_declared[i][1] 
    error_tracker.append(f'ERROR (Label): label name and instruction same for {index+1}')
    VALID = False
if validlbl[0] == -5:
    error_tracker.append(f'ERROR (Label): Label not given for {consterr+1}')
    VALID = False
if validlbl[0] == -6:
    error_tracker.append(f'ERROR (Label):Incorrect label (only numeric or empty) for {validlbl[1]+1}')
    VALID = False     
duptuple = ifVarLabdupli(lbl_declared,var_declared,lbl_declared2,var_declared2)
if duptuple[0]==-1:
    lenarr = len(var_declared2)
    index = 0
    for i in range(0,lenarr):
        if var_declared2[i] == duptuple[1]:
            index = i
            break
    error_tracker.append(f'ERROR (Label/Var): Label name and variable name same-- ERROR {index+1}')
    VALID = False
if duptuple[0]==-2:
    lenarr = len(lbl_declared2)
    index = 0
    for i in range(0,lenarr):
        if lbl_declared[i][0] == duptuple[1]:
            index = lbl_declared[i][1]
            break
    error_tracker.append(f'ERROR (Label): Label declared more than once for {index+1}')
    VALID = False
if duptuple[0]==-3:
    error_tracker.append(f'ERROR (Var): Variable declared more than once for {duptuple[1]+1}')
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
    if ifValidLine(line_comp) == -1:
        error_tracker.append(f'ERROR: Invalid instruction : {line_comp[0]} for {LINE_COUNT+1}')
        VALID = False
        break
    if ifValidLine(line_comp) == -2:
        error_tracker.append(f'ERROR: Wrong Syntax at line number {LINE_COUNT+1}, It is of Type {OPcodes[line_comp[0]]} whose syntax is of  {type_inputlen[OPcodes[line_comp[0]][-1]]}')
        VALID = False
        break
    if ifMatchLines(line_comp,lbl_declared2,var_declared2) == -1:
        if (line_comp[0] == 'movr' or line_comp[0] == 'movi'):
            error_tracker.append(f'ERROR (Register invalid (No such Register ) at line number {LINE_COUNT+1}): Wrong Syntax for Instruction mov, please use correct arguments which for this case of mov is/are {type_syntaxconst[OPcodes[line_comp[0]][-1]]}')
        else:
            error_tracker.append(f'ERROR (Register invalid (No such Register ) at line number {LINE_COUNT+1}): Wrong Syntax for Instruction {line_comp[0]}, please use correct arguments which for this case of {line_comp[0]} is/are {type_syntaxconst[OPcodes[line_comp[0]][-1]]}')
        VALID = False
        break
    if ifMatchLines(line_comp,lbl_declared2,var_declared2) == -2:
        error_tracker.append(f'ERROR (Incorrect immediate value at line number {LINE_COUNT+1})')
        VALID = False
        break
    if ifMatchLines(line_comp,lbl_declared2,var_declared2) == -3:
        error_tracker.append(f'ERROR (Incorrect immediate value at line number {LINE_COUNT+1})')
        VALID = False
        break
    if ifMatchLines(line_comp,lbl_declared2,var_declared2) == -4:
        error_tracker.append(f'ERROR Incorrect FLAG register at line number {LINE_COUNT+1}')
        VALID = False
        break
    if ifMatchLines(line_comp,lbl_declared2,var_declared2) == -5 or ifMatchLines(line_comp,lbl_declared2,var_declared2) == -8:
        error_tracker.append(f'ERROR Incorrect label present at line number {LINE_COUNT+1}')
        VALID = False
        break
    if ifMatchLines(line_comp,lbl_declared2,var_declared2) == -6 or ifMatchLines(line_comp,lbl_declared2,var_declared2) == -7:
        error_tracker.append(f'ERROR Incorrect variable present at line number {LINE_COUNT+1}')
        VALID = False
        break 
    if 'hlt' in line_comp:
        HLT_COUNT += 1   
    LINE_COUNT+=1
if HLT_COUNT == 0:
    error_tracker.append(f'ERROR (hlt) at line number : {LINE_COUNT}: No hlt instruction called')
    VALID = False
if HLT_COUNT > 1:
    error_tracker.append(f'ERROR (hlt) at line number : {LINE_COUNT}: More than 1 hlt instruction called')
    VALID = False
checkdiv = list(map(str, ls_inputs[-1].split()))
if HLT_COUNT == 1 and checkdiv[-1] != 'hlt':
    error_tracker.append(f'ERROR (hlt) at line number : {LINE_COUNT}: hlt not final instruction')
    VALID = False
if HLT_COUNT == 1 and checkdiv[-1] == 'hlt':
    a = checkdiv[0]
    b = a[-1::]
    if b==":":
        c = a[:-1:]
        if c not in lbl_called:
            error_tracker.append(f'ERROR (hlt) at line number : {LINE_COUNT}: hlt not final instruction,  hlt was never called')
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
        inst_type = OPcodes[temp][-1]
        output_string += opcode_tobin(temp)
        output_string += '0' * type_unusedbits[inst_type]
        for i in range(type_regno[inst_type]):
            output_string += reg_tobin(inst_comps[i+1])
        if inst_type == 'B':
            output_string += imm_tobin(inst_comps[-1])
        if inst_type == 'D':
            location = len_without_vars_and_labels
            for i in ls_vars:
                if i[-1] == inst_comps[-1]:
                    location += i[0]
            output_string += mem_add_tobin(location)
        if inst_type == 'E':
            location = 0
            for i in ls_labels:
                if i[-1] == inst_comps[1]:
                    location += i[0] - no_of_vars
            output_string +=mem_add_tobin(location)       
        print(output_string)