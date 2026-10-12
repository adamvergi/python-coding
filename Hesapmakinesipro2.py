print("-------HESAP MAKİNESİ PRO MAX-------")
while True:
    işlem = input("işlemini gir(4*4): ")
    işlemler = işlem.split()

    n1 = float(işlemler[0])
    p1 = işlemler[1]
    n2 = float(işlemler[2])

    if p1 == "+":
         output = n1 + n2
    elif p1 == "-":
     output = n1 - n2
    elif p1 == "*":
      output = n1 * n2
    elif p1 == "/":
     if n2 == 0:
        print("Hiçbir sayı sıfıra bölünemez!")
     else:
        output = n1 / n2
    else:
     print("Bu işlem geçerli değil!")

    print(f"Sonuç = {output}")




