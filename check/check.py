import copy
import decimal


class DeepCopyDict(dict):
    def copy(self):
        return copy.copy(self)


class KyribaPYHeaderDict(DeepCopyDict):

    def __setitem__(self, key, val):
        if key == "PROTOCOL" and val:
            val += '11111'
        dict.__setitem__(self, key, val)


R_HEADER = KyribaPYHeaderDict({
    'PROTOCOL': u'010',
    'ISSUER': {
        'COMPANY_CODE': u'COMP-FR1',
        'DESCRIPTION1': u'desc1.COMP-FR1',
    },
})

R_HEADER.__setitem__('PROTOCOL', 'FTP')

print(R_HEADER)






