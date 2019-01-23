import pebblecreek 

class Group:
	def __init__(self, name, members, current_hole, score=0):
		self.name = name
		self.members = members
		self.score = score
		self.current_hole = current_hole
		self.scorecard = {}

	def set_hole(self, hole):
		self.current_hole = hole

	def input_score(self, shots):
		hole_score = (shots - pebblecreek.pebblecreek[self.current_hole])
		self.score += hole_score
		self.scorecard[self.current_hole] = hole_score

TheBoys = Group("The Boys", ["Harry", "Dele", "Jermain", "Toby"], 1 )
TheDogs = Group( "The Dogs", ["Wilson", "Coop", "Tilghman", "Gunner"], 2)
TheJims = Group("TheJims", ["Reuter", "Elliot", "Shannon", "Carroll"], 3)

def varcheck(groupname):
	print("Groupname: {}".format(groupname.name), "Score: {}".format(groupname.score), "Current Hole: {}".format(groupname.current_hole))

for i in [TheBoys, TheDogs, TheJims]:
	varcheck(i)





 

