def get_name_cases(nameNumber, *values):
    genNames = ['' for i in range(nameNumber)]
    for element in values:
        fieldName = element.split('#')[0]
        values = element.split('#')[1].split(';')
        diffLen = len(genNames) - len(values)
        L = [values[-1]] * diffLen
        newValues = values + L
        counter = 0
        for value in newValues:
            genNames[counter] += fieldName + value + ' | '
            counter += 1
    return genNames


values = (
    'Set account nature#=2;<>2',
    'Set debit mode#=1;<>1;=2;<>2;=3;<>3;=4;<>4;=5;<>5;<>1,2,3,4,5;=1,2,3,4,5',
    'Set account type#=1;<>1'
)

for name in get_name_cases(12, *values):
    print(name.rstrip(' | '))
