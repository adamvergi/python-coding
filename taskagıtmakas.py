import random
import customtkinter as ctk

print("======================== TAŞ KAĞIT MAKAS OYUNU(ultra pro max) ===========================")
secimlistesi = ["taş","kağıt","makas"]

def kazandın():
    print("Kazandın!!!")
    print(f"Ben {AIsecim} seçmiştim.")
def kaybettin():
    print("Kaybettin!")
    print(f"Ben {AIsecim} seçmiştim.")
def berabere():
    print("Malesef... Berabere")
    print(f"Ben {AIsecim} seçmiştim.")
while True:
 AIsecim = random.choice(secimlistesi)
 secim = input("Seçimini yap(Taş,Kağıt,Makas): ").lower().strip()

   
 if secim not in secimlistesi:
    print("Geçersiz bir cevap verdin.")
 elif secim == AIsecim:
    berabere()
 elif secim == "kağıt" and AIsecim == "taş":
    kazandın()
 elif secim == "taş" and AIsecim == "makas":
    kazandın()
 elif secim == "makas" and AIsecim == "taş":
    kazandın()
 else:
    kaybettin()
    
    





