import re
match = re.search('iig','called piig')
print match
print match.group()
if match: print 'found'
else: print 'not found'
