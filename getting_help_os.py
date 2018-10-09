import os
import sys


user_input = input("Enter 'Help' for help on module os.\n")

if user_input == "Help":
	help(os)
elif (user_input == "exit") or (user_input == "Exit") or (user_input == "quit"):
	sys.exit()