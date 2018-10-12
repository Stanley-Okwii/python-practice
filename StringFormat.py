def joiner(s1,s2,s3):
  print("{0} is a big {2} of {1}".format(s1,s2,s3))

def notter(s = None):
  if(not s):
    print("S is not available")
  else:
    print("S is there{}".format(s))
# notter()
def digitize(n):
#   convert the number to a string
  # result = list(str(n))
  results = map(int, list(str(n)))
  print(results)
  
# digitize(134354435444)
a = 1
while a:
    a += 23
    print(a)