import os
if not os.path.exists("letters"):
   os.makedirs("letters")

os.chdir(os.getcwd() + '\letters')
   
upper_letters = [chr(x) for x in range(65, 91)]   
   
for letter in upper_letters:
   with open(letter + ".txt", "w") as fp:
       fp.write(letter)