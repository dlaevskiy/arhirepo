# import requests
# import re
#
# obj = requests.get('https://web.archive.org/web/20160303230643/http://cs.nyu.edu/~yusuke/tools/unicode_to_gb2312_or_gbk_table.html')
#
#
# result = re.findall(r'(<small>)(.{1,4})(</small>)', obj.text)
#
# l = []
#
# for elem in result:
#     code = elem[1]
#     format_code = '\\u' + code.rjust(4, '0')
#     l.append(format_code)
#
# print(len(l))
# print(l)
# print(''.join(l))

string = u'\uced6'

# encodedString = string.encode('gb2312')
#
# print encodedString


def utf2gbk(s, ignore=True):
    if ignore:
        return unicode(s, 'utf8', 'ingore').encode('gb18030', 'ingore')
    else:
        return unicode(s, 'utf8').encode('gb18030')


print(utf2gbk(string))