# *args example

def calculator(operator, *operends):

    if operator == 'add':
        result = sum(operends)
    elif operator == 'mul':
        result = 1
        for n in operends:
            result *= n

    else:
        raise ValueError(f"Unknown {operator}")
    
    return result

# print(calculator('add',2,3))
# print(calculator('mul',2,3,2))



# **kwargs

def set_option(**values):
    print(f"Recieved dicnory: {values}")

    for key, value in values.items():
        print(f"Key --> {key} and Value --> {value}")


set_option(a=1,b=2,c=3)