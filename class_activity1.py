i = 100
while i <= 999:
    strnum = str(i)
    st1 = str(strnum[0])
    st2 = str(strnum[1])
    st3 = str(strnum[2])

    num1 = int(st1)
    num2 = int(st2)
    num3 = int(st3)

    num1cu = num1**3
    num2cu = num2**3
    num3cu = num3**3
    sumofcu = num1cu+num2cu+num3cu
    if i == sumofcu:
        print(i)
    i+=1