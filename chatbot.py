#Sophia
import time
password = '111'
decoy_password = '000'
acess_type = None
print('Welcome to Secret Diary Chatbot!')
time.sleep(0.5)
name = input('What is your name? ')
time.sleep(0.5)
print('Hello ' + name + '!')
time.sleep(0.5)
guessed_password = input('What is the password? ')
wrong = 0
while acess_type == None:
    if guessed_password == password:
        acess_type = 'allowed'
    elif guessed_password == decoy_password:
        acess_type = 'decoy'
    else:
        if wrong == 2:
            acess_type = 'denied'
        else:
            guessed_password = input('What is the password? ')
            wrong = wrong + 1
time.sleep(0.5)
if acess_type == 'denied':
    print('You had too many guesses.')
elif acess_type == 'decoy':
    print('''Here is the secret diary:
Ghjshdgcuyewfgerfiukeryi!''')
else:
    op = input('''What would you like to do?
    (1) write in diary
    (2) read the diary ''')
    if op == '1':
        print('You want to write in the diary!')
        diary_entry = input('What do you want to write in your diary? ')
        diary = open('secret_diary.txt', 'a')
        diary_entry = diary_entry +'\n'
        diary.write(diary_entry)
        diary.close()
    elif op == '2':
        print('You want to read the diary!')
        diary = open('secret_diary.txt', 'r')
        print(diary.read().strip())
        diary.close()
    else:
        print('Not an option...try again.')
        

