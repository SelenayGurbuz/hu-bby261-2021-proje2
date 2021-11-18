
from random import randint
from tkinter import Tk, Label, Button, Entry

class sayisalLoto:
    def __init__(self, pencere):
        self.pencere = pencere
        pencere.title("Sayısal loto")

        self.baslik = Label(pencere, text="Günün Şanslı Numaraları")
        self.baslik.configure(font=("Arial", 25))
        self.baslik.pack()


        self.numaralar = Entry(pencere, text="Numaralar oluşturuluyor")
        self.numaralar.configure(width=100)
        self.numaralar.pack()


        self.yeniden = Button(pencere, text="Numara oluştur!", command=self.numaraOlustur, fg="green", bg="white")
        self.yeniden.pack()


        self.yardim = Button (root, text="SayisalLotoyardim", fg="blue", bg="white")
        self.yardim.pack()



        self.cikis = Button(pencere, text="Kapat", command=pencere.quit, fg="red", bg="white")
        self.cikis.pack()


    def numaraOlustur(self):
        i = 0
        self.numaralar.delete(0, 'end')
        secilenler = [0, 0, 0, 0, 0, 0]
        while i < len(secilenler):
            secilen = randint(1, 49)
            if secilen not in secilenler:
                secilenler[i] = secilen
                i += 1
        sansliNumaralar = str((sorted(secilenler)))
        self.numaralar.insert(0, sansliNumaralar)

root = Tk()
sayisalLotom = sayisalLoto(root)
sayisalLotom.numaraOlustur()
root.mainloop()
