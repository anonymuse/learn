from sys import exit

class Room(object):
	def __init__(self, next)
		self.next = next

def gold_room():
	print "In this room full of gold, how much do you take?"

	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("You fell asleep.")

	if how_much < 50:
		print "You win"
		exit(0)
	else:
		dead("You're greedy")

def bear_room():
	print "There's a bear here."
	bear_moved = False
	print "Choose '1' for run, '2' for hide, '3' for open door."

	while True:
		next = raw_input("> ")
		int_next = int(next)

		if int_next == 1:
			dead("Don't run")
		elif int_next == 2:
			print "Good work hiding"
			bear_moved = True
		elif int_next == 3 and bear_moved:
			gold_room()
		elif int_next == 3 and not bear_moved:
			print "Hide first"
		else:
			print "I have no idea"

def cthulu_room():
	print "Here's the bad guy. 'Flee' or 'Yell'?"
	next = raw_input("> ")
	next_lower = next.lower()

	if "flee" in next_lower:
		start()
	elif "yell" in next_lower:
		dead("Well, that was tasty")
	else:
		cthulu_room()

def dead(reason):
	print reason, "But good try."
	exit(0)

def start():
	print "This is the start. Go 'right' or 'left'?"

	next = raw_input("> ")
	next_lower = next.lower()

	if next_lower == "left":
		bear_room()
	elif next_lower == "right":
		cthulu_room()
	else:
		dead("Next time choose more carefully.")

start()
