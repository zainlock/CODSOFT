from tkinter import *
from tkinter import ttk
class todo:
    def __init__(self,window):
        self.window=window
        self.window.title('To-Do-List')
        self.window.geometry('640x710+350+250')
        self.label =Label(self.window,text="To-Do-List",
                          font='CourierNew, 25 italic bold',width=10,bd=3,bg='pink',fg='white')
        self.label.pack(side='top',fill=BOTH)
        
        self.task_label=Label(self.window,text="Enter a task",
                          font='CourierNew, 16 italic bold',width=15,bd=4,bg='pink',fg='white')
        self.task_label.place(x = 50, y = 60) 
        
        self.text1=Listbox(self.window,height=13,bd=5,width=20,font='ariel, 20 italic bold',bg='pink',fg='white')
        self.text1.place(x=300,y=60)
        
        self.text=Text(self.window,height=1,bd=5,width=20,
                       font='CourierNew, 15 italic bold',bg="white",fg="pink")
        self.text.place(x=20,y=120)
        
        def add_task():
            get_con=self.text.get(1.0,END)
            self.text1.insert(END,get_con)
            with open ('task_store.txt','a') as file:
                file.write(get_con)
                file.seek(0)
                file.close()
                self.text.delete(1.0,END)
        def delete_txt():
            delete_task=self.text1.curselection()
            look=self.text1.get(delete_task)
            with open ('task_store.txt','r+') as f:
                new_f=f.readlines()
                f.seek(0)
                for line in new_f:
                    item=str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.text1.delete(delete_task)
        with open ('task_store.txt','r') as file:
            read=file.readline()
            for i in read:
                ready=i.split()
                self.text1.insert(END,ready)
            file.close()
        self.Button=Button(window, text="add task",height=1,bd=4,width=24,
                           font="CourierNew, 10 italic bold",bg='pink',fg='white',command=add_task)
        self.Button.place(x=20,y=170)
        
        self.Button_delet=Button(window, text="Remove Task",height=1,bd=4,width=24,
                           font="CourierNew, 10 italic bold",bg='pink',fg='white',command=delete_txt)
        self.Button_delet.place(x=20,y=250)
                
def main():
    window=Tk()
    ui=todo(window)
    window.mainloop()
if __name__=="__main__":
    main()