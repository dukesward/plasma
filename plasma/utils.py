import xml.etree.ElementTree as tree
import json
import os

def tableToJson(path, filename):
    f = path + '/' + filename + '.xml'
    root = tree.parse(f).getroot()

    o = open('files/tables/' + filename + '.json', 'w')

    try:
        if root:
            table = []
            for child in root:
                if child.tag == 'Table':
                    item = {}
                    # c = 1
                    for field in child:
                        # c = c + 1
                        attrib = field.attrib
                        if 'ArraySize' in attrib:
                            size = field.attrib['ArraySize']
                        else:
                            size = 1
                        for i in range(int(size)):
                            item['column'] = field.attrib['Name']
                            item['type'] = field.attrib['Type']
                            if(int(size) > 1):
                                item['column'] = item['column'] + '_' + str(i)
                            table.append(item.copy())
                    # print(str(table).replace("'", '"'))
            o.write("%s\n" % str(table).replace("'", '"'))
    finally:
        o.close()

def fileStats(file):
    return os.stat(file)

def readByte(byte):
    print(byte)

	
