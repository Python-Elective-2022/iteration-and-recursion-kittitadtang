'''
Pseudocode:

define function interative power (base, exp)
    when result is 1 
    while exp is more than 0
    multiply the base exp times
    return result
    
'''
def iterativePower(base, exp):
    '''
    base: int or float.
    int >= 0

    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result

# test case
print(iterativePower(2, 2))
print(iterativePower(3, 3))
print(iterativePower(4, 4))

'''
Pseudocode:

define function recursive power (base, exp)
    if exp is equal to 1
    return base
    if not multiply until exp is 1
'''
def recursivePower(base, exp):
    '''
    base: int or float
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 1:
        return base 
    else:
        return base * recursivePower(base, exp-1)

# test case
print(recursivePower(2, 2))
print(recursivePower(3, 3))
print(recursivePower(4, 4))