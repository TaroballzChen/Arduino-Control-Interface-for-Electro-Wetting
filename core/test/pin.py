for i in range(48):
    for j in range(48):
        # if j == 0:
        #     print("{",end="")
        if j == i:
            print("1,",end="")
        elif j == i+1:
            print("-1,",end="")
        # elif j == i+1:
        #     print("1,",end="")
        else:
            print("0,",end="")
        if (j+1)%8==0:
            print("  ",end="")
    # else:
    #     print("},",end="")
    print()