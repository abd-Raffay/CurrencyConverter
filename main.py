from tkinter import *
from tkinter import ttk
import requests


# reset button function
def reset():
    # reset all the states
    currency_select.delete(0, "end")
    convert_into.delete(0, "end")
    amount_to_convert.delete(0, "end")
    converted.destroy()

# convert button function
def convert():
    global converted
    # converted currency label
    converted = Label(font=("Arial", 10, "bold"))

    # save amount
    amount = int(amount_to_convert.get())

    # saving the user input of currency to convert from
    currency_1 = currency_select.get()[-4:-1]

    # saving the currency to convert to
    currency_2 = convert_into.get()[-4:-1]

    URL = "https://openexchangerates.org/api/latest.json?app_id=4060505fbda74b9183e43079284f89ce"
    response = requests.get(URL).json()

    # fetch required values from API rates
    val_c1 = response["rates"][currency_1]
    val_c2 = response["rates"][currency_2]

    # display converted currency
    converted.config(text=f"\n1 {currency_1} = {round(val_c2 / val_c1, 4)} {currency_2}\n\n{amount:,.2f} {currency_1}"
                          f" = {round(val_c2 / val_c1 * amount, 2):,.2f} {currency_2}")
    converted.grid(column=2, row=16)


# initialize tkinter window
app = Tk()
app.title("Currency Converter ")
app.geometry("270x450")

# main heading of GUI
heading = Label(text="Currency Converter by\nAbdul Raffay", font=("Arial", 10, "bold"))
heading.grid(column=2, row=0)


# initializing currencies to use in the program
currencies = ['Australian Dollar (AUD)', 'Chinese Yuan (CNY)', 'Euro (EUR)', 'Japanese Yen (JPY)',
              'Pakistani Rupee (' 'PKR)', 'Pound sterling (GBP)', 'Russian Ruble (RUB)', 'Saudi Riyal (SAR)',
              'United Arab Emirates Dirham (''AED)', 'United States Dollar (USD)',
              'Indian Rupee	(INR)', 'Mexican Peso (MXN)', 'Hong Kong Dollar (HKD)', 'Canadian Dollar (CAD)']


# labeling and setting the dropdown/combobox for currency selection
n = StringVar()

# entry box for user to enter amount he/she wants to convert
enter_amount = Label(text="\n\nAmount to Convert:", font=("Arial", 10, "bold"))
enter_amount.grid(column=2, row=3)

amount_to_convert = Entry(width=23)
amount_to_convert.grid(column=2, row=4, pady=10)


# dropdown  of currencies to convert from
currency_select_from = Label(text="From: ", font=("Arial", 10, "bold"))
currency_select_from.grid(column=1, row=7)

currency_select = ttk.Combobox(app, values=currencies, width=20, textvariable=n)
currency_select.grid(column=2, row=7)


# dropdown for currency to convert into
convert_to = Label(text="To:", font=("Arial", 10, "bold"))
convert_to.grid(column=1, row=8, pady=10)

m = StringVar()
convert_into = ttk.Combobox(app, values=currencies, width=20, textvariable=m)
convert_into.grid(column=2, row=8)
converted = Label()

# convert button
convert_button = Button(text="Convert", font=("Arial", 10, "bold"), width=20, command=convert)
convert_button.grid(column=2, row=9, pady=10)

# reset button
reset_button = Button(text="Reset", font=("Arial", 10, "bold"), width=20, command=reset)
reset_button.grid(column=2, row=11)

# label for Result
result_label = Label(text="\nResults: ", font=("Arial", 10 ,"bold"))
result_label.grid(column=1, row=15)

# tkinter window loop
app.mainloop()
