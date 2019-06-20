total_electrode = 48
procedure = [[17,9,33,41],[10,18,42,34],[19,43],[44,47],[46,29],[45,28]]

def modify_electrode_per_step(procedure,total_electrode_num):
    for i,step in enumerate(procedure):
        array = [0 for _ in range(total_electrode_num)]
        modify_one(array,step)
        modify_GND(array,procedure,i)
        print_array(array)

def print_array(array):
    for i,e in enumerate(array,start=1):
        print(e,end=",")
        if i%8 ==0:
            print("\t\t",end="")
    else:
        print()

def modify_one(array,control_list):
    for num in control_list:
        array[num-1] = 1

def modify_GND(array,procedure,index):
    GND_list = [-1,1,2]
    if len(procedure) - 1 == index:
        GND_list.append(-2)
    for GND in GND_list:
        new_index = index + GND
        if new_index < 0 or new_index >len(procedure) -1:
            continue
        for e in procedure[new_index]:
            array[e-1] = -1


if __name__ == '__main__':
    modify_electrode_per_step(procedure,48)



