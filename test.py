# based on the input

def say_hello(name = None):
  # you can print to STDOUT to debug if you need to:
#   print(name)
  if(name):
    name = name
  else:
    name = "there"
  # but to complete the challenge you need to return a value
  return("Hello, "+name+"!")

#   if __name__ == "__main__":
# 	main()

def openOrSenior(data):
    # Hmmm.. Where to start?
    # Hmmm.. Where to start?
    memberList = []
    for member in data:
        if(member[1] > 55 & member[0] > 7):
            memberList.append("Senior")
        else:
            memberList.append("Open")
    return(memberList)

print(openOrSenior([[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]))