req_num = input("Enter the number")

def reversnum(no):
    var = str(no)

    b = var[::-1]
    if var == b:
        return "True"
    else:
        return "False"


print(reversnum(req_num))

#Some Activity should have for today