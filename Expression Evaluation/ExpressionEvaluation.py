"""
Author: Pavith Bambaravanage
URL: https://github.com/Pavith19
"""
def isvalidBinaryOparation(string):
    #avalable operators in the expression
    valid = True
    operators = ["+", "-", "*"]
    for index in range(1, len(string)-1):
        if string[index] in operators:
            if string[index -1].isdigit() and string[index+1].isdigit():
                continue
            else:
                valid =  False
                break
        else:continue
    return valid

def isBalancePara(string):
    balance = True
    para = []
    for ch in string:
        if ch=="(":
            para.append(ch)
        else:
            if len(para)>0:
                temp = para[len(para) -1]
                para.pop()
                if ch=="(" and temp != ")":
                    balance = False
                    break
            else:
                balance = False
                break
    if len(para) >0:
        balance = False
    return balance


T = int(input())
for line in range(T):
    state = True
    expression = input()
    if not isvalidBinaryOparation(expression):
        state = False
    # if not isBalancePara(expression):
    #     state = False
    print(state)


            
        


