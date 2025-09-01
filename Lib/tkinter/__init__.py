import tkinter as tk
from tkinter import messagebox

# Dicționar pentru stocare elevi și punctaje
elevi = {}

def adauga_elev():
    nume = entry_nume.get()
    punctaje_str = entry_punctaje.get()

    if not nume or not punctaje_str:
        messagebox.showwarning("Eroare", "Completează toate câmpurile!")
        return

    try:
        punctaje = [float(x) for x in punctaje_str.split(",")]
    except ValueError:
        messagebox.showwarning("Eroare", "Introdu punctajele separate prin virgulă (ex: 8,9,7)")
        return

    elevi[nume] = punctaje
    entry_nume.delete(0, tk.END)
    entry_punctaje.delete(0, tk.END)
    messagebox.showinfo("Succes", f"Elevul {nume} a fost adăugat!")

def calculeaza_clasament():
    if not elevi:
        messagebox.showwarning("Eroare", "Nu există date!")
        return

    rezultate = []
    for nume, puncte in elevi.items():
        media = sum(puncte) / len(puncte)
        rezultate.append((nume, round(media, 2)))

    clasament = sorted(rezultate, key=lambda x: x[1], reverse=True)

    text_afisare = "Clasament final:\n\n"
    for loc, (nume, medie) in enumerate(clasament, start=1):
        text_afisare += f"{loc}. {nume} - nota finală: {medie}\n"

    messagebox.showinfo("Clasament", text_afisare)


# === INTERFAȚA TKINTER ===
root = tk.Tk()
root.title("Calculator Note și Clasament")

# Câmp nume
tk.Label(root, text="Nume elev:").grid(row=0, column=0, padx=5, pady=5)
entry_nume = tk.Entry(root)
entry_nume.grid(row=0, column=1, padx=5, pady=5)

# Câmp punctaje
tk.Label(root, text="Punctaje (separate prin virgulă):").grid(row=1, column=0, padx=5, pady=5)
entry_punctaje = tk.Entry(root)
entry_punctaje.grid(row=1, column=1, padx=5, pady=5)

# Butoane
btn_adauga = tk.Button(root, text="Adaugă elev", command=adauga_elev)
btn_adauga.grid(row=2, column=0, padx=5, pady=10)

btn_calculeaza = tk.Button(root, text="Calculează clasament", command=calculeaza_clasament)
btn_calculeaza.grid(row=2, column=1, padx=5, pady=10)

root.mainloop()
