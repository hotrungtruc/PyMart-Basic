from customtkinter import *
from CTkTable import *
from tkinter import *
from donHang import *
from PIL import Image
import subprocess
import os
import glob
from PIL import Image, ImageTk
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import re


app = CTk()
app.config(bg='black')
set_appearance_mode("dark")
app.geometry("1800x900")
app.resizable(0, 0)
app.title("HỆ THỐNG QUẢN LÝ BÁN HÀNG")




def close_frame(frame):
    frame.destroy()

frames = {}

def create_frame(func):
    def wrapper(*args, **kwargs):
        global frames
        frame_name = func.__name__
        frames[frame_name] = CTkFrame(master=app, fg_color="#111111", width=1350, height=800, corner_radius=0)
        frames[frame_name].pack_propagate(False)
        frames[frame_name].place(relx=0.5, rely=0.5, anchor="center")
        func(frames[frame_name])
    return wrapper

@create_frame
def trangChu(frame):
    CTkLabel(master=frame, text="TRANG CHỦ", font=("Arial Bold", 36),fg_color="transparent", anchor="nw", width=150, height=125).place(relx=0.02, rely=0.13, anchor="w")
    CTkLabel(master=frame, text=f"Số đơn đã bán:\n\n\t{get_bill_count()}", font=("Arial Bold", 36), anchor="w", compound = 'bottom',corner_radius=32, fg_color="#C9A922", width=300, height=250).place(relx=0.03, rely=0.28, anchor="w")
    CTkLabel(master=frame, text=f"Doanh thu đã bán:\n\n\t{get_current_sales():.2f}", font=("Arial Bold", 36), anchor="w", corner_radius=32, fg_color="#FF5353", width=300, height=250).place(relx=0.465, rely=0.28, anchor="center")
    CTkLabel(master=frame, text=f"Số sản phẩm đã bán:\n\n\t{get_total_product()}", font=("Arial Bold", 36), anchor="w", corner_radius=32, fg_color="#4694FF", width=300, height=250).place(relx=0.97, rely=0.28, anchor="e")
    

@create_frame
def donHang(frame):
    headingLabel = Label(frame, text="Retail Billing System", font=("Poppins", 30,'bold'),bg = 'gray20', fg='gold', bd = 12, relief=GROOVE )
    headingLabel.pack(fill=X)
    customer_details_frame = LabelFrame(frame, text= 'Customer Details',font=('Poppins', 15, 'bold'),bg="gray20",
                                        fg="gold", bd =8, relief=GROOVE)
    customer_details_frame.pack(fill=X)

    nameLabel = Label(customer_details_frame, text = "Name",font=('time new roman', 15, 'bold'),bg="gray20", fg='white')
    nameLabel.grid(row = 0, column=0, padx=20, pady=2)

    nameEntry = Entry(customer_details_frame,font=('arial', 15, 'bold'), bd =7, width=15)
    nameEntry.grid(row=0, column=1, padx=8)

    phoneLabel = Label(customer_details_frame, text = "Phone",font=('time new roman', 15, 'bold'),bg="gray20", fg='white')
    phoneLabel.grid(row = 0, column=2, padx=20, pady=2)

    phoneEntry = Entry(customer_details_frame,font=('arial', 15, 'bold'), bd =7, width=15)
    phoneEntry.grid(row=0, column=3, padx=8)

    billNumberLabel = Label(customer_details_frame, text = "Bill Number",font=('time new roman', 15, 'bold'),bg="gray20", fg='white')
    billNumberLabel.grid(row = 0, column=4, padx=20, pady=2)

    billNumberEntry = Entry(customer_details_frame,font=('arial', 15, 'bold'), bd =7, width=15)
    billNumberEntry.grid(row=0, column=5,  padx=8)


    search = Button(customer_details_frame,text = "SEARCH",font=('arial', 10, 'bold'), bd =7, command = lambda:search_bill(billNumberEntry, textarea))
    search.grid(row=0, column=6, padx=10)


    productsFrame = Frame(frame)
    productsFrame.pack()

    close_button = CTkButton(frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")


    AFrame = LabelFrame(productsFrame, text = "",font=('time new roman', 12, 'bold'),bg="gray20", fg='gold', bd =8, relief =GROOVE)
    AFrame. grid(row = 0, column = 0)

    iphoneLabel = Label(AFrame, text = "IPHONE",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    iphoneLabel.grid(row=0, column = 0, pady=9, padx=9)
    iphoneEntry = Entry(AFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    iphoneEntry.grid(row=0, column = 1, pady=9, padx=9)
    iphoneEntry.insert(0,0)
    
    googlephoneLabel = Label(AFrame, text = "GOOGLE PHONE",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    googlephoneLabel.grid(row=1, column = 0, pady=9, padx=9)
    googlephoneEntry = Entry(AFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    googlephoneEntry.grid(row=1, column = 1, pady=9, padx=9)
    googlephoneEntry.insert(0,0)

    vareebaddphoneLabel = Label(AFrame, text = "VAREEBADD PHONE",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    vareebaddphoneLabel.grid(row=2, column = 0, pady=9, padx=9)
    vareebaddphoneEntry = Entry(AFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    vareebaddphoneEntry.grid(row=2, column = 1, pady=9, padx=9)
    vareebaddphoneEntry.insert(0,0)

    macLabel = Label(AFrame, text = "MACBOOK PRO",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    macLabel.grid(row=3, column = 0, pady=9, padx=9)
    macEntry = Entry(AFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    macEntry.grid(row=3, column = 1, pady=9, padx=9)
    macEntry.insert(0,0)

    aaaLabel = Label(AFrame, text = "AAA BATTERIES",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    aaaLabel.grid(row=4, column = 0, pady=9, padx=9)
    aaaEntry = Entry(AFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    aaaEntry.grid(row=4, column = 1, pady=9, padx=9)
    aaaEntry.insert(0,0)

    aaLabel = Label(AFrame, text = "AA BATTERIES",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    aaLabel.grid(row=5, column = 0, pady=9, padx=9)
    aaEntry = Entry(AFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    aaEntry.grid(row=5, column = 1, pady=9, padx=9)
    aaEntry.insert(0,0)





    bFrame = LabelFrame(productsFrame, text = "",font=('time new roman', 12, 'bold'),bg="gray20", fg='gold', bd =8, relief =GROOVE)
    bFrame. grid(row = 0, column = 1)

    usbcLabel = Label(bFrame, text = "USB-C",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    usbcLabel.grid(row=0, column = 0, pady=9, padx=9)
    usbcEntry = Entry(bFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    usbcEntry.grid(row=0, column = 1, pady=9, padx=9)
    usbcEntry.insert(0,0)
    
    whLabel = Label(bFrame, text = "WIRED HEADPHONES",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    whLabel.grid(row=1, column = 0, pady=9, padx=9)
    whEntry = Entry(bFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    whEntry.grid(row=1, column = 1, pady=9, padx=9)
    whEntry.insert(0,0)

    lccLabel = Label(bFrame, text = "CABLE",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    lccLabel.grid(row=2, column = 0, pady=9, padx=9)
    lccEntry = Entry(bFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    lccEntry.grid(row=2, column = 1, pady=9, padx=9)
    lccEntry.insert(0,0)

    BshLabel = Label(bFrame, text = "BOSE SOUNDSPORT",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    BshLabel.grid(row=3, column = 0, pady=9, padx=9)
    BshEntry = Entry(bFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    BshEntry.grid(row=3, column = 1, pady=9, padx=9)
    BshEntry.insert(0,0)

    m20Label = Label(bFrame, text = "20in Monitor",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    m20Label.grid(row=4, column = 0, pady=9, padx=9)
    m20Entry = Entry(bFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    m20Entry.grid(row=4, column = 1, pady=9, padx=9)
    m20Entry.insert(0,0)

    aahLabel = Label(bFrame, text = "AIRPORT",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    aahLabel.grid(row=5, column = 0, pady=9, padx=9)
    aahEntry = Entry(bFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    aahEntry.grid(row=5, column = 1, pady=9, padx=9)
    aahEntry.insert(0,0)






    cFrame = LabelFrame(productsFrame, text = "",font=('time new roman', 12, 'bold'),bg="gray20", fg='gold', bd =8, relief =GROOVE)
    cFrame. grid(row = 0, column = 2)

    tvLabel = Label(cFrame, text = "FLATCREEN TV",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    tvLabel.grid(row=0, column = 0, pady=9, padx=9)
    tvEntry = Entry(cFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    tvEntry.grid(row=0, column = 1, pady=9, padx=9)
    tvEntry.insert(0,0)
    
    m34Label = Label(cFrame, text = "34in MONITOR",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    m34Label.grid(row=1, column = 0, pady=9, padx=9)
    m34Entry = Entry(cFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    m34Entry.grid(row=1, column = 1, pady=9, padx=9)
    m34Entry.insert(0,0)

    gmLabel = Label(cFrame, text = "GAMING MONITOR",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    gmLabel.grid(row=2, column = 0, pady=9, padx=9)
    gmEntry = Entry(cFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    gmEntry.grid(row=2, column = 1, pady=9, padx=9)
    gmEntry.insert(0,0)

    lgdryerLabel = Label(cFrame, text = "LG DRYER",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    lgdryerLabel.grid(row=3, column = 0, pady=9, padx=9)
    lgdryerEntry = Entry(cFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    lgdryerEntry.grid(row=3, column = 1, pady=9, padx=9)
    lgdryerEntry.insert(0,0)

    wmLabel = Label(cFrame, text = "WASHING MACHINE",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    wmLabel.grid(row=4, column = 0, pady=9, padx=9)
    wmEntry = Entry(cFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    wmEntry.grid(row=4, column = 1, pady=9, padx=9)
    wmEntry.insert(0,0)

    thinkpadLabel = Label(cFrame, text = "THINKPAD LAPTOP",font=('time new roman', 12, 'bold'),bg="gray20", fg='white')
    thinkpadLabel.grid(row=5, column = 0, pady=9, padx=9)
    thinkpadEntry = Entry(cFrame,font=('time new roman', 12, 'bold'), width=8, bd =5)
    thinkpadEntry.grid(row=5, column = 1, pady=9, padx=9)
    thinkpadEntry.insert(0,0)

    billframe = Frame(productsFrame, bd =8, relief = GROOVE)
    billframe.grid(row = 0, column = 3, padx =8)

    billareaLabel = Label(billframe, text ="Bill Area", font = ('Poppins', 15, 'bold'),bd =7, relief = GROOVE)
    billareaLabel.pack(fill =X)

    scrollbar = Scrollbar(billframe, orient = VERTICAL)
    scrollbar.pack(side=RIGHT,fill=Y)
    textarea = Text(billframe, height = 18, width =55, yscrollcommand=scrollbar.set)
    textarea.pack()
    scrollbar.config(command=textarea.yview)




    billmenuFrame = LabelFrame(frame, text = "Bill Menu", font =('time new roman', 12, 'bold' ), fg ='gold', bd =8, relief = GROOVE, bg ='gray20')
    billmenuFrame.pack()

    totalLabel = Label(billmenuFrame, text="Total Price" , font=('time new roman', 12, 'bold'),bg="gray20", fg='white', bd =8)
    totalLabel.grid(row = 0, column = 0,pady=9, padx=10, sticky='w')
    totalEntry = Entry(billmenuFrame, font=('time new roman', 15, 'bold'), width =15, bd =7)
    totalEntry.grid(row = 0, column = 1,pady=9, padx=10, sticky='w', rowspan=3)

    tax = Label(billmenuFrame, text=" Tax" , font=('time new roman', 12, 'bold'),bg="gray20", fg='white', bd =8, width=10, height=5)
    tax.grid(row = 0, column = 2,pady=9, padx=10, sticky='w')
    taxentry = Entry(billmenuFrame, font=('time new roman', 15, 'bold'), width =15, bd =7)
    taxentry.grid(row = 0, column = 3,pady=9, padx=10, sticky='w',rowspan=3)   
    
    
    buttonFrame = Frame(billmenuFrame, bd =8, relief=GROOVE)
    buttonFrame.grid(row=0, column=5, rowspan=3)

    totalButton = Button(buttonFrame, command=lambda: total(aaaEntry, aaEntry, usbcEntry, whEntry, lccEntry, BshEntry, m20Entry, aahEntry, tvEntry, m34Entry, gmEntry, vareebaddphoneEntry, googlephoneEntry, lgdryerEntry, wmEntry, iphoneEntry, thinkpadEntry, macEntry, totalEntry,taxentry), text="Total", font=('arial', 16, 'bold'), bg="gray20", fg='white', bd=5, width=8, pady=10)
    totalButton.grid(row=0, column=0, pady=20, padx =35)


    billButton = Button(buttonFrame, text ="Bill", font = ('arial', 16, 'bold'), bg="gray20", fg ='white', bd =5, width =8, pady=10, command =lambda: bill_area(nameEntry, totalEntry, phoneEntry, textarea, aaaEntry, aaEntry, usbcEntry, whEntry, lccEntry, BshEntry, m20Entry, aahEntry, tvEntry, m34Entry, gmEntry, vareebaddphoneEntry, googlephoneEntry, lgdryerEntry, wmEntry, iphoneEntry, thinkpadEntry, macEntry,taxentry))
    billButton.grid(row=0, column=1, pady=20, padx =35)

    printButton = Button(buttonFrame, text ="Print", font = ('arial', 16, 'bold'), bg="gray20", fg ='white', bd =5, width =8, pady=10, command = lambda: print_bill(textarea))
    printButton.grid(row=0, column=2, pady=20, padx =35)



























qty_product = []

def total_product(aaaEntry, aaEntry, usbcEntry, whEntry, lccEntry, BshEntry, m20Entry, aahEntry, tvEntry, m34Entry, gmEntry, vareebaddphoneEntry, googlephoneEntry, lgdryerEntry, wmEntry, iphoneEntry, thinkpadEntry, macEntry):
    global current_qty_product, total
    current_qty_product = (
        int(aaaEntry.get()) +
        int(aaEntry.get()) +
        int(usbcEntry.get()) +
        int(whEntry.get()) +
        int(lccEntry.get()) +
        int(BshEntry.get()) +
        int(m20Entry.get()) +
        int(aahEntry.get()) +
        int(tvEntry.get()) +
        int(m34Entry.get()) +
        int(gmEntry.get()) +
        int(vareebaddphoneEntry.get()) +
        int(googlephoneEntry.get()) +
        int(lgdryerEntry.get()) +
        int(wmEntry.get()) +
        int(iphoneEntry.get()) +
        int(thinkpadEntry.get()) +
        int(macEntry.get()))
    qty_product.append(current_qty_product)
    total = sum(qty_product)
    return total

def get_total_product():
    return sum(qty_product)







current_sales=0
def total(aaaEntry, aaEntry, usbcEntry, whEntry, lccEntry, BshEntry, m20Entry, aahEntry, tvEntry, m34Entry, gmEntry, vareebaddphoneEntry, googlephoneEntry, lgdryerEntry, wmEntry, iphoneEntry, thinkpadEntry, macEntry, totalEntry,taxentry):
    global aaaprice
    global aaprice
    global usbprice
    global whprice
    global lccprice
    global bshprice
    global m20price
    global aahprice
    global tvprice
    global m34price
    global gmprice
    global vareebaddphoneprice
    global googlephoneprice
    global lgdryerprice
    global wmprice
    global iphoneprice
    global thinkpadprice
    global macprice
    global total_price
    global totalbill
    global current_sales
    aaaprice = int(aaaEntry.get())*2.99
    aaprice = int(aaEntry.get())*3.84
    usbprice = int(usbcEntry.get())*11.95
    whprice = int(whEntry.get())*11.99
    lccprice = int(lccEntry.get())*14.95
    bshprice = int(BshEntry.get())*99.99
    m20price = int(m20Entry.get())*109.99
    aahprice = int(aahEntry.get())*150
    tvprice = int(tvEntry.get())*300
    m34price = int(m34Entry.get())*379.99
    gmprice = int(gmEntry.get())*389.99
    vareebaddphoneprice = int(vareebaddphoneEntry.get())*400
    googlephoneprice = int(googlephoneEntry.get())*600
    lgdryerprice = int(lgdryerEntry.get())*600
    wmprice = int(wmEntry.get())*600
    iphoneprice = int(iphoneEntry.get())*700
    thinkpadprice = int(thinkpadEntry.get())*999.99
    macprice = int(macEntry.get())*1700
    total_price = (
    aaaprice + aaprice + usbprice + whprice + lccprice + bshprice +
    m20price + aahprice + tvprice + m34price + gmprice +
    vareebaddphoneprice + googlephoneprice + lgdryerprice +
    wmprice + iphoneprice + thinkpadprice + macprice)
    totalEntry.delete(0, END)
    totalEntry.insert(0,f'{total_price} $')
    tax(aaaEntry, aaEntry, usbcEntry, whEntry, lccEntry, BshEntry, m20Entry, aahEntry, tvEntry, m34Entry, gmEntry, vareebaddphoneEntry, googlephoneEntry, lgdryerEntry, wmEntry, iphoneEntry, thinkpadEntry, macEntry,taxentry)
    totalbill = total_price - total_tax
    current_sales=current_sales+total_price
    total_product(aaaEntry, aaEntry, usbcEntry, whEntry, lccEntry, BshEntry, m20Entry, aahEntry, tvEntry, m34Entry, gmEntry, vareebaddphoneEntry, googlephoneEntry, lgdryerEntry, wmEntry, iphoneEntry, thinkpadEntry, macEntry)

def get_current_sales():
    return current_sales

def tax(aaaEntry, aaEntry, usbcEntry, whEntry, lccEntry, BshEntry, m20Entry, aahEntry, tvEntry, m34Entry, gmEntry, vareebaddphoneEntry, googlephoneEntry, lgdryerEntry, wmEntry, iphoneEntry, thinkpadEntry, macEntry, taxentry):
    global aaatax
    global aatax
    global usbtax
    global whtax
    global lcctax
    global bshtax
    global m20tax
    global aahtax
    global tvtax
    global m34tax
    global gmtax
    global vareebaddphonetax
    global googlephonetax
    global lgdryertax
    global wmtax
    global iphonetax
    global thinkpadtax
    global mactax
    global total_tax
    aaatax = int(aaaEntry.get())*2.99*0.1
    aatax = int(aaEntry.get())*3.84*0.1
    usbtax = int(usbcEntry.get())*11.95*0.1
    whtax = int(whEntry.get())*11.99*0.1
    lcctax = int(lccEntry.get())*14.95*0.1
    bshtax = int(BshEntry.get())*99.99*0.1
    m20tax = int(m20Entry.get())*109.99*0.1
    aahtax = int(aahEntry.get())*150*0.1
    tvtax = int(tvEntry.get())*300*0.1
    m34tax = int(m34Entry.get())*379.99*0.1
    gmtax = int(gmEntry.get())*389.99*0.1
    vareebaddphonetax = int(vareebaddphoneEntry.get())*400*0.1
    googlephonetax = int(googlephoneEntry.get())*600*0.1
    lgdryertax = int(lgdryerEntry.get())*600*0.1
    wmtax = int(wmEntry.get())*600*0.1
    iphonetax = int(iphoneEntry.get())*700*0.1
    thinkpadtax = int(thinkpadEntry.get())*999.99*0.1
    mactax = int(macEntry.get())*1700*0.1
    total_tax = (
    aaatax + aatax + usbtax + whtax + lcctax + bshtax +
    m20tax + aahtax + tvtax + m34tax + gmtax +
    vareebaddphonetax + googlephonetax + lgdryertax +
    wmtax + iphonetax + thinkpadtax + mactax)
    taxentry.delete(0, END)
    taxentry.insert(0,f'{total_tax} $')


def bill_area(nameEntry, totalEntry, phoneEntry, textarea, aaaEntry, aaEntry, usbcEntry, whEntry, lccEntry, BshEntry, m20Entry, aahEntry, tvEntry, m34Entry, gmEntry, vareebaddphoneEntry, googlephoneEntry, lgdryerEntry, wmEntry, iphoneEntry, thinkpadEntry, macEntry,taxentry):
        if nameEntry.get() == '' or phoneEntry.get() == '':
            messagebox.showerror('Error', "Customer details are required!!!")
        elif totalEntry.get() == '' or totalEntry.get() == '0.0 $':
            messagebox.showerror('Error', "No product selected")
        else:
            textarea.insert(END, '\t\t**Welcome customer**')
            textarea.insert(END, f'\nBill Number: {billnumber}\n')
            textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}\n')
            textarea.insert(END, f'\nCustomer Phone Number: {phoneEntry.get()}\n')
            textarea.insert(END,'\n======================================================')
            textarea.insert(END, '\tProduct\t\t\tQuantity\t\tPrice')
            textarea.insert(END,'\n======================================================')
            if int(aaaEntry.get()) != 0:
                textarea.insert(END, f'\nAAA Batteries (4-pack)\t\t\t{aaaEntry.get()}\t\t{aaaprice}')
            if int(aaEntry.get()) != 0:
                textarea.insert(END, f'\nAA Batteries (4-pack)\t\t\t{aaEntry.get()}\t\t{aaprice}')
            if int(usbcEntry.get()) != 0:
                textarea.insert(END, f'\nUSB-C Charging Cable\t\t\t{usbcEntry.get()}\t\t{usbprice}')
            if int(whEntry.get()) != 0:
                textarea.insert(END, f'\nWired Headphones\t\t\t{whEntry.get()}\t\t{whprice}')
            if int(lccEntry.get()) != 0:
                textarea.insert(END, f'\nLightning Charging Cable\t\t\t{lccEntry.get()}\t\t{lccprice}')
            if int(BshEntry.get()) != 0:
                textarea.insert(END, f'\nBose SoundSport Headphones\t\t\t{BshEntry.get()}\t\t{bshprice}')
            if int(m20Entry.get()) != 0:
                textarea.insert(END, f'\n20in Monitor\t\t\t{m20Entry.get()}\t\t{m20price}')
            if int(aahEntry.get()) != 0:
                textarea.insert(END, f'\n27in FHD Monitor\t\t\t{aahEntry.get()}\t\t{aahprice}')
            if int(tvEntry.get()) != 0:
                textarea.insert(END, f'\nFlatscreen TV\t\t\t{tvEntry.get()}\t\t{tvprice}')
            if int(m34Entry.get()) != 0:
                textarea.insert(END, f'\n34in Ultrawide Monitor\t\t\t{m34Entry.get()}\t\t{m34price}')
            if int(gmEntry.get()) != 0:
                textarea.insert(END, f'\n27in 4K Gaming Monitor\t\t\t{gmEntry.get()}\t\t{gmprice}')
            if int(vareebaddphoneEntry.get()) != 0:
                textarea.insert(END, f'\nVareebadd Phone\t\t\t{vareebaddphoneEntry.get()}\t\t{vareebaddphoneprice}')
            if int(googlephoneEntry.get()) != 0:
                textarea.insert(END, f'\nGoogle Phone\t\t\t{googlephoneEntry.get()}\t\t{googlephoneprice}')
            if int(lgdryerEntry.get()) != 0:
                textarea.insert(END, f'\nLG Dryer\t\t\t{lgdryerEntry.get()}\t\t{lgdryerprice}')
            if int(wmEntry.get()) != 0:
                textarea.insert(END, f'\nLG Washing Machine\t\t\t{wmEntry.get()}\t\t{wmprice}')
            if int(iphoneEntry.get()) != 0:
                textarea.insert(END, f'\nIphone\t\t\t{iphoneEntry.get()}\t\t{iphoneprice}')
            if int(thinkpadEntry.get()) != 0:
                textarea.insert(END, f'\nThinkPad Laptops\t\t\t{thinkpadEntry.get()}\t\t{thinkpadprice}')
            if int(macEntry.get()) != 0:
                textarea.insert(END, f'\nMacbook Pro Laptops\t\t\t{macEntry.get()}\t\t{macprice}')
            textarea.insert(END,'\n-------------------------------------------------------')
            textarea.insert(END, f'\nTAX\t\t\t{taxentry.get()}')
            textarea.insert(END, f'\nTOTAL\t\t\t{totalbill}')
            check_inventory(phoneEntry, textarea, aaaEntry, aaEntry, usbcEntry, whEntry, lccEntry, BshEntry, m20Entry, aahEntry, tvEntry, m34Entry, gmEntry, vareebaddphoneEntry, googlephoneEntry, lgdryerEntry, wmEntry, iphoneEntry, thinkpadEntry, macEntry)
            save_bill(textarea)
            save_data_customer(nameEntry, phoneEntry,totalbill)
            



def check_inventory(phoneEntry, textarea, aaaEntry, aaEntry, usbcEntry, whEntry, lccEntry, BshEntry, m20Entry, aahEntry, tvEntry, m34Entry, gmEntry, vareebaddphoneEntry, googlephoneEntry, lgdryerEntry, wmEntry, iphoneEntry, thinkpadEntry, macEntry):
    file_path = "Database/Inventory.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    variable_names = {
        "AAA Batteries (4-pack)": "ab4p",
        "AA Batteries (4-pack)": "aab4p",
        "USB-C Charging Cable": "usb_cc",
        "Wired Headphones": "wh",
        "Lightning Charging Cable": "lcc",
        "Bose SoundSport Headphones": "bsh",
        "20in Monitor": "m20in",
        "27in FHD Monitor": "m27fhd",
        "Apple Airpods Headphones": "aah",
        "Flatscreen TV": "ftv",
        "34in Ultrawide Monitor": "m34uw",
        "27in 4K Gaming Monitor": "m27gk",
        "Vareebadd Phone": "vp",
        "Google Phone": "gp",
        "LG Dryer": "lgd",
        "LG Washing Machine": "lgwm",
        "Iphone": "iphone",
        "ThinkPad Laptops": "tpl",
        "Macbook Pro Laptops": "mbpl"
    }
    products = {}
    for row in range(2, sheet.max_row + 1):
        product_name = sheet.cell(row=row, column=1).value
        quantity = sheet.cell(row=row, column=2).value
        if product_name and product_name in variable_names:  
            variable_name = variable_names[product_name]
            products[variable_name] = quantity
    if int(aaaEntry.get()) > 0:
        products["ab4p"] -= int(aaaEntry.get())
        if products["ab4p"] < 20:
            messagebox.showwarning("Low Inventory", "AAA Batteries (4-pack) inventory is low. Please restock.")
        if products["ab4p"] < 0:
            messagebox.showerror("Out of Stock", "AAA Batteries (4-pack) is out of stock.")
    if int(aaEntry.get()) > 0:
        products["aab4p"] -= int(aaEntry.get())
        if products["aab4p"] < 20:
            messagebox.showwarning("Low Inventory", "AA Batteries (4-pack) inventory is low. Please restock.")
        if products["aab4p"] < 0:
            messagebox.showerror("Out of Stock", "AA Batteries (4-pack) is out of stock.")
    if int(usbcEntry.get()) > 0:
        products["usb_cc"] -= int(usbcEntry.get())
        if products["usb_cc"] < 20:
            messagebox.showwarning("Low Inventory", "USB-C Charging Cable inventory is low. Please restock.")
        if products["usb_cc"] < 0:
            messagebox.showerror("Out of Stock", "USB-C Charging Cable is out of stock.")

    if int(whEntry.get()) > 0:
        products["wh"] -= int(whEntry.get())
        if products["wh"] < 20:
            messagebox.showwarning("Low Inventory", "Wired Headphones inventory is low. Please restock.")
        if products["wh"] < 0:
            messagebox.showerror("Out of Stock", "Wired Headphones is out of stock.")

    if int(lccEntry.get()) > 0:
        products["lcc"] -= int(lccEntry.get())
        if products["lcc"] < 20:
            messagebox.showwarning("Low Inventory", "Lightning Charging Cable inventory is low. Please restock.")
        if products["lcc"] < 0:
            messagebox.showerror("Out of Stock", "Lightning Charging Cable is out of stock.")

    if int(BshEntry.get()) > 0:
        products["bsh"] -= int(BshEntry.get())
        if products["bsh"] < 20:
            messagebox.showwarning("Low Inventory", "Bose SoundSport Headphones inventory is low. Please restock.")
        if products["bsh"] < 0:
            messagebox.showerror("Out of Stock", "Bose SoundSport Headphones is out of stock.")

    if int(m20Entry.get()) > 0:
        products["m20in"] -= int(m20Entry.get())
        if products["m20in"] < 20:
            messagebox.showwarning("Low Inventory", "20in Monitor inventory is low. Please restock.")
        if products["m20in"] < 0:
            messagebox.showerror("Out of Stock", "20in Monitor is out of stock.")

    if int(aahEntry.get()) > 0:
        products["m27fhd"] -= int(aahEntry.get())
        if products["m27fhd"] < 20:
            messagebox.showwarning("Low Inventory", "27in FHD Monitor inventory is low. Please restock.")
        if products["m27fhd"] < 0:
            messagebox.showerror("Out of Stock", "27in FHD Monitor is out of stock.")

    if int(tvEntry.get()) > 0:
        products["ftv"] -= int(tvEntry.get())
        if products["ftv"] < 20:
            messagebox.showwarning("Low Inventory", "Flatscreen TV inventory is low. Please restock.")
        if products["ftv"] < 0:
            messagebox.showerror("Out of Stock", "Flatscreen TV is out of stock.")

    if int(m34Entry.get()) > 0:
        products["m34uw"] -= int(m34Entry.get())
        if products["m34uw"] < 20:
            messagebox.showwarning("Low Inventory", "34in Ultrawide Monitor inventory is low. Please restock.")
        if products["m34uw"] < 0:
            messagebox.showerror("Out of Stock", "34in Ultrawide Monitor is out of stock.")

    if int(gmEntry.get()) > 0:
        products["m27gk"] -= int(gmEntry.get())
        if products["m27gk"] < 20:
            messagebox.showwarning("Low Inventory", "27in 4K Gaming Monitor inventory is low. Please restock.")
        if products["m27gk"] < 0:
            messagebox.showerror("Out of Stock", "27in 4K Gaming Monitor is out of stock.")

    if int(vareebaddphoneEntry.get()) > 0:
        products["vp"] -= int(vareebaddphoneEntry.get())
        if products["vp"] < 20:
            messagebox.showwarning("Low Inventory", "Vareebadd Phone inventory is low. Please restock.")
        if products["vp"] < 0:
            messagebox.showerror("Out of Stock", "Vareebadd Phone is out of stock.")

    if int(googlephoneEntry.get()) > 0:
        products["gp"] -= int(googlephoneEntry.get())
        if products["gp"] < 20:
            messagebox.showwarning("Low Inventory", "Google Phone inventory is low. Please restock.")
        if products["gp"] < 0:
            messagebox.showerror("Out of Stock", "Google Phone is out of stock.")

    if int(lgdryerEntry.get()) > 0:
        products["lgd"] -= int(lgdryerEntry.get())
        if products["lgd"] < 20:
            messagebox.showwarning("Low Inventory", "LG Dryer inventory is low. Please restock.")
        if products["lgd"] < 0:
            messagebox.showerror("Out of Stock", "LG Dryer is out of stock.")

    if int(wmEntry.get()) > 0:
        products["lgwm"] -= int(wmEntry.get())
        if products["lgwm"] < 20:
            messagebox.showwarning("Low Inventory", "LG Washing Machine inventory is low. Please restock.")
        if products["lgwm"] < 0:
            messagebox.showerror("Out of Stock", "LG Washing Machine is out of stock.")

    if int(iphoneEntry.get()) > 0:
        products["iphone"] -= int(iphoneEntry.get())
        if products["iphone"] < 20:
            messagebox.showwarning("Low Inventory", "Iphone inventory is low. Please restock.")
        if products["iphone"] < 0:
            messagebox.showerror("Out of Stock", "Iphone is out of stock.")

    if int(thinkpadEntry.get()) > 0:
        products["tpl"] -= int(thinkpadEntry.get())
        if products["tpl"] < 20:
            messagebox.showwarning("Low Inventory", "ThinkPad Laptops inventory is low. Please restock.")
        if products["tpl"] < 0:
            messagebox.showerror("Out of Stock", "ThinkPad Laptops is out of stock.")

    if int(macEntry.get()) > 0:
        products["mbpl"] -= int(macEntry.get())
        if products["mbpl"] < 20:
            messagebox.showwarning("Low Inventory", "Macbook Pro Laptops inventory is low. Please restock.")
        if products["mbpl"] < 0:
            messagebox.showerror("Out of Stock", "Macbook Pro Laptops is out of stock.")

    for row in range(2, sheet.max_row + 1):
        product_name = sheet.cell(row=row, column=1).value
        if product_name and product_name in variable_names:
            variable_name = variable_names[product_name]
            sheet.cell(row=row, column=2).value = products[variable_name]
    workbook.save(file_path)


if not os.path.exists('bills'):
    os.mkdir('bills')

billno=0
def save_bill(textarea) :
    global billnumber, billno
    result = messagebox.askyesno('Cofirm', "Do you want to save bill?")
    if result:
        bill_content = textarea.get(1.0, END)
        filename = f'bills/{billnumber}.txt'
        with open(filename, 'w') as file:
            file.write(bill_content)
        messagebox.showinfo('Success', f'{billnumber} is saved successfully')
        billnumber = random.randint(1000, 9999)
        billno= billno+1

billnumber = random.randint(1000, 9999)

def get_bill_count():
    return billno

def search_bill(billnumberEntry, textarea):
    for i in os.listdir(r'bills'):
        if i.split('.')[0]==billnumberEntry.get():
            with open(f'bills/{i}', 'r') as f:
                textarea.delete(1.0, END)
                for data in f:
                    textarea.insert(END,data)
                f.close()
                break
    else:
        messagebox.showerror('Error','Invalid Bill Number')



def print_bill(textarea):
    if textarea.get(1.0, END)=='\n':
        messagebox.showerror('Error', "Bill is empty")
    else:
        file=tempfile.mktemp('.txt')
        with open(file,'w') as f:
            f.write(textarea.get(1.0, END))
        os.startfile(file, 'print')



def save_data_customer(nameEntry, phoneEntry, totalbill):
    try:
        workbook = openpyxl.load_workbook(r"Database\Customer.xlsx")
    except FileNotFoundError:
        workbook = openpyxl.Workbook()
    worksheet = workbook.active
    max_row = worksheet.max_row
    worksheet.cell(row=max_row + 1, column=1).value = billnumber
    worksheet.cell(row=max_row + 1, column=2).value = nameEntry.get()
    worksheet.cell(row=max_row + 1, column=3).value = phoneEntry.get()
    worksheet.cell(row=max_row + 1, column=4).value = totalbill
    workbook.save(r"Database\Customer.xlsx")



file_path = "Database/Inventory.xlsx"
workbook = openpyxl.load_workbook(file_path)
sheet = workbook.active
variable_names = {
    "AAA Batteries (4-pack)": "ab4p",
    "AA Batteries (4-pack)": "aab4p",
    "USB-C Charging Cable": "usb_cc",
    "Wired Headphones": "wh",
    "Lightning Charging Cable": "lcc",
    "Bose SoundSport Headphones": "bsh",
    "20in Monitor": "m20in",
    "27in FHD Monitor": "m27fhd",
    "Apple Airpods Headphones": "aah",
    "Flatscreen TV": "ftv",
    "34in Ultrawide Monitor": "m34uw",
    "27in 4K Gaming Monitor": "m27gk",
    "Vareebadd Phone": "vp",
    "Google Phone": "gp",
    "LG Dryer": "lgd",
    "LG Washing Machine": "lgwm",
    "Iphone": "iphone",
    "ThinkPad Laptops": "tpl",
    "Macbook Pro Laptops": "mbpl"
}
products = {}

# Lấy dữ liệu từ sheet
for row in range(2, sheet.max_row + 1):
    product_name = sheet.cell(row=row, column=1).value
    quantity = sheet.cell(row=row, column=2).value
    if product_name and product_name in variable_names:  # Đảm bảo sản phẩm không rỗng và có trong ánh xạ
        variable_name = variable_names[product_name]
        products[variable_name] = quantity


def iphone(frame):
    iphone_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    iphone_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(iphone_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(iphone_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    iphone_img_resized = CTkImage(dark_image=iphone_img_data, light_image=iphone_img_data,size = (500, 375))

    CTkLabel(master=iphone_frame, text="", image=iphone_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=iphone_frame, text="IphoNE",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 56), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=iphone_frame, text="700$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=iphone_frame, text="Loại sản phẩm: Điện thoại",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=iphone_frame, text=f"Số lượng : {products["iphone"]}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=iphone_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=iphone_frame, text="Chip Apple A15 Bionic",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=iphone_frame, text="OLED, 6.1 inches, 60Hz",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")
    CTkLabel (master=iphone_frame, text="Hệ thống camera kép 12MP",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.8, anchor="w")


def google_phone(frame):
    google_phone_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    google_phone_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(google_phone_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(google_phone_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    google_phone_img_resized = CTkImage(dark_image=googlephone_img_data, light_image=googlephone_img_data,size = (450, 325))

    CTkLabel(master=google_phone_frame, text="", image=google_phone_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=google_phone_frame, text="GOOGLE phoNE",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 42), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=google_phone_frame, text="600$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=google_phone_frame, text="Loại sản phẩm: Điện thoại",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=google_phone_frame, text=f"Số lượng : {products["gp"]}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=google_phone_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=google_phone_frame, text="Chip Qualcomm Snapdragon 888",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 22), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=google_phone_frame, text="OLED, 6.7 inches, 120Hz",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")
    CTkLabel (master=google_phone_frame, text="Hệ thống camera kép 50MP",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.8, anchor="w")

def macbook_pro_laptop(frame):
    macbook_pro_laptop_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    macbook_pro_laptop_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(macbook_pro_laptop_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(macbook_pro_laptop_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    macbook_pro_laptop_img_resized = CTkImage(dark_image=macbookpro_img_data, light_image=macbookpro_img_data,size = (480, 375))

    CTkLabel(master=macbook_pro_laptop_frame, text="", image=macbook_pro_laptop_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=macbook_pro_laptop_frame, text="MACBOOK PRO LAPTOP",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 46), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=macbook_pro_laptop_frame, text="1500$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=macbook_pro_laptop_frame, text="Loại sản phẩm: Laptop",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=macbook_pro_laptop_frame, text=f"Số lượng : {products["mbpl"]}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=macbook_pro_laptop_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=macbook_pro_laptop_frame, text="Chip Apple M1 Pro",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=macbook_pro_laptop_frame, text="Retina, 16 inches, 120Hz",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")
    CTkLabel (master=macbook_pro_laptop_frame, text="Hệ thống camera kép 1080p",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.8, anchor="w")

def thinkpad_laptop(frame):
    thinkpad_laptop_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    thinkpad_laptop_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(thinkpad_laptop_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(thinkpad_laptop_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    thinkpad_laptop_img_resized = CTkImage(dark_image=thinkpad_img_data, light_image=thinkpad_img_data,size = (450, 325))

    CTkLabel(master=thinkpad_laptop_frame, text="", image=thinkpad_laptop_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=thinkpad_laptop_frame, text="THINKPAD LAPTOP",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=thinkpad_laptop_frame, text="1200$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=thinkpad_laptop_frame, text="Loại sản phẩm: Laptop",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=thinkpad_laptop_frame, text=f"Số lượng : {products["tpl"]}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=thinkpad_laptop_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=thinkpad_laptop_frame, text="Chip Intel Core i7-1165G7",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=thinkpad_laptop_frame, text="IPS, 14 inches, 60Hz",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")
    CTkLabel (master=thinkpad_laptop_frame, text="Hệ thống camera kép 720p",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.8, anchor="w")

def lg_dryer(frame):
    lg_dryer_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    lg_dryer_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(lg_dryer_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(lg_dryer_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    lg_dryer_img_resized = CTkImage(dark_image=dryer_img_data, light_image=dryer_img_data,size = (400, 375))

    CTkLabel(master=lg_dryer_frame, text="", image=lg_dryer_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=lg_dryer_frame, text="LG DRYER",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 56), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=lg_dryer_frame, text="600$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=lg_dryer_frame, text="Loại sản phẩm: Đồ gia dụng",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=lg_dryer_frame, text=f"Số lượng : {products["lgd"]}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=lg_dryer_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=lg_dryer_frame, text="Công suất: 5.6 kg",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=lg_dryer_frame, text="Kích thước: 1.14m x 0.57m x 0.47m",  text_color="#555555", fg_color ="#000000", font=("Arial Bold", 20), corner_radius=12, anchor="w").place(relx=0.57, rely=0.75, anchor="w")

def aaa_batteries(frame):
    aaa_batteries_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    aaa_batteries_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(aaa_batteries_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(aaa_batteries_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    aaa_batteries_img_resized = CTkImage(dark_image=aaabatteries_img_data, light_image=aaabatteries_img_data,size = (400, 275))

    CTkLabel(master=aaa_batteries_frame, text="", image=aaa_batteries_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=aaa_batteries_frame, text="AAA BATTERIES (4-PACK)",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 28), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=aaa_batteries_frame, text="2.99$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=aaa_batteries_frame, text="Loại sản phẩm: Đồ gia dụng",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=aaa_batteries_frame, text=f"Số lượng : {products["ab4p"]}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=aaa_batteries_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=aaa_batteries_frame, text="4 điện trở AAA",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=aaa_batteries_frame, text="Hạn sử dụng: 5 năm",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")

def aa_batteries(frame):
    aa_batteries_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    aa_batteries_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(aa_batteries_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(aa_batteries_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    aa_batteries_img_resized = CTkImage(dark_image=aabatteries_img_data, light_image=aabatteries_img_data,size = (350, 245))

    CTkLabel(master=aa_batteries_frame, text="", image=aa_batteries_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=aa_batteries_frame, text="AA BATTERIES (4-PACK)",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 28), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=aa_batteries_frame, text="3.84$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=aa_batteries_frame, text="Loại sản phẩm: Đồ gia dụng",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=aa_batteries_frame, text=f"Số lượng : {products['aab4p']}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=aa_batteries_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=aa_batteries_frame, text="4 điện trở AA",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=aa_batteries_frame, text="Hạn sử dụng: 5 năm",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")

def usb_c_charging_cable(frame):
    usb_c_charging_cable_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    usb_c_charging_cable_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(usb_c_charging_cable_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(usb_c_charging_cable_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    usb_c_charging_cable_img_resized = CTkImage(dark_image=chargingcable_img_data, light_image=chargingcable_img_data,size = (400, 275))

    CTkLabel(master=usb_c_charging_cable_frame, text="", image=usb_c_charging_cable_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=usb_c_charging_cable_frame, text="USB-C CHARGING CABLE",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 28), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=usb_c_charging_cable_frame, text="11.95$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=usb_c_charging_cable_frame, text="Loại sản phẩm: Phụ kiện",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=usb_c_charging_cable_frame, text=f"Số lượng : {products['usb_cc']}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=usb_c_charging_cable_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=usb_c_charging_cable_frame, text="USB-C đầu ra, USB-A đầu vào",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=usb_c_charging_cable_frame, text="Dài 1.8m",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")

def wired_headphones(frame):
    wired_headphones_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    wired_headphones_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(wired_headphones_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(wired_headphones_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    wired_headphones_img_resized = CTkImage(dark_image=wiredheadphones_img_data, light_image=wiredheadphones_img_data,size = (400, 275))

    CTkLabel(master=wired_headphones_frame, text="", image=wired_headphones_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=wired_headphones_frame, text="WIRED HEADphoNES",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 34), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=wired_headphones_frame, text="11.99$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=wired_headphones_frame, text="Loại sản phẩm: Phụ kiện",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=wired_headphones_frame, text=f"Số lượng : {products['wh']}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=wired_headphones_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=wired_headphones_frame, text="Tai nghe dây, 3.5mm đầu vào",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=wired_headphones_frame, text="Dài 2m",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")

def lightning_charging_cable(frame):
    lightning_charging_cable_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    lightning_charging_cable_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(lightning_charging_cable_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(lightning_charging_cable_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    lightning_charging_cable_img_resized = CTkImage(dark_image=lightningcable_img_data, light_image=lightningcable_img_data,size = (400, 275))

    CTkLabel(master=lightning_charging_cable_frame, text="", image=lightning_charging_cable_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=lightning_charging_cable_frame, text="LIGHTNING CHARGING CABLE",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=lightning_charging_cable_frame, text="14.95$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=lightning_charging_cable_frame, text="Loại sản phẩm: Phụ kiện",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=lightning_charging_cable_frame, text=f"Số lượng : {products['lcc']}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=lightning_charging_cable_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=lightning_charging_cable_frame, text="Lightning đầu ra, USB-A đầu vào",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 23), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=lightning_charging_cable_frame, text="Dài 1.8m",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")

def bose_soundsport_headphones(frame):
    bose_soundsport_headphones_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    bose_soundsport_headphones_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(bose_soundsport_headphones_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(bose_soundsport_headphones_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    bose_soundsport_headphones_img_resized = CTkImage(dark_image=soundheadphones_img_data, light_image=soundheadphones_img_data,size = (375, 250))

    CTkLabel(master=bose_soundsport_headphones_frame, text="", image=bose_soundsport_headphones_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=bose_soundsport_headphones_frame, text="BOSE SOUNDSPORT HEADPHONES",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 20), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=bose_soundsport_headphones_frame, text="99.99$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=bose_soundsport_headphones_frame, text="Loại sản phẩm: Phụ kiện",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=bose_soundsport_headphones_frame, text=f"Số lượng : {products['bsh']}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=bose_soundsport_headphones_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=bose_soundsport_headphones_frame, text="Tai nghe Bluetooth, đầu vào không dây",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 18), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=bose_soundsport_headphones_frame, text="Dài 1.2m",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")

def twenty_inch_monitor(frame):
    twenty_inch_monitor_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    twenty_inch_monitor_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(twenty_inch_monitor_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(twenty_inch_monitor_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    twenty_inch_monitor_img_resized = CTkImage(dark_image=inmonitor_img_data, light_image=inmonitor_img_data,size = (425, 300))

    CTkLabel(master=twenty_inch_monitor_frame, text="", image=twenty_inch_monitor_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=twenty_inch_monitor_frame, text="20IN MONITOR",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 46), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=twenty_inch_monitor_frame, text="109.99$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=twenty_inch_monitor_frame, text="Loại sản phẩm: Màn hình",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=twenty_inch_monitor_frame, text=f"Số lượng : {products['m20in' ]}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=twenty_inch_monitor_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=twenty_inch_monitor_frame, text="Kích thước: 20 inches",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=twenty_inch_monitor_frame, text="Độ phân giải: 1080p",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")

def twentyseven_inch_fhd_monitor(frame):
    twentyseven_inch_fhd_monitor_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    twentyseven_inch_fhd_monitor_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(twentyseven_inch_fhd_monitor_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(twentyseven_inch_fhd_monitor_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    twentyseven_inch_fhd_monitor_img_resized = CTkImage(dark_image=fhdmonitor_img_data, light_image=fhdmonitor_img_data,size = (400, 275))

    CTkLabel(master=twentyseven_inch_fhd_monitor_frame, text="", image=twentyseven_inch_fhd_monitor_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=twentyseven_inch_fhd_monitor_frame, text="27IN FHD MONITOR",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 34), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=twentyseven_inch_fhd_monitor_frame, text="149.99$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=twentyseven_inch_fhd_monitor_frame, text="Loại sản phẩm: Màn hình",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=twentyseven_inch_fhd_monitor_frame, text=f"Số lượng : {products['m27fhd' ]}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=twentyseven_inch_fhd_monitor_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=twentyseven_inch_fhd_monitor_frame, text="Kích thước: 27 inches",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=twentyseven_inch_fhd_monitor_frame, text="Độ phân giải: 1080p",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")

def apple_airpods_headphones(frame):
    apple_airpods_headphones_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    apple_airpods_headphones_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(apple_airpods_headphones_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(apple_airpods_headphones_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    apple_airpods_headphones_img_resized = CTkImage(dark_image=airpod_img_data, light_image=airpod_img_data,size = (300, 225))

    CTkLabel(master=apple_airpods_headphones_frame, text="", image=apple_airpods_headphones_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=apple_airpods_headphones_frame, text="APPLE AIRPODS HEADphoNES",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 23), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=apple_airpods_headphones_frame, text="150$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=apple_airpods_headphones_frame, text="Loại sản phẩm: Phụ kiện",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=apple_airpods_headphones_frame, text=f"Số lượng : {products['aah']}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=apple_airpods_headphones_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=apple_airpods_headphones_frame, text="Tai nghe Bluetooth, không dây",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=apple_airpods_headphones_frame, text="Dài 1.2m",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")

def flatscreen_tv(frame):
    flatscreen_tv_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    flatscreen_tv_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(flatscreen_tv_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(flatscreen_tv_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    flatscreen_tv_img_resized = CTkImage(dark_image=tv_img_data, light_image=tv_img_data,size = (500, 375))

    CTkLabel(master=flatscreen_tv_frame, text="", image=flatscreen_tv_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=flatscreen_tv_frame, text="FLATSCREEN TV",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 42), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=flatscreen_tv_frame, text="300$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=flatscreen_tv_frame, text="Loại sản phẩm: Điện thoại",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=flatscreen_tv_frame, text=f"Số lượng : {products['ftv']}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=flatscreen_tv_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=flatscreen_tv_frame, text="Kích thước: 40 inches",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=flatscreen_tv_frame, text="Độ phân giải: 1080p",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")

def thirtyfour_inch_ultrawide_monitor(frame):
    thirtyfour_inch_ultrawide_monitor_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    thirtyfour_inch_ultrawide_monitor_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(thirtyfour_inch_ultrawide_monitor_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(thirtyfour_inch_ultrawide_monitor_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")


def twentyseven_inch_4k_gaming_monitor(frame):
    twentyseven_inch_4k_gaming_monitor_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    twentyseven_inch_4k_gaming_monitor_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(twentyseven_inch_4k_gaming_monitor_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(twentyseven_inch_4k_gaming_monitor_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    twentyseven_inch_4k_gaming_monitor_img_resized = CTkImage(dark_image=gamingmonitor_img_data, light_image=gamingmonitor_img_data,size = (450, 300))

    CTkLabel(master=twentyseven_inch_4k_gaming_monitor_frame, text="", image=twentyseven_inch_4k_gaming_monitor_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=twentyseven_inch_4k_gaming_monitor_frame, text="27IN 4K GAMING MONITOR",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 28), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=twentyseven_inch_4k_gaming_monitor_frame, text="389.99$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=twentyseven_inch_4k_gaming_monitor_frame, text="Loại sản phẩm: Màn hình",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=twentyseven_inch_4k_gaming_monitor_frame, text=f"Số lượng : {products['m27gk']}",  text_color="#000000", fg_color="transparent",font=("ArialBold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=twentyseven_inch_4k_gaming_monitor_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=twentyseven_inch_4k_gaming_monitor_frame, text="Kích thước: 27 inches",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=twentyseven_inch_4k_gaming_monitor_frame, text="Độ phân giải: 4K",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")

def var_e_badd_phone(frame):
    var_e_badd_phone_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    var_e_badd_phone_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(var_e_badd_phone_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(var_e_badd_phone_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    var_e_badd_phone_img_resized = CTkImage(dark_image=phone_img_data, light_image=phone_img_data,size = (500, 375))

    CTkLabel(master=var_e_badd_phone_frame, text="", image=var_e_badd_phone_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=var_e_badd_phone_frame, text="VAREEBADD phoNE",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=var_e_badd_phone_frame, text="400$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=var_e_badd_phone_frame, text="Loại sản phẩm: Điện thoại",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=var_e_badd_phone_frame, text=f"Số lượng : {products['vp']}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=var_e_badd_phone_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=var_e_badd_phone_frame, text="RAM: 8GB",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=var_e_badd_phone_frame, text="Bộ nhớ trong: 128GB",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")

def lg_washing_machine(frame):
    lg_washing_machine_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    lg_washing_machine_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(lg_washing_machine_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(lg_washing_machine_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    lg_washing_machine_img_resized = CTkImage(dark_image=washingmachine_img_data, light_image=washingmachine_img_data,size = (450, 325))

    CTkLabel(master=lg_washing_machine_frame, text="", image=lg_washing_machine_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")

    CTkLabel (master=lg_washing_machine_frame, text="LG WASHING MACHINE",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 30), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=lg_washing_machine_frame, text="600$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=lg_washing_machine_frame, text="Loại sản phẩm: Đồ gia dụng",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=lg_washing_machine_frame, text=f"Số lượng : {products['lgwm']}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=lg_washing_machine_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=lg_washing_machine_frame, text="Công suất: 7kg",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=lg_washing_machine_frame, text="Chế độ tự động",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")

def thirtyfour_inch_ultrawide_monitor(frame):
    thirtyfour_inch_ultrawide_monitor_frame = CTkFrame(master=app, fg_color="#ffffff", bg_color="transparent", border_color="#222324", width=900, height=600, corner_radius=30)
    thirtyfour_inch_ultrawide_monitor_frame.place(relx=0.5, rely=0.5, anchor="center")

    close_button = CTkButton(thirtyfour_inch_ultrawide_monitor_frame, text="X", fg_color="#000000", width=30, height=30, command=lambda: close_frame(thirtyfour_inch_ultrawide_monitor_frame))
    close_button.place(relx=1.0, rely=0.028, anchor="e")

    thirtyfour_inch_ultrawide_monitor_img_resized = CTkImage(dark_image=ultrawidemonitor_img_data, light_image=ultrawidemonitor_img_data,size = (425, 300))
    CTkLabel(master=thirtyfour_inch_ultrawide_monitor_frame, text="", image=thirtyfour_inch_ultrawide_monitor_img_resized, text_color="#000000", fg_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=400, height=600, anchor="n", compound="center").place(relx=0.3, rely=0.7, anchor="center")
    CTkLabel (master=thirtyfour_inch_ultrawide_monitor_frame, text="34IN ULTRAWIDE MONITOR",  text_color="#444444", fg_color="transparent",font=("Arial Bold", 26), corner_radius=12, anchor="w").place(relx=0.57, rely=0.25, anchor="w")
    CTkLabel (master=thirtyfour_inch_ultrawide_monitor_frame, text="379.99$",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 36), corner_radius=12, anchor="w").place(relx=0.57, rely=0.36, anchor="w")
    CTkLabel (master=thirtyfour_inch_ultrawide_monitor_frame, text="Loại sản phẩm: Màn hình",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12,  anchor="w").place(relx=0.57, rely=0.45, anchor="w")
    CTkLabel (master=thirtyfour_inch_ultrawide_monitor_frame, text=f"Số lượng : {products['m34uw']}",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.53, anchor="w")
    CTkLabel (master=thirtyfour_inch_ultrawide_monitor_frame, text="Chi tiết sản phẩm",  text_color="#000000", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.62, anchor="w")
    CTkLabel (master=thirtyfour_inch_ultrawide_monitor_frame, text="Kích thước: 34 inches",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.68, anchor="w")
    CTkLabel (master=thirtyfour_inch_ultrawide_monitor_frame, text="Độ phân giải: 1440p",  text_color="#555555", fg_color="transparent",font=("Arial Bold", 24), corner_radius=12, anchor="w").place(relx=0.57, rely=0.74, anchor="w")




def phanLoai(value,frame):
    sanPhamScroll = CTkScrollableFrame(master=frame, fg_color="#111111", height=550, width=800,
                            border_color="#27408B",
                            border_width=4, orientation="vertical",
                            scrollbar_button_color="#000000")
    sanPhamScroll.place(relx=0.35, rely=0.61, anchor="center")
    if value == "Tất cả":
        CTkButton(master=sanPhamScroll, text="IphoNE\n700$", image=iphone_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top", command=lambda: iphone(frame)).grid(row=0, column=0, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: google_phone(frame), text="GOOGLE phoNE\n600$", image=googlephone_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=1, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: macbook_pro_laptop(frame), text="MACBOOK PRO\n1700$", image=macbookpro_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=2,  pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: thinkpad_laptop(frame), text="THINKPAD LAPTOP\n999.99$", image=thinkpad_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=1, column=0, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: lg_dryer(frame),text="LG DRYER\n600$", image=dryer_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=250, height=250, anchor="n", compound = "top").grid(row=1, column=1, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: lg_washing_machine(frame),text="LG WASHING MACHINE\n600$", image=washingmachine_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=1, column=2, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: twenty_inch_monitor(frame),text="20in Monitor\n109.99$", image=inmonitor_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=2, column=0, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: twentyseven_inch_4k_gaming_monitor(frame),text="27in 4k Gaming Monitor\n149.99$", image=gamingmonitor_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=2, column=1, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: twentyseven_inch_fhd_monitor(frame),text="27in FHD Monitor\n379.99$",image=fhdmonitor_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=2, column=2, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: thirtyfour_inch_ultrawide_monitor(frame),text="34in Ultrawide Monitor\n389.99$", image=ultrawidemonitor_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=3, column=0, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: flatscreen_tv(frame),text="Flatscreen TV\n300$", image=tv_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=3, column=1, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: aa_batteries(frame),text="AA Batteries\n2.99$", image=aabatteries_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=3, column=2, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: aaa_batteries(frame),text="AAA Batteries\n3.84$", image=aaabatteries_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=6, column=0, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: apple_airpods_headphones(frame),text="Airpods\n150$", image=airpod_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=4, column=0, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: wired_headphones(frame),text="Wired Headphones\n11.99$", image=wiredheadphones_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=4, column=1, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: bose_soundsport_headphones(frame),text="Soundsport Headphones\n99.99$", image=soundheadphones_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=4, column=2, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: var_e_badd_phone(frame),text="Varrebadd phone\n400$", image=phone_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=5, column=0, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: usb_c_charging_cable(frame),text="USBC Charging cable\n11.95$", image=chargingcable_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=5, column=1, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: lightning_charging_cable(frame),text="Lightning Charging cable\n14.95$", image=lightningcable_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=5, column=2, padx=2, pady = 5)
    elif value=="Pin":
        CTkButton(master=sanPhamScroll, command=lambda: aa_batteries(frame),text="AA Batteries\n2.99$", image=aabatteries_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=0, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: aaa_batteries(frame),text="AAA Batteries\n3.84$", image=aaabatteries_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=1, padx=2, pady = 5)
    elif value=="USB-C":
        CTkButton(master=sanPhamScroll, command=lambda: usb_c_charging_cable(frame),text="USBC Charging cable\n11.95$", image=chargingcable_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=0, padx=2, pady = 5)
    elif value=="Tai nghe":
        CTkButton(master=sanPhamScroll, command=lambda: apple_airpods_headphones(frame),text="Airpods\n150$", image=airpod_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=0, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: wired_headphones(frame),text="Wired Headphones\n11.99$", image=wiredheadphones_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=1, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: bose_soundsport_headphones(frame),text="Soundsport Headphones\n99.99$", image=soundheadphones_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=2, padx=2, pady = 5)
    elif value =="Sạc":
        CTkButton(master=sanPhamScroll, command=lambda: lightning_charging_cable(frame),text="Lightning Charging cable\n14.95$", image=lightningcable_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=0, padx=2, pady = 5)
    elif value =="Màn hình":
        CTkButton(master=sanPhamScroll, command=lambda: twenty_inch_monitor(frame),text="20in Monitor\n109.99$", image=inmonitor_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=0, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: twentyseven_inch_4k_gaming_monitor(frame),text="27in 4k Gaming Monitor\n149.99$", image=gamingmonitor_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=1, padx=1, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: twentyseven_inch_fhd_monitor(frame),text="27in FHD Monitor\n379.99$",image=fhdmonitor_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=2, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: thirtyfour_inch_ultrawide_monitor(frame),text="34in Ultrawide Monitor\n389.99$", image=ultrawidemonitor_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=1, column=0, padx=2, pady = 5)
    elif value == "Điện thoại":
        CTkButton(master=sanPhamScroll, text="IphoNE\n700$", image=iphone_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top", command=lambda: iphone(frame)).grid(row=0, column=0, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: google_phone(frame), text="GOOGLE phoNE\n600$", image=googlephone_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=1, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: var_e_badd_phone(frame),text="Varrebadd phone\n400$", image=phone_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=2, padx=2, pady = 5)
    elif value == "Máy giặt":
        CTkButton(master=sanPhamScroll, command=lambda: lg_dryer(frame),text="LG DRYER\n600$", image=dryer_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=250, height=250, anchor="n", compound = "top").grid(row=0, column=0, padx=2, pady = 5)
        CTkButton(master=sanPhamScroll, command=lambda: lg_washing_machine(frame),text="LG WASHING MACHINE\n600$", image=washingmachine_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=1, padx=2, pady = 5)
    else:
        CTkButton(master=sanPhamScroll, command=lambda: macbook_pro_laptop(frame), text="MACBOOK PRO\n1700$", image=macbookpro_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=0,  pady = 5)



sanPham = StringVar()
soLuong = StringVar()

def close_frame(frame):
    frame.destroy()

def nhapHangHoa(frame):
    frame1 = CTkFrame(master=frame, bg_color="#27408B", fg_color="#ffffff", height=300, width=400)
    frame1.place(relx=0.82, rely=0.4, anchor="center")
    close_button = CTkButton(frame1, text="X", fg_color="#000000", width=20, height=20, command=lambda: close_frame(frame1))
    close_button.place(relx=1.0, rely=0.028, anchor="e")
    
    CTkLabel(master=frame1, text="Chọn loại sản phẩm", font=("Poppins", 15, 'bold'), text_color="#000000").place(relx=0.2, rely=0.1, anchor="center")
    
    combobox = CTkComboBox(master=frame1,
                           values=["AAA Batteries (4-pack)", "AA Batteries (4-pack)", "USB-C Charging Cable", "Wired Headphones",
                                   "Lightning Charging Cable", "Bose SoundSport Headphones", "20in Monitor", "27in FHD Monitor",
                                   "Apple Airpods Headphones", "Flatscreen TV", "34in Ultrawide Monitor", "27in 4K Gaming Monitor",
                                   "Vareebadd Phone", "Google Phone", "LG Dryer", "LG Washing Machine", "Iphone", "ThinkPad Laptops",
                                   "Macbook Pro Laptops"],
                           text_color="#000000",
                           fg_color="#27408B",
                           width=160,
                           height=45,
                           variable=sanPham,
                           dropdown_fg_color="#27408B",
                           corner_radius=9)
    combobox.place(relx=0.05, rely=0.15, anchor="nw")
    
    CTkLabel(master=frame1, text="Số lượng nhập", font=("Poppins", 15, 'bold'), text_color="#000000").place(relx=0.8, rely=0.1, anchor="center")
    
    soLuongNhap = CTkEntry(master=frame1, font=("Poppins", 15, 'bold'), text_color="#ffffff", textvariable=soLuong)
    soLuongNhap.place(relx=0.8, rely=0.2, anchor="center")
    
    CTkButton(master=frame1, text="THÊM", command=lambda: them(), height=50, width =370).place(relx=0.5, rely=0.55, anchor="center")
    

def them():
    selected_product = sanPham.get()
    quantity = soLuong.get()

    if not selected_product or not quantity:
        print("Please select a product and enter a quantity.")
        return

    try:
        workbook = openpyxl.load_workbook(r"Database\Inventory.xlsx")
    except FileNotFoundError:
        workbook = openpyxl.Workbook()
        workbook.active.append(["Product", "Quantity"])

    worksheet = workbook.active
    max_row = worksheet.max_row

    for row in range(2, max_row + 1):
        if worksheet.cell(row=row, column=1).value == selected_product:
            current_quantity = int(worksheet.cell(row=row, column=2).value)
            worksheet.cell(row=row, column=2).value = current_quantity + int(quantity)
            workbook.save(r"Database\Inventory.xlsx")
            messagebox.showinfo("Success", f"Added {quantity} to {selected_product}.")
            return

    # If the product is not found, add it as a new row
    worksheet.cell(row=max_row + 1, column=1).value = selected_product
    worksheet.cell(row=max_row + 1, column=2).value = int(quantity)
    workbook.save(r"Database\Inventory.xlsx")
    messagebox.showinfo("Success", f"Added {selected_product} with quantity {quantity}.")





def hienThiHang(textarea):
    try:
        workbook = openpyxl.load_workbook(r"Database\Inventory.xlsx")
        worksheet = workbook.active
        textarea.delete(1.0, 'end')  
        for row in worksheet.iter_rows(min_row=2, values_only=True):  
            product, quantity = row
            textarea.insert('end', f"{product}: {quantity}\n")
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No inventory file found.")


@create_frame
def khoHang(frame):
    CTkLabel(master=frame, text="SẢN PHẨM", font=("Arial Bold", 36), anchor="nw", width=150, height=125).place(relx=0.02, rely=0.13, anchor="w")
    sanPhamScroll = CTkScrollableFrame(master=frame, fg_color="#111111", height=550, width=800,
                            border_color="#27408B",
                            border_width=4, orientation="vertical",
                            scrollbar_button_color="#000000")
    sanPhamScroll.place(relx=0.35, rely=0.61, anchor="center")
    combobox = CTkComboBox(master=frame, values=["Tất cả", "Pin", "USB-C","Tai nghe","Sạc","Màn hình","Điện thoại","Máy giặt","Laptop"],text_color="#000000",
                       fg_color="#27408B", width=160, height=45,
                       dropdown_fg_color="#27408B", corner_radius=9,
                       command=lambda value: phanLoai(value,frame))
    combobox.place(relx = 0.05, rely = 0.15, anchor ="nw")
    nhapHang = CTkButton(master = frame, fg_color="#27408B", text = 'Nhập hàng', width=160, height=45,command=lambda: nhapHangHoa(frame))
    nhapHang.place(relx =0.95, rely=0.15, anchor = 'ne')
    scrollbar = Scrollbar(frame, orient = VERTICAL)
    scrollbar.pack(side=RIGHT,fill=Y)
    textarea = Text(frame, height = 35, width =45, yscrollcommand=scrollbar.set)
    textarea.place(relx=0.83, rely=0.6, anchor = 'center')
    scrollbar.config(command=textarea.yview)

    hienThiButton = CTkButton(master=frame, fg_color="#27408B", text='Kho hàng', width=160, height=45, command=lambda: hienThiHang(textarea))
    hienThiButton.place(relx=0.8, rely=0.15, anchor='ne')
    

    CTkButton(master=sanPhamScroll, text="IphoNE\n700$", image=iphone_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top", command=lambda: iphone(frame)).grid(row=0, column=0, padx=2, pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: google_phone(frame), text="GOOGLE phoNE\n600$", image=googlephone_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=1, pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: macbook_pro_laptop(frame), text="MACBOOK PRO\n1700$", image=macbookpro_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=0, column=2,  pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: thinkpad_laptop(frame), text="THINKPAD LAPTOP\n999.99$", image=thinkpad_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=1, column=0, pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: lg_dryer(frame),text="LG DRYER\n600$", image=dryer_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=250, height=250, anchor="n", compound = "top").grid(row=1, column=1, padx=2, pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: lg_washing_machine(frame),text="LG WASHING MACHINE\n600$", image=washingmachine_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=1, column=2, padx=2, pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: twenty_inch_monitor(frame),text="20in Monitor\n109.99$", image=inmonitor_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=2, column=0, padx=2, pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: twentyseven_inch_4k_gaming_monitor(frame),text="27in 4k Gaming Monitor\n149.99$", image=gamingmonitor_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=2, column=1, padx=2, pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: twentyseven_inch_fhd_monitor(frame),text="27in FHD Monitor\n379.99$",image=fhdmonitor_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=2, column=2, padx=2, pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: thirtyfour_inch_ultrawide_monitor(frame),text="34in Ultrawide Monitor\n389.99$", image=ultrawidemonitor_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=3, column=0, padx=2, pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: flatscreen_tv(frame),text="Flatscreen TV\n300$", image=tv_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=3, column=1, padx=2, pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: aa_batteries(frame),text="AA Batteries\n2.99$", image=aabatteries_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=3, column=2, padx=2, pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: aaa_batteries(frame),text="AAA Batteries\n3.84$", image=aaabatteries_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=6, column=0, padx=2, pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: apple_airpods_headphones(frame),text="Airpods\n150$", image=airpod_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=4, column=0, padx=2, pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: wired_headphones(frame),text="Wired Headphones\n11.99$", image=wiredheadphones_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=4, column=1, padx=2, pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: bose_soundsport_headphones(frame),text="Soundsport Headphones\n99.99$", image=soundheadphones_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=4, column=2, padx=2, pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: var_e_badd_phone(frame),text="Varrebadd phone\n400$", image=phone_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=5, column=0, padx=2, pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: usb_c_charging_cable(frame),text="USBC Charging cable\n11.95$", image=chargingcable_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=5, column=1, padx=2, pady = 5)
    CTkButton(master=sanPhamScroll, command=lambda: lightning_charging_cable(frame),text="Lightning Charging cable\n14.95$", image=lightningcable_img,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFFFFF",font=("Arial Bold", 20), corner_radius=12, width=210, height=250, anchor="n", compound = "top").grid(row=5, column=2, padx=2, pady = 5)



# Create the left frame
left_frame = CTkFrame(master=app, fg_color="#000000", width=220, height=650, corner_radius=0)
left_frame.pack_propagate(False)
left_frame.pack(fill="y", side="left", anchor="n")


# Create the left frame
right_frame = CTkFrame(master=app, fg_color="#000000", width=220, height=650, corner_radius=0)
right_frame.pack_propagate(False)
right_frame.pack(fill="y", side="right", anchor="n") 

# Notes
def run_notes_script():
    subprocess.run(["python", "Notes.py"])
notes_frame = CTkFrame(master=right_frame, fg_color="#363636", width=190, height=305, corner_radius=12)
notes_frame.pack_propagate(False)
taoNotes = CTkButton(master=notes_frame, text="*", text_color="black", command=run_notes_script, fg_color="white", height=10, width =10)
taoNotes.place(relx =0.8, rely=0.1, anchor="center")
notes_frame.place(relx=0.5, rely =0.5, anchor = "center")
title = CTkLabel(master = notes_frame, text = "NOTES", text_color = "#ffffff", font=("Arial Bold", 20))
title.place(relx=0.5, rely=0.1, anchor="center")
CTkTextbox(master = notes_frame,  font=("Arial Bold", 18),text_color="#000000", fg_color="#CCCCCC", height=245, width=170).place(relx=0.5, rely=0.57, anchor="center")

#QR 
def run_qr_script():
    subprocess.run(["python", "QR.py"])
taoQr = CTkButton(master=right_frame, text="Create QR",text_color="black", command=run_qr_script, fg_color="white")
taoQr.place(relx =0.5, rely=0.8, anchor="center")

#Time
def update_time():
    string = time.strftime("%H:%M:%S %p")
    clock.delete(0, tk.END)
    clock.insert(0, string)
    right_frame.after(1000, update_time)

clock = CTkEntry(master=right_frame, fg_color="#111111", bg_color="#111111", height=20, width=90)
clock.place(relx=0.5, rely=0.9, anchor="center")
update_time()


# Load images
logo_img_data = Image.open(r"hinh_anh\hình minh họa\TTECH.png")
home_img_data = Image.open(r"hinh_anh\hình minh họa\home-7-512.png")
order_img_data = Image.open(r"hinh_anh\hình minh họa\add_order.png")
product_img_data = Image.open(r"hinh_anh\hình minh họa\iphone-512.png")
cus_img_data = Image.open(r"hinh_anh\hình minh họa\user-5-512.png")
warehouse_img_data = Image.open(r"hinh_anh\hình minh họa\Warehouse-Icon-Transparent.png")
sold_img_data = Image.open(r"hinh_anh\hình minh họa\order.png")
iphone_img_data = Image.open(r"hinh_anh\hình sản phẩm\iphone.jpeg")
googlephone_img_data = Image.open(r"hinh_anh\hình sản phẩm\google phone.webp")
macbookpro_img_data = Image.open(r"hinh_anh\hình sản phẩm\macbook pro laptop.jpg")
thinkpad_img_data = Image.open(r"hinh_anh\hình sản phẩm\thinkpad laptop.jpg")
dryer_img_data = Image.open(r"hinh_anh\hình sản phẩm\lg dryer.jpg")
washingmachine_img_data = Image.open(r"hinh_anh\hình sản phẩm\lg washing machine.jpeg")
inmonitor_img_data = Image.open(r"hinh_anh\hình sản phẩm\20in monitor.jpg")
gamingmonitor_img_data = Image.open(r"hinh_anh\hình sản phẩm\27in 4k gaming monitor.jpg")
fhdmonitor_img_data = Image.open(r"hinh_anh\hình sản phẩm\27in fhd monitor.jpg")
ultrawidemonitor_img_data = Image.open(r"hinh_anh\hình sản phẩm\34ib ultrawide monitor.jpg")
tv_img_data = Image.open(r"hinh_anh\hình sản phẩm\flatscreen tv.jpeg")
aabatteries_img_data = Image.open(r"hinh_anh\hình sản phẩm\aa-batteries.jpg")
aaabatteries_img_data = Image.open(r"hinh_anh\hình sản phẩm\aaa- batteries.webp")
airpod_img_data = Image.open(r"hinh_anh\hình sản phẩm\airpod.jpg")
wiredheadphones_img_data = Image.open(r"hinh_anh\hình sản phẩm\wired headphones.jpg")
soundheadphones_img_data = Image.open(r"hinh_anh\hình sản phẩm\bose soundsport headphones.jpg")
phone_img_data = Image.open(r"hinh_anh\hình sản phẩm\vareebadd phone.webp")
chargingcable_img_data = Image.open(r"hinh_anh\hình sản phẩm\usb c charging cable.jpeg")
lightningcable_img_data = Image.open(r"hinh_anh\hình sản phẩm\lightning charging cable.jpg")
analytics_img_data = Image.open(r"hinh_anh\hình minh họa\analytics-512.png")
search_img_data = Image.open(r"hinh_anh\hình minh họa\search-3-512.png")
notes_img_data = Image.open(r"hinh_anh\hình minh họa\images (1).png")


# Create CTkImages
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(250, 250))
home_img = CTkImage(dark_image=home_img_data, light_image=home_img_data, size=(25,25))
order_img = CTkImage(dark_image=order_img_data, light_image=order_img_data)
product_img = CTkImage(dark_image=product_img_data, light_image=product_img_data, size=(25,25))
cus_img = CTkImage(dark_image=cus_img_data, light_image=cus_img_data, size=(25,25))
warehouse_img = CTkImage(dark_image=warehouse_img_data, light_image=warehouse_img_data, size=(25,25))
sold_img = CTkImage(dark_image=sold_img_data, light_image=sold_img_data, size=(25,25))
iphone_img = CTkImage(dark_image=iphone_img_data, light_image=iphone_img_data,size = (220, 180))
googlephone_img = CTkImage(dark_image=googlephone_img_data, light_image=googlephone_img_data,size = (220, 180))
macbookpro_img = CTkImage(dark_image=macbookpro_img_data, light_image=macbookpro_img_data,size = (220, 180))
thinkpad_img = CTkImage(dark_image=thinkpad_img_data, light_image=thinkpad_img_data,size = (220, 180))
dryer_img = CTkImage(dark_image=dryer_img_data, light_image=dryer_img_data,size = (180, 180))
washingmachine_img = CTkImage(dark_image=washingmachine_img_data, light_image=washingmachine_img_data,size = (220, 180))
inmonitor_img = CTkImage(dark_image=inmonitor_img_data, light_image=inmonitor_img_data,size = (220, 180))
gamingmonitor_img = CTkImage(dark_image=gamingmonitor_img_data, light_image=gamingmonitor_img_data,size = (220, 180))
fhdmonitor_img = CTkImage(dark_image=fhdmonitor_img_data, light_image=fhdmonitor_img_data,size = (220, 180))
ultrawidemonitor_img = CTkImage(dark_image=ultrawidemonitor_img_data, light_image=ultrawidemonitor_img_data,size = (220, 180))
tv_img = CTkImage(dark_image=tv_img_data, light_image=tv_img_data,size = (220, 180))
aabatteries_img = CTkImage(dark_image=aabatteries_img_data, light_image=aabatteries_img_data,size = (220, 180))
aaabatteries_img = CTkImage(dark_image=aaabatteries_img_data, light_image=aaabatteries_img_data,size = (220, 180))
airpod_img = CTkImage(dark_image=airpod_img_data, light_image=airpod_img_data,size = (220, 180))
wiredheadphones_img = CTkImage(dark_image=wiredheadphones_img_data, light_image=wiredheadphones_img_data,size = (220, 180))
soundheadphones_img = CTkImage(dark_image=soundheadphones_img_data, light_image=soundheadphones_img_data,size = (220, 180))
phone_img = CTkImage(dark_image=phone_img_data, light_image=phone_img_data,size = (220, 180))
chargingcable_img = CTkImage(dark_image=chargingcable_img_data, light_image=chargingcable_img_data,size = (220, 180))
lightningcable_img = CTkImage(dark_image=lightningcable_img_data, light_image=lightningcable_img_data,size = (220, 180))
analytics_img = CTkImage(dark_image=analytics_img_data, light_image=analytics_img_data, size=(25,25))
search_img = CTkImage(dark_image=search_img_data, light_image=search_img_data, size=(25,25))
notes_img = CTkImage(dark_image=notes_img_data, light_image=notes_img_data, size=(15,15))

# Add logo image to left frame
photo_label = CTkLabel(master=right_frame, text="", image=None)
photo_label.place(relx=0.5, rely=0.18, anchor="center")

def get_latest_photo():
    image_files = glob.glob("hinh_anh/dang_nhap/users/*.jpg") + glob.glob("hinh_anh/dang_nhap/users/*.jpeg") + glob.glob("hinh_anh/dang_nhap/users/*.png")
    image_files.sort(key=os.path.getmtime, reverse=True)
    if image_files:
        image_file = image_files[0]
        image = Image.open(image_file)
        image = image.resize((150, 200))
        photo_image = ImageTk.PhotoImage(image)
        photo_label.configure(image=photo_image)
        photo_label.image = photo_image
        photo_label.update()
get_latest_photo()


CTkButton(master=left_frame, image=logo_img, text="", fg_color="transparent", anchor="w").pack(anchor="center", ipady=7, pady=(50, 0))
CTkButton(master=left_frame, image=home_img, text="Trang chủ", command=trangChu, fg_color="transparent", font=("Arial Bold", 18), hover_color="#0000FF", anchor="w").pack(anchor="center", ipady=7, pady=(50, 0))
CTkButton(master=left_frame, image=order_img, text="Đơn hàng", command=donHang, fg_color="transparent", font=("Arial Bold", 18), hover_color="#0000FF", anchor="w").pack(anchor="center", ipady=7, pady=(32, 0))
CTkButton(master=left_frame, image=warehouse_img, text="Kho hàng", command = khoHang, fg_color="transparent", font=("Arial Bold", 18), hover_color="#0000FF", anchor="w").pack(anchor="center", ipady=7, pady=(32, 0))
trangChu()
app.mainloop()
