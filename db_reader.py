from plasma import readers, utils

from struct import *
from collections import namedtuple


def main():
	# utils.tableToJson('files/xml', 'ItemClass')
	f = readers.DBCReader('files/dbc','ItemClass')
	# print(f)
	# test()

def test():
	f = open('files/test', 'rb')
	try:
		utils.readByte(f.read())
	finally:
		f.close()

if __name__ == "__main__":
	main()