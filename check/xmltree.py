import lxml.etree as ET
import lxml.builder as BR
import xml.etree.ElementTree as eTree

XML_NAMESPACE = "urn:iso:std:iso:20022:tech:xsd:acmt.02z.001.01:Report"

E = BR.ElementMaker(namespace=XML_NAMESPACE,
                    nsmap={None: "urn:iso:std:iso:20022:tech:xsd:acmt.02z.001.01:Report"})

Document = E.Document
AcctSwtchngInfSvcRptV01 = E.AcctSwtchngInfSvcRptV01
Assgnmt = E.Assgnmt
MsgId = E.MsgId
CreDtTm = E.CreDtTm
Assgnr = E.Assgnr
Agt = E.Agt
FinInstnId = E.FinInstnId
BICFI = E.BICFI
Assgne = E.Assgne
Pty = E.Pty
Nm = E.Nm
Id = E.Id
OrgId = E.OrgId
Othr = E.Othr
Mod = E.Mod
AcctSwtchngRef = E.AcctSwtchngRef
AcctSwtchngId = E.AcctSwtchngId
DtOfSgntr = E.DtOfSgntr
OrgnlPtyAndAcctId = E.OrgnlPtyAndAcctId
Acct = E.Acct
IBAN = E.IBAN
UpdtdPtyAndAcctId = E.UpdtdPtyAndAcctId
TxRprt = E.TxRprt
TxsSummry = E.TxsSummry
TtlNtriesPerBkTxCd = E.TtlNtriesPerBkTxCd
NbOfNtries = E.NbOfNtries
BkTxCd = E.BkTxCd
TxDtls = E.TxDtls
Domn = E.Domn
Cd = E.Cd
Fmly = E.Fmly
SubFmlyCd = E.SubFmlyCd
Refs = E.Refs
EndToEndId = E.EndToEndId
RltdPties = E.RltdPties
Dbtr = E.Dbtr
AnyBIC = E.AnyBIC
DbtrAcct = E.DbtrAcct
UltmtDbtr = E.UltmtDbtr
RltdAgts = E.RltdAgts
DbtrAgt = E.DbtrAgt

xml_doc = Document(
    AcctSwtchngInfSvcRptV01(
        Assgnmt(
            MsgId('MSGID - 345678'),
            CreDtTm('2015-10-06T14:00:01Z'),
            Assgnr(
                Agt(
                    FinInstnId(
                        BICFI('BQFFFRPP')
                    )
                )
            ),
            Assgne(
                Pty(
                    Nm('SOCIETE CLIENT NATIXIS'),
                    Id(
                        OrgId(
                            Othr(
                                Id('FR7630007999990499999900069')
                            )
                        )
                    )
                )
            )
        ),
        Mod(
            Id('TEST2'),
            AcctSwtchngRef(
                AcctSwtchngId('ENTITE 10014_02'),
                DtOfSgntr('2016-11-08')
            ),
            OrgnlPtyAndAcctId(
                Pty(
                    Nm('M ROUQUAN JACQUES')
                ),
                Acct(
                    IBAN('FR783000301251000509999BB82')
                ),
                Agt(
                    FinInstnId(
                        BICFI('SOGEFRPPXXX')
                    )
                )
            ),
            UpdtdPtyAndAcctId(
                Pty(
                    Nm('M ROUQUAN J')
                ),
                Acct(
                    IBAN('FR411005702300222222222BB40')
                ),
                Agt(
                    FinInstnId(
                        BICFI('CMCIFRPPXXX')
                    )
                )
            ),
            TxRprt(
                TxsSummry(
                    TtlNtriesPerBkTxCd(
                        NbOfNtries('1'),
                        BkTxCd(
                            Domn(
                                Cd('PMNT'),
                                Fmly(
                                    Cd('ICDT'),
                                    SubFmlyCd('OTHR')
                                )
                            )
                        )
                    )
                ),
                TxDtls(
                    BkTxCd(
                        Domn(
                            Cd('PMNT'),
                            Fmly(
                                Cd('ICDT'),
                                SubFmlyCd('ESCT')
                            )
                        )
                    ),
                    Refs(
                        EndToEndId('VIR-SCT2')
                    ),
                    RltdPties(
                        Dbtr(
                            Nm('SOCIETE CLIENT NATIXIS'),
                            Id(
                                OrgId(
                                    AnyBIC('NATXFRPPXXX')
                                )
                            )
                        ),
                        DbtrAcct(
                            Id(
                                OrgId(
                                    AnyBIC('NATXFRPPXXX')
                                )
                            )
                        ),
                        UltmtDbtr(
                            Nm('SOCIETE CLIENT NATIXIS'),
                            Id(
                                OrgId(
                                    AnyBIC('NATXFRPPXXX')
                                )
                            )
                        )
                    ),
                    RltdAgts(
                        DbtrAgt(
                            FinInstnId(
                                BICFI('NATXFRPPXXX')
                            )
                        )
                    )
                )
            )
        )
    )
)

def Add_new_Assgmt(struct):
    struct.append(
        Assgnmt(
            MsgId('MSGID - 345678'),
            CreDtTm('2015-10-06T14:00:01Z'),
            Assgnr(
                Agt(
                    FinInstnId(
                        BICFI('BQFFFRPP')
                    )
                )
            )
        )
    )

def Add_new_AcctSwtchngInfSvcRptV01(struct):
    struct.append(
        AcctSwtchngInfSvcRptV01(
        )
    )

def set_xml_field_value(xpath, value, tagNumber=1):
    xpath = xpath.split('/')
    if XML_NAMESPACE:
        xpathWithNameSpace = ['{' + XML_NAMESPACE + '}' + element for element in xpath]
        xpath = '/'.join(xpathWithNameSpace)
    tagList = xml_doc.findall(xpath)
    try:
        tagList[int(tagNumber) - 1].text = value
    except IndexError:
        raise ValueError('There is no such tag with index {}!'.format(tagNumber))

# Add_new_Assgmt(xml_doc[0])
#
# set_xml_field_value('AcctSwtchngInfSvcRptV01/Assgnmt/MsgId', 'val1', 1)
# set_xml_field_value('AcctSwtchngInfSvcRptV01/Assgnmt/MsgId', 'val2', 2)
# set_xml_field_value('hui', 'val2')


# Add_new_Assgmt(xml_doc[0])
# a = xml_doc.findall('{urn:iso:std:iso:20022:tech:xsd:acmt.02z.001.01:Report}AcctSwtchngInfSvcRptV01/{urn:iso:std:iso:20022:tech:xsd:acmt.02z.001.01:Report}Assgnmt/{urn:iso:std:iso:20022:tech:xsd:acmt.02z.001.01:Report}MsgId')
#
# a[0].text = 'hui'
# a[1].text = 'pis'
#
# print a[0].text
# print a[1].text

# Add_new_AcctSwtchngInfSvcRptV01(xml_doc)
# Add_new_Assgmt(xml_doc[0])
# Add_new_Assgmt(xml_doc[0])
# Add_new_AcctSwtchngInfSvcRptV01(xml_doc)
# Add_new_Assgmt(xml_doc[1])

with open('xmlfile.xml', 'w') as xfile:
    xfile.write(ET.tostring(xml_doc, xml_declaration=True, pretty_print=True, encoding='UTF-8'))

# print ET.tostring(xml_doc, xml_declaration=True, pretty_print=True, encoding='UTF-8')
