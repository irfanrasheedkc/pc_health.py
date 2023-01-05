#!/usr/bin/env python
# coding: utf-8

# In[2]:





# In[ ]:


import tkinter as tk 
import shutil#importing packages
import psutil


top = tk.Tk()  
top.geometry("750x270")
top.title(" PC HealthCheaker ")

#this function is used to check disk usage
def check_disk_usage():
    disk=e1.get()
    du=shutil.disk_usage(disk)
    free=du.free/du.total*100
    l3= tk.Label(top,text = "Disk Usage of your computer :  ").grid(row = 2, column = 1)
    l4= tk.Label(top,text = free).grid(row = 2, column = 2)
    return free

#this function is used to check cpu usage
def check_cpu_usage():
    usage=psutil.cpu_percent(0.1)
    l5= tk.Label(top,text = "CPU Usage of your computer :  ").grid(row = 5, column = 1)
    l6= tk.Label(top,text = usage).grid(row = 5, column = 2)
    return usage
    
def healthchcker():
    if check_disk_usage()<50 and check_cpu_usage()<50:
        l8= tk.Label(top,text = "Everything is okay :)").grid(row = 8, column = 2)
        
    else:
        l8= tk.Label(top,text = "Error!! Error!S Bad Health!!!").grid(row = 8, column = 2)

    
 
#Create label


l = tk.Label(top, text = "Know your PC Health")
l.config(font =("Courier", 14))

top.grid_columnconfigure(10, minsize=400)

l1 = tk.Label(top,text = "CHECK YOUR DISK UASAGE",bg='light pink').grid(row = 0, column = 0) 
e1 = tk.Entry(top)
e1.grid(row = 0, column = 1)
e1.insert(0,'C:\\')


l11 = tk.Label(top).grid(row = 5, column = 0)
l12 = tk.Label(top).grid(row = 6, column = 0)

l2 = tk.Label(top,text = "CHECK YOUR CPU UASAGE",bg='light pink').grid(row = 4, column = 0) 
B1 = tk.Button(top, text = "Submit",command = check_disk_usage,bd = '5',bg='white').grid(row = 0, column = 2) 

B2 = tk.Button(top, text = "Submit",command = check_cpu_usage,bd = '5',bg='white').grid(row = 4, column = 1) 

l7 = tk.Label(top,text = "Check Overall System Health", bg='deep pink').grid(row = 7, column = 0) 
B3 = tk.Button(top, text = "Submit",command = healthchcker,bd = '5',bg='white').grid(row = 7, column = 1) 


#Entering the event main loop  
top.mainloop()  


# In[ ]:




