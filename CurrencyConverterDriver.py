#Importing the module
from CurrencyConverterClass import CurrencyConvert 
from tkinter import *

def main():
    # Make window
    tk = Tk()
    tk.title("Currency Converter")
    tk.geometry("400x250")

    #Run the class
    CurrencyConvert(tk)
    
    #Run the Program
    tk.mainloop()

if __name__ == "__main__":
    main()