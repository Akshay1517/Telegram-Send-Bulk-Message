from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.errors.rpcerrorlist import PeerFloodError
from time import sleep
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox



def main():
	root = tkinter.Tk()
	root.geometry("1400x700")
	image = Image.open('bg.jpg')
	photo_image = ImageTk.PhotoImage(image)
	label = tkinter.Label(root, image = photo_image)
	label.pack()
	L1 = Label(root, text="TELEGRAM", fg='#4B0082', font=("Hoefler Text", 25))
	L1.pack(anchor=CENTER)
	L1.place(height=80, width=250, x=650, y=50)
	L10 = Label(root, text="api_id", bg='#C0C0C0', fg='#4B0082', font=("Hoefler Text", 17))
	L10.pack(anchor=CENTER)
	L10.place(height=40, width=130, x=270, y=200)
	E1 = Entry(root, bd =5, font=("Hoefler Text", 20))
	E1.pack(anchor=CENTER)
	E1.place(height=40, width=650, x=450, y=200)
	L10 = Label(root, text="api_hash", bg='#C0C0C0', fg='#4B0082', font=("Hoefler Text", 17))
	L10.pack(anchor=CENTER)
	L10.place(height=40, width=130, x=270, y=300)
	E2 = Entry(root, bd =5, font=("Hoefler Text", 20))
	E2.pack(anchor=CENTER)
	E2.place(height=40, width=650, x=450, y=300)
	L10 = Label(root, text="Phone Number", bg='#C0C0C0', fg='#4B0082', font=("Hoefler Text", 17))
	L10.pack(anchor=CENTER)
	L10.place(height=40, width=130, x=270, y=500)
	E = Entry(root, bd =5, font=("Hoefler Text", 20))
	E.pack(anchor=CENTER)
	E.place(height=40, width=350, x=450, y=500)
	L10 = Label(root, text="username", bg='#C0C0C0', fg='#4B0082', font=("Hoefler Text", 17))
	L10.pack(anchor=CENTER)
	L10.place(height=40, width=130, x=270, y=400)
	E3 = Entry(root, bd =5, font=("Hoefler Text", 20))
	E3.pack(anchor=CENTER)
	E3.place(height=40, width=650, x=450, y=400)
	B2 = tkinter.Button(root, text ="LOGIN",cursor='man',command=lambda:login(root,E1,E2,E3,E) , activebackground='#01F5FD', activeforeground='blue', bd=10, fg='#4B0082', font=("Arial Black", 18))
	B2.pack(expand=True, fill='both')
	B2.place(bordermode=OUTSIDE, height=55, width=250, x=650, y=600)
	root.mainloop()


def login(root,E1,E2,E3,E):
	api_id = E1.get()
	api_hash = E2.get()
	phone = E.get()
	username = E3.get()
	try:
		client = TelegramClient(username, api_id, api_hash)
		client.connect()
		me = client.get_me()
		if me==None:
			messagebox.showinfo("Error", "Please Input Correct Value")
			root.destroy()
			main()
		else:
			root.destroy()
			s_msg(client)
	except:
		messagebox.showinfo("Error", "Please Input Correct Value")
		root.destroy()
		main()

		
	

def s_msg(client):
	root1 = tkinter.Tk()
	root1.geometry("1400x700")
	root1.configure(background='Black')
	L1 = Label(root1, text="TELEGRAM", fg='#4B0082', font=("Hoefler Text", 25))
	L1.pack(anchor=CENTER)
	L1.place(height=80, width=250, x=650, y=50)
	L10 = Label(root1, text="Enter Channel Link", bg='#C0C0C0', fg='#4B0082', font=("Hoefler Text", 17))
	L10.pack(anchor=CENTER)
	L10.place(height=40, width=200, x=270, y=250)
	E1 = Entry(root1, bd =5, font=("Hoefler Text", 20))
	E1.pack(anchor=CENTER)
	E1.place(height=40, width=650, x=500, y=250)
	E2 = Entry(root1, bd =5, font=("Hoefler Text", 20))
	E2.pack(anchor=CENTER)
	E2.place(height=50, width=10000, x=200, y=350)
	B2 = tkinter.Button(root1, text ="SEND",cursor='man',command=lambda:msg(root1,E1,client,E2) , activebackground='#01F5FD', activeforeground='blue', bd=10, fg='#4B0082', font=("Arial Black", 18))
	B2.pack(expand=True, fill='both')
	B2.place(bordermode=OUTSIDE, height=55, width=250, x=650, y=550)


def msg(root1,E1,client,E2):
	Channel = E1.get()
	LIMIT = 4000
	offset = 0
	output = []
	while True:
		participants = client(GetParticipantsRequest(
			Channel, ChannelParticipantsSearch(''), offset, LIMIT, hash=0))
		if not participants.users:
			break
		for user in participants.users:
			output.append(user.to_dict())
		offset += len(participants.users)
	print('Fetched %s users' % len(output))
	for x in range(0,len(output)):
		q = output[x]['username']
		if q==None:
			print("not exist username")
		else:
			try:
				client.send_message(q,E2.get())
			except PeerFloodError:
				print("PeerFloodError")

main()