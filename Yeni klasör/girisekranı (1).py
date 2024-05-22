import tkinter as tk
from tkinter import messagebox


def giris():
    kullanici_adi = kullanici_adi_entry.get()
    sifre = sifre_entry.get()

    if kullanici_adi== "berke" and sifre=="1234":
        messagebox.showinfo("Giriş Kontrolü", "Giriş Başarılı")

        def AnaEkran_ac():
            import AnaEkran
            AnaEkran.mainloop()
        AnaEkran_ac()
    else:
        if kullanici_adi != "berke" and sifre != "1234":
            messagebox.showerror("Hata", "Şifre ve Kullanıcı Adı Hatalı!")
        elif kullanici_adi != "berke":
            messagebox.showerror("Hata", "Kullanıcı Adı Hatalı!")
        else:
            messagebox.showerror("Hata", "Şifre Hatalı!")


root=tk.Tk()
root.title("Mobil Uygulama İstatiskleri Dashboard")
root.geometry("550x300")
root.config(bg="#9fb6cd")

giris_boyut = tk.Frame(root, padx=50, pady=50, bg="#9fb6cd")
giris_boyut.pack()

baslik_label = tk.Label(giris_boyut, text="Mobil uygulama istatistikleri Dashboard Giriş Ekranı", bg="#9fb6cd", fg="white", font=("Arial", 15))
baslik_label.grid(row=0, column=0, columnspan=2, pady=10)

kullanici_adi_label = tk.Label(giris_boyut, text="Kullanıcı Adı:",bg="#9fb6cd", fg="white", font=("Arial", 10))
kullanici_adi_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)

kullanici_adi_entry = tk.Entry(giris_boyut)
kullanici_adi_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

sifre_label = tk.Label(giris_boyut, text="Şifre:",bg="#9fb6cd", fg="white", font=("Arial", 10))
sifre_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)

sifre_entry = tk.Entry(giris_boyut, show="*")
sifre_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

giris_button = tk.Button(giris_boyut, text="Giriş Yap", command=giris)
giris_button.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

root.mainloop()
