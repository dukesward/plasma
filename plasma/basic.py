from plasma.statistics import *

class Dot:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __repr__(self):
		return '<%s, %s>' % (self.x, self.y)

class Set:
    def __init__(self, dot):
        if(type(dot) is Dot):
            self.dots = [dot]
        else:
            raise Exception("a set must be initialized by a dot")

    def append(self, dot):
        if(type(dot) is Dot):
            self.dots.append(dot)
        else:
            raise Exception("a set can only append dots")

    def __repr__(self):
        return '[%s]' % ','.join([str(d) for d in self.dots])


class Matrix:
    def __init__(self, rows, cols, mod=0):
        self.rows = rows
        self.cols = cols
        self.mod = mod
        self._matrix = self.build(self.mod)

    def __repr__(self):
        return str(self._matrix)

    def build(self, mod=0, prototype=None):
        if prototype is None:
            prototype = [[x for x in range(self.cols)] for y in range(self.rows)]

        if type(mod) is int:
            return [[mod for x in y] for y in prototype]
            # print(self._matrix)
        elif type(mod) is str:
            return [[interpret(mod, str(x), str(y)) for x in y] for y in prototype]
            # print(self._matrix)
        else:
            # if user provided mod not valid, use default mod
            # self.mod = 0
            return self.build(0)


    def weight(self):
        self._pmatrix = self.build(self.wt)
        # self._pmatrix = [[interpret(str(self.wt), str(x), str(y)) for x in y] for y in self._matrix]
        self.normal = self.normalize()
        print(self._pmatrix)
        return

    def normalize(self):
        return sum(sum(x) for x in self._matrix)

    def expect(self):
        return


class Network:
    def __init__(self, model=None):
        self.model = model

    def train(self, input):
        return

    def refine():
        return