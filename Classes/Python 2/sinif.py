class Animal(object):

	def __init__(self, bacak_sayisi):
		self.leg_count = bacak_sayisi

	def walk(self):
		print "Hayvan {0} bacagi ile yuruyor.".format(self.leg_count)

class Cat(Animal):

	def __init__(self):
		self.leg_count = 4

	def walk(self):
		super(Cat, self).walk()
		print "Bu bahsettigimiz hayvan bir kedidir."

orumcek = Animal(8)
pamuk = Cat()

orumcek.walk()
print " "
pamuk.walk()
