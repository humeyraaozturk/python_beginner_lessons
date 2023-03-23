class User():
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

    def login(self):
        username_input = input("Username: ")
        password_input = int(input("Password: "))
        if (username_input == self.username) and (password_input == self.password):
            print("Your account informations are true")
            return 1
        else:
            print("Your account informations are wrong")
            return 0

member1 = User("humeyraaoztrk","humeyra@gmail.com",12345)
member2 = User("wandaaa", "wanda@gmail.com",13579)

class Moderator(User):  #Inheritance
    def __init__(self,username,email,password,api):     #Overriding
        super().__init__(username,email,password)
        #super fonksiyonunu tanımladığımız için User fonksiyonunda verdiğimiz parametreleri
        #tekrar yazmamıza gerek kalmıyor.
        self.api = api

    def panel(self):
        input1 = int(input("Insert your API Key to access to the Admin Panel: "))
        if input1 == self.api:
            print("Access Granted")
            return 1
        else:
            print("Access Denied")
            return 0

    def quit(self):
        quest= input("Do you want to log out? (y/n):")
        if quest == "y":
            passw = int(input("You must confirm your password to log out of the system: "))
            if passw == self.password:
                print("Goodbye")
            else:
                print("Incorrect password. Log out failed.")
        elif quest == "n":
            print("We are happy to see you again")
        else:
            print("Invalide choice")

mod1 = Moderator("istanbul","istanbul@gmail.com",12345, 2002)
result = mod1.login()
if result == 1:
    result2 = mod1.panel()
    if result2 == 1:
        mod1.quit()
else:
    pass


