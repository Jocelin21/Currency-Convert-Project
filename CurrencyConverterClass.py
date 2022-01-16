from tkinter import *  # import everything from tkinter

# List of the available currencies: Australia, Canada, China, Europe, Indonesia, India, America
currency_list = ["AUD", "CAD", "CNH", "EUR", "IDR", "INR", "USD"]

class CurrencyConvert:
    #Innitializing
    def __init__(self):
        # Make window
        self.tk = Tk()
        self.tk.title("Currency Converter")
        self.tk.geometry("400x250")

        # Setting the Initial Currency Button
        self.variable1 = StringVar(self.tk, currency_list[0])
        self.variable2 = StringVar(self.tk, currency_list[1])

        # First dropdown menu button
        self.currencyOpt1 = OptionMenu(self.tk, self.variable1, *currency_list)
        self.currencyOpt1.config(width=10, fg='#282828', font=('Helvetica', 12))
        self.currencyOpt1.place(x=40, y=10)
        self.currencyOpt1.pack(pady=5)

        # Input the amount of money
        self.moneyOri = Entry(self.tk)
        self.moneyOri.pack(side="top", pady=4)

        # Second dropdown menu button
        self.currencyOpt2 = OptionMenu(self.tk, self.variable2, *currency_list)
        self.currencyOpt2.config(width=10, fg='#282828', font=('Helvetica', 12))
        self.currencyOpt2.place(x=40, y=80)
        self.currencyOpt2.pack()

        # Convert Button
        self.convertButton = Button(self.tk, text="Calulate", command=self.currency)
        self.convertButton.config(height=1, width=10, fg='#282828', font=('Helvetica', 12))
        self.convertButton.pack(pady=8)

        # The result of the converted money
        self.total = StringVar()
        self.money_converted = Label(self.tk, text="", textvariable=self.total)
        self.money_converted.config(fg='#282828', font=('Helvetica', 12))
        self.money_converted.pack(pady=2)

        # From-To labels
        self.from_label = Label(self.tk, text="From", fg='#282828', font=('Helvetica', 12)).place(x=40, y=10)
        self.to_label = Label(self.tk, text="To", fg='#282828', font=('Helvetica', 12)).place(x=40, y=80)
        self.total_label = Label(self.tk, text="Total:", fg='#282828', font=('Helvetica', 12)).place(x=40, y=155)

        # To start the window
        self.tk.mainloop()

    def currency(self):
        # Getting the variable
        self.__currency1 = self.variable1.get()
        self.__currency2 = self.variable2.get()
        self.__money_original = float(self.moneyOri.get())

        # Converting the currency
        if (self.__currency1 == "AUD" and self.__currency2 == "CAD"):
            self.__result = self.__money_original * 0.93
        elif (self.__currency1 == "AUD" and self.__currency2 == "CNH"):
            self.__result = self.__money_original * 4.60
        elif (self.__currency1 == "AUD" and self.__currency2 == "EUR"):
            self.__result = self.__money_original * 0.64
        elif (self.__currency1 == "AUD" and self.__currency2 == "IDR"):
            self.__result = self.__money_original * 10290.06
        elif (self.__currency1 == "AUD" and self.__currency2 == "INR"):
            self.__result = self.__money_original * 54.23
        elif (self.__currency1 == "AUD" and self.__currency2 == "USD"):
            self.__result = self.__money_original * 0.72
        elif (self.__currency1 == "CAD" and self.__currency2 == "AUD"):
            self.__result = self.__money_original * 1.08
        elif (self.__currency1 == "CAD" and self.__currency2 == "CNH"):
            self.__result = self.__money_original * 4.98
        elif (self.__currency1 == "CAD" and self.__currency2 == "EUR"):
            self.__result = self.__money_original * 0.69
        elif (self.__currency1 == "CAD" and self.__currency2 == "IDR"):
            self.__result = self.__money_original * 11108.11
        elif (self.__currency1 == "CAD" and self.__currency2 == "INR"):
            self.__result = self.__money_original * 58.54
        elif (self.__currency1 == "CAD" and self.__currency2 == "USD"):
            self.__result = self.__money_original * 0.78
        elif (self.__currency1 == "CNH" and self.__currency2 == "AUD"):
            self.__result = self.__money_original * 0.22
        elif (self.__currency1 == "CNH" and self.__currency2 == "CAD"):
            self.__result = self.__money_original * 0.20
        elif (self.__currency1 == "CNH" and self.__currency2 == "EUR"):
            self.__result = self.__money_original * 0.14
        elif (self.__currency1 == "CNH" and self.__currency2 == "IDR"):
            self.__result = self.__money_original * 2231.32
        elif (self.__currency1 == "CNH" and self.__currency2 == "INR"):
            self.__result = self.__money_original * 11.76
        elif (self.__currency1 == "CNH" and self.__currency2 == "USD"):
            self.__result = self.__money_original * 0.16
        elif (self.__currency1 == "EUR" and self.__currency2 == "AUD"):
            self.__result = self.__money_original * 1.57
        elif (self.__currency1 == "EUR" and self.__currency2 == "CAD"):
            self.__result = self.__money_original * 1.45
        elif (self.__currency1 == "EUR" and self.__currency2 == "CNH"):
            self.__result = self.__money_original * 7.22
        elif (self.__currency1 == "EUR" and self.__currency2 == "IDR"):
            self.__result = self.__money_original * 16105.12
        elif (self.__currency1 == "EUR" and self.__currency2 == "INR"):
            self.__result = self.__money_original * 84.87
        elif (self.__currency1 == "EUR" and self.__currency2 == "USD"):
            self.__result = self.__money_original * 1.13
        elif (self.__currency1 == "IDR" and self.__currency2 == "AUD"):
            self.__result = self.__money_original * 0.000097
        elif (self.__currency1 == "IDR" and self.__currency2 == "CAD"):
            self.__result = self.__money_original * 0.000090
        elif (self.__currency1 == "IDR" and self.__currency2 == "CNH"):
            self.__result = self.__money_original * 0.00045
        elif (self.__currency1 == "IDR" and self.__currency2 == "EUR"):
            self.__result = self.__money_original * 0.000062
        elif (self.__currency1 == "IDR" and self.__currency2 == "INR"):
            self.__result = self.__money_original * 0.0053
        elif (self.__currency1 == "IDR" and self.__currency2 == "USD"):
            self.__result = self.__money_original * 0.000070
        elif (self.__currency1 == "INR" and self.__currency2 == "AUD"):
            self.__result = self.__money_original * 0.018
        elif (self.__currency1 == "INR" and self.__currency2 == "CAD"):
            self.__result = self.__money_original * 0.017
        elif (self.__currency1 == "INR" and self.__currency2 == "CNH"):
            self.__result = self.__money_original * 0.085
        elif (self.__currency1 == "INR" and self.__currency2 == "EUR"):
            self.__result = self.__money_original * 0.012
        elif (self.__currency1 == "INR" and self.__currency2 == "IDR"):
            self.__result = self.__money_original * 189.76
        elif (self.__currency1 == "INR" and self.__currency2 == "USD"):
            self.__result = self.__money_original * 0.013
        elif (self.__currency1 == "USD" and self.__currency2 == "AUD"):
            self.__result = self.__money_original * 1.38
        elif (self.__currency1 == "USD" and self.__currency2 == "CAD"):
            self.__result = self.__money_original * 1.28
        elif (self.__currency1 == "USD" and self.__currency2 == "CNH"):
            self.__result = self.__money_original * 6.37
        elif (self.__currency1 == "USD" and self.__currency2 == "EUR"):
            self.__result = self.__money_original * 0.88
        elif (self.__currency1 == "USD" and self.__currency2 == "IDR"):
            self.__result = self.__money_original * 14216.70
        elif (self.__currency1 == "USD" and self.__currency2 == "INR"):
            self.__result = self.__money_original * 74.92
        else:
            self.__result = self.__money_original

        #Set the Result and formatting the commas
        self.total.set("{:,}".format(self.__result))