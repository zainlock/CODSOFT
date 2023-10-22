 import random
from tkinter import *

def game(event):
    global player1image,player1ImageLabel,player2image,player2imageLabel,winnerLab
    options=["rock","paper","scissor"]
    user_select=event.widget.cget("text")
    compute_select=random.choice(options)
    print(user_select, compute_select)
    try:
        if(user_select==compute_select):
            print("it's draw")
            
            User_image=PhotoImage(file=f"{str(user_select.lower())}.png")
            Computer_image=PhotoImage(file=f"{str(compute_select.lower())}.png")
            player1ImageLabel.config(image=User_image)
            player1ImageLabel.image=User_image
            player2imageLabel.config(image=Computer_image)
            player2image.image=Computer_image
                
            winnerLab.config(text="It's a Draw")
            game()
                
        elif (user_select=="rock" and compute_select=="scissor")or(user_select=="paper" and compute_select=="rock")or (user_select=="scissor" and compute_select=="paper"):
                User_image=PhotoImage(file=f"{str(user_select.lower())}.png")
                Computer_image=PhotoImage(file=f"{str(compute_select.lower())}.png")
                player1ImageLabel.config(image=User_image)
                player1ImageLabel.image=User_image
                player2imageLabel.config(image=Computer_image)
                player2image.image=Computer_image
                winnerLab.config(text="You win")
                print("You win")
                game()
                
        else:
                User_image=PhotoImage(file=f"{str(user_select.lower())}.png")
                Computer_image=PhotoImage(file=f"{str(compute_select.lower())}.png")
                player1ImageLabel.config(image=User_image)
                player1ImageLabel.image=User_image
                player2imageLabel.config(image=Computer_image)
                player2image.image=Computer_image
                winnerLab.config(text="Computer win")
                print("computer win")
                
                game()
    except:
        pass

if __name__=="__main__":
    window=Tk()
    window.geometry("1300x1000")
    window.title("Rock Paper Scissor Game")
    
    Heading=Label(text="Rock Paper Scissor Game",font="sans-serif 30 italic bold",fg="#6E7B8B")
    Heading.grid(row=0, column=0, pady=10,padx=350)
    
    frame=Frame(window)
    frame.grid(row=1,column=0)
    
    player1=Label(frame,text="You",font="CourierNew, 25 italic bold",fg="#7A7A7A")
    player1.grid(column=0,row=2,padx=150)
    
    
    player2=Label(frame,text="Computer",font="CourierNew, 25 italic bold",fg="#7A7A7A")
    player2.grid(row=2,column=3,padx=150)
    
    player1image=PhotoImage(file="rock.png")
    player1ImageLabel=Label(frame,image=player1image,bg="#E5E5E5",width=490,height=470)
    player1ImageLabel.grid(row=3,column=0)
    
    
    VS_label=Label(frame,text="VS",font="Times, 100 italic bold",fg="black")
    VS_label.grid(column=1,row=3,padx=100)
    
    player2image=PhotoImage(file="rock.png")
    player2imageLabel=Label(frame,image=player2image,bg="#E5E5E5",width=490,height=470)
    player2imageLabel.grid(row=3,column=3)
    
    Button_fream=Frame(window)
    Button_fream.grid(row=5,column=0)
    
    winnerLab=Label(Button_fream,text="Winner",font="Sitka 20 bold italic",fg="#555555")
    winnerLab.grid(row=0,column=3)
    
    Rock_button=Button(Button_fream,text="rock",width=6,height=1,font="Sitka 20 bold italic",fg="#E5E5E5",bg="#808080")
    Rock_button.grid(row=3,column=3,padx=20)
    Rock_button.bind("<Button-1>",game)
    
    Paper_button=Button(Button_fream,text="paper",width=6,height=1,font="Sitka 20 bold italic",fg="#E5E5E5",bg="#808080")
    Paper_button.grid(row=3,column=4)
    Paper_button.bind("<Button-1>",game)
    
    Scissor_button=Button(Button_fream,text="scissor",width=6,height=1,font="Sitka 20 bold italic",fg="#E5E5E5",bg="#808080")
    Scissor_button.grid(row=3,column=1)
    Scissor_button.bind("<Button-1>",game)
    
    window.mainloop()
