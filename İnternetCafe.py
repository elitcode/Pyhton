#def dialog():
#    var = messagebox.showinfo("Uyarı" , "www.yazilimbilisim.net")


import sqlite3
from tkinter import *
from tkinter import messagebox,Menu
 
db = sqlite3.connect("siparis.sqlite")
dbh = sqlite3.connect("hesap.sqlite")

im = db.cursor()
imh = dbh.cursor()

pencere = Tk()

ucret=15	

def temizle():
	yazı_g.destroy()
	yazı_s.destroy()
	g_ent.destroy()
	s_ent.destroy()
	gr_button.destroy()
	
def masaA10(deger0,deger1,deger2,deger3):
	im.execute(""" UPDATE siparis SET sure = ? , ak = ? , tl = ? , durum = ? WHERE masa_n = "10" """, (deger1,deger2,deger3,deger0))
	db.commit()
		
	
def masaA9(deger0,deger1,deger2,deger3):
	im.execute(""" UPDATE siparis SET sure = ? , ak = ? , tl = ? , durum = ? WHERE masa_n = "9" """, (deger1,deger2,deger3,deger0))
	db.commit()
		
	
def masaA8(deger0,deger1,deger2,deger3):
	im.execute(""" UPDATE siparis SET sure = ? , ak = ? , tl = ? , durum = ? WHERE masa_n = "8" """, (deger1,deger2,deger3,deger0))
	db.commit()
		

def masaA7(deger0,deger1,deger2,deger3):
	im.execute(""" UPDATE siparis SET sure = ? , ak = ? , tl = ? , durum = ? WHERE masa_n = "7" """, (deger1,deger2,deger3,deger0))
	db.commit()
		
	
def masaA6(deger0,deger1,deger2,deger3):
	im.execute(""" UPDATE siparis SET sure = ? , ak = ? , tl = ? , durum = ? WHERE masa_n = "6" """, (deger1,deger2,deger3,deger0))
	db.commit()
		
	
def masaA5(deger0,deger1,deger2,deger3):
	im.execute(""" UPDATE siparis SET sure = ? , ak = ? , tl = ? , durum = ? WHERE masa_n = "5" """, (deger1,deger2,deger3,deger0))
	db.commit()
		

def masaA4(deger0,deger1,deger2,deger3):
	im.execute(""" UPDATE siparis SET sure = ? , ak = ? , tl = ? , durum = ? WHERE masa_n = "4" """, (deger1,deger2,deger3,deger0))
	db.commit()

	
def masaA3(deger0,deger1,deger2,deger3):
	im.execute(""" UPDATE siparis SET sure = ? , ak = ? , tl = ? , durum = ? WHERE masa_n = "3" """, (deger1,deger2,deger3,deger0))
	db.commit()

def masaA2(deger0,deger1,deger2,deger3):
	im.execute(""" UPDATE siparis SET sure = ? , ak = ? , tl = ? , durum = ? WHERE masa_n = "2" """, (deger1,deger2,deger3,deger0))
	db.commit()


def masaA1(deger0,deger1,deger2,deger3):
	im.execute(""" UPDATE siparis SET sure = ? , ak = ? , tl = ? , durum = ? WHERE masa_n = "1" """, (deger1,deger2,deger3,deger0))
	db.commit()

def masa1():
	masa1 = Tk()
	masa1.geometry("900x900")
	im.execute("""SELECT * FROM siparis WHERE masa_n = "1" """)
	data = im.fetchone()	
	
	
	masa1_label1=Label(masa1,text='Süre')
	masa1_label1.place(x=20,y=20)
	masa1_entry1=Entry(masa1)
	masa1_entry1.insert(0,data[2])
	masa1_entry1.place(x=20,y=64)
	
	masa1_label5=Label(masa1,text='Ek Fiyat')
	masa1_label5.place(x=20,y=590)
	masa1_entry5=Entry(masa1)
	masa1_entry5.insert(3,data[4])
	masa1_entry5.place(x=20,y=640)
	
	masa1_label2=Label(masa1,text='Masa Durumu Açık(A)/Kapalı(K)')
	masa1_label2.place(x=20,y=120)
	masa1_entry2=Entry(masa1)
	masa1_entry2.insert(1,data[1])
	masa1_entry2.place(x=20,y=164)
	
	
	masa1_label3=Label(masa1,text='Ücret = ').place(x=20,y=400)
	
	masa1_label4=Label(masa1,text=data[5]).place(x=135,y=400)	
		
	sıfırla=Button(masa1,text='Sıfırla',bg='red').place(x=20,y=250)
	
	kaydet1=Button(masa1,text='Kaydet',command=lambda:masaA1(masa1_entry5.get(),masa1_entry1.get(),masa1_entry2.get(),int(masa1_entry1.get())*ucret+int(masa1_entry5.get()))).place(x=20,y=450)
	
	listbox = Listbox(masa1)
	listbox.pack()
	listbox.place(x=20,y=700)
	listbox.insert(END, "Valorant")
	listbox.insert(END, "CSGO")
	listbox.insert(END, "GTA V")
	db.commit()
	masa1.mainloop()


def masa2():
	masa1 = Tk()
	masa1.geometry("900x900")
	im.execute("""SELECT * FROM siparis WHERE masa_n = "2" """)
	data = im.fetchone()	
	
	
	masa1_label1=Label(masa1,text='Süre')
	masa1_label1.place(x=20,y=20)
	masa1_entry1=Entry(masa1)
	masa1_entry1.insert(0,data[2])
	masa1_entry1.place(x=20,y=64)
	
	masa1_label5=Label(masa1,text='Ek Fiyat')
	masa1_label5.place(x=20,y=590)
	masa1_entry5=Entry(masa1)
	masa1_entry5.insert(3,data[4])
	masa1_entry5.place(x=20,y=640)
	
	masa1_label2=Label(masa1,text='Masa Durumu Açık(A)/Kapalı(K)')
	masa1_label2.place(x=20,y=120)
	masa1_entry2=Entry(masa1)
	masa1_entry2.insert(1,data[1])
	masa1_entry2.place(x=20,y=164)
	
	
	masa1_label3=Label(masa1,text='Ücret = ').place(x=20,y=400)
	
	masa1_label4=Label(masa1,text=data[5]).place(x=135,y=400)	
		
	sıfırla=Button(masa1,text='Sıfırla',bg='red').place(x=20,y=250)
	
	kaydet1=Button(masa1,text='Kaydet',command=lambda:masaA2(masa1_entry5.get(),masa1_entry1.get(),masa1_entry2.get(),int(masa1_entry1.get())*ucret+int(masa1_entry5.get()))).place(x=20,y=450)
	
	listbox = Listbox(masa1)
	listbox.pack()
	listbox.place(x=20,y=700)
	listbox.insert(END, "Valorant")
	listbox.insert(END, "CSGO")
	listbox.insert(END, "GTA V")
	db.commit()
	masa1.mainloop()

def masa3():
	masa1 = Tk()
	masa1.geometry("900x900")
	im.execute("""SELECT * FROM siparis WHERE masa_n = "3" """)
	data = im.fetchone()	
	
	
	masa1_label1=Label(masa1,text='Süre')
	masa1_label1.place(x=20,y=20)
	masa1_entry1=Entry(masa1)
	masa1_entry1.insert(0,data[2])
	masa1_entry1.place(x=20,y=64)
	
	masa1_label5=Label(masa1,text='Ek Fiyat')
	masa1_label5.place(x=20,y=590)
	masa1_entry5=Entry(masa1)
	masa1_entry5.insert(3,data[4])
	masa1_entry5.place(x=20,y=640)
	
	masa1_label2=Label(masa1,text='Masa Durumu Açık(A)/Kapalı(K)')
	masa1_label2.place(x=20,y=120)
	masa1_entry2=Entry(masa1)
	masa1_entry2.insert(1,data[1])
	masa1_entry2.place(x=20,y=164)
	
	
	masa1_label3=Label(masa1,text='Ücret = ').place(x=20,y=400)
	
	masa1_label4=Label(masa1,text=data[5]).place(x=135,y=400)	
		
	sıfırla=Button(masa1,text='Sıfırla',bg='red').place(x=20,y=250)
	
	kaydet1=Button(masa1,text='Kaydet',command=lambda:masaA3(masa1_entry5.get(),masa1_entry1.get(),masa1_entry2.get(),int(masa1_entry1.get())*ucret+int(masa1_entry5.get()))).place(x=20,y=450)
	
	listbox = Listbox(masa1)
	listbox.pack()
	listbox.place(x=20,y=700)
	listbox.insert(END, "Valorant")
	listbox.insert(END, "CSGO")
	listbox.insert(END, "GTA V")
	db.commit()
	masa1.mainloop()

def masa4():
	masa1 = Tk()
	masa1.geometry("900x900")
	im.execute("""SELECT * FROM siparis WHERE masa_n = "4" """)
	data = im.fetchone()	
	
	
	masa1_label1=Label(masa1,text='Süre')
	masa1_label1.place(x=20,y=20)
	masa1_entry1=Entry(masa1)
	masa1_entry1.insert(0,data[2])
	masa1_entry1.place(x=20,y=64)
	
	masa1_label5=Label(masa1,text='Ek Fiyat')
	masa1_label5.place(x=20,y=590)
	masa1_entry5=Entry(masa1)
	masa1_entry5.insert(3,data[4])
	masa1_entry5.place(x=20,y=640)
	
	masa1_label2=Label(masa1,text='Masa Durumu Açık(A)/Kapalı(K)')
	masa1_label2.place(x=20,y=120)
	masa1_entry2=Entry(masa1)
	masa1_entry2.insert(1,data[1])
	masa1_entry2.place(x=20,y=164)
	
	
	masa1_label3=Label(masa1,text='Ücret = ').place(x=20,y=400)
	
	masa1_label4=Label(masa1,text=data[5]).place(x=135,y=400)	
		
	sıfırla=Button(masa1,text='Sıfırla',bg='red').place(x=20,y=250)
	
	kaydet1=Button(masa1,text='Kaydet',command=lambda:masaA4(masa1_entry5.get(),masa1_entry1.get(),masa1_entry2.get(),int(masa1_entry1.get())*ucret+int(masa1_entry5.get()))).place(x=20,y=450)
	
	listbox = Listbox(masa1)
	listbox.pack()
	listbox.place(x=20,y=700)
	listbox.insert(END, "Valorant")
	listbox.insert(END, "CSGO")
	listbox.insert(END, "GTA V")
	db.commit()
	masa1.mainloop()
	
def masa5():
	masa1 = Tk()
	masa1.geometry("900x900")
	im.execute("""SELECT * FROM siparis WHERE masa_n = "5" """)
	data = im.fetchone()	
	
	
	masa1_label1=Label(masa1,text='Süre')
	masa1_label1.place(x=20,y=20)
	masa1_entry1=Entry(masa1)
	masa1_entry1.insert(0,data[2])
	masa1_entry1.place(x=20,y=64)
	
	masa1_label5=Label(masa1,text='Ek Fiyat')
	masa1_label5.place(x=20,y=590)
	masa1_entry5=Entry(masa1)
	masa1_entry5.insert(3,data[4])
	masa1_entry5.place(x=20,y=640)
	
	masa1_label2=Label(masa1,text='Masa Durumu Açık(A)/Kapalı(K)')
	masa1_label2.place(x=20,y=120)
	masa1_entry2=Entry(masa1)
	masa1_entry2.insert(1,data[1])
	masa1_entry2.place(x=20,y=164)
	
	
	masa1_label3=Label(masa1,text='Ücret = ').place(x=20,y=400)
	
	masa1_label4=Label(masa1,text=data[5]).place(x=135,y=400)	
		
	sıfırla=Button(masa1,text='Sıfırla',bg='red').place(x=20,y=250)
	
	kaydet1=Button(masa1,text='Kaydet',command=lambda:masaA5(masa1_entry5.get(),masa1_entry1.get(),masa1_entry2.get(),int(masa1_entry1.get())*ucret+int(masa1_entry5.get()))).place(x=20,y=450)
	
	listbox = Listbox(masa1)
	listbox.pack()
	listbox.place(x=20,y=700)
	listbox.insert(END, "Valorant")
	listbox.insert(END, "CSGO")
	listbox.insert(END, "GTA V")
	db.commit()
	masa1.mainloop()
	
def masa6():
	masa1 = Tk()
	masa1.geometry("900x900")
	im.execute("""SELECT * FROM siparis WHERE masa_n = "6" """)
	data = im.fetchone()	
	
	
	masa1_label1=Label(masa1,text='Süre')
	masa1_label1.place(x=20,y=20)
	masa1_entry1=Entry(masa1)
	masa1_entry1.insert(0,data[2])
	masa1_entry1.place(x=20,y=64)
	
	masa1_label5=Label(masa1,text='Ek Fiyat')
	masa1_label5.place(x=20,y=590)
	masa1_entry5=Entry(masa1)
	masa1_entry5.insert(3,data[4])
	masa1_entry5.place(x=20,y=640)
	
	masa1_label2=Label(masa1,text='Masa Durumu Açık(A)/Kapalı(K)')
	masa1_label2.place(x=20,y=120)
	masa1_entry2=Entry(masa1)
	masa1_entry2.insert(1,data[1])
	masa1_entry2.place(x=20,y=164)
	
	
	masa1_label3=Label(masa1,text='Ücret = ').place(x=20,y=400)
	
	masa1_label4=Label(masa1,text=data[5]).place(x=135,y=400)	
		
	sıfırla=Button(masa1,text='Sıfırla',bg='red').place(x=20,y=250)
	
	kaydet1=Button(masa1,text='Kaydet',command=lambda:masaA6(masa1_entry5.get(),masa1_entry1.get(),masa1_entry2.get(),int(masa1_entry1.get())*ucret+int(masa1_entry5.get()))).place(x=20,y=450)
	
	listbox = Listbox(masa1)
	listbox.pack()
	listbox.place(x=20,y=700)
	listbox.insert(END, "Valorant")
	listbox.insert(END, "CSGO")
	listbox.insert(END, "GTA V")
	db.commit()
	masa1.mainloop()
	
	
def masa7():
	masa1 = Tk()
	masa1.geometry("900x900")
	im.execute("""SELECT * FROM siparis WHERE masa_n = "7" """)
	data = im.fetchone()	
	
	
	masa1_label1=Label(masa1,text='Süre')
	masa1_label1.place(x=20,y=20)
	masa1_entry1=Entry(masa1)
	masa1_entry1.insert(0,data[2])
	masa1_entry1.place(x=20,y=64)
	
	masa1_label5=Label(masa1,text='Ek Fiyat')
	masa1_label5.place(x=20,y=590)
	masa1_entry5=Entry(masa1)
	masa1_entry5.insert(3,data[4])
	masa1_entry5.place(x=20,y=640)
	
	masa1_label2=Label(masa1,text='Masa Durumu Açık(A)/Kapalı(K)')
	masa1_label2.place(x=20,y=120)
	masa1_entry2=Entry(masa1)
	masa1_entry2.insert(1,data[1])
	masa1_entry2.place(x=20,y=164)
	
	
	masa1_label3=Label(masa1,text='Ücret = ').place(x=20,y=400)
	
	masa1_label4=Label(masa1,text=data[5]).place(x=135,y=400)	
		
	sıfırla=Button(masa1,text='Sıfırla',bg='red').place(x=20,y=250)
	
	kaydet1=Button(masa1,text='Kaydet',command=lambda:masaA7(masa1_entry5.get(),masa1_entry1.get(),masa1_entry2.get(),int(masa1_entry1.get())*ucret+int(masa1_entry5.get()))).place(x=20,y=450)
	
	listbox = Listbox(masa1)
	listbox.pack()
	listbox.place(x=20,y=700)
	listbox.insert(END, "Valorant")
	listbox.insert(END, "CSGO")
	listbox.insert(END, "GTA V")
	db.commit()
	masa1.mainloop()

def masa8():
	masa1 = Tk()
	masa1.geometry("900x900")
	im.execute("""SELECT * FROM siparis WHERE masa_n = "8" """)
	data = im.fetchone()	
	
	
	masa1_label1=Label(masa1,text='Süre')
	masa1_label1.place(x=20,y=20)
	masa1_entry1=Entry(masa1)
	masa1_entry1.insert(0,data[2])
	masa1_entry1.place(x=20,y=64)
	
	masa1_label5=Label(masa1,text='Ek Fiyat')
	masa1_label5.place(x=20,y=590)
	masa1_entry5=Entry(masa1)
	masa1_entry5.insert(3,data[4])
	masa1_entry5.place(x=20,y=640)
	
	masa1_label2=Label(masa1,text='Masa Durumu Açık(A)/Kapalı(K)')
	masa1_label2.place(x=20,y=120)
	masa1_entry2=Entry(masa1)
	masa1_entry2.insert(1,data[1])
	masa1_entry2.place(x=20,y=164)
	
	
	masa1_label3=Label(masa1,text='Ücret = ').place(x=20,y=400)
	
	masa1_label4=Label(masa1,text=data[5]).place(x=135,y=400)	
		
	sıfırla=Button(masa1,text='Sıfırla',bg='red').place(x=20,y=250)
	
	kaydet1=Button(masa1,text='Kaydet',command=lambda:masaA8(masa1_entry5.get(),masa1_entry1.get(),masa1_entry2.get(),int(masa1_entry1.get())*ucret+int(masa1_entry5.get()))).place(x=20,y=450)
	
	listbox = Listbox(masa1)
	listbox.pack()
	listbox.place(x=20,y=700)
	listbox.insert(END, "Valorant")
	listbox.insert(END, "CSGO")
	listbox.insert(END, "GTA V")
	db.commit()
	masa1.mainloop()
	
def masa9():
	masa1 = Tk()
	masa1.geometry("900x900")
	im.execute("""SELECT * FROM siparis WHERE masa_n = "9" """)
	data = im.fetchone()	
	
	
	masa1_label1=Label(masa1,text='Süre')
	masa1_label1.place(x=20,y=20)
	masa1_entry1=Entry(masa1)
	masa1_entry1.insert(0,data[2])
	masa1_entry1.place(x=20,y=64)
	
	masa1_label5=Label(masa1,text='Ek Fiyat')
	masa1_label5.place(x=20,y=590)
	masa1_entry5=Entry(masa1)
	masa1_entry5.insert(3,data[4])
	masa1_entry5.place(x=20,y=640)
	
	masa1_label2=Label(masa1,text='Masa Durumu Açık(A)/Kapalı(K)')
	masa1_label2.place(x=20,y=120)
	masa1_entry2=Entry(masa1)
	masa1_entry2.insert(1,data[1])
	masa1_entry2.place(x=20,y=164)
	
	
	masa1_label3=Label(masa1,text='Ücret = ').place(x=20,y=400)
	
	masa1_label4=Label(masa1,text=data[5]).place(x=135,y=400)	
		
	sıfırla=Button(masa1,text='Sıfırla',bg='red').place(x=20,y=250)
	
	kaydet1=Button(masa1,text='Kaydet',command=lambda:masaA9(masa1_entry5.get(),masa1_entry1.get(),masa1_entry2.get(),int(masa1_entry1.get())*ucret+int(masa1_entry5.get()))).place(x=20,y=450)
	
	listbox = Listbox(masa1)
	listbox.pack()
	listbox.place(x=20,y=700)
	listbox.insert(END, "Valorant")
	listbox.insert(END, "CSGO")
	listbox.insert(END, "GTA V")
	db.commit()
	masa1.mainloop()

def masa10():
	masa1 = Tk()
	masa1.geometry("900x900")
	im.execute("""SELECT * FROM siparis WHERE masa_n = "10" """)
	data = im.fetchone()	
	
	
	masa1_label1=Label(masa1,text='Süre')
	masa1_label1.place(x=20,y=20)
	masa1_entry1=Entry(masa1)
	masa1_entry1.insert(0,data[2])
	masa1_entry1.place(x=20,y=64)
	
	masa1_label5=Label(masa1,text='Ek Fiyat')
	masa1_label5.place(x=20,y=590)
	masa1_entry5=Entry(masa1)
	masa1_entry5.insert(3,data[4])
	masa1_entry5.place(x=20,y=640)
	
	masa1_label2=Label(masa1,text='Masa Durumu Açık(A)/Kapalı(K)')
	masa1_label2.place(x=20,y=120)
	masa1_entry2=Entry(masa1)
	masa1_entry2.insert(1,data[1])
	masa1_entry2.place(x=20,y=164)
	
	
	masa1_label3=Label(masa1,text='Ücret = ').place(x=20,y=400)
	
	masa1_label4=Label(masa1,text=data[5]).place(x=135,y=400)	
		
	sıfırla=Button(masa1,text='Sıfırla',bg='red').place(x=20,y=250)
	
	kaydet1=Button(masa1,text='Kaydet',command=lambda:masaA10(masa1_entry5.get(),masa1_entry1.get(),masa1_entry2.get(),int(masa1_entry1.get())*ucret+int(masa1_entry5.get()))).place(x=20,y=450)
	
	listbox = Listbox(masa1)
	listbox.pack()
	listbox.place(x=20,y=700)
	listbox.insert(END, "Valorant")
	listbox.insert(END, "CSGO")
	listbox.insert(END, "GTA V")
	db.commit()
	masa1.mainloop()
			

																
	
def masa():
		temizle()
		masa1_label=Label(text='Masa 1')
		masa1_label.place(x=10,y=10)
		
		masa1_button=Button(text='Detaylar',bg='red',command=masa1)
		masa1_button.place(x=130,y=10)
		
		masa2_label=Label(text='Masa 2')
		masa2_label.place(x=10,y=100)
		
		masa2_button=Button(text='Detaylar',bg='red',command=masa2)
		masa2_button.place(x=130,y=100)
		
		masa3_label=Label(text='Masa 3')
		masa3_label.place(x=10,y=210)
		
		masa3_button=Button(text='Detaylar',bg='red',command=masa3)
		masa3_button.place(x=130,y=210)
		
		masa4_label=Label(text='Masa 4')
		masa4_label.place(x=10,y=320)
		
		masa4_button=Button(text='Detaylar',bg='red',command=masa4)
		masa4_button.place(x=130,y=320)
		
		masa5_label=Label(text='Masa 5')
		masa5_label.place(x=10,y=430)
		
		masa5_button=Button(text='Detaylar',bg='red',command=masa5)
		masa5_button.place(x=130,y=430)
		
		masa6_label=Label(text='Masa 6')
		masa6_label.place(x=10,y=540)
		
		masa6_button=Button(text='Detaylar',bg='red',command=masa6)
		masa6_button.place(x=130,y=540)
		
		masa7_label=Label(text='Masa 7')
		masa7_label.place(x=10,y=650)
		
		masa7_button=Button(text='Detaylar',bg='red',command=masa7)
		masa7_button.place(x=130,y=650)
		
		masa8_label=Label(text='Masa 8')
		masa8_label.place(x=10,y=760)
		
		masa8_button=Button(text='Detaylar',bg='red',command=masa8)
		masa8_button.place(x=130,y=760)
		
		masa9_label=Label(text='Masa 9')
		masa9_label.place(x=10,y=870)
		
		masa9_button=Button(text='Detaylar',bg='red',command=masa9)
		masa9_button.place(x=130,y=870)
		
		masa10_label=Label(text='Masa 10')
		masa10_label.place(x=10,y=980)
		
		masa10button=Button(text='Detaylar',bg='red',command=masa10)
		masa10button.place(x=130,y=980)
		
		
def giris():
	if 1 == 1:
		masa()
		
		


 
yazı_g = Label(text='Kullanıcı Adınız')
yazı_s = Label(text='Şifreniz')
yazı_g.place(x=230,y=100)
yazı_s.place(x=230,y=200)

g_ent = Entry()
s_ent = Entry(show='*')
g_ent.place(x=230,y=150)
s_ent.place(x=230,y=250)

gr_button = Button(text='Giriş',bg='red',command=giris)
gr_button.place(x=250,y=300)


pencere.mainloop()