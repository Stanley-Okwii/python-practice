# def get_sum(a,b):
#     result = []
#     if(a == b):
#         return a
#     if(a > b):
#         # for i in range(a,b):
# #           result.append(sti))
#         return (result[a:b])
#     if(b > a):
#         # for i in range(b,a):
# #            result.append(str(i))
#         return (result[b:a])

# print(get_sum(1,6))
def numbertoordinal(number):
#   Return a string with the correct ordinal indicator suffix 

  num = str(number)
  teen_number_list = []

  for i in range(11, 19):
      teen_number_list.append(str(i))
  teen_number_set = set(teen_number_list)

  if(num in teen_number_set) or (num[-2:] in teen_number_set):
    return(num + "th")
  elif(num[-1:] == "1"):
    return(num + "st")
  elif(num[-1:] == "2"):
    return(num + "nd")
  elif(num[-1:] == "3"):
    return(num + "rd")
  elif(num[-1:] == "0") and (num[0] =="0"):
    return(num)
  else:
    return(num + "th")
  
print(numbertoordinal(00))
