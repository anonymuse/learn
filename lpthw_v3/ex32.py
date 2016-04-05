the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
	print "This is the count %d" % number

for fruit in fruits:
	print "A fruit of type %s" % fruit

for bankroll in change:
	print "I have %r" % bankroll

elements = []

for i in range(0, 6):
	print "Adding %d to the list." % i
	elements.append(i)
	elements.pop(0)
	
print elements

for i in elements:
	print "Element was %d" % i
