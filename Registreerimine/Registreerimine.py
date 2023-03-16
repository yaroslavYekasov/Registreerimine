from tkinter import *

usernames = []
passwords = []

def register():
    username = username_entry.get()
    password = password_entry.get()
    if username in usernames:
        result_label.config(text="Vabandust, see kasutajanimi on juba võetud.")
    else:
        usernames.append(username)
        passwords.append(password)
        result_label.config(text="Registreerimine edukas.")

def authorize():
    username = username_entry.get()
    password = password_entry.get()
    if username not in usernames:
        result_label.config(text="Vabandust, seda kasutajanime ei ole olemas.")
    elif password != passwords[usernames.index(username)]:
        result_label.config(text="Vabandust, vale parool.")
    else:
        result_label.config(text="Autoriseerimine õnnestus.")

def change_password():
    username = username_entry.get()
    current_password = current_password_entry.get()
    new_password = new_password_entry.get()
    if username not in usernames:
        result_label.config(text="Vabandust, seda kasutajanime ei ole olemas.")
    elif current_password != passwords[usernames.index(username)]:
        result_label.config(text="Vabandust, vale parool.")
    else:
        passwords[usernames.index(username)] = new_password
        result_label.config(text="Parool muutus edukalt.")

def forgot_password():
    username = username_entry.get()
    new_password = new_password_entry.get()
    if username not in usernames:
        result_label.config(text="Vabandust, seda kasutajanime ei ole olemas.")
    else:
        passwords[usernames.index(username)] = new_password
        result_label.config(text="Parooli lähtestamine õnnestus.")


window = Tk()
window.title("Registreerimine")
window.geometry("400x300")

username_label = Label(window, text="Kasutajanimi:")
username_label.pack()

username_entry = Entry(window)
username_entry.pack()

password_label = Label(window, text="Parool:")
password_label.pack()

password_entry = Entry(window, show="*")
password_entry.pack()

current_password_label = Label(window, text="Praegune parool:")
current_password_label.pack()

current_password_entry = Entry(window, show="*")
current_password_entry.pack()

new_password_label = Label(window, text="Uus parool:")
new_password_label.pack()

new_password_entry = Entry(window, show="*")
new_password_entry.pack()

register_button = Button(window, text="registreerimine", command=register)
register_button.pack()

authorize_button = Button(window, text="autoriseerimine", command=authorize)
authorize_button.pack()

change_password_button = Button(window, text="parooli muutmine", command=change_password)
change_password_button.pack()

forgot_password_button = Button(window, text="unustanud parooli taastamine", command=forgot_password)
forgot_password_button.pack()

result_label = Label(window, text="")
result_label.pack()

window.mainloop()