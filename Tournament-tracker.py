##BUG! Need a function to ensure alpha only
##BUG! What if the name I want to cancel is not in the list? Program ends.
##BUG! What if user enters cancellation and realized they dont want to cancel anyone? They'll have to full exit and won't be able to save work without actually cancelling someone and then re-adding them, assuming they remember at least one key/value.

menu_options = {1: 'Sign Up', 2: 'Cancel Sign Up', 3: 'View Participants', 4: 'Save Changes', 5: 'Exit'}

def display_main_menu():
    print("\nParticipant Menu\n")
    print("====================")
    for i in menu_options:
        print(f'{i}. {menu_options[i]}')

def get_particip_int(prompt):
    my_int = 0
    is_valid = False
    while not is_valid:
        try:
            my_int = int(input(prompt))
            is_valid = True
        except:
            print('Invalid Integer, try again')
    return my_int

def get_menu_int(prompt):
    my_int = 0
    is_Valid = False
    while not is_Valid:
        try:
            my_int = int(input(prompt))
            if my_int <1 or my_int>5:
                raise ValueError
            else:
                return my_int
        except ValueError:
            print('Invalid Integer, try again. Select menu option from 1 to 5.   ')
    return my_int

def sign_up():
    print("Sign Up Menu")
    print("====================")
    is_valid = False
    while not is_valid:
        particip_name = str(input("Participant Name:    ")).title()
    ##BUG! Need a function to ensure this is alpha only.
        if particip_name not in particip_dict.values():
            is_valid = True
        else:
            print(f'{particip_name} is already signed up.')
        continue
    is_valid = False
    while not is_valid:
        particip_slot = get_particip_int(f"Desired starting slot #[1-{int(num_particip)}]:    ")
        if particip_slot<1 or particip_slot>num_particip:
            print(f'{particip_slot} is out of range. Choose between 1 and {num_particip}.')
        elif particip_dict[particip_slot] == None: 
            print(f'Success:\n{particip_name} is signed up in starting slot #{particip_slot}.')
            is_valid = True
        else:
            print(f"Starting slot #{particip_slot} is already taken. Choose another slot.")
        continue
    particip_dict[particip_slot] = particip_name
    print(particip_dict) #just checking to see if it worked
    
def cancellation():
    print('Participant Cancellation')
    print("====================")
    is_valid = False
    while not is_valid:
        particip_slot = get_particip_int(f"Starting slot #[1-{int(num_particip)}]:  ")
        particip_name = input("Participant Name:    ").title()
        if particip_slot in particip_dict and particip_name in particip_dict[particip_slot]:
            print(f'Success:\n{particip_name} has been cancelled from starting slot #{particip_slot}.')
            is_valid = True
        #elif particip_name not in particip_dict.keys():
        #    print(f'{particip_name} is not signed up yet')
        #    continue
        ##BUG! What if the name I want to cancel is not in the list? Program ends.
        ##BUG! What if user enters cancellation and realized they dont want to cancel anyone? They'll have to full exit and won't be able to save work without actually cancelling someone and then re-adding them, assuming they remember at least one key/value.
        else:
            print(f'{particip_name} is not in that starting point.')
        continue
    particip_dict[particip_slot] = None
    print(particip_dict) #just checking to see if it worked

def view_participants():
    print('View Participants')
    print("====================")
    particip_slot = get_particip_int(f"Starting slot #[1-{int(num_particip)}]:     ")
    print('Starting Slot: Participant')
    res = dict((k,particip_dict[k]) for k in range(particip_slot-5,particip_slot+6) if k in particip_dict)
    for key in res:
        print(key, ":", res[key])

def save_changes():
    print('Save Changes')
    print("====================")
    keys = particip_dict.keys()
    fields = ['Participant Number','Participant Name']
    vals = particip_dict.values()
    keys = list(keys)
    vals = list(vals)
    fill_list = []
    for i in range(len(keys)):
        fill_list.append([keys[i],vals[i]])
    import csv
    filename = "participants.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(fill_list)

###################################################

###################################################

print('Welcome to Tournaments R Us\n \n====================\n')

num_particip = get_particip_int('Enter number of participants:  ')
print(f'There are {num_particip} participant slots ready for sign ups.\n')
particip_dict = dict.fromkeys(range(1,num_particip+1)) 
print(particip_dict) #just checking to see if it worked

exit_choice = 'y'
while exit_choice != 'n':
    display_main_menu()
    menu_choice = get_menu_int('Select menu option from 1 to 5.     ')

    if menu_choice == 1:
        sign_up()

    elif menu_choice ==2:
        cancellation()

    elif menu_choice ==3:
        view_participants()
        
    elif menu_choice ==4:
        save_changes()
       
    elif menu_choice ==5:
        print('Exit')
        print("====================")
        print("Any unsaved changes will be lost.")
    exit_choice = input('Back to main menu? Any unsaved changes will be lost. [y/n]     ')


print('Goodbye!')