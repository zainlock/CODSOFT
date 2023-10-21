from tkinter import * 
import random

def game(event):
    
    global defulteimage,imagelabel,defulteimage1,imagelabel1,winnerLab
    
    option=["Rock","Paper","Scissor"] 
    userselect=event.widget.cget("text")
    computeselect=random.choice(option)
    try:
            if userselect==computeselect:
                userimage=PhotoImage(file=f"{str(userselect.lower())}.png")
                computerimage=PhotoImage(file=f"{str(computeselect.lower())}.png")
                imagelabel.config(image=userimage)
                imagelabel.image=userimage
                
                imagelabel1.config(image=computerimage)
                imagelabel1.image=computerimage
                
                winnerLab.config(text="It's a Draw")
                game()
                
            elif (userselect=="Paper" and computeselect=="Rock") or (userselect=="Scissor" and computeselect=="Paper") or(userselect=="Rock" and computeselect=="Scissor"):
                    
                userimage=PhotoImage(file=f"{str(userselect.lower())}.png")
                computerimage=PhotoImage(file=f"{str(computeselect.lower())}.png")
                imagelabel.config(image=userimage)
                imagelabel.image=userimage
                
                imagelabel1.config(image=computerimage)
                imagelabel1.image=computerimage
                
                
                game()
                
            else:
                
                userimage=PhotoImage(file=f"{str(userselect.lower())}.png")
                computerimage=PhotoImage(file=f"{str(computeselect.lower())}.png")
                imagelabel.config(image=userimage)
                imagelabel.image=userimage
                
                imagelabel1.config(image=computerimage)
                imagelabel1.image=computerimage
                
                winnerLab.config(text="Computer win")
                
                game()
    except:
            pass
#main window
if __name__=="__main__":
    window=Tk()
    window.title("Rock Paper Scissor Game")
    window.geometry("1330x1000")
    heading=Label(text="Rock Paper Scissor Game",font="sans-serif 30 italic bold",fg="#6E7B8B")
    heading.grid(row=0,column=0,pady=10)
    
    frame=Frame(window)
    frame.grid(column=0,row=1)
    
    player1=Label(frame,text="You",font="CourierNew, 20 italic bold",fg="#7A7A7A")
    player1.grid(column=0,row=2,padx=150)
    
    
    player2=Label(frame,text="Computer",font="CourierNew, 20 italic bold",fg="#7A7A7A")
    player2.grid(row=2,column=3,padx=150)
    
    defulteimage=PhotoImage(file="rock.png")
    imagelabel=Label(frame,image=defulteimage,bg="#E5E5E5",width=490,height=470)
    imagelabel.grid(row=3,column=0)
     
    
    VS_label=Label(frame,text="VS",font="Times, 100 italic bold",fg="black")
    VS_label.grid(column=1,row=3,padx=100)
    
    defulteimage1=PhotoImage(file="rock.png")
    imagelabel1=Label(frame,image=defulteimage1,bg="#E5E5E5",width=490,height=470)
    imagelabel1.grid(column=3,row=3)
    
    botton1=Frame(window)
    botton1.grid(row=6,column=0)
    
    winnerLab=Label(botton1,text="Winner",font="Sitka 20 bold italic",fg="#555555")
    winnerLab.grid(row=0,column=3)
    
    
    btn=Button(botton1,text="Rock",width=6,height=1,font="Sitka 20 bold italic",fg="#E5E5E5",bg="#808080")
    btn.grid(row=3,column=3,padx=20)
    btn.bind("<Button-1>",game)
    
    btn1=Button(botton1,text="Paper",width=6,height=1,font="Sitka 20 bold italic",fg="#E5E5E5",bg="#808080")
    btn1.grid(row=3,column=4)
    btn1.bind("<Button-1>",game)
    
    
    btn2=Button(botton1,text="scissor",width=6,height=1,font="Sitka 20 bold italic",fg="#E5E5E5",bg="#808080")
    btn2.grid(row=3,column=1)
    btn2.bind("<Button-1>",game)
    window.mainloop()