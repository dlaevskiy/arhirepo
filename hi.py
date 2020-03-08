import re
import time


def getTime(self):
    string = self.readerContent['REFERENCE']['NOTE_2']
    match = re.search(r'([01][0-9]|2[0-3]):[0-5][0-9]$', string)
    if match:
        return match.group(0).replace(':', '')
    else:
        return '1600'


# if transaction.Note 2 contains a time with format HH:MM
# def isTimeFormat(input):
#     try:
#         time.strptime(input, '%H:%M')
#         return True
#     except ValueError:
#         return False

def getTime2(self):
    note2 = self.readerContent['REFERENCE']['NOTE_2']
    try:
        time.strptime(note2, '%H:%M')
        return note2.replace(':', '')
    except ValueError:
        return '1600'


def getTime3(field):
    try:
        time.strptime(field, '%H:%M')
        return field.replace(':', '')
    except ValueError:
        return '1600'


print(getTime3('00:11'))


aga = '<br>'.join(['11', '22', '33'])


with open('testfile.html', 'w') as tFile:
    tFile.write(aga)
