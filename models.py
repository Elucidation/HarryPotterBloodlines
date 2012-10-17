from random import random, sample
from randomName import *
MAGIC_YES = "M"
MAGIC_NO = "_"
EXCHANGE_RATE = 0.1 # Percentage of people to die and be replaced with new children
DNA_LENGTH = 20 # N > 1 = Harry's first hypothesis, N = 1 is his 2nd

SQUIB_THRESHOLD = 0.3
WIZARD_THRESHOLD = 0.7

class World:
	def __init__(self,NumPeople,dnaLength=DNA_LENGTH,exchangeRate = EXCHANGE_RATE): 
		self.ppl = []
		self.date = 0 # Generators since
		self.allPeople = []
		self.dnaLength = dnaLength 
		self.exchangeRate = exchangeRate
		for x in xrange(NumPeople):
			self.ppl.append( Person(0,None,None,dnaLength) )
			self.allPeople.append( self.ppl[-1] )
		# gandalf = Person()
		# gandalf.dnaA = gandalf.dnaB = 'M'*self.dnaLength
		# gandalf.gender = 'M'
		# gandalf.name = ['Gandalf', 'Awesome']
		# self.ppl.append(gandalf)
		self.history = [] # Strings keeping track of who was born and died

	def step(self):
		self.date += 1
		children = []
		replacement_indices = sample(xrange(self.size()),int(self.size()*self.exchangeRate))
		for i in replacement_indices:
			# For the percentage of people dieing and being replaced
			dad = sample(filter(lambda p: p.gender=='M',self.ppl), 1)[0]
			mum = sample(filter(lambda p: p.gender=='F',self.ppl), 1)[0]
#			dad,mum = sample(self.ppl, 2) # Choose any two people
			self.ppl[i].dead = self.date
			child = Person(self.date,dad,mum,self.dnaLength)
			self.history.append("%s (%s), was born in the year %d. %s father is %s (%s) and %s mother is %s (%s)." % (
				child, child.gender, self.date, "His" if child.gender == 'M' else "Her", 
				dad, dad.gender, "his" if child.gender == 'M' else "her" ,mum, mum.gender
				))
			
			# print "%s and %s gave birth to %s. %s died." % (dad,mum,child, self.ppl[i])
			self.history.append("%s died in the year %d at age %d." % ( self.ppl[i], self.date, self.date - self.ppl[i].born )   )
			self.ppl[i] = child
			self.allPeople.append( child )

	def size(self):
		return len(self.ppl)
	def __str__(self):
		numWizards=numSquibs=numMuggles=0
		for p in self.ppl:
			magicLevel = float(p.dnaA.count(MAGIC_YES)+p.dnaB.count(MAGIC_YES)) / (2*self.dnaLength)
			if magicLevel > 0.7:
				numWizards+=1
			elif magicLevel > 0.3:
				numSquibs+=1
			else:
				numMuggles+=1
		s = "World:: Generation %d :: Population: %s, Wizards: %d, Squibs: %d, Muggles: %d\n" % (self.date, self.size(), numWizards, numSquibs,numMuggles)
		self.ppl = sorted(self.ppl, key=lambda p: p.name[1]+p.name[0])
		for p in self.ppl:
			s += "%s\n" % p.longString()
		return s
	def __repr__(self):
		return self.__str__()

class Person:
	def __init__(self,birthday=0,dad=None,mum=None,dnaLength=DNA_LENGTH):
		self.born = birthday
		self.dnaLength = dnaLength
		if not dad or not mum:
			# Test-tube baby
			self.randChild()
			self.name = [randName(),randName()]
		else:
			self.childOf(birthday,dad,mum)
		self.gender = 'M' if flipCoin() else 'F' # Male/Female
		self.dead = False
	def copyOf(person):
		p = Person()
		p.name = person.name
		p.gender = person.gender
		p.born = person.born
		p.dead = person.dead
		p.parents = person.parents
		p.dnaLength = person.dnaLength
		return p
	def deepCopyOf(person):
		p = Person.copyOf(person)
		p.parents = list(p.parents)
		if isinstance(person.parents[0],Person):
			p.parents[0] = Person.copyOf(person.parents[0])
		if isinstance(person.parents[1],Person):
			p.parents[1] = Person.copyOf(person.parents[1])
		return p
	def randChild(self):
		self.dnaA = ""
		self.dnaB = ""
		for x in xrange(self.dnaLength):
			self.dnaA += MAGIC_YES if flipCoin() else MAGIC_NO
			self.dnaB += MAGIC_YES if flipCoin() else MAGIC_NO
		self.parents = ["Alpha","Omega"]

	def childOf(self,birthday,dad,mum):
		self.born = birthday
		self.dnaA = ""
		self.dnaB = ""
		for dadA,dadB,mumA,mumB in zip(dad.dnaA, dad.dnaB, mum.dnaA, mum.dnaB):
			self.dnaA += dadA if flipCoin() else dadB
			self.dnaB += mumA if flipCoin() else mumB
		self.name = [randName(), (dad.name[1] if random() > 0.2 else mum.name[1]) ] # Male-centric I know...
		self.parents = [dad,mum]

	def longString(self):
		pronoun = 'he' if self.gender == 'M' else 'she'
		possessive = 'his' if self.gender == 'M' else 'her'
		s = "%20s" % ("%s %s" % (self.name[0],self.name[1]))
		s += ". Born in the year %d. %s is a %s." % (self.born, pronoun.capitalize(), magicalness(self))
		s += " %s parents are %s and %s" % (possessive.capitalize(),self.parents[0],self.parents[1])
		s += " DNA: %s/%s"  % (self.dnaA,self.dnaB)
		return s
	def __str__(self):
		if self.getMagicLevel() > WIZARD_THRESHOLD:
			return "*%s %s*" % (self.name[0],self.name[1])
		else:
			return "%s %s" % (self.name[0],self.name[1])
	def __repr__(self):
		return self.__str__()

	def getMagicLevel(self):
		# 0 = Muggle, 1 = Wizard of massive proportions
		return float(self.dnaA.count(MAGIC_YES)+self.dnaB.count(MAGIC_YES)) / (2*self.dnaLength)

def magicalness(person):
	magicLevel = person.getMagicLevel()
	if magicLevel > WIZARD_THRESHOLD:
		return "Wizard!"
	elif magicLevel > SQUIB_THRESHOLD:
		return "Squib"
	else:
		return "Muggle"

def flipCoin():
	return random() < 0.5
