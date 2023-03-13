import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
	pass

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

input1 = tkinter.Entry(width=40)
input1.configure(bg="#FEFAE0")
input1.grid(column=1, row=1, columnspan=2)

input2 = tkinter.Entry(width=40)
input2.configure(bg="#FEFAE0")
input2.grid(column=1, row=2, columnspan=2)

input3 = tkinter.Entry(width=21)
input3.configure(bg="#FEFAE0")
input3.grid(column=1, row=3)

generate_button = tkinter.Button(text="Generate password", command=generate_password, width=14)
generate_button.grid(column=2, row=3)

save_button = tkinter.Button(text="Save", command=generate_password, width=33)
save_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
