# Choose a random park to visit
# 9-26-2020

import random, tkinter

from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as tkt


######################## Globals #############################
FILE_NAME = "parks.txt"
FILE_LENGTH = 30

###############################################################


######################## Set up GUI #############################
# window setup
window = Tk()
window.title("Parks")
frame_a = ttk.Frame(window, padding="100 100 100 100")
frame_a.pack()

# set up text boxes
firstLabel = StringVar()
ttk.Label(frame_a, textvariable=firstLabel).grid(column=4, row=4, sticky=(W, E))
firstLabel.set('Choose a park by number')
inputBox = ttk.Entry(frame_a, width = 30, textvariable = StringVar())
inputBox.grid(column=6, row=4, sticky=W)
inputBox.insert(END, '')

# set up button
enterButton = ttk.Button(frame_a, text = "Pick a park", width = 15, command = lambda: pickAPark() )
enterButton.grid(column=6, row=50, sticky=W)
###############################################################

######################## Functions ############################
def pickAPark():
    lines = [i for i in open(FILE_NAME).readlines()]
    userNum = inputBox.get()
    if userNum != "":
        try: 
            num = int(userNum)
        except: 
            print("That's not a valid integer. BYE! \n")
            sys.exit()
    else:    
        num = random.randint(0,FILE_LENGTH)

    parkName = lines[num]
    displ(parkName)
    print(num) # for debug


def displ(parkName): 
    textbox = tkt.ScrolledText(master = frame_a, width = 35, height = 4)
    textbox.grid(column = 6, row = 25)
    textbox.insert(END, 'You chose: ' + parkName + '\n')
    textbox.see(END)

###############################################################

####################### Future Work ###########################
# implement "closer" and "farther" buttons so the user can narrow the search
# improve aesthetics
# insert photos
# make the distances the value in the key-value pair
# implement "list" feature to list all the possible parks
# scrape nearby parks from online
# integrate with Google Maps API?

###############################################################

def main():
    window.mainloop()
    
if __name__=="__main__":
    main()
