from tkinter import *
import time
from turtle import left

root = Tk()
root['bg']='#696969'
frame = Frame(root)
frame2 = Frame(root)
frame.pack()
frame2.pack(side=TOP)

Label(frame, font =('Ubuntu',22), text = 'Timer',bg ='#696969').pack(side=TOP)
sec = StringVar()
mins= StringVar()
hrs= StringVar()
sec.set('00')
mins.set('00')
hrs.set('00')

Entry(frame, textvariable = hrs, width =2, font = 'Helvetica 14').pack(side=LEFT)
Entry(frame, textvariable = mins, width =2, font = 'Helvetica 14').pack(side=LEFT)
Entry(frame, textvariable=sec, width = 2, font = 'Ubuntu 14').pack(side=LEFT)

def timer():
   times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
   while times > -1:
      minute,second = (times // 60 , times % 60)
      hour = 0
      if minute > 60:
         hour , minute = (minute // 60 , minute % 60)
      sec.set(second)
      mins.set(minute)
      hrs.set(hour)
      root.update()
      time.sleep(1)
      if(times == 0):
         sec.set('00')
         mins.set('00')
         hrs.set('00')
      times -= 1
Button(frame2, text='START', bd ='2', bg = '#696969',font =('Helvetica bold',10), command = timer).pack(side=TOP)
root.mainloop()
