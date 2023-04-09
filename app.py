# მოდულების იმპორტაცია კამათელისათვის
import tkinter
from PIL import Image, ImageTk
import random

# ფანჯარა აპლიკაციისთვის
root = tkinter.Tk()
root.geometry('400x400')
root.title('კამათელი')



BlankLine = tkinter.Label(root, text="")
BlankLine.pack()
# ფონტი
HeadingLabel = tkinter.Label(root, text="კამათლის სიმულატორი",
   fg = "light green",
     bg = "dark green",
     font = "Helvetica 16 bold italic")
HeadingLabel.pack()
# სურათები
dice = ['die1.png', 'die2.png', 'die3.png', 
    'die4.png', 'die5.png', 'die6.png']

# შემთხვევით გენერირება
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

ImageLabel.pack( expand=True)

# ფუნქციის აქტივაცია
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # სურათის განახლება
    ImageLabel.configure(image=DiceImage)
    
    ImageLabel.image = DiceImage
# ღილაკი და ბრძანება
button = tkinter.Button(root, text='გააგორე', fg='black', command=rolling_dice)
button.pack( expand=True)


# ფანჯრის გამოძახება
root.mainloop()