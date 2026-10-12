print("-------HESAP MAKİNESİ PRO MAX-------")
while True:
    n1 = float(input("1.Sayıyı gir: "))
    p1 = input("İşleminiz(+,-,*,/) ")
    n2 = float(input("2.Sayıyı gir: "))
    output = 0
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

    def cevir(n):
     if int(len(n)) == 1:
       return int(n)
     else:
       return n

    print(f"Sonuç = {output}")




