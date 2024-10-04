#IDEA
#Povezati sa OS i izvuci sve procese

from localprogram import run_cmd_program
from flaskapp import start_server,open_browser,run_all

counter_p = 0
process_list = []

user_choice = -99
input("Please press to start")
user_choice = input("\n-1 -> Cmd program\n1 -> webapp\n0 -> all functions full appEnter your choice:")
user_choice = int(user_choice)

print("Staaaa")

if user_choice == -1:
    print("You are choice cmd program")
    run_cmd_program()

if user_choice == 1:
    print("You are choice a webapp")
    open_browser()
    start_server()

if user_choice == 0:
    print("You start all, cmd conneted to webapp, thats full app.")
    run_cmd_program()
    open_browser()
    start_server()

