import tkinter as tk
from tkinter import *
import sqlite3
# Abhigna KV
r = tk.Tk()
r.resizable(0,0)
r.title("Vending Machine")
Label(r, text="VENDING MACHINE", bg="pink", font=('arial', 15, "bold")).pack(pady=10)
Label(r, text="MENU", font=('arial', 12, "bold")).pack(pady=10)
Label(r, text="1.Coke Rs 20/-\n2.Lays Rs 30/-\n3.Five Star Rs 5/-\n4.Snickers Rs 35/-\n5.Biscuits Rs 10/-\n6.Pepsi Rs "
              "20/-\n7.Silk Rs 60/-\n8.Kurkure Rs 35/-\n9.Doritos Rs 20/-", bg="#ccb3ff",
      font=("Times New Roman", 15)).pack(pady=10)
r.geometry("280x380+450+20")
r["bg"] = "#cfebed"
conn = sqlite3.connect('C:\\Users\\HP\\PycharmProjects\\vm\\items_final.db')
cur_con = conn.cursor()
cur_con.execute("SELECT * FROM vending_machine_final")
for row in cur_con.fetchall():
    [coke_db, lays_db, five_db, sni_db, bis_db, pep_db, silk_db, kur_db, dor_db] = list(row)[1:]
# print(coke_db)
[c, l, f, s, b, p, si, ku, dor] = [20, 30, 5, 35, 10, 25, 60, 35, 20]


# print(coke)


def admin():
    top = Toplevel(r)
    top.resizable(0, 0)
    top["bg"] = "#cfebed"
    x = r.winfo_x()
    y = r.winfo_y()
    top.geometry("%dx%d+%d+%d" % (280, 80, x, y))

    def add_items():
        rows = [(1, 10, 20, 20, 10, 40, 20, 30, 23, 45)]
        cur_con.executemany('insert into vending_machine_final values (?,?,?,?,?,?,?,?,?,?)', rows)
        conn.commit()
        Label(top, text="Items added to Vending Machine!", font=("Times New Roman", 12)).place(x=25, y=40)
        # print("Success!")

    button2 = tk.Button(top, text='Add items',bg="pink", width=25, command=add_items)
    button2.pack()


tk.Button(r, text='Admin Login', width=10, bg="#ccb3ff", command=admin).place(x=10, y=340)

sum = 0


def bill():
    global sum
    sum = 0
    if coke.get() and coke_db > 0:
        sum = sum + cm
    if lays.get() and lays_db > 0:
        sum = sum + lm
    if fs.get() and five_db > 0:
        sum = sum + fm
    if sni.get() and sni_db > 0:
        sum = sum + sm
    if bis.get() and bis_db > 0:
        sum = sum + bm
    if pep.get() and pep_db > 0:
        sum = sum + pm
    if silk.get() and silk_db > 0:
        sum = sum + sim
    if kur.get() and kur_db > 0:
        sum = sum + km
    if doritos.get() and dor_db > 0:
        sum = sum + dorm
    else:
        print("No bill generated")
    # print(sum)
    Label(top1, text="You Have to pay:", font=("Times New Roman", 15)).place(x=60, y=300)
    Label(top1, text=sum, font=("Times New Roman", 15)).place(x=210, y=300)


def pay():
    top2 = Toplevel(r)
    top2.resizable(0, 0)
    top2["bg"] = "#cfebed"
    top2.title("Payment")
    x = r.winfo_x()
    y = r.winfo_y()
    top2.geometry("%dx%d+%d+%d" % (280, 380, x, y))
    payamt = StringVar()
    Label(top2, text="Amount:", font=("Times New Roman", 15)).place(x=60, y=80)
    Entry(top2, textvariable=payamt, width=10, font=("Times New Roman", 15)).place(x=150, y=80)
    Label(top2, text="You Have to pay:", font=("Times New Roman", 15)).place(x=60, y=30)
    Label(top2, text=sum, font=("Times New Roman", 15)).place(x=210, y=30)
    Label(top2, text="Your Change:", font=("Times New Roman", 15)).place(x=60, y=130)

    def payamount():
        amt = int(payamt.get())
        chnage = amt - sum
        # print(chnage)
        if chnage >= 0:
            Label(top2, text=chnage, font=("Times New Roman", 15)).place(x=210, y=130)
            Label(top2, text="Payment Successful!", font=("Times New Roman", 15)).place(x=55, y=180)
        else:
            Label(top2, text="Insufficient, Please pay the exact amount", font=("Times New Roman",12)).place(x=25, y=180)

    Button(top2, text="Pay", bg="pink", command=payamount, width=25).place(x=50, y=350)


def order():
    # global p_get
    global coke, lays, fs, sni, bis, pep, silk, kur, doritos, top1
    top1 = Toplevel(r)
    top1.resizable(0, 0)
    top1["bg"] = "#cfebed"
    top1.title("Order")
    x = r.winfo_x()
    y = r.winfo_y()
    top1.geometry("%dx%d+%d+%d" % (280, 380, x, y))
    coke = StringVar()
    lays = StringVar()
    fs = StringVar()
    sni = StringVar()
    bis = StringVar()
    pep = StringVar()
    silk = StringVar()
    kur = StringVar()
    doritos = StringVar()

    # p_get = pep.get()

    def coke_func():
        global cm
        if not coke.get():
            cm = 0
        else:
            cr = coke.get()
            icr = [int(cr)]
            cm = int(cr) * c
            if coke_db > 0:
                cur_con.execute("UPDATE vending_machine_final set coke = coke-? where id = '1' ", icr)
                conn.commit()
            else:
                Label(top1, text="Coke out of stock", font=("Times New Roman", 15)).place(x=60, y=300)
            # print("yay!")

    def lays_func():
        global lm
        if not lays.get():
            lm = 0
        else:
            lr = lays.get()
            ilr = [int(lr)]
            lm = int(lr) * l
            if lays_db > 0:
                cur_con.execute("UPDATE vending_machine_final set lays = lays-? where id = '1' ", ilr)
                conn.commit()
            else:
                Label(top1, text="Lays out of stock", font=("Times New Roman", 15)).place(x=60, y=300)

    def fs_func():
        global fm
        if not fs.get():
            fm = 0
        else:
            fr = fs.get()
            ifr = [int(fr)]
            fm = int(fr) * f
            if five_db > 0:
                cur_con.execute("UPDATE vending_machine_final set five = five-? where id = '1' ", ifr)
                conn.commit()
            else:
                Label(top1, text="Five Star out of stock", font=("Times New Roman", 15)).place(x=60, y=300)

    def sni_func():
        global sm
        if not sni.get():
            sm = 0
        else:
            sr = sni.get()
            sm = int(sr) * s
            isr = [int(sr)]
            if sni_db > 0:
                cur_con.execute("UPDATE vending_machine_final set snickers = snickers-? where id = '1' ", isr)
                conn.commit()
            else:
                Label(top1, text="Snickers out of stock", font=("Times New Roman", 15)).place(x=60, y=300)

    def bis_func():
        global bm
        if not bis.get():
            bm = 0
        else:
            br = bis.get()
            bm = int(br) * b
            ibr = [int(br)]
            if bis_db > 0:
                cur_con.execute("UPDATE vending_machine_final set biscuits = biscuits-? where id = '1' ", ibr)
                conn.commit()
            else:
                Label(top1, text="Biscuits out of stock", font=("Times New Roman", 15)).place(x=60, y=300)

    def pep_func():
        global pm
        if not pep.get():
            pm = 0
        else:
            pr = pep.get()
            pm = int(pr) * p
            ipr = [int(pr)]
            if pep_db > 0:
                cur_con.execute("UPDATE vending_machine_final set pepsi = pepsi-? where id = '1' ", ipr)
                conn.commit()
            else:
                Label(top1, text="Pepsi out of stock", font=("Times New Roman", 15)).place(x=60, y=300)

    def silk_func():
        global sim
        if not silk.get():
            sim = 0
        else:
            sr = silk.get()
            sim = int(sr) * si
            isir = [int(sr)]
            if silk_db > 0:
                cur_con.execute("UPDATE vending_machine_final set silk = silk-? where id = '1' ", isir)
                conn.commit()
            else:
                Label(top1, text="Silk out of stock", font=("Times New Roman", 15)).place(x=60, y=300)

    def kur_func():
        global km
        if not kur.get():
            km = 0
        else:
            kr = kur.get()
            km = int(kr) * ku
            ikr = [int(kr)]
            if kur_db > 0:
                cur_con.execute("UPDATE vending_machine_final set kurkure = kurkure-? where id = '1' ", ikr)
                conn.commit()
            else:
                Label(top1, text="Kurkure out of stock", font=("Times New Roman", 15)).place(x=60, y=300)

    def doritos_func():
        global dorm
        if not doritos.get():
            dorm = 0
        else:
            dr = doritos.get()
            dorm = int(dr) * dor
            idr = [int(dr)]
            if dor_db >0:
                cur_con.execute("UPDATE vending_machine_final set doritos = doritos-? where id = '1' ", idr)
                conn.commit()
            else:
                Label(top1, text="Doritos out of stock", font=("Times New Roman", 15)).place(x=60, y=300)

    Entry(top1, textvariable=coke, width=5).place(x=25, y=50)
    tk.Button(top1, text='Coke', command=coke_func, bg="#F40009", fg="#ffffff", width=10).place(x=10, y=20)

    Entry(top1, textvariable=lays, width=5).place(x=120, y=50)
    tk.Button(top1, text='Lays', command=lays_func, bg="#002966", fg="white", width=10).place(x=100, y=20)

    Entry(top1, textvariable=fs, width=5).place(x=210, y=50)
    tk.Button(top1, text='Five Star', command=fs_func, bg="#996600", width=10).place(x=190, y=20)

    Entry(top1, textvariable=sni, width=5).place(x=25, y=130)
    tk.Button(top1, text='Snickers', command=sni_func, bg="black", fg="white", width=10).place(x=10, y=100)

    Entry(top1, textvariable=bis, width=5).place(x=120, y=130)
    tk.Button(top1, text='Biscuits', command=bis_func, bg="purple", fg="white", width=10).place(x=100, y=100)

    Entry(top1, textvariable=pep, width=5).place(x=210, y=130)
    tk.Button(top1, text='Pepsi', command=pep_func, bg="navy blue", fg="white", width=10).place(x=190, y=100)

    Entry(top1, textvariable=silk, width=5).place(x=25, y=210)
    tk.Button(top1, text='Silk', command=silk_func, bg="brown", fg="white", width=10).place(x=10, y=180)

    Entry(top1, textvariable=kur, width=5).place(x=120, y=210)
    tk.Button(top1, text='Kurkure', command=kur_func, bg="#ff6600", fg="white", width=10).place(x=100, y=180)

    Entry(top1, textvariable=doritos, width=5).place(x=210, y=210)
    tk.Button(top1, text='Doritos', command=doritos_func, bg="#4c0080", fg="white", width=10).place(x=190, y=180)

    tk.Button(top1, text='Generate Bill', command=bill, bg="#4d88ff", width=25).place(x=50, y=250)
    Button(top1, text="Pay Bill", bg="pink", command=pay, width=25).place(x=50, y=350)


tk.Button(r, text='Next', width=10, bg="#ccb3ff", command=order).place(x=185, y=340)
r.mainloop()
