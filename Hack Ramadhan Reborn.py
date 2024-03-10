import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

X_SPACING_BETWEEN_ELEMENTS = 50
Y_SPACING_BETWEEN_ELEMENTS = 10
CHECKBOX_BOOTSTYLE = "square-toggle"

root = tk.Tk()
style = ttk.Style(theme='superhero')
root.title("Hack Ramadhan 2024 Reborn v2.4")
root.iconbitmap("favicon.ico")

title = ttk.Label(root, text="Hack Ramadhan Reborn | 2024", font=("Arial", 30))
title.grid(row=0, column=0, padx=20, pady=80, sticky=N)

ElementFrame = ttk.Frame(root)

HausBypassFrame = ttk.Frame(ElementFrame)

HausBypassState = tk.BooleanVar()
HausBypassState.set(False)
HausBypassCheckbox = ttk.Checkbutton(HausBypassFrame, variable=HausBypassState, bootstyle=CHECKBOX_BOOTSTYLE)
HausBypassCheckbox.grid(row=0, column=0, padx=0, pady=0, sticky=W)
HausBypassLabel = ttk.Label(HausBypassFrame, text="Haus Bypass", font=("Arial", 14))
HausBypassLabel.grid(row=0, column=1, padx=0, pady=0, sticky=E)

HausBypassFrame.grid(row=1, column=0, padx=X_SPACING_BETWEEN_ELEMENTS, pady=Y_SPACING_BETWEEN_ELEMENTS, sticky=W)



AutoBukaFrame = ttk.Frame(ElementFrame)

AutoBukaState = tk.BooleanVar()
AutoBukaState.set(False)
AutoBukaCheckbox = ttk.Checkbutton(AutoBukaFrame, variable=AutoBukaState, bootstyle=CHECKBOX_BOOTSTYLE)
AutoBukaCheckbox.grid(row=0, column=0, padx=0, pady=0, sticky=W)
AutoBukaLabel = ttk.Label(AutoBukaFrame, text="Auto Buka", font=("Arial", 14))
AutoBukaLabel.grid(row=0, column=1, padx=0, pady=0, sticky=E)

AutoBukaFrame.grid(row=2, column=0, padx=X_SPACING_BETWEEN_ELEMENTS, pady=Y_SPACING_BETWEEN_ELEMENTS, sticky=W)



AntiLaparFrame = ttk.Frame(ElementFrame)

AntiLaparState = tk.BooleanVar()
AntiLaparState.set(False)
AntiLaparCheckbox = ttk.Checkbutton(AntiLaparFrame, variable=AntiLaparState, bootstyle=CHECKBOX_BOOTSTYLE)
AntiLaparCheckbox.grid(row=0, column=0, padx=0, pady=0, sticky=W)
AntiLaparLabel = ttk.Label(AntiLaparFrame, text="Anti Lapar", font=("Arial", 14))
AntiLaparLabel.grid(row=0, column=1, padx=0, pady=0, sticky=E)

AntiLaparFrame.grid(row=3, column=0, padx=X_SPACING_BETWEEN_ELEMENTS, pady=Y_SPACING_BETWEEN_ELEMENTS, sticky=W)



Khatam30JuzFrame = ttk.Frame(ElementFrame)

Khatam30JuzState = tk.BooleanVar()
Khatam30JuzState.set(False)
Khatam30JuzCheckbox = ttk.Checkbutton(Khatam30JuzFrame, variable=Khatam30JuzState, bootstyle=CHECKBOX_BOOTSTYLE)
Khatam30JuzCheckbox.grid(row=0, column=0, padx=0, pady=0, sticky=W)
Khatam30JuzLabel = ttk.Label(Khatam30JuzFrame, text="Khatam 30 Juz", font=("Arial", 14))
Khatam30JuzLabel.grid(row=0, column=1, padx=0, pady=0, sticky=E)

Khatam30JuzFrame.grid(row=4, column=0, padx=X_SPACING_BETWEEN_ELEMENTS, pady=Y_SPACING_BETWEEN_ELEMENTS, sticky=W)



AntiTelatSahurFrame = ttk.Frame(ElementFrame)

AntiTelatSahurState = tk.BooleanVar()
AntiTelatSahurState.set(False)
AntiTelatSahurCheckbox = ttk.Checkbutton(AntiTelatSahurFrame, variable=AntiTelatSahurState, bootstyle=CHECKBOX_BOOTSTYLE)
AntiTelatSahurCheckbox.grid(row=0, column=0, padx=0, pady=0, sticky=W)
AntiTelatSahurLabel = ttk.Label(AntiTelatSahurFrame, text="Anti Telat Sahur", font=("Arial", 14))
AntiTelatSahurLabel.grid(row=0, column=1, padx=0, pady=0, sticky=E)

AntiTelatSahurFrame.grid(row=5, column=0, padx=X_SPACING_BETWEEN_ELEMENTS, pady=Y_SPACING_BETWEEN_ELEMENTS, sticky=W)



MempercepatMaghribFrame = ttk.Frame(ElementFrame)

MempercepatMaghribState = tk.BooleanVar()
MempercepatMaghribState.set(False)
MempercepatMaghribCheckbox = ttk.Checkbutton(MempercepatMaghribFrame, variable=MempercepatMaghribState, bootstyle=CHECKBOX_BOOTSTYLE)
MempercepatMaghribCheckbox.grid(row=0, column=0, padx=0, pady=0, sticky=W)
MempercepatMaghribLabel = ttk.Label(MempercepatMaghribFrame, text="Mempercepat Maghrib", font=("Arial", 14))
MempercepatMaghribLabel.grid(row=0, column=1, padx=0, pady=0, sticky=E)

MempercepatMaghribFrame.grid(row=1, column=1, padx=X_SPACING_BETWEEN_ELEMENTS, pady=Y_SPACING_BETWEEN_ELEMENTS, sticky=W)



AntiHausFrame = ttk.Frame(ElementFrame)

AntiHausState = tk.BooleanVar()
AntiHausState.set(False)
AntiHausCheckbox = ttk.Checkbutton(AntiHausFrame, variable=AntiHausState, bootstyle=CHECKBOX_BOOTSTYLE)
AntiHausCheckbox.grid(row=0, column=0, padx=0, pady=0, sticky=W)
AntiHausLabel = ttk.Label(AntiHausFrame, text="Anti Haus", font=("Arial", 14))
AntiHausLabel.grid(row=0, column=1, padx=0, pady=0, sticky=E)

AntiHausFrame.grid(row=2, column=1, padx=X_SPACING_BETWEEN_ELEMENTS, pady=Y_SPACING_BETWEEN_ELEMENTS, sticky=W)



MenutupSemuaAuratFrame = ttk.Frame(ElementFrame)

MenutupSemuaAuratState = tk.BooleanVar()
MenutupSemuaAuratState.set(False)
MenutupSemuaAuratCheckbox = ttk.Checkbutton(MenutupSemuaAuratFrame, variable=MenutupSemuaAuratState, bootstyle=CHECKBOX_BOOTSTYLE)
MenutupSemuaAuratCheckbox.grid(row=0, column=0, padx=0, pady=0, sticky=W)
MenutupSemuaAuratLabel = ttk.Label(MenutupSemuaAuratFrame, text="Menutup Semua Aurat", font=("Arial", 14))
MenutupSemuaAuratLabel.grid(row=0, column=1, padx=0, pady=0, sticky=E)

MenutupSemuaAuratFrame.grid(row=3, column=1, padx=X_SPACING_BETWEEN_ELEMENTS, pady=Y_SPACING_BETWEEN_ELEMENTS, sticky=W)



DosaBypassFrame = ttk.Frame(ElementFrame)

DosaBypassState = tk.BooleanVar()
DosaBypassState.set(False)
DosaBypassCheckbox = ttk.Checkbutton(DosaBypassFrame, variable=DosaBypassState, bootstyle=CHECKBOX_BOOTSTYLE)
DosaBypassCheckbox.grid(row=0, column=0, padx=0, pady=0, sticky=W)
DosaBypassLabel = ttk.Label(DosaBypassFrame, text="Dosa Bypass", font=("Arial", 14))
DosaBypassLabel.grid(row=0, column=1, padx=0, pady=0, sticky=E)

DosaBypassFrame.grid(row=4, column=1, padx=X_SPACING_BETWEEN_ELEMENTS, pady=Y_SPACING_BETWEEN_ELEMENTS, sticky=W)



MempercepatTarawihFrame = ttk.Frame(ElementFrame)

MempercepatTarawihState = tk.BooleanVar()
MempercepatTarawihState.set(False)
MempercepatTarawihCheckbox = ttk.Checkbutton(MempercepatTarawihFrame, variable=MempercepatTarawihState, bootstyle=CHECKBOX_BOOTSTYLE)
MempercepatTarawihCheckbox.grid(row=0, column=0, padx=0, pady=0, sticky=W)
MempercepatTarawihLabel = ttk.Label(MempercepatTarawihFrame, text="Mempercepat Tarawih", font=("Arial", 14))
MempercepatTarawihLabel.grid(row=0, column=1, padx=0, pady=0, sticky=E)

def update_status():
    IsEnabled = MempercepatTarawihState.get()
    if IsEnabled == False:
        KecepatanTarawihScrollbar.configure(state="disabled")
        KecepatanTarawihLabel.configure(text=f"Kecepatan Tarawih: 1x Lebih Cepat")
        KecepatanTarawihScrollbar.configure(value=1)
    else:
        KecepatanTarawihScrollbar.configure(state="enabled")

MempercepatTarawihCheckbox.configure(command=update_status)

MempercepatTarawihFrame.grid(row=5, column=1, padx=X_SPACING_BETWEEN_ELEMENTS, pady=Y_SPACING_BETWEEN_ELEMENTS, sticky=W)



KecepatanTarawihFrame = ttk.Frame(ElementFrame)

KecepatanTarawihLabel = ttk.Label(KecepatanTarawihFrame, text="Kecepatan Tarawih: 1x Lebih Cepat", font=("Arial", 14))
KecepatanTarawihLabel.grid(row=0, column=0, padx=0, pady=Y_SPACING_BETWEEN_ELEMENTS, sticky=W)
KecepatanTarawihScrollbar = ttk.Scale(KecepatanTarawihFrame, orient=HORIZONTAL, from_="1", to="6", length="480", state="disabled")

KecepatanTarawihScrollbar.grid(row=1, column=0, padx=0, pady=Y_SPACING_BETWEEN_ELEMENTS, sticky=W)



KecepatanTarawihScrollbarPrecisionModeToggle = tk.BooleanVar()
KecepatanTarawihScrollbarPrecisionModeToggle.set(False)

def update_label(value):
    IsPrecisionModeEnabled = KecepatanTarawihScrollbarPrecisionModeToggle.get()
    if IsPrecisionModeEnabled == False:
        roundvalue = round(float(value))
        KecepatanTarawihLabel.configure(text=f"Kecepatan Tarawih: {roundvalue}x Lebih Cepat")
        KecepatanTarawihScrollbar.configure(value=roundvalue)
    else:
        roundvalue_2 = round(float(value), 1)
        KecepatanTarawihLabel.configure(text=f"Kecepatan Tarawih: {roundvalue_2}x Lebih Cepat")
        KecepatanTarawihScrollbar.configure(value=roundvalue_2)

KecepatanTarawihScrollbar.configure(command=update_label)

for i in range(1, 7):
    tick = ttk.Label(KecepatanTarawihFrame, text=str(i), font=("Arial", 12))
    tick.place(x=0 + (i-1)*93.3, y=70)

separator = ttk.Label(KecepatanTarawihFrame, text=" ", font=("Arial", 5))
separator.grid(row=2, column=0, padx=0, pady=Y_SPACING_BETWEEN_ELEMENTS, sticky=W)



KecepatanTarawihScrollbarPrecisionModeFrame = ttk.Frame(KecepatanTarawihFrame)

KecepatanTarawihScrollbarPrecisionModeCheckbox = ttk.Checkbutton(KecepatanTarawihScrollbarPrecisionModeFrame, variable=KecepatanTarawihScrollbarPrecisionModeToggle, bootstyle=CHECKBOX_BOOTSTYLE)
KecepatanTarawihScrollbarPrecisionModeCheckbox.grid(row=0, column=0, padx=0, pady=0, sticky=W)
KecepatanTarawihScrollbarPrecisionModeLabel = ttk.Label(KecepatanTarawihScrollbarPrecisionModeFrame, text="Mode Presisi", font=("Arial", 14))
KecepatanTarawihScrollbarPrecisionModeLabel.grid(row=0, column=1, padx=0, pady=0, sticky=E)

KecepatanTarawihScrollbarPrecisionModeFrame.grid(row=2, column=0, padx=0, pady=Y_SPACING_BETWEEN_ELEMENTS*2, sticky=W)



KecepatanTarawihFrame.grid(row=6, column=0, columnspan=2, padx=X_SPACING_BETWEEN_ELEMENTS, pady=Y_SPACING_BETWEEN_ELEMENTS, sticky=W)



ElementFrame.grid(row=1, column=0, padx=10, pady=0)

LicenseKeyValue = "CKAOPQ-FAK-EOO24-0705-QEBUMILIBO" # Egg?

LicenseKey = ttk.Label(root, text=f"License Key: Valid until 2026 ({LicenseKeyValue})", font=("Arial", 12))
LicenseKey.grid(row=2, column=0, padx=20, pady=20, sticky=SW)

root.mainloop()