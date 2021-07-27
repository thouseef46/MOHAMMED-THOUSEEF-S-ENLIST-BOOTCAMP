
#final project
#project Title-URL shortner

import pyperclip
import pyshorteners
from tkinter import*

root=Tk()
root.geometry("400x200")
root.title("URL Shortener")
root.configure(bg="#49A")
url =StringVar()
url_address = StringVar()

def urlshorteners():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root,text="my URL Shorteners",font="popins").pack(pady=10)
Entry(root,textvariable=url).pack(pady=5)
Button(root,text="Generate short URL",command=urlshorteners).pack(pady=7)
Entry(root,textvariable=url_address).pack(pady=5)
Button(root, text="copy URL",command = copyurl).pack(pady=5)

root.mainloop()

