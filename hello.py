import sys
def Hello(name):
  if name == 'tom':
     name = name + '???'
  else:
    name = name+ '!!!!!'
  print 'Hello', name


 
def main():
	 Hello(sys.argv[1])
if __name__=='__main__':
	main()

