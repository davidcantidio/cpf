from django.shortcuts import render
from django.http import HttpResponse


def get10DigCPF(nine_dig_cpf):
    n_digits = list(range(2, 11, 1))
    n_digits.reverse()
    i = 0
    l = list()

    for n in nine_dig_cpf:
        multiplied = int(n) * n_digits[i]
        l.append(multiplied)
        i += 1
                        
    l = sum(l)
    r = l % 11
    if r == 0 or r == 1:
        tenth_digit = 0
    else: 
        tenth_digit = 11 - r

    ten_dig_cpf = nine_dig_cpf + str(tenth_digit)

    return(ten_dig_cpf)


def get11DigCPF(ten_dig_cpf):
    n_digits = list(range(2, 12, 1))
    n_digits.reverse()
    i = 0
    l = list()
    for n in ten_dig_cpf:
        multiplied = int(n) * n_digits[i]
        i += 1
        l.append(multiplied)
    l = sum(l)
    r = l % 11
    if r == 0 or r == 1:
        eleventh_digit = 0
    else: 
        eleventh_digit = 11 - r

    eleven_dig_cpf = ten_dig_cpf + str(eleventh_digit)

    return(eleven_dig_cpf)




def home(request):
    
    cpf_input = request.POST.get('cpf')
    ten_dig = get10DigCPF(cpf_input)
    eleven_dig_cpf = get11DigCPF(ten_dig)
    last_two_digits = eleven_dig_cpf[-2:]
    context = {'last_two_digits':last_two_digits}
    return  render(request, 'CpfLastTwoDigitsFinder/home.html', context)
