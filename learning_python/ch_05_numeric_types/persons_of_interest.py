engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}

def sepr():
    print '-' * 5

print "'bob' in engineers"
sepr()
print 'bob' in engineers            # Is bob an engineer?

print "engineers & managers"
sepr()
print engineers & managers          # Who is both an engineer and a manager?

print "engineers | managers"
sepr()
print engineers | managers          # All people in either category?

print "engineers - managers"
sepr()
print engineers - managers          # All engineers who are not managers?

print "engineers > managers"
sepr()
print engineers > managers         # Are all engineers managers (superset)?

print "{\"bob\", \"sue\"}  < engineers"
sepr()
print {"bob", "sue"} < engineers    # Are both engineers? (subset)?

print "( managers | engineers) > managers"
sepr()
print (managers | engineers) > managers     # Are all people managers (superset)?

print "managers ^ engineers"
sepr()
print managers ^ engineers          # Who is in one but not both?

print "(managers | engineers) - (managers ^ engineers)"
sepr()
print (managers | engineers) - (managers ^ engineers)   # Intersection!
