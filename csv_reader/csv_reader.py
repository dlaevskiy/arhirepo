import csv

transactionsList = []
startTransaction = False
accountNumber = ''

transactionFieldNames = ['Date', 'Trans_ID', 'Num_Deposit', 'Deposit_Amount', 'Number_Withdrawal',
                         'Withdrawal_Amount', 'Detail_1', 'Detail_2', 'Balance']

with open('h.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

    for row in spamreader:
        if startTransaction:
            transactionsList.append(dict(zip(transactionFieldNames, row)))
        elif row[0].lower().strip() == 'date' and row[1].lower().strip() == 'transaction id':
            startTransaction = True
        elif row[0].lower().strip().startswith('account number'):
            accountNumber = (row[0].split(':')[1]).strip()

print accountNumber
