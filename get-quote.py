import random

def primary():
  add_response = input("Would you like to add quotes to file: ")
  print(add_response)

  while (add_response == 'Y' or add_response == 'y'):
  	quote = input("Type quote: ")
  	f = open("quotes.txt", "a")
  	f.writelines(quote + "\n")
  	f.close()
  	add_response = input("Would you like to add more quotes to file: ")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print("Keep it logically awesome.")
  last = len(quotes) - 1
  
  x = 0
  while x < last:
  	rnd = random.randint(0, last)
  	print(quotes[rnd], end = '')
  	x = x + 1


if __name__== "__main__":
  primary()
