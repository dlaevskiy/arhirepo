import datetime
import re
import time

import mock


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print '%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000)
        return result
    return timed


@timeit
def test1(transactionCode):
    purpose = 'salary'
    match = re.search(r"\s*PURP(\S{1,35})(?:\s+|$)", transactionCode)
    if match:
        result = match.group(1)
    else:
        result = "SALA" if purpose == 'salary' else "SUPP"
    return result


@timeit
def test2(transactionCode):
    purpose = 'salary'
    try:
        result = re.search(r"\s*PURP(\S{1,35})(?:\s+|$)", transactionCode).group(1)
    except AttributeError:
        result = "SALA" if purpose == 'salary' else "SUPP"
    return result


def mockDate():
    return datetime.date(2017, 11, 29)


# class NewDate(datetime.date):
#     @classmethod
#     def today(cls):
#         return cls(2010, 1, 1)
#
#
# datetime.date = NewDate
#
# print datetime.date.today()


# with mock.patch('datetime.date', mock.Mock(today=mock.Mock(return_value=datetime.date(2017, 11, 29)))):
#     today = datetime.date.today()
#     # settlementDate = datetime.datetime.strptime(u'2017-02-02', '%Y-%m-%d').date()
#     print today


# with mock.patch("datetime.date.today", mockDate):
#     today = datetime.date.today()
#     print today


# today = datetime.date.today()
# settlementDate = datetime.datetime.strptime(u'2017-02-02', '%Y-%m-%d').date()
# print settlementDate
# print type(settlementDate)
# print today
# print type(today)


# with mock.patch('datetime.date') as mock_date:
#     mock_date.today.return_value = datetime.date(2010, 10, 8)
#     today = datetime.date.today()
#     print today


str1 = '0100070'
# print str1.count('0')


i = 521

# print ("%02d" % i)


def countLeadingZeros(string):
    droppedString = string.lstrip('0')
    diffZeros = len(string) - len(droppedString)
    return '{:0{}d}'.format(int(string), len(string))


print type(countLeadingZeros(str1))
print type("%02d" % int(7))
print type('{:06.2f}'.format(3.141592653589793))

x = int(1)
NewStringVariable = str(x).zfill(3)
print type(NewStringVariable)
print int(NewStringVariable)