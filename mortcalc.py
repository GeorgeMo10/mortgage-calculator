from tkinter import *
from tkinter import filedialog
root=Tk()
root.title('Mortgage Calculator by George')
root.geometry("500x800")

#import house image

#my_text=Text(root,width=18, height=10, font=("Helvetica", 16))
#my_text.pack(pady=20)
#def add_image():
   # global my_image
   # my_image = PhotoImage(file="assets/house.png")
    #my_text.image_create(END, image=my_image)
#image_button = Button(root, text ="add image", command = add_image)
#image_button.pack(pady=5)

    
#calculation / loan with apr within timeframe
def payment():
    if LOANENTRY.get()and INTERESTENTRY.get() and TIMEENTRY.get():
        #define variables
        years= int(TIMEENTRY.get())
        months = years * 12
        rate= float(INTERESTENTRY.get())
        loan = int(LOANENTRY.get())
        monthlyRate= rate / 100 /12
        #calc of loan / interest / years
        calc = (monthlyRate / (1-(1 +monthlyRate)**(-months))) * loan
        payment = calc
        #format calc
        payment = f"{payment:,.2f}"
        PAYMENT.config(text =f"Monthly payment: ${payment}")
        #if user chooses to add taxes or other yearly expenses It will get added to calc
        if INSURANCEENTRY.get() or PROPERTYTAXENTRY.get() or FEESENTRY.get():
            #define variables
            monthlyPayment= float(INSURANCEENTRY.get()) 
            monthlyPayment1= float(PROPERTYTAXENTRY.get())
            monthlyPayment2= float(FEESENTRY.get())
            monthlyPayments = monthlyPayment + monthlyPayment1 + monthlyPayment2
            #adds taxes to calc
            total = calc + (monthlyPayments // 12)
            total = f"{total:,.2f}"
            PAYMENT.config(text =f"Monthly payment: ${total}")
            
            
            
    else:
        PAYMENT.config(text="Please Enter Data!")

    
#outer line label and title of frame"
LABELFRAME=LabelFrame(root,text="Mortgage Calculator")
LABELFRAME.pack(pady=70)

FRAME=Frame(LABELFRAME)
FRAME.pack(pady=30, padx=40)

#Create labels of Loan,interest,and time with fonts
LOANFRAME= Label(FRAME, text = "Loan Amount")
LOANENTRY= Entry(FRAME, font =("Times", 24, "bold italic"))

INTERESTFRAME= Label(FRAME, text = "interest Amount\n (in decimals)")
INTERESTENTRY= Entry(FRAME, font =("Times", 24, "bold italic"))
                 
TIMEFRAME= Label(FRAME, text = "Time Amount\n(yrs)")
TIMEENTRY= Entry(FRAME, font =("Times", 24, "bold italic"))

# taxes + other fees accounted for(optional)
INSURANCEFRAME= Label(FRAME, text = "Insurance Amount\n Per Year \n (optional)")
INSURANCEENTRY= Entry(FRAME, font =("Times", 24, "bold italic"))

PROPERTYTAXFRAME= Label(FRAME, text = "PropertyTax \n Per year \n (optional)")
PROPERTYTAXENTRY= Entry(FRAME, font =("Times", 24, "bold italic"))

FEESFRAME= Label(FRAME, text = "Other Yearly fees \n Per Year \n (optional)")
FEESENTRY= Entry(FRAME, font =("Times", 24, "bold italic"))

#call frames to screen / use grid system to place locations on screen
LOANFRAME.grid(row= 0, column= 0) 
LOANENTRY.grid(row= 0, column= 1)

INTERESTFRAME.grid(row= 1, column= 0)
INTERESTENTRY.grid(row= 1, column= 1, pady=20)

TIMEFRAME.grid(row= 2, column= 0)
TIMEENTRY.grid(row= 2, column= 1,pady=20)

INSURANCEFRAME.grid(row= 3, column= 0) 
INSURANCEENTRY.grid(row= 3, column= 1)

PROPERTYTAXFRAME.grid(row= 4, column= 0)
PROPERTYTAXENTRY.grid(row= 4, column= 1, pady=20)

FEESFRAME.grid(row= 5, column= 0)
FEESENTRY.grid(row= 5, column= 1)
#create button

BUTTON= Button(LABELFRAME, text = "Calculate Payment", command=payment)
BUTTON.pack(pady=20)

#output/ outside of frame/ call
PAYMENT= Label(root,text="",font=("times", 18))
PAYMENT.pack(pady=20)                     
                     
root.mainloop()
