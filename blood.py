from random import seed
from models import *
SEED_VALUE = 43425264
seed(SEED_VALUE)

# A person has dna which states their magic level

# M = Magic, H = Human


def printAncestry(person,currentDate=None):
	p = person
	# Dads
	print "##########################"
	if currentDate and not p.dead:
		print "Ancestry of %s, born %03d. Current age %d." % (p,p.born, currentDate-p.born),
	else:
		print "Ancestry of %s, born %03d." % (p,p.born),
	print "%s. Dad & Mum are %s and %s." % ("Male" if p.gender=='M' else "Female", p.parents[0],p.parents[1])
	if p.parents[0] == 'Alpha' and p.parents[1] == "Omega": 
		print "One of the Original." 
		return
	
	for name,i in zip(["Patriarchy","Matriarchy"],[0,1]):
		print "###############"
		print "#%s" % name
		p = person
		n=1
		while isinstance(p,Person):
			print "%s%s (B:%03d D:%s, Age %d), Magic level: %g%%" % (
				(" "*2*n+"^"+" ")*(n>1),p,p.born,"%03d"%(p.dead) if p.dead else "---", currentDate-p.born if not p.dead else p.dead-p.born,
				p.getMagicLevel() * 100
				)
			p = p.parents[i]
			n+=1

STEPS = 200
N = 200 # Number of people initially
DNA_LENGTH = 10
EXCHANGE_RATE = 0.1 # Percentage of people to die and be replaced with new children

print "Seed used: %d" % SEED_VALUE
print "People per generation: %d, Total number of generations: %d" % (N,STEPS)
print "Creating world...",
world = World(N,DNA_LENGTH,EXCHANGE_RATE)
print "Done."
print world

print "Running world...",
for x in xrange(1,STEPS):
	world.step()
	# if x % (STEPS/10) == 0:
	# 	print world
print "Done."
print world

# print '\n'.join(world.history)

checkAge = 40
ancients = filter(lambda person: (not person.dead and world.date-person.born > checkAge) or (person.dead and person.dead-person.born > checkAge),world.allPeople)
# if ancients:
# 	printAncestry(ancients[len(ancients)/2],world.date)
print "All people in world dead/alive: %d, People who lived beyond %d: %d" % (len(world.allPeople), checkAge, len(ancients))

wizards = filter(lambda person: person.getMagicLevel() > 0.7, world.allPeople)
if wizards:
	print "Number of all wizards who ever existed: %d" % (len(wizards))
	printAncestry(wizards[-1],world.date)
