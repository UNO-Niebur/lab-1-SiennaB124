#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("Enter a noun: ")
  verb1 = input("Enter a verb: ")
  noun2 = input("Enter a noun: ")
  verb2 = input("Enter a verb: ")
  adjetive1 = input("Enter an adjetive: ")
  noun3 = input("Enter a noun: ")
  #Print the story with the user supplied words.
  print("One day I found a " + noun1 + ".")
  print("I then used it to " + verb1 + "!")
  print("The next day the " + noun1 + " ripped my paper" + ".")
  print("I was told I was " + verb2 + " to hard.")
  print("So then I switched to using " + noun2 + "!")
  print("That turned out to be way to " + adjetive1 + "!")
  print("So I completly changed and now use " + noun3 + "!")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
