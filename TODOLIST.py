#!/usr/bin/env python
# coding: utf-8

# In[21]:


import tkinter as tk

def add_task():
    task=entry.get()
    if task!="":
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)


def delete():
    selected=listbox.curselection()
    if selected:
        listbox.delete(selected)


win=tk.Tk()
win.title("to do list")
win.geometry("300x400")
win.configure(bg="blue")

lbl=tk.Label(win,text="Please enter your task",fg="white",bg="lightblue")
lbl.pack()
entry=tk.Entry(win,font=("Arial",12),bg="pink")
entry.pack(pady=10)

btn=tk.Button(win,text="add task",command=add_task,bg="purple",fg="white")
btn.pack()

lbl=tk.Label(win,text="Your task",fg="white",bg="lightblue")
lbl.pack()
listbox=tk.Listbox(win,width=30,height=15,bg="pink")
listbox.pack(pady=10)

delete_btn=tk.Button(win,text="DELET SELECTED TAST",command=delete,bg="purple",fg="white")
delete_btn.pack(pady=10)


win.mainloop()



# In[ ]:





# In[ ]:




