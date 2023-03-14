import tkinter
from tkinter import messagebox
import pandas
import random
import pyperclip
import pandas as pd
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
	label4.config(text="")
	nr_letters = random.randint(8, 14)
	nr_symbols = random.randint(2, 6)
	nr_numbers = random.randint(2, 6)

	password = []

	for ltr in range(0, nr_letters, 1):
		add = random.choice(letters)
		password.append(add)

	for sym in range(0, nr_symbols, 1):
		add = random.choice(symbols)
		pos = random.randint(0, len(password))
		password.insert(pos, add)

	for num in range(0, nr_numbers, 1):
		add = random.choice(numbers)
		pos = random.randint(0, len(password))
		password.insert(pos, add)

	random.shuffle(password)
	password_str = "".join(password)
	input3.delete(0, tkinter.END)
	input3.insert(0, password_str)
	pyperclip.copy(password_str)
	label4.config(text="Password ready for paste")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
	label4.config(text="")
	website = input1.get()
	username = input2.get()
	password = input3.get()

	if not website or not username or not password:
		label4.config(text="Please fill all fields")
		return
	is_ok = messagebox.askokcancel(title=website, message=f"These are your details:\n Username: {username} \n "
																	f"Password: {password} \n Is it ok to save?")
	if is_ok:
		try:
			data = pandas.read_excel("data.xlsx", sheet_name="Sheet1", )
			new_dict = data.to_dict()
			print(new_dict)

		except FileNotFoundError:
			new_dict = {
				'website': {},
				'login': {},
				'password': {}
			}
		position = -1
		for n in new_dict["website"]:
			if new_dict["website"][n] == website:
				if new_dict["login"][n] == username:
					position = n
		if position == -1:
			next_nr = len(new_dict["website"])
			new_dict["website"][next_nr] = website
			new_dict["login"][next_nr] = username
			new_dict["password"][next_nr] = password
		else:
			new_dict["password"][position] = password

		df1 = pd.DataFrame.from_dict(new_dict)
		df1.to_excel("data.xlsx", index=False)
		input1.delete(0, tkinter.END)
		input3.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password keeper")
window.config(padx=40, pady=40, bg="white")

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0, bg="white")
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, row=0, columnspan=3)

label1 = tkinter.Label(text="Website:", bg="white", anchor="e", width=15)
label1.config(padx=10, pady=5)
label1.grid(column=0, row=1)

label2 = tkinter.Label(text="Email/Username:", bg="white", anchor="e", width=15)
label2.config(padx=10, pady=5)
label2.grid(column=0, row=2)

label3 = tkinter.Label(text="Password:", bg="white", anchor="e", width=15)
label3.config(padx=10, pady=5)
label3.grid(column=0, row=3)

label4 = tkinter.Label(text="", bg="white", anchor="e", width=25, fg="red", font=("Arial", 12, "bold"))
label4.config(padx=0, pady=5)
label4.grid(column=1, row=5, columnspan=2)


input1 = tkinter.Entry(width=50)
input1.focus()
input1.configure(bg="#FEFAE0")
input1.grid(column=1, row=1, columnspan=2)

input2 = tkinter.Entry(width=50)
input2.configure(bg="#FEFAE0")
input2.insert(0, "ansokolkin@gmail.com")
input2.grid(column=1, row=2, columnspan=2)

input3 = tkinter.Entry(width=31)
input3.configure(bg="#FEFAE0")
input3.grid(column=1, row=3)

generate_button = tkinter.Button(text="Generate password", command=generate_password, width=14)
generate_button.grid(column=2, row=3)

save_button = tkinter.Button(text="Save", command=save_password, width=43)
save_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
