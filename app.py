cpf = '069498484'
n_digits = list(range(1,11,1))



def getD1(cpf):
    n_digits = list(range(1, 11, 1))
    i = 0
    l = list()


    for n in cpf:
        multiplied = int(n) * n_digits[i]
        l.append(multiplied)
        i =+ 1            
    l = sum(l)
    r = l % 11
    if r == 0 or r == 1:
        d1 = 0
    else: 
        d1 = 11 - r
    
    cpf += str(d1)

    return(cpf)


def getD2(cpf):
    n_digits = list(range(2, 12, 1))
    n_digits.reverse()
    i = 0
    l = list()
    for n in cpf:
        multiplied = int(n) * n_digits[i]
        i =+ 1
        l.append(multiplied)
    l = sum(l)
    r = l % 11
    print(r)
    if r == 0 or r == 1:
        d2 = 0
    else: 
        d2 = 11 - r

    cpf += d2

    return(cpf)


getD2(cpf=getD1)