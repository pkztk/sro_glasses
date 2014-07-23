#!/usr/bin/python2


class Figura:

	no_figures = 0

	def __init__(self, n_sides,):
		self.n_sides = n_sides
		Figura.no_figures += 1

	def __str__(self):
		return "Figura ma {} bokow".format(self.n_sides)

	def getName(self):
	
		if self.n_sides == 3:
			return "Trojkat"
		else:
			return "Who knows"

class Restaurant(object):
	bankrupt = False
	def open_branch(self):
		if not self.bankrupt:
			print("branch opened")




class Inst:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, I am %s, and my name is " %(self.name))

def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)


print import_from("os", "system")
