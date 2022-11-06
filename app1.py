
def find_sum():
    n1 = float(entry_firstnumber.get())
    n2 = float(entry_secondnumber.get())
    sum = n1 + n2

    output = "The sum of " + str(n1) + " and " + str(n2) + " is = " + str(sum)

    label_result.configure(text = output)

def find_difference():
    n1 = float(entry_firstnumber.get())
    n2 = float(entry_secondnumber.get())
    difference = n1 - n2

    output = "The difference of " + str(n1) + " and " + str(n2) + " is = " + str(difference)

    label_result.configure(text = output)

def find_product():
    n1 = float(entry_firstnumber.get())
    n2 = float(entry_secondnumber.get())
    product = n1 * n2

    output = "The product of " + str(n1) + " and " + str(n2) + " is = " + str(product)

    label_result.configure(text = output)

def find_quotient():
    n1 = float(entry_firstnumber.get())
    n2 = float(entry_secondnumber.get())
    quotient = n1 / n2

    output = "The quotient after dividing " + str(n1) + " by " + str(n2) + " is = " + str(quotient)

    label_result.configure(text = output)

def find_remainder():
    n1 = float(entry_firstnumber.get())
    n2 = float(entry_secondnumber.get())
    remainder = n1 % n2

    output = "The remainder after dividing " + str(n1) + " by " + str(n2) + " is = " + str(remainder)

    label_result.configure(text = output)


import tkinter


root_window = tkinter.Tk()
root_window.title("Calculator")
root_window.geometry("700x450")
root_window.configure(background = 'navy blue', pady = 10)

#Create a label to display heading
label_heading = tkinter.Label(
    master = root_window,  
    text = 'Simple Calculator',
    background = 'lavender',
    foreground = 'navy blue',
    font = ('Arial', 15, 'bold'),
    padx = 250,
    pady = 5
)

#Create a label to prompt the first number
label_firstnumber = tkinter.Label(
    master = root_window,  
    text = 'Enter the first number',
    background = 'navy blue',
    foreground = 'lavender',
    font = ('Arial', 10, 'bold'),
    padx = 5,
    pady = 10
)

#Create a label to prompt the second number
label_secondnumber = tkinter.Label(
    master = root_window,  
    text = 'Enter the second number',
    background = 'navy blue',
    foreground = 'lavender',
    font = ('Arial', 10, 'bold'),
    padx = 5,
    pady = 10
)

#Create an entry box to accept first number
entry_firstnumber = tkinter.Entry(master = root_window)

#Create an entry box to accept second number
entry_secondnumber = tkinter.Entry(master = root_window)

#Create a button to find the sum
button_findsum = tkinter.Button(
    master = root_window,
    text = "SUM",
    background = 'lavender',
    foreground = 'navy blue',
    font = ('Arial', 10, 'bold'),
    padx = 20,
    command = find_sum
)

#Create a button to find the difference
button_finddifference = tkinter.Button(
    master = root_window,
    text = "DIFFERENCE",
    background = 'lavender',
    foreground = 'navy blue',
    font = ('Arial', 10, 'bold'),
    padx = 20,
    command = find_difference
)

#Create a button to find the product
button_findproduct = tkinter.Button(
    master = root_window,
    text = "PRODUCT",
    background = 'lavender',
    foreground = 'navy blue',
    font = ('Arial', 10, 'bold'),
    padx = 20,
    command = find_product
)

#Create a button to find the quotient
button_findquotient = tkinter.Button(
    master = root_window,
    text = "QUOTIENT",
    background = 'lavender',
    foreground = 'navy blue',
    font = ('Arial', 10, 'bold'),
    padx = 20,
    command = find_quotient
)

#Create a button to find the remainder
button_findremainder = tkinter.Button(
    master = root_window,
    text = "REMAINDER",
    background = 'lavender',
    foreground = 'navy blue',
    font = ('Arial', 10, 'bold'),
    padx = 20,
    command = find_remainder
)

#Create a label to display the result
label_result = tkinter.Label(
    master = root_window,  
    text = 'Output will appear here',
    font = ('Arial', 12, 'bold'),
    background = 'navy blue',
    foreground = 'lavender'
)


#Pack all the widgets
label_heading.pack()

label_firstnumber.pack()
entry_firstnumber.pack()

label_secondnumber.pack()
entry_secondnumber.pack()

button_findsum.pack(pady = 10)
button_finddifference.pack()
button_findproduct.pack(pady = 10)
button_findquotient.pack()
button_findremainder.pack(pady = 10)

label_result.pack(pady = 20)

tkinter.mainloop()