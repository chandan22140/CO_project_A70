
list_of_inputs = []
while True:
    try:
        input_line = input()
        if (input_line!=""):
            list_of_inputs.append(input_line)
    except EOFError:
        break


# VALID = True
# HLT_COUNT = 0
# error_tracker = []
# LINE_COUNT = 0
# LINE_COUNT2 = 1
# LINE_COUNT3 = 1
# var_declared = []
# var_declared2 = []
# var_called = []
# var_called2 = []

labels_declared = []
labels_declared2 = []

# lbl_called = []
# lbl_called2 = []
list_nonlabelonly_instruction = []
# this stores all the instructions(list) withoun mnemonic if its not label-only

# count_ls_1 = 0
# consterr = 0






count_of_lines_1=0
for line in list_of_inputs:
    line = line.strip()
    line_list = line.split()
    # we need to make sure if str mapping is actually not needed..
    first_entry_of_instruction_list = line_list[0]
    length_of_instruction = len(line_list)
    if first_entry_of_instruction_list[-1::] == ":":
        #  first_entry_of_instruction_list[-1::] represents last index right? why not [-1] then?

        instruction_without_head = []
        for i in range(1,length_of_instruction):
            instruction_without_head.append(line_list[i])
        # lbl_inst  = line_list[1::]

        if len(instruction_without_head)==0:
            consterr = count_of_lines_1
        if len(instruction_without_head)!=0:
            list_nonlabelonly_instruction.append(instruction_without_head)    
        label_name = first_entry_of_instruction_list[:-1:]
        line_number = count_of_lines_1
        labels_declared.append((label_name,line_number))
        labels_declared2.append(label_name)
    count_of_lines_1+=1  


