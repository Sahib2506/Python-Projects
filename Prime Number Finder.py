def prime_checker(number):
  prime = 0
  for i in range(2, number):
    if number % i !=0:
      prime +=1
    else:
      pass
  if prime == 1:
    print(f"{number} is a Prime")
  else:
    print(f"{number} is not a Prime")


n = int(input("Check this number: "))
prime_checker(number=n)



