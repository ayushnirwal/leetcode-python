def valid_parenthesis(str):
    stack = [str[0]]

    for i in range(1,len(str)):
        c = str[i]
        if (len(stack)!=0) and ((c == ")" and stack[len(stack)-1] == "(") or (c == "}" and stack[len(stack)-1] == "{") or (c == "]" and stack[len(stack)-1] == "[")):
            stack.pop()
        else:
            stack.append(c)
            
        print(stack)

valid_parenthesis("(){}}{")
         
