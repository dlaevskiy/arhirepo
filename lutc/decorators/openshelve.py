import shelve
import os
import tempfile

if os.path.isfile('d:\\HubCom\\data\\DB\\EuroConv.py.dat'):
    f = shelve.open('d:\\HubCom\\data\\DB\\EuroConv.py.dat', writeback=False)
    try:
        print f
    except KeyError:
        print 'No key'
    f.close()
else:
    print 'No processing'

if os.path.isfile('d:\\HubCom\\data\\DB\\EuroConv.py.dat.orig'):
    f = shelve.open('d:\\HubCom\\data\\DB\\EuroConv.py.dat.orig', writeback=False)
    try:
        print f['BYN']
    except KeyError:
        print 'No origin key'
    f.close()
else:
    print 'No processing orig'

f = shelve.open('d:\\HubCom\\data\\DB\\EuroConv.py.dat', writeback=False)

t = tempfile.NamedTemporaryFile(delete=False)

with open(t.name, 'r') as file:
    for i in file:
        print i

print t.name

f.close()
t.close()

