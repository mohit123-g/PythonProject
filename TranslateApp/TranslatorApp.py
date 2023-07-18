from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# import googletrans
from googletrans import Translator,LANGUAGES
import textblob

root=Tk()
root.title("Google Translator")
root.geometry("1080x500")
root.resizable(False,False)
root.configure(background="black")



def label_change():
     c=combo1.get()
     c1=combo2.get()
     label1['text']=c
     label2['text']=c1
     root.after(800,label_change)


# def change(text="type",src="English",dest="Hindi"):
#      texts=Translator()
#      trans1=texts.translate(text=text1.get(1.0,END),src=combo1.get(),dest=combo2.get())
#      text2.delete(1.0,END)
#      text2.insert(END,trans1.text)

     

# def d():
#       s=combo1.get()
#       d=combo2.get()
#       masg=text1.get(1.0,END)
#       textget=change(text=masg,src=s,dest=d)
#       text2.delete(1.0,END)
#       print(masg)

#       text2.insert(END,textget)

def change():
     try:
           texts=Translator()
           trans1=texts.translate(text=text1.get(1.0,END),src=combo1.get(),dest=combo2.get())
           text2.delete(1.0,END)
           text2.insert(END,trans1.text)
     except Exception as e:
           messagebox.showerror("Error","Please Select Language")



#icom
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

# frame=Frame(root).pack(side=BOTTOM)
#arrow
arrow_img=PhotoImage(file="arrow.png")
image_label=Label(root,image=arrow_img,width=150)
image_label.place(x=460,y=110)

# language=googletrans.LANGUAGES
languageV=list(LANGUAGES.values())
# lang1=language.keys()

#first combobox
combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo1.place(x=110,y=20)
combo1.set("English")

label1=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
# label1["text"]=combo1.get()
label1.place(x=10,y=50)

#second combobox
combo2=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo2.place(x=730,y=20)
combo2.set("Select Language")

label2=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
# label1["text"]=combo1.get()
label2.place(x=620,y=50)

#first frame
f=Frame(root,bg="Black",bd=5)
text1=Text(f,font="Robote 15",bg="white",relief=GROOVE,wrap=WORD)
f.place(x=10,y=118,width=440,height=300)
text1.place(x=0,y=0,width=430,height=295)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


#second frame
f1=Frame(root,bg="Black",bd=5)
text2=Text(f1,font="Robote 15",bg="white",relief=GROOVE,wrap=WORD)
f1.place(x=620,y=118,width=440,height=300)
text2.place(x=0,y=0,width=430,height=295)


scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)


#translate button
translate1=Button(root,text="Translate",activebackground="white",cursor="hand2",command=change,bd=1,width=15,height=4,bg="blue",fg="white")
translate1.place(x=480,y=290)
label_change()
root.mainloop()