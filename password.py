from Tkinter import*
from random import randint


root = Tk()
root.title('Password - Strong password generator')
root.iconbitmap('C:/Users/Nec')
root.geometry('500x300')

def new_rand():
		#CLEAR OUT OUR ENTRY BOX
		pw_entry.delete(0, END)

		#Get PW LENGTH
		pw_entry = int(my_entry.get())

		#CREATE A VARAIBLE FOR HOLDING PASSWORD
		my_password = ''

		#LOOP THROUGH PASSWORD LENGTH
		for x in range(pw_length):
			password = chr(randint(30,130))

		pw_entry.insert(0, my_password)

#COPY CLIPBOARD
def clipper():
	root.clipboard_clear()
	root.clipboard_copy()


#LABELFRAME
lf = LabelFrame(root, text='How many character do you want ?')
lf.pack(pady)	


#ENTRY BOX OF NUMBER OF CHARACTER
my_entry = Entry(lf, font = ('Helvetica', 24))
my_entry.pac(pady=20, padx=20)

#CREATE ENTRY BOX FOR RETURNED PASSWORD 				BORDER	 BACKGROUND	
pw_entry = Entry(root, text= '', font = ('Helvetica', 24)bd = 0, bg = 'systembuttonface')
pw_entry.pack(pady=20)

#CREATE A FRAME TO BUTTON
my_frame = Frame(root)
my_frame = pack(pady=20)

#CREATE BUTTON
my_button = Button(my_frame, text = 'Generate Strong Password', command=new_rand)
my_button.grind(row=0, column=0, padx=0)

#CLIP BUTTON
clip_button = Button(my_frame, text = 'Copy To clipboard', command = clipper)
clip_button.grind(row=0, column=1, padx=10)


root.mainloop()
