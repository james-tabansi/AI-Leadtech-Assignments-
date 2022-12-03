#!/usr/bin/env python
# coding: utf-8

# In[25]:


class Olympus_Bank:
    trials = 1
    def __init__(self, name, acct_balance, pin = None):
        self.name = name
        self.acct_balance = acct_balance
        self.pin = None
        self.log_in_trials = 0
    
    def new_user(self):
        """navigation to main menu, new users to set new pin and old users to reset pin"""
        
        print('*'*10, f'Dear {self.name} Welcome to Olympus', '*'*10)
        
        print('select an option that applies: ')
        
        act = int(input('1. Set first time Pin\n2. Proceed to main menu\n3. Reset Pin\n\n'))
        while act not in range(1,4):
            print('Invalid option selected')
            act = int(input('1. Set first time Pin\n2. Proceed to main menu\n3. Reset Pin\n\n'))
        
        if act == 1:
            #new user to set pin
            self.set_new_pin()
            
        elif act == 2:
            
            #this is for old users only, new users always have pin attribute set as None
            #first check if user is new and not old and redirect to set new pin instead
            if self.pin == None:
                print(f'Dear {self.name}, you are a new user, please proceed to set new pin instead')
                self.new_user()
                
            else:
            #if user is old, display menu
                self.display_menu()
                
                
        elif act == 3:
            #this is for old users only, 
            #first check if user is new and not old and redirect to set new pin instead
            if self.pin == None:
                print(f'Dear {self.name}, you are a new user, please proceed to set new pin instead')
                self.new_user()
            else:
            #if user is old, reset pin
                self.reset_pin()
            
            
        
    def set_new_pin(self):
        """stores the new pin as an attribute of the object"""
    
    
    #check if user is new, new users always have pin attribute set as None
        if self.pin == None:
            pin1 = int(input('Enter your new pin: '))
            pin2 = int(input('Repeat your new pin: '))
            
            #ensure pin correctness
            if pin1 == pin2:
                
                #store the new pin as the attribute of the object
                self.pin = pin1
                print('Pin successfully created, proceed to sign in\n\n')
                
                #return back
                self.new_user()
                
            else:
                print('pin does not match, please retry')
                self.set_new_pin()
        
        #if user is an old user, advice to reset pin instead
        else:
            print(f'Dear {self.name}, you are an existing user, please proceed to reset pin instead')
            self.new_user()
            
            
    def reset_pin(self):
        """resets the initial pin to a newer pin and stores the pin as an attribute of the object"""
    
    #check if user is new, new users always have pin attribute set as None
        if self.pin != None:
            pin1 = int(input('Enter your new pin: '))
            pin2 = int(input('Repeat your new pin: '))
            
            #check for correctness
            if pin1 == pin2:
                self.pin = pin1
                print('Pin successfully created, proceed to sign in\n\n')
                self.new_user()
                
            else:
                print('pin does not match, please retry')
                self.reset_pin()
                
    #if user is a new user, advice to set new pin instead
        else:
            print(f'Dear {self.name}, you are a new user, please proceed to set new pin instead')
            self.set_new_pin()
    
    
    
    def display_menu(self):
        """returns the menu every time the method is called, after verifying the user's pin."""
        status = False
        while self.log_in_trials < 3 and status == False:
            
            #input pin
            verify_pin = int(input("Enter your pin: \n\n")) 
            
            
        #pin verification, set to block pin after 3 succesive failed attempts by increasing self.log_in_trials
            if verify_pin != self.pin:
                print("Incorrect Pin, Enter the correct Pin")
                self.log_in_trials += self.trials
                if self.log_in_trials == 3:
                    print('Account Blocked due to Invalid Password entered, contact your Bank')
                    self.exit()
                    
                    
        #pin verification, display menu when pin is correct and break the loop by making status to be True
            elif verify_pin == self.pin:
                print('Pin OK')
                status = True
                self.log_in_trials = 0
                print('*'*10, f'Dear {self.name} Welcome to Olympus', '*'*10)
                print('*'*10, 'MAIN MENU','*'*10,'\n1. Check Balance\n2. Deposit\n3. Withdrawal\n4. Exit')
                action = int(input('select an option that applies: \n'))
                
                
        #navigation block
        
                #if input is not from range 1-4, loop continuously to get the right input
                while action not in range(1,5):
                    print('Invalid option selected')
                    action = int(input('select an option that applies: \n'))
                    
                if action == 1:
                #check balance
                    self.check_balance()
                    
                elif action == 2:
                #deposit
                    self.deposit()
                    
                elif action == 3:
                #withdrawal
                    self.withdrawal()
                    
                elif action == 4:
                #exit
                    self.exit()
                    
    
        
    
    def check_balance(self):
        """returns the available balance of the customer"""
        
        print(f'Dear {self.name}, your account balance is {self.acct_balance}')
        
    #option to return to main menu or exit
        go_back = int(input("Select an option \n 1. Go back to Main Menu\n 2. Exit\n\n"))
        
    
    #if input is not from range 1-3, loop continuously to get the right input
        while go_back not in range(1,3):
            print('Invalid option selected')
            go_back = int(input("Select an option \n 1. Go back to Main Menu\n 2. Exit\n\n"))
            
        if go_back == 1:
            #main menu
            self.display_menu()
        elif go_back ==2:
            #exit
            self.exit()

        
    def deposit(self):
        """accepts money from customers and returns an increased account balance by the value deposited"""
        
        #collect deposit amount and increase balance
        value = int(input('How much would you like to deposit: '))
        self.acct_balance += value
        
        print('Successful Deposit, your account balance is $'+str(self.acct_balance))
        
        #option to return to main menu or exit
        go_back = int(input("Select an option \n 1. Go back to Main Menu\n 2. Exit\n\n"))
        
        #if input is not from range 1-3, loop continuously to get the right input
        while go_back not in range(1,3):
            print('Invalid option selected')
            go_back = int(input("Select an option \n 1. Go back to Main Menu\n 2. Exit\n\n"))
            
        if go_back == 1:
            #main menu
            self.display_menu()
        elif go_back ==2:
            #exit
            self.exit()
        
    
    def withdrawal(self):
        """dispense money to customers and returns an decreased account balance by the value withdrawn"""
        
    #amount to be collected
        value = int(input('How much would you like to withdraw: '))
        
        #check for sufficient funds
        if value > self.acct_balance or self.acct_balance == 0:
            print('Insufficient Balance')
            
            #opportunity to retry withdrawal operation if wrong amount was inputed
            try_again = int(input('Opertaion Unsuccessful, would you like to try again?\n 1. Yes\n 2. No'))
            if try_again == 1:
                self.withdrawal()
            
            elif try_again == 2:
                self.exit()
                
        #check for sufficient funds     
        elif value < self.acct_balance:
            self.acct_balance -= value
            print('Successful Withdrawal, your account balance is $' + str(self.acct_balance))
            
            
            #option to return to main menu or exit
            go_back = int(input("Select an option \n 1. Go back to Main Menu\n 2. Exit\n\n"))
            
             #if input is not from range 1-3, loop continuously to get the right input
            while go_back not in range(1,3):
                print('Invalid option selected')
                go_back = int(input("Select an option \n 1. Go back to Main Menu\n 2. Exit\n\n"))
            
            if go_back == 1:
                #main menu
                self.display_menu()
            elif go_back ==2:
                #exit
                self.exit()
        
    
    def exit(self):
        """terminates the code"""
        print(f"Thanks for your patronage, {self.name}, Please collect your card")
        pass
        
        
        
        
User1 = Olympus_Bank('James Tabansi', 0)
User1.new_user()


# In[ ]:




