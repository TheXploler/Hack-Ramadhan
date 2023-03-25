import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        root.title("Hack Ramadhan Reborn | 2023 v1.4")
        width=600
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.configure(bg='White')
        root.resizable(width=False, height=False)

        MainTitle=tk.Label(root)
        MainTitle["anchor"] = "n"
        ft = tkFont.Font(family='Arial',size=30)
        MainTitle["font"] = ft
        MainTitle["fg"] = "#333333"
        MainTitle["justify"] = "center"
        MainTitle["text"] = "Hack Ramadhan Reborn | 2023"
        MainTitle.config(bg="White")
        MainTitle.place(x=0,y=70,width=600,height=200)

        HausBypassButton=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=14)
        HausBypassButton["font"] = ft
        HausBypassButton["fg"] = "#333333"
        HausBypassButton["justify"] = "left"
        HausBypassButton["text"] = " Haus Bypass"
        HausBypassButton.place(x=20,y=210,width=175,height=30)
        HausBypassButton["offvalue"] = "0"
        HausBypassButton["onvalue"] = "1"
        HausBypassButton.configure(bg='White')

        AutoBukaButton=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=14)
        AutoBukaButton["font"] = ft
        AutoBukaButton["fg"] = "#333333"
        AutoBukaButton["justify"] = "left"
        AutoBukaButton["text"] = " Auto Buka"
        AutoBukaButton.place(x=20,y=260,width=153,height=30)
        AutoBukaButton["offvalue"] = "0"
        AutoBukaButton["onvalue"] = "1"
        AutoBukaButton.configure(bg='White')

        AntiLaparButton=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=14)
        AntiLaparButton["font"] = ft
        AntiLaparButton["fg"] = "#333333"
        AntiLaparButton["justify"] = "left"
        AntiLaparButton["text"] = " Anti Lapar"
        AntiLaparButton.place(x=20,y=310,width=150,height=30)
        AntiLaparButton["offvalue"] = "0"
        AntiLaparButton["onvalue"] = "1"
        AntiLaparButton.configure(bg='White')

        Khatam30JuzButton=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=14)
        Khatam30JuzButton["font"] = ft
        Khatam30JuzButton["fg"] = "#333333"
        Khatam30JuzButton["justify"] = "left"
        Khatam30JuzButton["text"] = " Khatam 30 Juz"
        Khatam30JuzButton.place(x=20,y=360,width=184,height=30)
        Khatam30JuzButton["offvalue"] = "0"
        Khatam30JuzButton["onvalue"] = "1"
        Khatam30JuzButton.configure(bg='White')

        AntiTelatSahurButton=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=14)
        AntiTelatSahurButton["font"] = ft
        AntiTelatSahurButton["fg"] = "#333333"
        AntiTelatSahurButton["justify"] = "left"
        AntiTelatSahurButton["text"] = " Anti Telat Sahur"
        AntiTelatSahurButton.place(x=20,y=410,width=190,height=30)
        AntiTelatSahurButton["offvalue"] = "0"
        AntiTelatSahurButton["onvalue"] = "1"
        AntiTelatSahurButton.configure(bg='White')

        MempercepatMaghribButton=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=14)
        MempercepatMaghribButton["font"] = ft
        MempercepatMaghribButton["fg"] = "#333333"
        MempercepatMaghribButton["justify"] = "left"
        MempercepatMaghribButton["text"] = " Mempercepat Maghrib"
        MempercepatMaghribButton.place(x=270,y=210,width=250,height=30)
        MempercepatMaghribButton["offvalue"] = "0"
        MempercepatMaghribButton["onvalue"] = "1"
        MempercepatMaghribButton.configure(bg='White')

        AntiHausButton=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=14)
        AntiHausButton["font"] = ft
        AntiHausButton["fg"] = "#333333"
        AntiHausButton["justify"] = "left"
        AntiHausButton["text"] = " Anti Haus"
        AntiHausButton.place(x=270,y=260,width=145,height=30)
        AntiHausButton["offvalue"] = "0"
        AntiHausButton["onvalue"] = "1"
        AntiHausButton.configure(bg='White')

        DosaBypassButton=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=14)
        DosaBypassButton["font"] = ft
        DosaBypassButton["fg"] = "#333333"
        DosaBypassButton["justify"] = "left"
        DosaBypassButton["text"] = " Dosa Bypass"
        DosaBypassButton.place(x=270,y=360,width=174,height=30)
        DosaBypassButton["offvalue"] = "0"
        DosaBypassButton["onvalue"] = "1"
        DosaBypassButton.configure(bg='White')

        MenutupSemuaAuratButton=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=14)
        MenutupSemuaAuratButton["font"] = ft
        MenutupSemuaAuratButton["fg"] = "#333333"
        MenutupSemuaAuratButton["justify"] = "left"
        MenutupSemuaAuratButton["text"] = " Menutup Semua Aurat"
        MenutupSemuaAuratButton.place(x=270,y=310,width=250,height=30)
        MenutupSemuaAuratButton["offvalue"] = "0"
        MenutupSemuaAuratButton["onvalue"] = "1"
        MenutupSemuaAuratButton.configure(bg='White')

        MempercepatTarawihButton=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=14)
        MempercepatTarawihButton["font"] = ft
        MempercepatTarawihButton["fg"] = "#333333"
        MempercepatTarawihButton["justify"] = "left"
        MempercepatTarawihButton["text"] = " Mempercepat Tarawih"
        MempercepatTarawihButton.place(x=270,y=410,width=250,height=30)
        MempercepatTarawihButton["offvalue"] = "0"
        MempercepatTarawihButton["onvalue"] = "1"
        MempercepatTarawihButton.configure(bg='White')

        KecepatanTarawihLabel=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12)
        KecepatanTarawihLabel["font"] = ft
        KecepatanTarawihLabel["fg"] = "#333333"
        KecepatanTarawihLabel["justify"] = "left"
        KecepatanTarawihLabel["text"] = "Kecepatan Tarawih:"
        KecepatanTarawihLabel.place(x=-95,y=450,width=373,height=30)
        KecepatanTarawihLabel.configure(bg='White')

        LicenseLabel=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12)
        LicenseLabel["font"] = ft
        LicenseLabel["fg"] = "#333333"
        LicenseLabel["justify"] = "left"
        LicenseLabel["text"] = "License: Valid Until 2024 (1KDN-XXX-XXXX-XX)"
        LicenseLabel.place(x=-95,y=565,width=580,height=30)
        LicenseLabel.configure(bg='White')

        KecepatanTarawihSlider=tk.Scale(root)
        KecepatanTarawihSlider["orient"] = "horizontal"
        KecepatanTarawihSlider["from_"] = "1"
        KecepatanTarawihSlider["to"] = "6"
        KecepatanTarawihSlider.place(x=20,y=490,width=550,height=70)
        KecepatanTarawihSlider.configure(bg='White')
        KecepatanTarawihSlider["tickinterval"] = "1"

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
