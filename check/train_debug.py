def name_generator(nameNumber, *values):
    genNames = ['' for i in range(nameNumber)]
    for element in values:
        fieldName = element.split('#')[0]
        values = element.split('#')[1].split(';')
        diffLen = len(genNames) - len(values)
        L = [values[-1]] * diffLen
        newvalues = values + L
        counter = 0
        for value in newvalues:
            genNames[counter] += fieldName + value + ' | '
            counter += 1
    return genNames


for name in name_generator(12, 'ACCOUNT_NATURE#=2;<>2',
                               'DEBIT_MODE#=1;<>1;=2;<>2;=3;<>3;=4;<>4;=5;<>5;<>1,2,3,4,5;=1,2,3,4,5',
                               'TYPE#=1;<>1'):
    print(name.rstrip(' | '))
