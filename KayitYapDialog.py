from HashAraci import HashAraci
from tkinter import *
from Yonetici import *
import sqlite3

class KayıtYapDialog:
    def __init__(self):
        self.bg = '#123456'
        self.fg = 'white'
        self.window_size = "1024x800"
        self.widget_font =("Arial",20,"")
        self.geri_donulsun = False
        self.window = Tk()
        self.window.minsize(1024,900)
        self.window.geometry(self.window_size)
        self.window.title("Admin Paneli")
        self.window.iconbitmap("./logo.ico")
        self.veri_tabanina_baglan()
        
        self.window.config(background=self.bg)

        self.frame_box = Frame(self.window,bg=self.bg)
        
        self.mesaj_label = Label(self.frame_box,text="", font=self.widget_font, bg=self.bg)

        self.title = Label(self.frame_box, text="Kayıt Ekranı", font=("Arial", 40, "bold"), fg=self.fg,bg=self.bg)
        
        self.admin_id_label = Label(self.frame_box, text="Admin ID", font=self.widget_font, fg=self.fg,bg=self.bg)
        self.admin_id_entry = Entry(self.frame_box, font=self.widget_font)
        
        self.admin_sifre_label = Label(self.frame_box, text="Admin Şifre", font=self.widget_font, fg=self.fg,bg=self.bg)
        self.admin_sifre_entry = Entry(self.frame_box, font=self.widget_font, show='*')
        
        self.id_label = Label(self.frame_box, text="ID", font=self.widget_font, fg=self.fg,bg=self.bg)
        self.id_entry = Entry(self.frame_box, font=self.widget_font)
        
        self.sifre_label = Label(self.frame_box, text="Şifre", font=self.widget_font, fg=self.fg,bg=self.bg)
        self.sifre_entry = Entry(self.frame_box, font=self.widget_font, show='*')
        
        self.kayit_yap_btn = Button(self.frame_box, text='Kayıt Yap', command=self.kayit_yap, 
                                font=self.widget_font, bg='black',fg='white',highlightthickness = 0, bd = 0)
        self.geri_don_btn = Button(self.frame_box, text='Geri Dön', command=self.geri_don, 
                                font=self.widget_font, bg='black',fg='white',highlightthickness = 0, bd = 0)

        self.satis_radio_btn = Radiobutton(self.frame_box,
                                           text="Satış",
                                           bg=self.bg,
                                           fg="white",
                                           selectcolor="black",
                                           value=1,
                                           command=lambda :self.yonetici_sec(YoneticiTipi.SATIS),
                                           font=self.widget_font,
                                           width=6,highlightthickness = 0, bd = 0,)
        self.satis_radio_btn.select()
        self.yonetici_sec(YoneticiTipi.SATIS)
        
        self.servis_radio_btn = Radiobutton(self.frame_box,
                                            text="Servis",
                                            bg=self.bg,
                                            fg="white",
                                            selectcolor="black",
                                            value=0,
                                            command=lambda :self.yonetici_sec(YoneticiTipi.SERVIS),
                                            font=self.widget_font,
                                            width=6,highlightthickness = 0, bd = 0)
       
        self.frame_box.pack(pady=30)
        self.title.grid(row=0,column=1,columnspan=2,pady=10)
        
        self.admin_id_label.grid(row=1,column=1,columnspan=2,pady=10)
        self.admin_id_entry.grid(row=2,column=1,columnspan=2,pady=10)
        self.admin_sifre_label.grid(row=3,column=1,columnspan=2,pady=10)
        self.admin_sifre_entry.grid(row=4,column=1,columnspan=2,pady=10)
        
        self.id_label.grid(row=5,column=1,columnspan=2,pady=10)
        self.id_entry.grid(row=6,column=1,columnspan=2,pady=10)
        self.sifre_label.grid(row=7,column=1,columnspan=2,pady=10)
        self.sifre_entry.grid(row=8,column=1,columnspan=2,pady=10)
        
        self.kayit_yap_btn.grid(row=9,column=0,columnspan=2,pady=10)
        self.geri_don_btn.grid(row=9,column=2,columnspan=2,pady=10)
        self.satis_radio_btn.grid(row=10, column=0,columnspan=2,pady=10)
        self.servis_radio_btn.grid(row=10, column=2,columnspan=2,pady=10)
        self.mesaj_label.grid(row=11, column=1, columnspan=2, pady=10)
        """Sayfa yüklenince id girişinin yapılacağı kısıma tıklamadan giriş yapılabilir"""
        self.admin_id_entry.focus()
        """Enter tuşu ile giriş yapılması"""
        self.window.bind("<Return>", lambda event: self.kayit_yap())
        """Pencere kapatılınca sonsuz döngüye girmemesi için"""
        self.window.protocol("WM_DELETE_WINDOW", self.sonlandir)
        self.window.mainloop()
    @property
    def geri_donulsun(self):
        return self.__geri_donulsun
    @geri_donulsun.setter
    def geri_donulsun(self, geri_donulsun:bool):
        self.__geri_donulsun = geri_donulsun
    def yonetici_sec(self, yonetici_tipi:YoneticiTipi):
        self.secili_yonetici = yonetici_tipi
    def veri_tabanina_baglan(self):
        self.conn = sqlite3.connect("yonetici.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS servis_yoneticisi(Id TEXT, sifre TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS admin(Id TEXT, sifre TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS satis_yoneticisi(Id TEXT, sifre TEXT)")
        
        self.conn.commit()
        
    def admin_giris_kontrol(self):
        admin_hash = HashAraci.hash_yap(self.admin_id_entry.get(),self.admin_sifre_entry.get())
        admin_flag = False
        self.cur.execute("SELECT * FROM admin")
        for row in self.cur.fetchall():
            if row[0] == admin_hash["Id"] and row[1] == admin_hash["sifre"]:
                admin_flag = True
                break
        if not admin_flag:
            self.mesaj_label.config(text="Admin Id veya şifre hatalı!", fg='#FF0000')
            return False
        return True
    def kayit_yap(self):
        if self.admin_giris_kontrol():
            if self.secili_yonetici == YoneticiTipi.SATIS:
                yonetici_tipi_adi = "satis_yoneticisi"
            elif self.secili_yonetici == YoneticiTipi.SERVIS:
                yonetici_tipi_adi = "servis_yoneticisi"
            else:
                return
            yonetici_hash = HashAraci.hash_yap(self.id_entry.get(),self.sifre_entry.get())
            self.cur.execute(f"SELECT * FROM {yonetici_tipi_adi} WHERE Id=?",(yonetici_hash["Id"],))
            if len(self.cur.fetchall()) != 0:
                self.mesaj_label.config(text="Yönetici Id zaten mevcut!", fg='#FF0000')
                return
            else:
                if not self.sifre_kontrol(self.sifre_entry.get()):
                    return
                else:
                    self.cur.execute(f"INSERT INTO {yonetici_tipi_adi} VALUES(:id,:sifre)",(yonetici_hash["Id"],yonetici_hash["sifre"]))
                    self.conn.commit()
                    self.mesaj_label.config(text="Kayıt işlemi başarılı...",fg='#00FF00')
    def sifre_kontrol(self, sifre):
        if len(sifre) > 8:
            self.mesaj_label.config(text="Şifre 8 karakterden büyük olamaz!", fg='#FF0000')
            return False
        elif len(sifre) < 4:
            self.mesaj_label.config(text="Şifre minimum 4 karakter olmalıdır!", fg='#FF0000')
            return False
        return True
    def geri_don(self):
        self.sonlandir()
        self.geri_donulsun = True
    def sonlandir(self):
        """window.quit() -> mainloop sonlandırılır"""
        self.window.quit()
        """window.destroy() -> pencere yok edilir"""
        self.window.destroy()