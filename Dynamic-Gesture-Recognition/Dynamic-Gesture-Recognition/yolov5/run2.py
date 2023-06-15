import os
from tkinter import *


root = Tk()
root.title('Tkinter Apps')
root.resizable(width=TRUE, height=TRUE)
root.geometry('{}x{}'.format(1300, 900))

headerbanner=Frame(root,width=1290,height=100,bg='khaki')
headerbanner.grid(row=0,column=0,padx=5,pady=2)

#bodycontainer=Frame(root,width=790,height=380,bg='tan')
#bodycontainer.grid(row=1,column=0,padx=5,pady=0)
#bodycontainer.grid_propagate(True) # Stop grid() from resizing bodycontainer
def show_msg():
   #import detect
   #detect.run()
   os.system("python detect.py --weights best.pt --img 416 --conf 0.8 --source 0")
   root.update()
  # bodycontainer=Frame(root,bg = "green",bd=10,width=100,  
   #          height=50,cursor = "target").pack(side=TOP)  
   #bodycontainer.grid(row=1,column=0,padx=5,pady=0)

 # creating a button instance
btn = Button(root, text = 'Start !', bd = '5',
                          command = show_msg)
   
btn.place(x=540, y=0)

btn = Button(root, text = 'Quit !', bd = '5',
                          command = root.destroy)
   
btn.place(x=600, y=0)
#buttoncontainer=Frame(bodycontainer,width=50,height=300,bg='powder blue')
#buttoncontainer.grid(row=0,column=0)




root.mainloop()



#os.system("python detect.py --weights best.pt --img 416 --conf 0.8 --source 0")
