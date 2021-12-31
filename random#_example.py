import random

# Create random_list of 100 numbers.
random_list = []
for i in range(101):
  random_list.append(random.randint(1,100))
print(len(random_list))

# Create randomer_number below:
randomer_number = random.choice(random_list)
print(randomer_number)


