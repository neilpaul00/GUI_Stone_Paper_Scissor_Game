from cProfile import label
from random import choices
from tkinter import*
from PIL import Image,ImageTk
from random import randint
#main window
root=Tk()
root.title("Stone Paper Scissor")
root.configure(background="teal")

#picture
rock_img=ImageTk.PhotoImage(Image.open ("rock-user.png"))
paper_img=ImageTk.PhotoImage(Image.open ("paper-user.png"))
scissor_img=ImageTk.PhotoImage(Image.open ("scissor-user.png"))
rock_img_comp=ImageTk.PhotoImage(Image.open ("rock.png"))
paper_img_comp=ImageTk.PhotoImage(Image.open ("paper.png"))
scissor_img_comp=ImageTk.PhotoImage(Image.open ("scissor.png"))

# insert pic
user_label = Label(root,image=scissor_img,bg="teal")
comp_label = Label(root,image=scissor_img_comp,bg="teal")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=60)

#scores
playerScore=Label(root,text=0,font=100,bg="teal",fg="yellow")
computerScore=Label(root,text=0,font=100,bg="teal",fg="yellow")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicator
user_indicator=Label(root,font=200,text="USER",bg="teal",fg="white")
vs_indicator=Label(root,font=200,text="VS",bg="teal",fg="black")
comp_inicator=Label(root,font=200,text="COMPUTER",bg="teal",fg="white")
user_indicator.grid(row=0,column=3)
vs_indicator.grid(row=0,column=2)
comp_inicator.grid(row=0,column=1)

#messages
msg=Label(root,font=150,bg="teal",fg="yellow")
msg.grid(row=3,column=2)

#update messages
def updateMessage(x):
    msg['text']=x

#update user score
def updateUserScore():
    score=int(playerScore["text"])
    score+=1
    playerScore["text"]=str(score)
#update computer score
def updateCompScore():
    score=int(computerScore["text"])
    score+=1
    computerScore["text"]=str(score)

#check winner
def checkWin(player,computer):
    if player==computer:
        updateMessage("ITS A TIE!!")
    elif player=="rock":
        if computer=="paper":
            updateMessage("YOU LOOSE")
            updateCompScore()
        else:
             updateMessage("YOU WON")
             updateUserScore()
    elif player=="paper":
        if computer=="scissor":
            updateMessage("YOU LOOSE")
            updateCompScore()
        else:
             updateMessage("YOU WON")
             updateUserScore()
    elif player=="scissor":
        if computer=="rock":
            updateMessage("YOU LOOSE")
            updateCompScore()
        else:
             updateMessage("YOU WON")
             updateUserScore()  
    else:
        pass      
#Update choices
choices=["rock","paper","scissor"]
def updateChoice(x):
#for computer
    compChoice=choices[randint(0,2)]

    if compChoice=="rock":
          comp_label.configure(image=rock_img_comp)
    elif compChoice=="paper":
         comp_label.configure(image=paper_img_comp) 
    else:
         comp_label.configure(image=scissor_img_comp)      

#for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img) 

    checkWin(x,compChoice)
#button
rock=Button(root,width=20,height=2,text="ROCK",bg="#FF3E4d",fg="black",command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="yellow",fg="black",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="green",fg="black",command=lambda:updateChoice("scissor")).grid(row=2,column=3)
root.mainloop()