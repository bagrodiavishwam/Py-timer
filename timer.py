# @author: bagrodiavishwam
from tkinter import *
import time
window=Tk()
window.title('Timer')
window.geometry('600x600')
window.config(bg='#000')
window.resizable(True,True)

heading= Label(window, text="Timer", font="arial 25 bold", bg='#000', fg="#ff0000")
heading.place(x=150, y=70)
heading.pack(pady=5)

# timer
hr=StringVar()
Entry(window, textvariable=hr, width=3, font="arial 40").place(x=40, y=140)
hr.set("00")

min=StringVar()
Entry(window, textvariable=min, width=3, font="arial 40").place(x=190, y=140)
min.set("00")

sec=StringVar()
Entry(window, textvariable=sec, width=3, font="arial 40").place(x=340, y=140)
sec.set("00")

Label(window, text="Hours", font="arial 15", bg="#000", fg="#fff").place(x=30, y=160)
Label(window, text="Mins", font="arial 15", bg="#000", fg="#fff").place(x=170, y=160)
Label(window, text="Secs", font="arial 15", bg="#000", fg="#fff").place(x=330, y=160)

def Timer():
    times=int(hr.get())*3600+int(min.get())*60+int(sec.get())*1

    while times >-1:
        minute, second=(times//60, times%60)
        hour=0
        if minute>60:
            hour,minute =(minute//60, minute%60)
        sec.set(second)
        min.set(minute)
        hr.set(hour)

        window.update()
        time.sleep(1)

        if(times==0):
            sec.set("00")
            min.set("00")
            hr.set("00")
        times-=1

def Pause():
        for second in Timer():
            sec.set(second)
        
        for minute in Timer():
            min.set(minute)
        
        for hour in Timer():
            hr.set(hour)
        
        window.update()

def Resume():
    for second in Timer():
        sec.set(second)
        
    for minute in Timer():
        min.set(minute)
        
    for hour in Timer():
        hr.set(hour)
    
    times=int(hour)*3600+int(minute)*60+int(second)*1

    while times >-1:
        minute, second=(times//60, times%60)
        hour=0
        if minute>60:
            hour,minute =(minute//60, minute%60)
        sec.set(second)
        min.set(minute)
        hr.set(hour)

        window.update()
        time.sleep(1)

        if(times==0):
            sec.set("00")
            min.set("00")
            hr.set("00")
        times-=1
     
    window.update()


button=Button(window, text="START", bg="#ff0000", bd=0, fg="#fff", width=20, height=2, font="ariaal 22 bold", command=Timer)
button.pack(padx=5, pady=40, side=BOTTOM)

button=Button(window, text="PAUSE", bg="#ff0000", bd=0, fg="#fff", width=20, height=2, font="ariaal 22 bold", command=Timer)
button.pack(padx=5, pady=40, side=BOTTOM)

button=Button(window, text="RESUME", bg="#ff0000", bd=0, fg="#fff", width=20, height=2, font="ariaal 22 bold", command=Timer)
button.pack(padx=5, pady=40, side=BOTTOM)

window.mainloop()
