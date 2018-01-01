from struct import *
from collections import namedtuple
from plasma import utils
import json

class DBCReader:

	def __init__(self, path, fileName):
		if type(fileName) is str:
			self.table = []
			self.extension = '.dbc'
			self.fileName = path + '/' + fileName
			self.baseSize = utils.fileStats(self.fileName + self.extension).st_size
			self.actualSize = 0
			self.configName = 'files/tables/' + fileName
			self.configure(self.configName)
			self.extract(self.fileName)
		else:
			raise Exception("a string must be provided for fileName")

	def __repr__(self):
		return str(self.table)

	def _testDecode(self, byte):
		print(byte)
		return byte

	def types(self, type, byte):
		return {
			# use I for unsigned int and i fot signed int
			'int' : unpack('i', byte),
			'float' : unpack('f', byte),
			# self._testDecode(byte).decode('utf-8')
			'string' : unpack('i', byte)
		}[type]

	def extract(self, fileName):
		f = open(fileName + self.extension, 'rb')
		try:
			head = f.read(4)
			if head == b'WDBC':
				if self.checkHeader(f.read(16)):
					record_c = self.desc.record_c
					field_c = self.desc.field_c
					# string table start = head_s + desc_s + record_c*record_s
					str_table_start = 4 + 16 + self.actualSize
					str_table_s = self.baseSize - str_table_start - 1
					# read the record table which contains the records
					actualRecords = f.read(self.actualSize)
					# read the string table which contains string dictionary in utf-8
					stringTable = f.read(str_table_s)
					record_r = 1 # record_c
					print(stringTable.decode('utf-8'))
					# print(self.table)
				else:
					raise Exception("the input dbc file is corrupted, or does not match the config table")
			else:
				print(head)
				raise Exception("the input file is not a valid dbc file")
		finally:
			f.close()

	def configure(self, fileName):
		f = open(fileName + '.json', 'r')
		try:
			self.config = json.loads(f.read())
			# print(self.config)
		finally:
			f.close()

	def checkHeader(self, byte):
		desc = namedtuple('Desc', 'record_c field_c record_s table_s')
		self.desc = desc._make(unpack('IIII', byte))
		self.actualSize = self.desc.record_c * self.desc.record_s
		print(self.desc)
		# print(len(self.config))
		# check the fields num of dbc only if should match the table config
		return self.desc.table_s # and len(self.config) == self.desc.field_c

	def readString(self, bytes):
		for i in range(record_r):
			cols = {}
			for j in range(len(self.config)):
				col = f.read(4)
				config = self.config[j]
				# obtain a tuple with format (d,) -> d
				# if config['type'] == 'string':
					# print(self.config)
					# print(config['column'] + ' : ')
					# print(col)
					# print(col.decode('utf-8'))
				data = self.types(config['type'], col)[0]
				cols[config['column']] = data
			self.table.append(cols)


