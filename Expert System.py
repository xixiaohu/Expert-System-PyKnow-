from pyknow import *

print ("This expert system will ask questions about Mascots of universities which are top 5 in Big 10 East Football of 2017.")
print ("For people who don't know Big 10, the top 5 teams in 2017 are Ohio State U, Penn State U, Michigan State U, U of Michigan, Rutgers.")
print ("You can google the mascots of these 5 universities to answer questions")
print ("Please input information as in bracket")


#gather information from users
fm = input("Is this Mascot a fruit or a mammal? (fruit/mammal)\n")
#force users to enter right answers.
while (fm != 'fruit') and (fm != 'mammal'):
	print ("Your answer should be either fruit or mammal.")
	fm = input("Is it a fruit or a mammal?\n")

# na is a valid answer for questions that not apply.
ah = input("Is this Mascot an animal or a human? (animal/human/na)\n") 
while (ah != 'animal') and (ah != 'human') and (ah != 'na'):
	print ("Your answer should be either animal or human or na.")
	ah = input("Is it an animal or a human?\n")

cl = input("If it's an animal, does it wear clothes? (yes/no/na)\n") 
while (cl != 'yes') and (cl != 'no') and (cl != 'na'):
	print ("Your answer should be either yes or no or na.")
	cl = input("Does it wear clothes?\n")

cc = input("If it's a human, what's the color of his clothes? (green/red/na)\n")
while (cc != 'red') and (cc != 'green') and (cc != 'na'):
	print ("Your answer should be either red or green or na.")
	cc = input("What's the color of his clothes?\n")



class Mascot(Fact):
	"""Identification about universities."""
	pass

class UniversityIdentify(KnowledgeEngine):
	#if it's a fruit, and na for rest of questions, it's Brutus. GO BUCKS!
	@Rule(AND(Mascot(frumam='fruit'), Mascot(anihum='na'), Mascot(clothes='na'), Mascot(color='na')))
	def osu(self):
		print("It's Brutus Buckeye from OSU!! No.1 in 2017!! Go Bucks!!!")
	
	#if it's a fruit, but has answers for rest of questions, it's wrong.
	@Rule(AND(Mascot(frumam='fruit'), OR(Mascot(anihum='animal'), Mascot(anihum='human'), Mascot(clothes='yes'), Mascot(clothes='no'), Mascot(color='green'), Mascot(color='red'))))
	def fw(self):
		print("Information you input is incorrect!!")

	#if it's mammal, but na for rest of questions, it's wrong.
	@Rule(AND(Mascot(frumam='mammal'), Mascot(anihum='na')))
	def mw(self):
		print("Information you input is incorrect!!")

	#if it's an animal, wears clothes and na for rest of questions, it's Biff. Beat Mich!
	@Rule(AND(Mascot(frumam='mammal'), Mascot(anihum='animal'), Mascot(clothes='yes'), Mascot(color='na')))
	def um(self):
		print("It's Biff Wolverine from UM, No.4 in 2017. Beat Michigan!!")
	
	#if it's an animal, doesn't wear clothes and na for rest of questions, it's Nittany. Beat PSU!
	@Rule(AND(Mascot(frumam='mammal'), Mascot(anihum='animal'), Mascot(clothes='no'), Mascot(color='na')))
	def psu(self):
		print("It's Nittany Lion from PSU, No.2 in 2017. Beat PSU!!")

	#if it's animal, but na for clothes or has answers for rest of questions, it's wrong.
	@Rule(AND(Mascot(frumam='mammal'), Mascot(anihum='animal'), OR(Mascot(clothes='na'), Mascot(color='green'), Mascot(color='red'))))
	def aw(self):
		print("Information you input is incorrect!!")

	#if it's a human in green and na for rest of questions, it's Sparty.
	@Rule(AND(Mascot(frumam='mammal'), Mascot(anihum='human'), Mascot(clothes='na'), Mascot(color='green')))
	def msu(self):
		print("It's Sparty from MSU, No.3 in 2017.")

	#if it's a human in red and na for rest of questions, it's Scarlet.
	@Rule(AND(Mascot(frumam='mammal'), Mascot(anihum='human'), Mascot(clothes='na'), Mascot(color='red')))
	def Rutgers(self):
		print("It's Scarlet Knight from Rutgers, No.5 in 2017.")

	#if it's a human, but na for color or has answers for rest of questions, it's wrong.
	@Rule(AND(Mascot(frumam='mammal'), Mascot(anihum='human'), OR(Mascot(color='na'), Mascot(clothes='yes'), Mascot(clothes='no'))))
	def hw(self):
		print("Information you input is incorrect!!")


engine = UniversityIdentify()
engine.reset()
engine.declare(Mascot(frumam=fm, anihum=ah, clothes=cl, color=cc))
engine.run()


