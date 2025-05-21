import tkinter as tk 
from tkinter import ttk 
from tkinter import * 
from tkinter.messagebox import showinfo 
import mysql.connector as connect 
import random
import json 
import os
from datetime import datetime
from datetime import date
import calendar
from  sqlconnect  import  cursor, db

root=tk.Tk()
root.title('Jishnu Train Ticket Booking App!') 
root.geometry("600x600") 
root['background']='#FF4040' 
root.resizable(True,True)
bgimg=  tk.PhotoImage(file="bg.png") 
limg= tk.Label(root, i=bgimg,bg="#FF4040") 
limg.pack()


def mainMenu():
    label1 = tk.Label(root, text = "WELCOME TO RAILWAY RESERVATION SYSTEM!!",font=('Algerian', 12),bg="#FF4040").pack()
    button1 = tk.Button(root, text="1. ADMIN MODE",command=adminMode,font=('Lucida Handwriting', 10),bg="#FF4040").pack()
    button2 = tk.Button(root, text="2. USER MODE",command=userMode,font=('Lucida Handwriting', 10),bg="#FF4040").pack()
    button3  =  tk.Button(root, text="3.EXIT",command=destroy1,font=('Lucida Handwriting', 10),bg="#FF4040").pack()

def destroy1(): 
    root.destroy()

def destroy2(): 
    admin.destroy()
    root.destroy()

def adminMode(): 
    global admin
    admin=tk.Toplevel()
    admin.title("Admin Mode")
    admin.geometry("600x600") 
    admin.resizable(True,True)
    admin['background']='#CDCD00'
    label3 = tk.Label(admin, text = "WELCOME TO ADMIN MODE!!",font=('Lucida Handwriting', 12),bg="#8B8B00").pack()
    button9 = tk.Button(admin, text="1. Add a Train",command=addtrain,font=('Impact', 10),bg="#FFFF00").pack()
    button10 = tk.Button(admin, text="2. Assign Seats",command=assignSeats,font=('Impact', 10),bg="#FFFF00").pack()
    button11 = tk.Button(admin, text="3. Add Train Route",command=addRouteDetails,font=('Impact', 10),bg="#FFFF00").pack()
    button12 = tk.Button(admin, text="4. Reservation Chart",command=reservationChart,font=('Impact', 10),bg="#FFFF00").pack()
    button13 = tk.Button(admin, text="5. Delete a Train",command=deleteTrain,font=('Impact', 10),bg="#FFFF00").pack()
    button14 = tk.Button(admin, text="6. Exit",command=destroy2,font=('Impact', 10),bg="#FFFF00").pack()


def addtrain():
    global add
    add=tk.Toplevel()
    add.title("Add Train")
    add.geometry("600x600") 
    add.resizable(True,True)
    add['background']='#FFD39B'
    m1=tk.StringVar()
    m2=tk.StringVar()
    m3=tk.StringVar()
    a1=tk.Label(add,text="Enter Train No: ",font=('Calibri', 10),bg="#CDAA7D").pack()
    e1=tk.Entry(add,textvariable=m1).pack()
    a2=tk.Label(add,text="Enter Train Name: ",font=('Calibri', 10),bg="#CDAA7D").pack()
    e2=tk.Entry(add,textvariable=m2).pack()
    a3=tk.Label(add,text="Enter running days seperated by comma(e.g. Monday,Wednesday): ",font=('Calibri', 10),bg="#CDAA7D").pack()
    e2=tk.Entry(add,textvariable=m3).pack()
    g1=tk.Button(add,text='Enter',command=lambda:creating_train(m1,m2,m3)).pack()


def creating_train(m1,m2,m3):
    p1=m1.get()
    p2=m2.get()
    p3=m3.get()
    running_days_list = str(p3.split(","))
    cursor.execute("SELECT * from trains;")
    table_names = [i[0] for i in cursor.fetchall()]
    if p1 not in table_names:
        p1=int(p1)
        add_train_sql = '''CREATE TABLE IF NOT EXISTS `%s`(
            `id` INT(11) NOT NULL AUTO_INCREMENT,
            `station_code` VARCHAR(255) NOT NULL,
            `station_name` VARCHAR(255) NOT NULL,
            `arrival` TIME NOT NULL,
            `departure` TIME NOT NULL,
            PRIMARY KEY (`id`)
        )'''
        cursor.execute(add_train_sql, (p1,))
        cursor.execute("INSERT INTO trains(train_no,train_name,running_days,coaches) VALUES(%s,%s,%s,'later')",(p1,p2,running_days_list,))
        db.commit()
        t10=("Sucessfully Updated!")
        tk.Label(add,text=t10,font=('Calibri', 10),bg="#CDAA7D").pack()
        tk.Button(add,text="Exit",command=lambda:destroy13()).pack()

def destroy13():
    add.destroy()

def assignSeats():
    global ass
    ass=tk.Toplevel()
    ass.title("Assign Seats")
    ass.geometry("600x600") 
    ass.resizable(True,True)
    ass['background']='#98F5FF'
    m4=tk.StringVar()
    a4=tk.Label(ass,text="Enter train number to assign seats:",font=('Calibri', 14),bg="#53868B").pack()
    e4=tk.Entry(ass,textvariable=m4).pack()
    g4=tk.Button(ass,text='Enter',command=lambda:assigning(m4)).pack()

def assigning(m4):
    train_no=m4.get()
    train_no=int(train_no)
    tk.Label(ass,font=('Calibri', 12),bg="#98F5FF").pack()
    tk.Label(ass,text="All Coaches Should have the Same Values!!",font=('Calibri', 12),bg="#53868B").pack()
    m5=tk.StringVar()
    tk.Label(ass,font=('Calibri', 12),bg="#98F5FF").pack()
    a5=tk.Label(ass,text="Enter no of coaches of SL:",font=('Calibri', 10),bg="#53868B").pack()
    e5=tk.Entry(ass,textvariable=m5).pack()
    m6=tk.StringVar()
    a6=tk.Label(ass,text="Enter no of coaches of 2A:",font=('Calibri', 10),bg="#53868B").pack()
    e6=tk.Entry(ass,textvariable=m6).pack()
    m7=tk.StringVar()
    a7=tk.Label(ass,text="Enter no of coaches of 3A:",font=('Calibri', 10),bg="#53868B").pack()
    e7=tk.Entry(ass,textvariable=m7).pack()
    g20=tk.Button(ass,text='Enter',command=lambda:updating_assigned(m4,m5,m6,m7)).pack()

def updating_assigned(m4,m5,m6,m7):
    dict={}
    train_no=m4.get()
    sleeper=m5.get()
    second_ac =m6.get()
    third_ac =m7.get()
    dict = {"2A":int(second_ac),"3A":int(third_ac),"SL":int(sleeper)}
    cursor.execute("UPDATE `trains` SET coaches = %s WHERE train_no = %s",(str(dict),train_no))
    db.commit()
    tk.Label(ass,font=('Calibri', 12),bg="#98F5FF").pack()
    tk.Label(ass,text="Sucessfully Updated!",font=('Calibri', 12),bg="#53868B").pack()
    tk.Button(ass,text="Exit",command=destroy3).pack()

def destroy3():
    ass.destroy()

def addRouteDetails():
    global addr
    addr=tk.Toplevel()
    addr.title("Add Route Details")
    addr.geometry("600x600") 
    addr.resizable(True,True)
    addr['background']='#7FFF00'
    m13=tk.StringVar()
    a13=tk.Label(addr,text="Enter Train No: ",font=('Calibri', 12),bg="#458B00").pack()
    e13=tk.Entry(addr,textvariable=m13).pack()
    g39=tk.Button(addr,text="Enter",command=lambda:adding_route_details(m13)).pack()
    
def adding_route_details(m13):
    global p13
    p13=m13.get()
    cursor.execute("use rrs;")
    cursor.execute("show tables;")
    c=cursor.fetchall()
    if (p13,) in c:
        p13=int(p13)
        m14=tk.StringVar()
        a14=tk.Label(addr,text="Enter the station code:",font=('Calibri', 10),bg="#458B00").pack()
        e14=tk.Entry(addr,textvariable=m14).pack()
        m15=tk.StringVar()
        a15=tk.Label(addr,text="Enter the station name:",font=('Calibri', 10),bg="#458B00").pack()
        e15=tk.Entry(addr,textvariable=m15).pack()
        m16=tk.StringVar()
        a16=tk.Label(addr,text="Enter the arrival time in HH:MM:SS format:",font=('Calibri', 10),bg="#458B00").pack()
        e16=tk.Entry(addr,textvariable=m16).pack()
        m17=tk.StringVar()
        a17=tk.Label(addr,text="Enter the departure time in HH:MM:SS format:",font=('Calibri', 10),bg="#458B00").pack()
        e17=tk.Entry(addr,textvariable=m17).pack()
        g10=tk.Button(addr,text='Enter',command=lambda:updating_route_details(p13,m14,m15,m16,m17)).pack()
    else:
        tk.Label(addr,text="Incorrect Train Number",font=('Calibri', 10),bg="#458B00").pack()

def updating_route_details(p13,m14,m15,m16,m17):
    p14=m14.get()
    p15=m15.get()
    p16=m16.get()
    p17=m17.get()
    sql = 'INSERT INTO `%s` (station_code,station_name,arrival,departure) VALUES(%s,%s,%s,%s)'
    values = (p13,p14, p15, p16, p17)
    cursor.execute(sql, values)
    db.commit()
    t20=("You have successfully added the route!")
    tk.Label(addr,text=t20,font=('Calibri', 12),bg="#458B00").pack()
    tk.Button(addr,text="Exit",command=destroy4).pack()

def destroy4():
    addr.destroy()
    
def reservationChart():
    global res
    res=tk.Toplevel()
    res.title("Reservation Chart")
    res.geometry("600x600") 
    res.resizable(True,True)
    res['background']='#EEE8CD'
    m45=tk.StringVar()
    a45=tk.Label(res,text="Enter train number:",font=('Calibri', 12),bg="#8B8878").pack()
    e45=tk.Entry(res,textvariable=m45).pack()
    a45=tk.Button(res,text='Enter',command=lambda:reservation_details(m45)).pack()
    
def reservation_details(m45):
    train_no=m45.get()
    l1=('--------------------------------------------------')
    l2=("RESERVATION CHART FOR TRAIN NO. ",train_no)
    l3=("NAME         GENDER    AGE        PNR      BERTH            BOARD          DESTINATION")
    tk.Label(res,text=l1,font=('Calibri', 10),bg="#8B8878").pack()
    tk.Label(res,text=l2,font=('Calibri', 10),bg="#8B8878").pack()
    tk.Label(res,text=l1,font=('Calibri', 10),bg="#8B8878").pack()
    tk.Label(res,text=l3,font=('Calibri', 10),bg="#8B8878").pack()
    tk.Label(res,text=l1,font=('Calibri', 10),bg="#8B8878").pack()
    cursor.execute("SELECT * FROM user_bookings WHERE train_no = %s", (train_no,))
    for l in cursor:
        t=(l[8],"     ",l[10],"   ",l[9],"      ",l[4],"  ",l[6],"      ",l[11],"          ",l[12])
        tk.Label(res,text=t,font=('Calibri', 10),bg="#8B8878").pack()
    tk.Button(res,text="Exit",command=destroy5).pack()

def destroy5():
    res.destroy()

def deleteTrain():
    global dele
    dele=tk.Toplevel()
    dele.title("Delete Train")
    dele.geometry("600x600") 
    dele.resizable(True,True)
    dele['background']='#BF3EFF'
    m55=tk.StringVar()
    a15=tk.Label(dele,text="Enter train number:",font=('Calibri', 12),bg="#68228B").pack()
    e15=tk.Entry(dele,textvariable=m55).pack()
    a16=tk.Button(dele,text='Enter',command=lambda:deleting_train(m55)).pack()

def deleting_train(m55):
    train_no=m55.get()
    train_no=int(train_no)
    cursor.execute("DROP TABLE `%s`;",(train_no,))
    cursor.execute("DELETE FROM trains WHERE train_no = %s;",(train_no,))
    db.commit()
    tk.Label(dele,text="Successfully Deleted!",font=('Calibri', 10),bg="#68228B").pack()
    tk.Button(dele,text="Exit",command=destroy6).pack()

def destroy6():
    dele.destroy()

def userMode():
    global user
    user=tk.Toplevel()
    user.title("User Mode")
    user.geometry("600x600") 
    user.resizable(True,True)
    user['background']='#FF8000'
    label2 = tk.Label(user, text = "WELCOME TO USER MODE!!",font=('Lucida Handwriting', 12),bg="#8B5A00").pack()
    button4 = tk.Button(user, text="1. Book a Ticket",command=book_a,font=('Impact', 10),bg="#8B5A00").pack()
    button5 = tk.Button(user, text="2. PNR Enquiry",command=pnrChecker,font=('Impact', 10),bg="#8B5A00").pack()
    button6 = tk.Button(user, text="3. Cancel Ticket",command=cancelTicket,font=('Impact', 10),bg="#8B5A00").pack()
    button7 = tk.Button(user, text="4. Booking History",command=bookingHistory,font=('Impact', 10),bg="#8B5A00").pack()
    button8 = tk.Button(user, text="5. Exit",command=destroy7,font=('Impact', 10),bg="#8B5A00").pack()

def destroy7():
    user.destroy()
    root.destroy()
    
def book_a():
    global book
    book=tk.Toplevel()
    book.title("Train Finder")
    book.geometry("600x600") 
    book.resizable(True,True)
    book['background']='#548B54'
    m21=tk.StringVar()
    a21=tk.Label(book,text="Type your boarding station code (e.g. ADI):",font=('Calibri', 10),bg="#98FB98").pack()
    e21=tk.Entry(book,textvariable=m21).pack()
    m22=tk.StringVar()
    a22=tk.Label(book,text="Type your destination station code (e.g. CYI): ",font=('Calibri', 10),bg="#98FB98").pack()
    e22=tk.Entry(book,textvariable=m22).pack()
    m23=tk.StringVar()
    a23=tk.Label(book,text="Enter date of journey in YYYY-MM-DD format: ",font=('Calibri', 10),bg="#98FB98").pack()
    e23=tk.Entry(book,textvariable=m23).pack()
    g23=tk.Button(book,text='Enter',command=lambda:booking_findings(m21,m22,m23)).pack()

def booking_findings(m21,m22,m23):
    global p21
    global p22
    global p23
    p21=m21.get()
    p22=m22.get()
    p23=m23.get()
    today = date.today()
    today = str(today)
    if p23 < today:
        print("Incorrect Details")
    journey_day = weekDayFinder(p23)
    trainFinder(p21,p22,journey_day)

def weekDayFinder(journey_date):
    day_name=['Monday','Tuesday','Wednesay','Thursday','Friday','Saturday','Sunday']
    journey_day=datetime.strptime(journey_date, "%Y-%m-%d").weekday()
    return (calendar.day_name[journey_day])

def trainFinder(p21,p22,p23):
    indexBoard = int()
    trains_available = []
    indexDestination = int()
    # MYSQL Queries
    cursor.execute("SELECT * FROM trains;")
    table_names = [i[0] for i in cursor.fetchall()]

    #table_names contain all the table in the rrs database. rrs = railway reservation system

    for j in range(len(table_names)):
        if table_names[j] != "trains" and table_names[j] != "user_bookings":
            cursor.execute("SELECT * FROM `trains`;")
            train_no_list = [x[0] for x in cursor.fetchall()]
            for y in range(len(train_no_list)):
                cursor.execute("SELECT running_days FROM `trains` WHERE train_no = %s", (table_names[j],))
                running_days = cursor.fetchone()[0]
                break
            if p23 in running_days:
                #MySQL query to get the list of all the station codes for each train
                cursor.execute("SELECT station_code FROM `%s`", (table_names[j],))
                routeList = [k[0] for k in cursor.fetchall()]

                #check if any of the station code matches with boarding station
                for l in range(len(routeList)):
                    if routeList[l] == p21:
                        #indexBoard stores the index of the station code when it's equal to boarding station
                        indexBoard = routeList.index(routeList[l])
                for m in range(len(routeList)):
                    if routeList[m] == p22:
                        #indexBoard stores the index of the station code when it's equal to destination station
                        indexDestination = routeList.index(routeList[m])
                        break
                if indexBoard < indexDestination:
                    trains_available.append(table_names[j])

    if trains_available != []:
        for trainNo in range(len(trains_available)):
            cursor.execute("SELECT train_name FROM trains WHERE train_no = %s", (trains_available[trainNo],))
            row1 = cursor.fetchall()
            cursor.execute("SELECT arrival FROM `%s` WHERE station_code = %s",
                                   (int(trains_available[trainNo]), p21))
            row2 = cursor.fetchall()
            cursor.execute("SELECT arrival FROM `%s` WHERE station_code = %s",
                                   (int(trains_available[trainNo]), p22))
            row3 = cursor.fetchall()
            q=(str(trainNo + 1),". Train No: ",str(trains_available[trainNo])," Train Name: ",row1,"  Boarding Arrival Time: ",row2,"  Destination Arrival Time: ",row3)
            tk.Label(book,text=q,font=('Calibri', 10),bg="#98FB98").pack()
            tk.Button(book,text="Book Ticket",command=lambda:bookTicket(p21,p22,p23)).pack()
            tk.Button(book,text="Exit",command=lambda:destroy12()).pack()
            
    else:
        tk.Label(book,text="No Train Found!",font=('Calibri', 10),bg="#98FB98").pack()
        tk.Button(book,text="Exit",command=lambda:destroy12()).pack()

def destroy12():
    book.destroy()
    user.destroy()

def bookTicket(p21,p22,p23):
    global booka
    booka=tk.Toplevel()
    booka.title("Book A Ticket")
    booka.geometry("600x600") 
    booka.resizable(True,True)
    booka['background']='#8B2252'
    a80=tk.Label(booka,text="Enter the train number to book: ",font=('Calibri', 10),bg="#EE82EE").pack()
    m80=tk.Entry(booka)
    m80.pack()
    a81=tk.Label(booka,text="Enter the coach category(SL,3A,2A): ",font=('Calibri', 10),bg="#EE82EE").pack()
    m81=tk.Entry(booka)
    m81.pack()
    a82=tk.Label(booka,text="Enter passenger name: ",font=('Calibri', 10),bg="#EE82EE").pack()
    m82=tk.Entry(booka)
    m82.pack()
    a83=tk.Label(booka,text="Enter passenger age: ",font=('Calibri', 10),bg="#EE82EE").pack()
    m83=tk.Entry(booka)
    m83.pack()
    a84=tk.Label(booka,text="Enter passenger gender: ",font=('Calibri', 10),bg="#EE82EE").pack()
    m84=tk.Entry(booka)
    m84.pack()
    g80=tk.Button(booka,text="Enter",command=lambda:booking_details(p21,p22,p23,m80,m81,m82,m83,m84)).pack()

def booking_details(p21,p22,p23,m80,m81,m82,m83,m84):
    p80 = m80.get()
    bookTicket_class = m81.get()
    passenger = m82.get()
    passenger= passenger.upper()
    passenger_age = m83.get()
    passenger_gender = m84.get()
    passenger_gender=passenger_gender.upper()
    username="Jishnu"
    cursor.execute("SELECT `coaches` FROM `trains` WHERE train_no = %s", (p80,))
    coach_count = cursor.fetchall()
    v=random.randint(0,101)
    for i in coach_count:
        for j in i:
            v1=j[2:4] #2A
            v2=j[11:13] #3A
            v3=j[20:22] #SL
            count=j[7:8]
            if bookTicket_class == v3:
                berth_class = "S" + str(v + 1)
                booking_status = "CNF/" + str(berth_class) + "/" + str(int(count) + 1) + "/GN"
            elif bookTicket_class == v2:
                berth_class = "B" + str(v + 1)
                booking_status = "CNF/" + str(berth_class) + "/" + str(int(count) + 1) + "/GN"
            elif bookTicket_class == v1:
                berth_class = "A" + str(v + 1)
                booking_status = "CNF/" + str(berth_class) + "/" + str(int(count) + 1) + "/GN"
            else:
                tk.Label(booka,text="Sorry, No seats available!,Please check the coach and try again.").pack()

    # PNR Generate
    pnr = random.randint(10000, 99999)
    
    # Journey Start and End Date Time
    cursor.execute("SELECT arrival FROM `%s` WHERE station_code = %s;", (int(p80),str(p21)))
    start_datetime = str(p23) + " " + str(cursor.fetchone()[0])
    cursor.execute("SELECT arrival FROM `%s` WHERE station_code = %s;", (int(p80), str(p22)))
    end_datetime = str(p23) + " " + str(cursor.fetchone()[0])
    cursor.execute("SELECT train_name FROM `trains` WHERE train_no = %s;",(p80,))
    train_name = cursor.fetchone()[0]
    cursor.execute('INSERT INTO `user_bookings` (username,start_datetime,end_datetime,train_no,pnr,'
                           'booking_status,current_status,class,name,age,gender,board,destination,status,train_name) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"booked",%s)',
                           (username, start_datetime, end_datetime, p80, pnr, booking_status,
                            booking_status, bookTicket_class, passenger, passenger_age, passenger_gender,p21,p22,train_name))
    db.commit()
    z1=("PNR: " + str(pnr))
    cursor.execute("SELECT train_name FROM `trains` WHERE train_no = %s", (p80,))
    train_name = cursor.fetchone()[0]
    z2=("TRAIN NO. " + str(p80) + "\nTRAIN NAME: " + str(train_name))
    z21=("PASSENGER NAME:" + str(passenger))
    z22=("PASSENGER AGE:" + str(passenger_age))
    z23=("PASSENGER GENDER:" + str(passenger_gender))
    z3=("FROM " + str(p21) + " TO " + str(p22))
    z4=("SCH DEP: " + str(start_datetime) + "     SCH ARR: " + str(end_datetime))
    z5=("BOOKING STATUS: " + str(booking_status))
    z6=("Successfully Booked!")
    z7=("-----------------------------------------------")
    z8=("          Ticket Successfully Booked!          ")
    z9=("               Reservation Slip                ")
    z10=("\n")
    list=[str(z7),str(z8),str(z7),str(z9),str(z7),str(z1),str(z2),str(z21),str(z22),str(z23),str(z3),str(z4),str(z5),str(z6),str(z10)]
    with open('ticket.txt', 'w+') as fp:
        fp.write('\n'.join(list))
    tk.Label(booka,text="Please see the text file opened for the ticket!").pack()
    os.startfile("ticket.txt")
    tk.Button(booka,text="Exit",command=lambda:destroy8()).pack()


def destroy8():
    booka.destroy()
    book.destroy()
    
def pnrChecker():
    global pnr
    pnr=tk.Toplevel()
    pnr.title("PNR Checker")
    pnr.geometry("600x600") 
    pnr.resizable(True,True)
    pnr['background']='#8B7B8B'
    m100=tk.StringVar()
    a100=tk.Label(pnr,text="Enter PNR to cancel: ",font=('Calibri', 12),bg="#FFE1FF").pack()
    e100=tk.Entry(pnr,textvariable=m100).pack()
    g100=tk.Button(pnr,text='Enter',command=lambda:pnr_checking(m100)).pack()

def pnr_checking(m100):
    p100=m100.get()
    sql = cursor.execute("SELECT * FROM user_bookings WHERE `pnr` = %s", (p100,))
    l = cursor.fetchall()[0]
    if l[10]=='cancelled':
        tk.Label(pnr,text="Cancelled",font=('Calibri', 10),bg="#FFE1FF").pack()
    else:
        t1=("Train No. ",l[3])
        t2=("FROM " +l[11] + " TO " + l[12])
        t3=("\nPassenger Details:")
        t4=(l[8],"    ",l[9],"     ",l[10])
        t5=("BOOKING STATUS: " + l[5])
        t6=("CURRENT STATUS: " + l[6])
        tk.Label(pnr,text=t1,font=('Calibri', 10),bg="#FFE1FF").pack()
        tk.Label(pnr,text=t2,font=('Calibri', 10),bg="#FFE1FF").pack()
        tk.Label(pnr,text=t3,font=('Calibri', 10),bg="#FFE1FF").pack()
        tk.Label(pnr,text=t4,font=('Calibri', 10),bg="#FFE1FF").pack()
        tk.Label(pnr,text=t5,font=('Calibri', 10),bg="#FFE1FF").pack()
        tk.Label(pnr,text=t6,font=('Calibri', 10),bg="#FFE1FF").pack()
    tk.Button(pnr,text="Exit",command=destroy10).pack()

def destroy10():
    pnr.destroy()

def bookingHistory():
    global bhis
    bhis=tk.Toplevel()
    bhis.title("Booking History")
    bhis.geometry("600x600") 
    bhis.resizable(True,True)
    bhis['background']='#848484'
    cursor.execute("SELECT * FROM `user_bookings`;")
    for l in cursor.fetchall():
        list=[]
        x1=('---------------------------------------------')
        x2=("Booking username:",l[0])
        x3=('---------------------------------------------')
        x4=("Train No. ",l[3])
        x5=("FROM " ,l[11] + " TO " , l[12])
        x6=("Start Date:",l[1])
        x7=("End Date:",l[2])
        x14=("PNR:",l[4])
        x8=("Passenger Details:")
        x9=("Name:",l[8],"     ","Passenger Age:",l[9],"     ","Passenger Gender:",l[10])
        x10=("BOOKING STATUS: " + l[5])
        x11=("CURRENT STATUS: " + l[6])
        x12=("Ticket Status:",l[13])
        x13=("\n")
        list=[str(x1),str(x2),str(x3),str(x4),str(x5),str(x6),str(x7),str(x14),str(x8),str(x9),str(x10),str(x11),str(x12),str(x13)]
        with open('booking history.txt', 'a+') as fp:
            fp.write('\n'.join(list))
    tk.Label(bhis,text="Please see the text file opened!").pack()
    os.startfile("booking history.txt")
    tk.Button(bhis, text="Exit",command=destroy11).pack()

def destroy11():
    bhis.destroy()

def cancelTicket():
    global cancel
    cancel=tk.Toplevel()
    cancel.title("Cancel Ticket")
    cancel.geometry("600x600") 
    cancel.resizable(True,True)
    cancel['background']='#8B4C39'
    m75=tk.StringVar()
    a75=tk.Label(cancel,text="Enter PNR to check: ",font=('Calibri', 10),bg="#FA8072").pack()
    e75=tk.Entry(cancel,textvariable=m75).pack()
    g75=tk.Button(cancel,text='Enter',command=lambda:mysql_train_deletion(m75)).pack()

def mysql_train_deletion(m75):
    p75=m75.get()
    cursor.execute("UPDATE `user_bookings` SET status='Cancelled' WHERE pnr = %s",(p75,))
    cursor.execute("UPDATE `user_bookings` SET current_status='Cancelled' WHERE pnr = %s",(p75,))
    db.commit()
    tk.Label(cancel,text="Ticket successfully cancelled!",font=('Calibri', 10),bg="#FA8072").pack()
    tk.Button(cancel,text="Exit",command=lambda:destroy13()).pack()

def destroy13():
    cancel.destroy()

mainMenu()
root.mainloop()
