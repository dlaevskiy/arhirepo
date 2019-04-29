import re
documentPattern = "(.+?</Document>)\s*"
inputFilePath = r'D:\EBCScamt54510FONCIA.RDP075VIRRECUS.S20190308073005.P20190308073005'

with open(inputFilePath) as inputFile:
    multidocContent = inputFile.read()

print 'regex start'
re.findall(documentPattern, multidocContent, re.DOTALL | re.UNICODE)
print 'regex finish'


