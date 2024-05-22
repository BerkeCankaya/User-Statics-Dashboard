import tkinter as tk
from tkinter import messagebox
import mysql.connector

def en_cok_indirilen_uygulamalar():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="mobil_uygulama_istatiskleri"
        )

        if mydb.is_connected():
            print("Veritabanına başarıyla bağlandı!")

        sql = """
            SELECT uygulamalar.Uygulama_Adı,uygulamalar.Uygulama_Geliştirici,COUNT(indirme_istatiskleri.Uygulama_ID) AS Indirme_Sayisi
            FROM indirme_istatiskleri,uygulamalar
            WHERE indirme_istatiskleri.İndirme_Durumu = 'Tamamlandı' AND
            indirme_istatiskleri.İndirme_tarihi BETWEEN "2020.01.01" AND "2023.12.31" AND
            indirme_istatiskleri.Uygulama_ID = uygulamalar.Uygulama_ID
            GROUP BY uygulamalar.Uygulama_Adı,uygulamalar.Uygulama_Geliştirici
            ORDER BY Indirme_Sayisi DESC
            LIMIT 3;
        """

        mycursor = mydb.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()

        messagebox.showinfo("Uygulama Adı", f"Uygulama Geliştiricisi {result}")



        mydb.close()

    except mysql.connector.Error as err:
        print("Hata:", err)
        messagebox.showerror("Hata", "Veritabanına bağlanırken bir hata oluştu!")

def kullanici_indirme_sayisi():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="mobil_uygulama_istatiskleri"
        )

        if mydb.is_connected():
            print("Veritabanına başarıyla bağlandı!")

        mycursor = mydb.cursor()

        secilen_cihaz = secim.get()
        cihaz_adlari = {1: 'İOS', 2: 'Android', 3: 'Windows'}

        sql = f"SELECT COUNT(*) FROM indirme_istatiskleri WHERE İndirme_cihazı = '{cihaz_adlari[secilen_cihaz]}' AND İndirme_durumu='Tamamlandı'"
        mycursor.execute(sql)
        indirme_sayisi = mycursor.fetchone()[0]

        messagebox.showinfo(f"{cihaz_adlari[secilen_cihaz]} Kullanıcı Sayısı",
                            f"{cihaz_adlari[secilen_cihaz]} Kullanıcı Sayısı: {indirme_sayisi}")

        mydb.close()
    except mysql.connector.Error as err:
        print("Hata:", err)
        messagebox.showerror("Hata", "Veritabanına bağlanırken bir hata oluştu!")
def Uygulama_Ekle():
    Uygulama_Adı = Uygulama_Adı_entry.get()
    Uygulama_Geliştirici = Uygulama_Geliştirici_entry.get()

    if Uygulama_Adı and Uygulama_Geliştirici:
        try:

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="mobil_uygulama_istatiskleri"
            )

            if mydb.is_connected():
                print("Veritabanına başarıyla bağlandı!")

            mycursor = mydb.cursor()
            sql = "INSERT INTO uygulamalar (Uygulama_Adı,Uygulama_Geliştirici) VALUES (%s, %s)"
            values = ( Uygulama_Adı,Uygulama_Geliştirici)
            mycursor.execute(sql, values)

            mydb.commit()

            print("Uygulama başarıyla eklendi!")

            mydb.close()

            Uygulama_Adı_entry.delete(0, tk.END)
            Uygulama_Geliştirici_entry.delete(0, tk.END)

            messagebox.showinfo("Başarılı", "Yeni Uygulama oluşturuldu!")
        except mysql.connector.Error as err:
            print("Hata:", err)
            messagebox.showerror("Hata", "Uygulama eklenemedi!")
    else:
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurun!")

def toplamuygulama():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="mobil_uygulama_istatiskleri"
        )

        if mydb.is_connected():
            print("Veritabanına başarıyla bağlandı!")

        mycursor = mydb.cursor()
        mycursor.execute("SELECT COUNT(*) FROM uygulamalar")
        total_users = mycursor.fetchone()[0]

        messagebox.showinfo("Toplam Uygulama Sayısı", f"Toplam Uygulama Sayısı: {total_users}")

        mydb.close()
    except mysql.connector.Error as err:
        print("Hata:", err)
        messagebox.showerror("Hata", "Veritabanına bağlanırken bir hata oluştu!")



def kullanici_ekle():
    Kullanıcı_Adı = kullanici_adi_entry.get()
    Kullanıcı_Soyadı = kullanıcı_soyadı_entry.get()
    Kullanıcı_Ülke = ülke_entry.get()
    Kullanıcı_Cinsiyet = cinsiyet_entry.get()
    Kullanıcı_Yas = yas_entry.get()

    if Kullanıcı_Adı and Kullanıcı_Soyadı and Kullanıcı_Ülke and Kullanıcı_Cinsiyet and Kullanıcı_Yas:
        try:
            # Veritabanı bağlantısı
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="mobil_uygulama_istatiskleri"
            )

            if mydb.is_connected():
                print("Veritabanına başarıyla bağlandı!")

            # Veri ekleme işlemi
            mycursor = mydb.cursor()
            sql = "INSERT INTO Kullanıcılar (Kullanıcı_Adı, Kullanıcı_Soyadı, Kullanıcı_Ülke, Kullanıcı_Cinsiyet, Kullanıcı_Yas) VALUES (%s, %s, %s, %s, %s)"
            values = (Kullanıcı_Adı, Kullanıcı_Soyadı, Kullanıcı_Ülke, Kullanıcı_Cinsiyet, Kullanıcı_Yas)
            mycursor.execute(sql, values)

            # Değişiklikleri kaydetme
            mydb.commit()

            print("Kullanıcı başarıyla eklendi!")

            # Bağlantıyı kapatma
            mydb.close()

            kullanici_adi_entry.delete(0, tk.END)
            kullanıcı_soyadı_entry.delete(0, tk.END)
            ülke_entry.delete(0, tk.END)
            cinsiyet_entry.delete(0, tk.END)
            yas_entry.delete(0, tk.END)

            messagebox.showinfo("Başarılı", "Yeni kullanıcı oluşturuldu!")
        except mysql.connector.Error as err:
            print("Hata:", err)
            messagebox.showerror("Hata", "Kullanıcı eklenemedi!")
    else:
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurun!")


def toplamkullanıcı():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="mobil_uygulama_istatiskleri"
        )

        if mydb.is_connected():
            print("Veritabanına başarıyla bağlandı!")

        mycursor = mydb.cursor()
        mycursor.execute("SELECT COUNT(*) FROM Kullanıcılar")
        total_users = mycursor.fetchone()[0]

        messagebox.showinfo("Toplam Kullanıcı Sayısı", f"Toplam Kullanıcı Sayısı: {total_users}")

        mydb.close()
    except mysql.connector.Error as err:
        print("Hata:", err)
        messagebox.showerror("Hata", "Veritabanına bağlanırken bir hata oluştu!")


root = tk.Tk()
root.title("Mobil Uygulama Dashboard Sayfası")
root.geometry("1200x800")
baslik_label = tk.Label(root, text="Mobil Uygulama İstatistikleri Dashboard Sayfası", font=("Arial", 18, "bold"), bg="#9fb6cd",fg="white")
baslik_label.grid(row=2, column=7, columnspan=2, padx=100,pady=50)

root.config(bg="#9fb6cd",padx=200)



# Kullanıcı Bilgi Girişi Formu
kullanici_adi_label = tk.Label(root, text="Kullanıcı Adı :",bg="#9fb6cd")
kullanici_adi_label.grid(row=6, column=6,sticky="e",pady=5)
kullanici_adi_entry = tk.Entry(root)
kullanici_adi_entry.grid(row=6, column=7,sticky="w")

kullanıcı_soyadı_label = tk.Label(root, text="Kullanıcı Soyadı :",bg="#9fb6cd")
kullanıcı_soyadı_label.grid(row=7, column=6,sticky="e",pady=5)
kullanıcı_soyadı_entry = tk.Entry(root)
kullanıcı_soyadı_entry.grid(row=7, column=7,sticky="w")

ülke_label = tk.Label(root, text="Ülke :",bg="#9fb6cd")
ülke_label.grid(row=8, column=6,sticky="e",pady=5)
ülke_entry = tk.Entry(root)
ülke_entry.grid(row=8, column=7,sticky="w")

cinsiyet_label = tk.Label(root, text="Cinsiyet :",bg="#9fb6cd")
cinsiyet_label.grid(row=9, column=6,sticky="e",pady=5)
cinsiyet_entry = tk.Entry(root)
cinsiyet_entry.grid(row=9, column=7,sticky="w")

yas_label = tk.Label(root, text="Yaş :",bg="#9fb6cd")
yas_label.grid(row=10, column=6,sticky="e",pady=5)
yas_entry = tk.Entry(root)
yas_entry.grid(row=10, column=7,sticky="w")

kullanici_ekle_button = tk.Button(root, text="Kullanıcı Ekle", command=kullanici_ekle)
kullanici_ekle_button.grid(row=12, column=7,sticky="w",pady=10)

toplamkullanıcı_button = tk.Button(root, text="Toplam Kullanıcı Sayısını Göster", command=toplamkullanıcı)
toplamkullanıcı_button.grid(row=15, column=7,sticky="w",pady=10)

Uygulama_Adı_label = tk.Label(root, text="Uygulama Adı :", bg="#9fb6cd")
Uygulama_Adı_label.place(x=10,y=503)
Uygulama_Adı_entry = tk.Entry(root)
Uygulama_Adı_entry.place(x=135,y=503)


Uygulama_Geliştirici_label = tk.Label(root, text="Uygulama Geliştiricisi :", bg="#9fb6cd")
Uygulama_Geliştirici_label.place(x=10,y=533)
Uygulama_Geliştirici_entry = tk.Entry(root)
Uygulama_Geliştirici_entry.place(x=135,y=533)

Uygulama_Ekle_button = tk.Button(root, text="Uygulama Ekle", command=Uygulama_Ekle)
Uygulama_Ekle_button.place(x=135,y=570)

toplamuygulama_button = tk.Button(root, text="Toplam Uygulama Sayısını Göster", command=toplamuygulama)
toplamuygulama_button.place(x=135,y=610)

secim = tk.IntVar()

radioButton1 = tk.Radiobutton(root, text="İos", variable=secim, value=1,bg="#9fb6cd")
radioButton1.place(x=600,y=125)

radioButton2 = tk.Radiobutton(root, text="Android", variable=secim, value=2,bg="#9fb6cd")
radioButton2.place(x=600,y=150)

radioButton3 = tk.Radiobutton(root, text="Windows", variable=secim, value=3,bg="#9fb6cd")
radioButton3.place(x=600,y=175)

İndirmeCihazı_button = tk.Button(root, text="İndirme Cihazı İstatistikleri",command=kullanici_indirme_sayisi)
İndirmeCihazı_button.place(x=600,y=220)

PopülerUygulamalar_button = tk.Button(root, text="Son 3 yılda en çok indirilen Uygulamalar",command=en_cok_indirilen_uygulamalar)
PopülerUygulamalar_button.place(x=600,y=420)

root.mainloop()


