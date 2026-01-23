#FirstProgram.py
#Name:Sienna Bonner
#Date:1/22/26
#Assignment:Lab 1 

def main():
  print("First Program")
  #Say hello
  print("hello")
  #Ask for the user's name
  name = input("what is your name?\n")
  #Use the user's name in the program.
  print("hello " + name)
  #Ask the user for their age.
  age = input("what is your age?\n")
  #Tell the user what year they were born in.
  #Assume that they have not had their birthday yet this year.
  birthYear = (2025 - int(age))
  print("You were born in " + str(birthYear))
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
