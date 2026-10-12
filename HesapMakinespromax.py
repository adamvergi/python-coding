import tkinter as tk

print("-------HESAP MAKİNESİ PRO MAX-------")

output = ""
işlem = ""
işlemler = []


def sonuc():
    global output, işlem, işlemler

    işlem = TextB.get()
    işlemler = işlem.split()

    if len(işlemler) == 3:
        n1 = float(işlemler[0])
        p1 = işlemler[1]
        n2 = float(işlemler[2])

        kontrol(n1, p1, n2)
    else:
        Text.config(
            text="Lütfen aralarda boşluk bırakın!\nÖrnek format: 4 * 4"
        )


def kontrol(n1, p1, n2):
    global output

    if p1 == "+":
        output = n1 + n2
    elif p1 == "-":
        output = n1 - n2
    elif p1 == "*":
        output = n1 * n2
    elif p1 == "/":
        if n2 == 0:
            output = "Sıfıra bölünemez!"
        else:
            output = n1 / n2
    else:
        output = "Geçersiz işlem!"

    Text.config(text=f"Sonuç = {output}")


main = tk.Tk()
main.title("Hesap Makinesi Pro Max")
main.geometry("500x500")

TextB = tk.Entry(main)
Button = tk.Button(master=main, text="İşlemi yap", command=sonuc)
Text = tk.Label(main, font=("Arial", 12))

TextB.pack(pady=10)
Button.pack(pady=5)
Text.pack(pady=10)

main.mainloop()