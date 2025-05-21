print('''Welcome to JKNS Ticket Booking Portal



      ''')
print("Login or Registration")
print('''1.Login
2.Register''')
ch=int(input("Enter Your Choice:"))
if ch==1:
      print('''


            Welcome! To Kevin's Login Portal''')
      print("******LOGIN******")
      a=input('Enter your Username:')
      b=input('Enter password:')
      c=input('Re-Enter password for confirmation:')
      if b==c:
            print('Confirmed')
            
      else:
            print('Password is wrong')
            print('Run from Start again')
            exit()
      print('--------CAPTCHA------------')
      import random
      d=random.randint(10000,100000)
      print(d)
      e=int(input('Enter the above number:'))
      if d==e:
            print('\tNot a Bot')
      else:
            print('Restart')
            exit()
      print('--------Destination and Return----------')
      ql=input("Enter From Destination:") 
      f=input('Enter To destination:')
      print('Enter 1 if Return Ticket wanted')
      print('Enter 2 to Continue')
      g=int(input('Enter valid choice:'))
      if g==1:
            print('Opted for return ticket')
            h=input('Enter return destination:')
      elif g==2:
            print('***DISCLAIMER***')
            print('No return Ticket wanted')
      else:
            exit()
      if g==1:
            print('Date of travelling, Date of return(For e.g : 12 09 22)')
            i=input('Enter date of travelling in above format:')
            j=input('Enter date of return in above format:')
            print("Date of travelling:",i,", Date of return:",j)
            print('Enter Confirm for proceeding')
            k=input()
      elif g==2:
            print('Date of travelling(For e.g : 12 09 22)')
            i=input('Enter date of travelling in above format:')
            print("Date of travelling:",i)
            print('Enter Confirm for proceeding')
            k=input()

if ch==2:
      print("Welcome! To Shravan's New User Registration Portal")
      l=input("Enter username:")
      m=input("Enter password:")
      n=input("Enter confirmed password:")
      if m==n:
          print("confirmed")
      else:
          print("wrong password")
          print("run from start")
      print("--------CAPTCHA------------")
      import random
      o=random.randint(10000,100000)
      print(o)
      p=int(input("Enter the above numbers:"))
      if o==p:
            print("\tNot a bot")
      else:
            print("restart")
            exit()
      q=input("Enter name:")
      r=input("Enter date of birth:")
      print("Martial Status:")
      print("Enter 1 if married")
      print("Enter 2 if not married")
      y=int(input("Enter valid choice:"))
      if y==1:
            print("Married")
      elif y==2:
            print("Not Married")
      else:
            exit()
      g=input("Enter Email id:")
      m=input("Enter Mobile Number:")
      if len(m)==10:
            print("Mobile Number is valid")
      else:
            print("Mobile Number is invalid")
            exit()
      n=input("Enter Nationality:")
      print("Address:")
      print("Enter 1 if Residential")
      print("Enter 2 if Corporate")
      w=int(input("enter valid choice:"))
      if w==1:
            print("Residental")
            t=input("Enter the address in one line:")
      elif w==2:
            print("Corporate")
            t=int("Enter the address in one line:")
      else:
            exit()
      print("------OTP------")
      import random
      u=random.randint(10000000,100000000)
      print(u)
      v=int(input("Enter the above numbers:"))
      if u==v:
            print("OTP confirmed")
            print("Registration Completed, Please Login")
      else:
            print("Failed to Register")
            exit()
      print('''


Welcome! To Kevin's Login Portal''')
      print("******LOGIN******")
      a=input('Enter your Username:')
      b=input('Enter password:')
      c=input('Re-Enter password for confirmation:')
      if b==c:
            print('Confirmed')
            
      else:
            print('Password is wrong')
            print('Run from Start again')
            exit()
      print('--------CAPTCHA------------')
      import random
      d=random.randint(10000,100000)
      print(d)
      e=int(input('Enter the above number:'))
      if d==e:
            print('\tNot a Bot')
      else:
            print('Restart')
            exit()
      print('--------Destination and Return----------')
      ql=input("Enter From Destination:") 
      f=input('Enter To destination:')
      print('Enter 1 if Return Ticket wanted')
      print('Enter 2 to Continue')
      g=int(input('Enter valid choice:'))
      if g==1:
            print('Opted for return ticket')
            h=input('Enter return destination:')
      elif g==2:
            print('***DISCLAIMER***')
            print('No return Ticket wanted')
      else:
            exit()
      if g==1:
            print('Date of travelling, Date of return(For e.g : 12 09 22)')
            i=input('Enter date of travelling in above format:')
            j=input('Enter date of return in above format:')
            print("Date of travelling:",i,", Date of return:",j)
            print('Enter Confirm for proceeding')
            k=input()
      elif g==2:
            print('Date of travelling(For e.g : 12 09 22)')
            i=input('Enter date of travelling in above format:')
            print("Date of travelling:",i)
            print('Enter Confirm for proceeding')
            k=input()






print("\n\n\n******Welcome! To Niranjan's Ticket Booking System******")
print("1.Check PNR status")
print("2.Ticket Reservation")
option = int(input("Enter your option : "))

if option == 1:
    print("Your PNR Status is t2")
    print("Your PNR NO. is:988829AE2")
    exit()

elif option == 2:
    people = int(input("\nEnter no. of Ticket you want : "))
    name_l = []
    age_l = []
    sex_l = []
    classt_l=[]
    coach_l=[]
    train_l=[]
    phone_l=[]
    email_l=[]

for p in range(people):
    name = str(input("Name:"))
    name_l.append(name)
    age  = int(input("Age:"))
    age_l.append(age)
    sex  = str(input("Male or Female:"))
    sex_l.append(sex)
    classt=str(input("Enter the class you want to travel(first class or second class or sleeper or seating):"))
    if classt in ("first","second","SLEEPER","FIRST CLASS","SECOND CLASS","FIRST","SECOND","Sleeper","sleeper","first class","First Class","First class","second class","Second class","Second Class","Seating","SEATING","seating","Seating"):
        types=input("Enter which type you want?ac or non-ac:")
        if types in ("Ac","ac","AC"):
            print("You have chosen AC Sleeper")
        else:
            print("You have chosen Non-AC Sleeper")
    classt_l.append(classt)
                        
    train=str(input("Enter the train you want to travel to:"))
    train_l.append(train)
    if classt=="first" or "first class" or "First Class"or "First class" or "FIRST" or "FIRST CLASS":
          print("A1","A2","A3","A4","A5","A6",'a1','a2','a3','a4','a5','a6')
          coach=i=str(input("Enter the coach you want to travel:"))
          print("____You have chosen A-coach______")
          coach_l.append(coach)
    elif classt=="second" or "second class" or "Second class" or "Second Class" or "SECOND" or "SECOND CLASS":
          print('B1','B2','B3','B4','B5','B6','b1','b2','b3','b4','b5','b6')
          coach=i=str(input("Enter the coach you want to travel:"))
          print("____You have chosen B-coach______")
    elif classt=="Sleeper" or "sleeper" or "SLEEPER":
          print('C1','c1','C2','c2','C3','c3','C4','c4','C5','c5','C6','c6')
          coach=i=str(input("Enter the coach you want to travel:"))
          print("____You have chosen C-coach______")
    elif classt=="Seating" or "SEATING" or "seating":
          print('D1','d1','d2','D2','d3','D3','D4','d4','d5','D5','D6','D7')
          coach=i=str(input("Enter the coach you want to travel:"))
          print("____You have chosen D-coach______")
    phone=int(input("Enter your Phone Number:"))
    phone_l.append(phone)
    email=input("Enter your email:")
    email_l.append(email)
    y=input("Travel Insurance is available...Do want it?:")
    if y in('y','YES','yes','Yes'):
        print("Thank you..,Your Travel insurance is availed")
    else:
        print("No Travel Insurance is availed")

print("The Entered details for the ticket are below:")         
print("\nTotal Ticket:  ",people)
if coach in ("A1","A2","A3","A4","A5","A6",'a1','a2','a3','a4','a5','a6'):
    ticket_sum=people*1000
elif coach in ('B1','B2','B3','B4','B5','B6','b1','b2','b3','b4','b5','b6'):
    ticket_sum=people*500
elif coach in ('C1','c1','C2','c2','C3','c3','C4','c4','C5','c5','C6','c6'):
    ticket_sum=people*250
elif coach in ('D1','d2','D2','d1','d3','D3','D4','d4','d5','D5','D6','D7'):
    ticket_sum=people*125
x=0
for p in range(1,people+1):
      print("Ticket:            ",p)
      print("Name:            ",name_l[x])
      print("Age:             ",age_l[x])
      print("Sex:             ",sex_l[x])
      print("Class:           ",classt_l[x])
      print("Train Choosed:   ",train_l[x])
      print("Phone No:        ",phone_l[x])
      print("Email Id:        ",email_l[x])
      print("Coach preferred: ",coach_l[x])
      print("\n\nTotal Cost of Tickets:  ",ticket_sum)





print("\n\n\n\n******Welcome to Jishnu's Payment Gateway******")
payment_options=print('''1.Pay through Credit & Debit Cards / Net Banking / Wallets
2.Pay through BHIM/UPI''')
option_selected=int(input("Enter Your Choice(1 or 2) through which you want to pay:"))

if option_selected==1:
    print('''\n\n\n1.Netbanking 
2.Credit Card or Debit Card
3.Wallets''')
    opt=int(input("Enter Your Choice(1 or 2 or 3) through which you want to pay:"))
    if opt==1:
        print("\n\nYou have chose to pay via Netbanking")
        bank_name=input("Enter the bank name:")
        user_name=input("Enter the user name:")
        pass_word=input("Enter the password:")
        import random
        y=random.randint(10000000,100000000)
        print(y)
        z=int(input('Enter the above OTP number:'))
        if y==z:
              print('\tNot a Bot')
        else:
              print('Restart')
              exit()
        confirmation=input("Enter C to confirm or N to cancel:")
        if confirmation=="C" or confirmation=="c":
            print("Ticket Confirmed.Check Your registered mail id for the ticket.")
        else:
            print("Ticket has been cancelled.")
            exit()
    elif opt==2:
        print("\n\nYou have chose to pay through Debit Card or Credit Card")
        card_number=input("Enter the card number(16 digits):")
        if len(card_number)==19:
            print("Card number exists.")
        else:
            print("Card number does not exist")
            exit()
        card_name=input("Enter the Name as per card:")
        expiry_month=input("Enter the Expiry Month(mm):")
        if len(expiry_month)==2:
            print("Month Exists")
        else:
            print("Month entered is wrong")
            exit()
        expiry_year=input("Enter the Expiry Year(yy):")
        if len(expiry_year)==2:
            print("Year Exists")
        else:
            print("Year entered is wrong")
            exit()
        cvv=input("Enter the CVV number on the backside of your card(3 digits):")
        if len(cvv)==3:
            print("CVV entered is correct")
        else:
            print("CVV entered is out of range")
            exit()
        w=random.randint(10000000,100000000)
        print(d)
        x=int(input('Enter the above OTP number:'))
        if w==x:
              print('\tNot a Bot')
        else:
              print('Restart')
              exit()
        confirmation=input("Enter C to confirm or N to cancel:")
        if confirmation=="C" or confirmation=="c":
            print("Ticket Confirmed.Check Your registered mail id for the ticket.")
        else:
            print("Ticket has been cancelled.")
            exit()
    elif opt==3:
        print("\n\nYou have chose to pay through Wallet")
        payment_via=("1.Phonepay,        2.Airtel Money")
        option=int(input("Enter your option(1 or 2) through which you want to pay:"))
        if option==1:
            print("\n1.Phonepay")
            paynumber=input("Enter the mobile number through which you want to pay:")
            if len(paynumber)==10:
                print("Phone number exists")
            else:
                print("Phone number does not exist")
                exit()
            otp=input("Enter the One Time Password sent to your registered mobile number with your account(8 digits):")
            if len(otp)>8:
                print("OTP number is incorrect")
            else:
                print("OTP number is correct")
                exit()
            m_digit=input("Enter the m-digit(4 or 6)")
            if m_digit==4 or m_digit==6:
                print("Entered m-digit is correct")
            else:
                print("Entered m-digit is incorrect")
                exit()
            confirmation=input("Enter C to confirm or N to cancel:")
            if confirmation=="C" or confirmation=="c":
                print("Ticket Confirmed.Check Your registered mail id for the ticket.")
            else:
                print("Ticket has been cancelled.")
                exit()
        elif option==2:
            print("\n1.Airtel Money")
            paynumber=input("Enter the mobile number through which you want to pay:")
            if len(paynumber)==10:
                print("Phone number exists")
            else:
                print("Phone number does not exist")
                exit()
            otp=input("Enter the One Time Password sent to your registered mobile number with your account(8 digits):")
            if len(otp)>8:
                print("OTP number is incorrect")
            else:
                print("OTP number is correct")
                exit()
            m_digit=input("Enter the m-digit(4 or 6)")
            if m_digit==4 or m_digit==6:
                print("Entered m-digit is correct")
            else:
                print("Entered m-digit is incorrect")
                exit()
            confirmation=input("Enter C to confirm or N to cancel:")
            if confirmation=="C" or confirmation=="c":
                print("Ticket Confirmed.Check Your registered mail id for the ticket.")
            else:
                print("Ticket has been cancelled.")
                exit()



elif option_selected==2:
    print("\n\n\n2.Pay through BHIM/UPI")
    print("1. Phonepay          2.Googlepay       3.Paytm")
    py=int(input("Enter the option(1 or 2 or 3) through which you want to pay:"))
    if py==1:
        print("\n\n1.Phonepay")
        payid=input("Enter the email id(email@okbankname) through which you want to pay:")
        print("Click on the notification just appeared in the phone by googlepay app")
        print("Open your samrtphone and go the respective app")
        print("Enter the app password")
        print("Select the bank acoount through which you want to pay")
        print("Enter the m-digit accordingly")
        print("Press OK")
        confirmation=input("Enter C to confirm or N to cancel:")
        if confirmation=="C"or confirmation=="c":
            print("Ticket Confirmed.Check Your registered mail id for the ticket.")
        else:
            print("Ticket has been cancelled.")
            exit()
    if py==2:
        print("\n\n2.Googlepay")
        payid=input("Enter the email id(email@okbankname) through which you want to pay:")
        print("Click on the notification just appeared in the phone by phonepay app")
        print("Open your samrtphone and go the respective app")
        print("Enter the app password")
        print("Select the bank acoount through which you want to pay")
        print("Enter the m-digit accordingly")
        print("Press OK")
        confirmation=input("Enter C to confirm or N to cancel:")
        if confirmation=="C" or confirmation=="c":
            print("Ticket Confirmed.Check Your registered mail id for the ticket.")
        else:
            print("Ticket has been cancelled.")
            exit()
    if py==3:
        print("\n\n3.Paytm")
        payid=input("Enter the email id(email@okbankname) through which you want to pay:")
        print("Click on the notification just appeared in the phone by googlepay app")
        print("Open your samrtphone and go the respective app")
        print("Enter the app password")
        print("Select the bank acoount through which you want to pay")
        print("Enter the m-digit accordingly")
        print("Press OK")
        confirmation=input("Enter C to confirm or N to cancel:")
        if confirmation=="C" or confirmation=="c":
            print("Ticket Confirmed.Check Your registered mail id for the ticket.")
        else:
            print("Ticket has been cancelled.")
            exit()
