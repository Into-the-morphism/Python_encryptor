from tkinter import *
import pybase64
from tkinter import messagebox
root = Tk()
root.title('Encryption/Decryption Base64')
root.iconbitmap('icon/one.ico')
root.geometry('500x400')


def encrypt():
    secret =my_text.get(1.0, END)
    my_text.delete(1.0, END)

    if my_entry.get() == 'password':
        secret = secret.encode('ascii')

        secret = pybase64.b64encode(secret)

        secret = secret.decode('ascii')

        my_text.insert(END, secret)
    else:
        messagebox.showwarning('Incorrect!', 'Incorrect Password, Try Again! ')
def decrypt():
    secret = my_text.get(1.0, END)
    my_text.delete(1.0, END)


    if my_entry.get() == 'password':
        secret = secret.encode('ascii')

        secret = pybase64.b64decode(secret)

        secret = secret.decode('ascii')

        my_text.insert(END, secret)
    else:
        messagebox.showwarning('Incorrect!', 'Incorrect Password, Try Again! ')
def clear():
    my_text.delete(1.0 , END)
    my_entry.delete(0, END)
my_frame = Frame(root)
my_frame.pack(pady=20)

encr_button = Button(my_frame, text='Encrypt',font=('Helvetica', 18), command=encrypt)
encr_button.grid(row=0, column=0)

decr_button = Button(my_frame, text='Decrypt',font=('Helvetica', 18), command=decrypt)
decr_button.grid(row=0, column=1,padx=10)

encr_button = Button(my_frame, text='Clear',font=('Helvetica', 18), command=clear)
encr_button.grid(row=0, column=2)

enc_label = Label(root, text='Encrypt/Decrypt Text ...', font=('Helvetica', 14))
enc_label.pack()
my_text = Text(root, width=57, height=10)
my_text.pack(pady=10)


password_label = Label(root, text='Enter your password', font=('Helvetica', 14))

my_entry = Entry(root, font=('Helvetica', 18),width=35,  show='*')
my_entry.pack(pady=10)

password_label.pack()
root.mainloop()