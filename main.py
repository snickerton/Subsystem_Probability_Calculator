import re

# valstack contains the INDEXES, not the actual values, in which we operate on
def calcSystemProb(exp, vals):
    if exp[0] != '(' or exp[-1] != ')':
        exp = exp + ')'
        exp = '(' + exp
    print("STARTING EXP: " + exp)
    exp2 = re.split('([|]|[(]|[)]|[&])', exp)
    exp2.pop(0)
    exp2.pop(len(exp2)-1)

    for i,x in enumerate(exp2):
        if x == '':
            exp2.pop(i)

    print(str(exp2))

    opStack = []
    valStack = []
    for i, x in enumerate(exp2):
        if x.isdigit():
            try:
                valStack.append(float(vals[int(x)-1]))
            except:
                print("Didn't specify enough values to fill expression")
        if not x.isdigit():
            if x == '(':
                opStack.append(x)
            elif x == ')':
                while(opStack[-1] != '('):
                    a = float(valStack.pop())
                    b = float(valStack.pop())
                    op = opStack.pop()
                    if op == '|':
                        valStack.append(TonyOr(a,b))
                    elif op == '&':
                        valStack.append(a*b)
                    else:
                        print("WARNING: unexpected value in opstack: " + op)
                print("popping left parenth: " + opStack.pop())
            elif x == '|':
                opStack.append(x)
            elif x == '&':
                opStack.append(x)
            else:
                print("WARNING: unidentified non-digit found: " + x)
        print(valStack)
        print(opStack)
    while len(opStack) != 0:
        a = float(valStack.pop())
        b = float(valStack.pop())
        op = opStack.pop()
        if op == '|':
            valStack.append(TonyOr(a, b))
        elif op == '&':
            valStack.append(a * b)
        else:
            print("WARNING: unexpected value in opstack: " + op)
    print("returning valstack: " + str(valStack))
    return valStack[0]

def TonyOr(a,b):
    return float(a)+float(b)-float(a)*float(b);


# print("ESET Subsystem Probability Calculator")
# print("     *Use & for series items and | for parallel")
# print("     *No two numbers should be adjacent without an operator!")
# print("     *Syntax for values: [1,2,3,4] or .95x10")
# print("\n************\n\n")
# exp = input("Please input expression:\n")
#
# # replace all whitespace
# exp = exp.replace(" ", "")
#
#
# vals = input("Please input starting values:\n")
# if "x" in vals:
#     temp = vals.split('x')
#     vals = [float(temp[0])]*int(temp[1])
# else:
#     vals = vals.split(',')
#     vals = [int(x) for x in vals]
#
# print("Received vals: " + str(vals))
# print(calcSystemProb(exp,vals))

