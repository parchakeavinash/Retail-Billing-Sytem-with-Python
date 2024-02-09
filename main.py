from tkinter import *
from tkinter import messagebox
import random
import os, tempfile, smtplib

bill_number = random.randint(500, 1000)

def clear():

    bathSoapEntry.delete(0, END)
    faceCreamEntry.delete(0, END)
    faceWashEntry.delete(0, END)
    hairSprayEntry.delete(0, END)
    hairgelEntry.delete(0, END)
    BodyLotionEntry.delete(0, END)

    bathSoapEntry.insert(0, 0)
    faceCreamEntry.insert(0, 0)
    faceWashEntry.insert(0, 0)
    hairSprayEntry.insert(0, 0)
    hairgelEntry.insert(0, 0)
    BodyLotionEntry.insert(0, 0)

    RiceEntry.delete(0, END)
    oilEntry.delete( 0, END)
    daalEntry.delete(0, END)
    wheatEntry.delete(0, END)
    sugarEntry.delete(0, END)
    teaEntry.delete( 0, END)

    RiceEntry.insert(0, 0)
    oilEntry.insert(0, 0)
    daalEntry.insert(0, 0)
    wheatEntry.insert(0, 0)
    sugarEntry.insert(0, 0)
    teaEntry.insert(0, 0)

    maazaEntry.delete(0, END)
    PepsiEntry.delete(0, END)
    spriteEntry.delete(0, END)
    smoothEntry.delete(0, END)
    fruitiEntry.delete(0, END)
    coco_colaEntry.delete(0, END)

    maazaEntry.insert(0, 0)
    PepsiEntry.insert(0, 0)
    spriteEntry.insert(0, 0)
    smoothEntry.insert(0, 0)
    fruitiEntry.insert(0, 0)
    coco_colaEntry.insert(0, 0)

    cosmeticPriceEntry.delete(0, END)
    groceryPriceEntry.delete(0, END)
    drinksPriceEntry.delete(0, END)

    cosmeticTaxEntry.delete(0, END)
    groceryTaxEntry.delete(0, END)
    drinksTaxEntry.delete(0, END)

    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    billEntry.delete(0, END)

    textarea.delete(1.0,END)




def send_email():
    def send_gmail():
        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = email_textarea.get(1.0, END)
            ob.sendmail(senderEntry.get(), recieverEntry.get(), message)
            ob.quit()
            messagebox.showinfo("Success", "Email is successfully send", parent=window1)
            window1.destroy()
        except:
            messagebox.showerror("Error", "Something went wrong, Please try again", parent=window1)

    if textarea.get(1.0, END) == "\n":
        messagebox.showerror("Error", "Bill is empty")
    else:
        window1 = Toplevel()
        window1.grab_set()
        window1.title("send email")
        window1.config(bg="gray20")
        window1.resizable(0, 0)

        senderFrame = LabelFrame(window1, text="SENDER", font=("arial", 16, "bold"), bd=6, bg="gray20", fg="white")
        senderFrame.grid(row=0, column=0, padx=40, pady=20)

        senderLabel = Label(senderFrame, text="Sender's Email", font=("arial", 14, "bold"), bg="gray20", fg="white")
        senderLabel.grid(row=0, column=0, padx=10, pady=8)

        senderEntry = Entry(senderFrame, font=("arial", 14, "bold"), bd=2, width=23, relief=RIDGE)
        senderEntry.grid(row=0, column=1, padx=10, pady=8)

        passwordLabel = Label(senderFrame, text="Password", font=("arial", 14, "bold"), bg="gray20", fg="white")
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=("arial", 14, "bold"), bd=2, width=23, relief=RIDGE, show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        recipientFrame = LabelFrame(window1, text="RECIPIENT", font=("arial", 16, "bold"), bd=6, bg="gray20",
                                    fg="white")
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recieverLabel = Label(recipientFrame, text="Email Address", font=("arial", 14, "bold"), bg="gray20", fg="white")
        recieverLabel.grid(row=0, column=0, padx=10, pady=8)

        recieverEntry = Entry(recipientFrame, font=("arial", 14, "bold"), bd=2, width=23, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text="Message", font=("arial", 14, "bold"), bg="gray20", fg="white")
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea = Text(recipientFrame, font=("arial", 14, "bold"), bd=2, relief=SUNKEN, width=42, height=11)
        email_textarea.grid(row=2, column=0, columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(1.0, textarea.get(1.0, END).replace("=", "").replace("-", "").replace("\t\t\t", "\t\t"))

        send_button = Button(window1, text="Send", font=("arial", 16, "bold"), width=15, command=send_gmail)
        send_button.grid(row=2, column=0, pady=20)
        window1.mainloop()


def print_bill():
    if textarea.get(1.0, END) == "\n":
        messagebox.showerror("Error", "Bill is empty")
    else:
        file = tempfile.mktemp(".txt")
        open(file, "w").write(textarea.get(1.0, END))
        os.startfile(file, "Print")


def search_bill():
    bill_number = int(billEntry.get())  # Assuming billEntry contains the bill number as an integer
    file_name = f"{bill_number}.txt"

    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            textarea.delete(1.0, "end")  # Clear existing content in textarea
            textarea.insert("end", file.read())  # Insert content of the file into the textarea
    else:
        messagebox.showerror("Error", "Invalid Bill Number")


def save_bill():
    global bill_number
    result = messagebox.askyesno("Confirm", "Do you want to save the bill")
    if result:
        bill_content = textarea.get(1.0, END)
        file = open(f"{bill_number}.txt", "w")
        file.write(bill_content)
        file.close()
        messagebox.showinfo("Success", "file is saved successfully")
        bill_number = random.randint(500, 1000)


# functionality part
def bill_area():
    if nameEntry.get() == "" and phoneEntry.get() == "":
        messagebox.showerror("Error", "Customer Details Are Required")

    elif cosmeticPriceEntry.get() == "" and groceryPriceEntry.get() == "" and drinksPriceEntry.get() == "":
        messagebox.showerror("Error", "No Products Are Selected")

    elif cosmeticPriceEntry.get() == "0 Rs" and groceryPriceEntry.get() == "0 Rs" and drinksPriceEntry.get() == "0 Rs":
        messagebox.showerror("Error", "No Products Are Selected")
    else:
        textarea.delete(1.0, END)

        textarea.insert(END, "\t\t***Welcome Customer***\n\n")
        textarea.insert(END, f"Bill Number: {bill_number}\n")
        textarea.insert(END, f"Customer Name: {nameEntry.get()}\n")
        textarea.insert(END, f"Phone Name: {phoneEntry.get()}\n")
        textarea.insert(END, "=======================================================\n")
        textarea.insert(END, "Proudct\t\t\tQty\t\t\tPrice\n")
        textarea.insert(END, "=======================================================\n")
        if bathSoapEntry.get() != "0":
            textarea.insert(END, f"Bath Soup:\t\t\t{bathSoapEntry.get()}\t\t\t{soapPrice} Rs\n")
        if faceCreamEntry.get() != "0":
            textarea.insert(END, f"Face Cream:\t\t\t{bathSoapEntry.get()}\t\t\t{facecreamPrice} Rs\n")
        if faceWashEntry.get() != "0":
            textarea.insert(END, f"Face Wash:\t\t\t{bathSoapEntry.get()}\t\t\t{faceWashPrice} Rs\n")
        if hairSprayEntry.get() != "0":
            textarea.insert(END, f"Hair Spray:\t\t\t{bathSoapEntry.get()}\t\t\t{hairsprayPrice} Rs\n")
        if hairgelEntry.get() != "0":
            textarea.insert(END, f"Hair gel:\t\t\t{bathSoapEntry.get()}\t\t\t{hairgelPrice} Rs\n")
        if BodyLotionEntry.get() != "0":
            textarea.insert(END, f"Body Lotion:\t\t\t{bathSoapEntry.get()}\t\t\t{bodylotionPrice} Rs\n")

        if RiceEntry.get() != "0":
            textarea.insert(END, f"Rich:\t\t\t{RiceEntry.get()}\t\t\t{ricePrice} Rs\n")
        if daalEntry.get() != "0":
            textarea.insert(END, f"Daal:\t\t\t{daalEntry.get()}\t\t\t{daalPrice} Rs\n")
        if oilEntry.get() != "0":
            textarea.insert(END, f"oil:\t\t\t{oilEntry.get()}\t\t\t{oilPrice} Rs\n")
        if wheatEntry.get() != "0":
            textarea.insert(END, f"Wheat:\t\t\t{wheatEntry.get()}\t\t\t{wheatPrice} Rs\n")
        if sugarEntry.get() != "0":
            textarea.insert(END, f"Sugar:\t\t\t{sugarEntry.get()}\t\t\t{sugarPrice} Rs\n")
        if teaEntry.get() != "0":
            textarea.insert(END, f"Tea:\t\t\t{teaEntry.get()}\t\t\t{teaPrice} Rs\n")

        if maazaEntry.get() != "0":
            textarea.insert(END, f"Maaza:\t\t\t{maazaEntry.get()}\t\t\t{maazaPrice} Rs\n")
        if PepsiEntry.get() != "0":
            textarea.insert(END, f"Pepsi\t\t\t{daalEntry.get()}\t\t\t{daalPrice} Rs\n")
        if spriteEntry.get() != "0":
            textarea.insert(END, f"Sprite\t\t\t{spriteEntry.get()}\t\t\t{spritePrice} Rs\n")
        if smoothEntry.get() != "0":
            textarea.insert(END, f"Smooth\t\t\t{smoothEntry.get()}\t\t\t{smoothPrice} Rs\n")
        if fruitiEntry.get() != "0":
            textarea.insert(END, f"Fruit\t\t\t{fruitiEntry.get()}\t\t\t{fruitPrice} Rs\n")
        if coco_colaEntry.get() != "0":
            textarea.insert(END, f"Tea\t\t\t{coco_colaEntry.get()}\t\t\t{coco_colaPrice} Rs\n")

        textarea.insert(END, "-------------------------------------------------------\n")

        if cosmeticTaxEntry.get() != "0.0 Rs":
            textarea.insert(END, f"\nCosmetic Tax\t\t\t\t{cosmeticTaxEntry.get()}")
        if groceryTaxEntry.get() != "0.0 Rs":
            textarea.insert(END, f"\nGrocery Tax\t\t\t\t{groceryTaxEntry.get()}")
        if drinksTaxEntry.get() != "0.0 Rs":
            textarea.insert(END, f"\nDrinks Tax\t\t\t\t{drinksTaxEntry.get()}")

        textarea.insert(END, f"\n\nTotal Bill: \t\t\t\t{totalbill} Rs\n")
        textarea.insert(END, "-------------------------------------------------------")
        save_bill()


def total():
    global soapPrice, facecreamPrice, faceWashPrice, hairsprayPrice, hairgelPrice, bodylotionPrice
    global ricePrice, daalPrice, oilPrice, wheatPrice, sugarPrice, teaPrice
    global maazaPrice, pepsiPrice, spritePrice, smoothPrice, fruitPrice, coco_colaPrice
    global totalbill
    soapPrice = int(bathSoapEntry.get()) * 20
    facecreamPrice = int(faceCreamEntry.get()) * 50
    faceWashPrice = int(faceWashEntry.get()) * 100
    hairsprayPrice = int(hairSprayEntry.get()) * 150
    hairgelPrice = int(hairgelEntry.get()) * 80
    bodylotionPrice = int(BodyLotionEntry.get()) * 60

    totalcosmeticPrice = soapPrice + facecreamPrice + faceWashPrice + hairgelPrice + hairgelPrice + bodylotionPrice
    cosmeticPriceEntry.delete(0, END)
    cosmeticPriceEntry.insert(0, f"{totalcosmeticPrice} Rs")
    cosmetictax = round(totalcosmeticPrice * 0.12)
    cosmeticTaxEntry.delete(0, END)
    cosmeticTaxEntry.insert(0, f"{cosmetictax} Rs")

    # grocery functionality calculation
    ricePrice = int(RiceEntry.get()) * 30
    daalPrice = int(daalEntry.get()) * 100
    oilPrice = int(oilEntry.get()) * 120
    wheatPrice = int(wheatEntry.get()) * 50
    sugarPrice = int(sugarEntry.get()) * 40
    teaPrice = int(teaEntry.get()) * 80

    totalgroceryPrice = ricePrice + daalPrice + oilPrice + wheatPrice + sugarPrice + teaPrice
    groceryPriceEntry.delete(0, END)
    groceryPriceEntry.insert(0, f"{totalgroceryPrice} Rs")
    grocerytax = totalgroceryPrice * 0.05
    groceryTaxEntry.delete(0, END)
    groceryTaxEntry.insert(0, f"{grocerytax} Rs")

    # cold drinks functionality calculation
    maazaPrice = int(maazaEntry.get()) * 50
    pepsiPrice = int(PepsiEntry.get()) * 20
    spritePrice = int(spriteEntry.get()) * 30
    smoothPrice = int(smoothEntry.get()) * 20
    fruitPrice = int(fruitiEntry.get()) * 45
    coco_colaPrice = int(coco_colaEntry.get()) * 90

    totalcoldDrinksPrice = maazaPrice + pepsiPrice + spritePrice + smoothPrice + fruitPrice + coco_colaPrice
    drinksPriceEntry.delete(0, END)
    drinksPriceEntry.insert(0, f"{totalcoldDrinksPrice} Rs")
    drinksTax = round(totalcoldDrinksPrice * 0.08)
    drinksTaxEntry.delete(0, END)
    drinksTaxEntry.insert(0, f"{drinksTax} Rs")

    totalbill = round(
        totalcoldDrinksPrice + totalcosmeticPrice + totalgroceryPrice + cosmetictax + grocerytax + drinksTax)


# Gui part
window = Tk()
window.title("Retail Billing System")
window.geometry("1270x685")
window.iconbitmap("icons.ico")

# window.resizable(False, False)

headingLabel = Label(window, text="Retail Billing System", font=("times new roman", 30, "bold"), bg="gray20", fg="gold",
                     bd=12, relief="groove")
headingLabel.pack(fill=X)

customer_labelframe = LabelFrame(window, text="Customer Details", font=("times new roman", 15, "bold"), fg="gold",
                                 bg="gray20", bd="8", relief="groove")
customer_labelframe.pack(fill=X)

nameLabel = Label(customer_labelframe, text="Name", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
nameLabel.grid(row=0, column=0, padx=20)

nameEntry = Entry(customer_labelframe, font=("Arial", 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8)

phoneLabel = Label(customer_labelframe, text="Phone Number", font=("times new roman", 15, "bold"), bg="gray20",
                   fg="white")
phoneLabel.grid(row=0, column=2, padx=20, pady=2)

phoneEntry = Entry(customer_labelframe, font=("Arial", 15), bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8)

billLabel = Label(customer_labelframe, text="Bill Number", font=("times new roman", 15, "bold"), bg="gray20",
                  fg="white")
billLabel.grid(row=0, column=4, padx=20, pady=2)

billEntry = Entry(customer_labelframe, font=("Arial", 15), bd=7, width=18)
billEntry.grid(row=0, column=5, padx=8)

search_button = Button(customer_labelframe, text="search", font=("Arial", 12), bd=7, width=10, command=search_bill)
search_button.grid(row=0, column=6, padx=20, pady=8)

productFrame = Frame(window)
productFrame.pack()

cosmeticFrame = LabelFrame(productFrame, text="Cosmetic", font=("times new roman", 15, "bold"), fg="gold", bg="gray20",
                           bd="8", relief="groove")
cosmeticFrame.grid(row=0, column=0)

bathSoupLabel = Label(cosmeticFrame, text="Bath Soap", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
bathSoupLabel.grid(row=0, column=0, pady=9, padx=10, sticky="w")

bathSoapEntry = Entry(cosmeticFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
bathSoapEntry.grid(row=0, column=1, pady=9, padx=10)
bathSoapEntry.insert(0, 0)

faceCreamLabel = Label(cosmeticFrame, text="Face Cream", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
faceCreamLabel.grid(row=1, column=0, pady=9, padx=10, sticky="w")

faceCreamEntry = Entry(cosmeticFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
faceCreamEntry.grid(row=1, column=1, pady=9, padx=10)
faceCreamEntry.insert(0, 0)

faceWashLabel = Label(cosmeticFrame, text="Face Wash", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
faceWashLabel.grid(row=2, column=0, pady=9, padx=10, sticky="w")

faceWashEntry = Entry(cosmeticFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
faceWashEntry.grid(row=2, column=1, pady=9, padx=10)
faceWashEntry.insert(0, 0)

hairSprayLabel = Label(cosmeticFrame, text="Hair Spray", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
hairSprayLabel.grid(row=3, column=0, pady=9, padx=10, sticky="w")

hairSprayEntry = Entry(cosmeticFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
hairSprayEntry.grid(row=3, column=1, pady=9, padx=10)
hairSprayEntry.insert(0, 0)

hairgelLabel = Label(cosmeticFrame, text="Hair gel", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
hairgelLabel.grid(row=4, column=0, pady=9, padx=10, sticky="w")

hairgelEntry = Entry(cosmeticFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
hairgelEntry.grid(row=4, column=1, pady=9, padx=10)
hairgelEntry.insert(0, 0)

BodyLotionLabel = Label(cosmeticFrame, text="Body Lotion", font=("times new roman", 15, "bold"), bg="gray20",
                        fg="white")
BodyLotionLabel.grid(row=5, column=0, pady=9, padx=10, sticky="w")

BodyLotionEntry = Entry(cosmeticFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
BodyLotionEntry.grid(row=5, column=1, pady=9, padx=10)
BodyLotionEntry.insert(0, 0)

groceryFrame = LabelFrame(productFrame, text="Grocery", font=("times new roman", 15, "bold"), fg="gold", bg="gray20",
                          bd="8", relief="groove")
groceryFrame.grid(row=0, column=1)

RiceLabel = Label(groceryFrame, text="Rice", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
RiceLabel.grid(row=0, column=0, pady=9, padx=10, sticky="w")

RiceEntry = Entry(groceryFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
RiceEntry.grid(row=0, column=1, pady=9, padx=10)
RiceEntry.insert(0, 0)

oilLabel = Label(groceryFrame, text="Oil", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
oilLabel.grid(row=1, column=0, pady=9, padx=10, sticky="w")

oilEntry = Entry(groceryFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
oilEntry.grid(row=1, column=1, pady=9, padx=10)
oilEntry.insert(0, 0)

daalLabel = Label(groceryFrame, text="Daal", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
daalLabel.grid(row=2, column=0, pady=9, padx=5, sticky="w")

daalEntry = Entry(groceryFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
daalEntry.grid(row=2, column=1, pady=9, padx=10)
daalEntry.insert(0, 0)

wheatLabel = Label(groceryFrame, text="Wheat", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
wheatLabel.grid(row=3, column=0, pady=9, padx=10, sticky="w")

wheatEntry = Entry(groceryFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
wheatEntry.grid(row=3, column=1, pady=9, padx=10)
wheatEntry.insert(0, 0)

sugarLabel = Label(groceryFrame, text="Sugar", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
sugarLabel.grid(row=4, column=0, pady=9, padx=10, sticky="w")

sugarEntry = Entry(groceryFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
sugarEntry.grid(row=4, column=1, pady=9, padx=10)
sugarEntry.insert(0, 0)

teaLabel = Label(groceryFrame, text="Tea", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
teaLabel.grid(row=5, column=0, pady=9, padx=10, sticky="w")

teaEntry = Entry(groceryFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
teaEntry.grid(row=5, column=1, pady=9, padx=10)
teaEntry.insert(0, 0)

drinkFrame = LabelFrame(productFrame, text="Cold Drinks", font=("times new roman", 15, "bold"), fg="gold", bg="gray20",
                        bd="8", relief="groove")
drinkFrame.grid(row=0, column=3)

maazaLabel = Label(drinkFrame, text="Maaza", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
maazaLabel.grid(row=0, column=0, pady=9, padx=10, sticky="w")

maazaEntry = Entry(drinkFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
maazaEntry.grid(row=0, column=1, pady=9, padx=10)
maazaEntry.insert(0, 0)

PepsiLabel = Label(drinkFrame, text="Pepsi", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
PepsiLabel.grid(row=1, column=0, pady=9, padx=10, sticky="w")

PepsiEntry = Entry(drinkFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
PepsiEntry.grid(row=1, column=1, pady=9, padx=10)
PepsiEntry.insert(0, 0)

spriteLabel = Label(drinkFrame, text="Sprite", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
spriteLabel.grid(row=2, column=0, pady=9, padx=10, sticky="w")

spriteEntry = Entry(drinkFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
spriteEntry.grid(row=2, column=1, pady=9, padx=10)
spriteEntry.insert(0, 0)

smoothLabel = Label(drinkFrame, text="Smooth", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
smoothLabel.grid(row=3, column=0, pady=9, padx=10, sticky="w")

smoothEntry = Entry(drinkFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
smoothEntry.grid(row=3, column=1, pady=9, padx=10)
smoothEntry.insert(0, 0)

fruitiLabel = Label(drinkFrame, text="Fruit", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
fruitiLabel.grid(row=4, column=0, pady=9, padx=10, sticky="w")

fruitiEntry = Entry(drinkFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
fruitiEntry.grid(row=4, column=1, pady=9, padx=10)
fruitiEntry.insert(0, 0)

coco_colaLabel = Label(drinkFrame, text="Coca Cola", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
coco_colaLabel.grid(row=5, column=0, pady=9, padx=10, sticky="w")

coco_colaEntry = Entry(drinkFrame, font=("times new roman", 15, "bold"), bd=5, width=10)
coco_colaEntry.grid(row=5, column=1, pady=9, padx=10)
coco_colaEntry.insert(0, 0)

billFrame = Frame(productFrame, bd=8, relief=GROOVE)
billFrame.grid(row=0, column=4, padx=10)

billAreaLabel = Label(billFrame, text="Bill Area", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE)
billAreaLabel.pack(fill=X)

scrollbar = Scrollbar(billFrame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(billFrame, height=18, width=55, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame = LabelFrame(window, text="Bill Menu", font=("times new roman", 15, "bold"), fg="gold", bg="gray20",
                           bd="8", relief="groove")
billmenuFrame.pack()

cosmeticPriceLabel = Label(billmenuFrame, text="Cosmetic", font=("times new roman", 14, "bold"), bg="gray20",
                           fg="white")
cosmeticPriceLabel.grid(row=0, column=0, pady=6, padx=10, sticky="w")

cosmeticPriceEntry = Entry(billmenuFrame, font=("times new roman", 14, "bold"), bd=5, width=10)
cosmeticPriceEntry.grid(row=0, column=1, pady=6, padx=10)

groceryPriceLabel = Label(billmenuFrame, text="Grocery", font=("times new roman", 14, "bold"), bg="gray20", fg="white")
groceryPriceLabel.grid(row=1, column=0, pady=6, padx=10, sticky="w")

groceryPriceEntry = Entry(billmenuFrame, font=("times new roman", 14, "bold"), bd=5, width=10)
groceryPriceEntry.grid(row=1, column=1, pady=6, padx=10)

drinksPriceLabel = Label(billmenuFrame, text="Cold Drinks", font=("times new roman", 14, "bold"), bg="gray20",
                         fg="white")
drinksPriceLabel.grid(row=2, column=0, pady=6, padx=10, sticky="w")

drinksPriceEntry = Entry(billmenuFrame, font=("times new roman", 14, "bold"), bd=5, width=10)
drinksPriceEntry.grid(row=2, column=1, pady=6, padx=10)

cosmeticTaxLabel = Label(billmenuFrame, text="Cosmetic Tax", font=("times new roman", 14, "bold"), bg="gray20",
                         fg="white")
cosmeticTaxLabel.grid(row=0, column=2, pady=6, padx=10, sticky="w")

cosmeticTaxEntry = Entry(billmenuFrame, font=("times new roman", 14, "bold"), bd=5, width=10)
cosmeticTaxEntry.grid(row=0, column=3, pady=6, padx=10)

groceryTaxLabel = Label(billmenuFrame, text="Grocery Tax", font=("times new roman", 14, "bold"), bg="gray20",
                        fg="white")
groceryTaxLabel.grid(row=1, column=2, pady=6, padx=10, sticky="w")

groceryTaxEntry = Entry(billmenuFrame, font=("times new roman", 14, "bold"), bd=5, width=10)
groceryTaxEntry.grid(row=1, column=3, pady=6, padx=10)

drinksTaxLabel = Label(billmenuFrame, text="Cold Drinks Tax", font=("times new roman", 14, "bold"), bg="gray20",
                       fg="white")
drinksTaxLabel.grid(row=2, column=2, pady=6, padx=10, sticky="w")

drinksTaxEntry = Entry(billmenuFrame, font=("times new roman", 14, "bold"), bd=5, width=10)
drinksTaxEntry.grid(row=2, column=3, pady=6, padx=10)

buttonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)

totalButton = Button(buttonFrame, text="Total", font=("Arial", 16, "bold"), bg="gray20", fg="white", bd=5, width=8,
                     pady=10, command=total)
totalButton.grid(row=0, column=0, pady=20, padx=5)

billButton = Button(buttonFrame, text="Bill", font=("Arial", 16, "bold"), bg="gray20", fg="white", bd=5, width=8,
                    pady=10, command=bill_area)
billButton.grid(row=0, column=1, pady=20, padx=5)

emailButton = Button(buttonFrame, text="Email", font=("Arial", 16, "bold"), bg="gray20", fg="white", bd=5, width=8,
                     pady=10, command=send_email)
emailButton.grid(row=0, column=2, pady=20, padx=5)

pritnButton = Button(buttonFrame, text="Print", font=("Arial", 16, "bold"), bg="gray20", fg="white", bd=5, width=8,
                     pady=10, command=print_bill)
pritnButton.grid(row=0, column=3, pady=20, padx=5)

clearButton = Button(buttonFrame, text="Clear", font=("Arial", 16, "bold"), bg="gray20", fg="white", bd=5, width=8,
                     pady=10,command=clear)
clearButton.grid(row=0, column=4, pady=20, padx=5)

window.mainloop()
