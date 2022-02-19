from KayitYapDialog import KayıtYapDialog
from tkinter import *
from typing import Collection
from Yonetici import *
from AracSatis import AracSatis
from AracServis import AracServis
from SatisYoneticisi import SatisYoneticisi
from ServisYoneticisi import ServisYoneticisi



class GirisEkrani:
    def __init__(self):
        self.bg = '#123456'
        self.fg = 'white'
        self.window_size = "1024x800"
        self.widget_font =("Arial",20,"")
        self.giris_basarili = False
        self.window = Tk()
        self.window.minsize(1024,768)
        self.window.geometry(self.window_size)
        self.window.title("Giriş Ekranı")
        
        self.secili_yonetici = IntVar()

        
        #self.window.iconbitmap("./logo.ico")
        self.window.config(background=self.bg)

        self.frame_box = Frame(self.window,bg=self.bg)
        
        self.giris_mesaji_label = Label(self.frame_box, font=self.widget_font, bg=self.bg)

        self.title = Label(self.frame_box, text="Giriş Ekranı", font=("Arial", 40, "bold"), fg=self.fg,bg=self.bg)
        self.id_label = Label(self.frame_box, text="ID", font=self.widget_font, fg=self.fg,bg=self.bg)
        self.Id_entry = Entry(self.frame_box, font=self.widget_font)
        
        self.sifre_label = Label(self.frame_box, text="ŞİFRE", font=self.widget_font, fg=self.fg,bg=self.bg)
        self.sifre_entry = Entry(self.frame_box, font=self.widget_font, show='*')
        
        self.giris_btn = Button(self.frame_box, text='Giriş Yap', command=lambda: self.giris_kontrol(self.Id_entry.get(), 
                                                                                                    self.sifre_entry.get()), 
                                font=self.widget_font, bg='black',fg='white',highlightthickness = 0, bd = 0)
        self.kayit_yap_btn = Button(self.frame_box, text='Kayıt Yap', command=self.kayit_yap, 
                                font=self.widget_font, bg='black',fg='white',highlightthickness = 0, bd = 0)
        
        """Yönetici tipi IntEnum olduğu için IntVar.get() yapabilmek için value'yu int'e cast etmeliyiz"""
        self.satis_radio_btn = Radiobutton(self.frame_box,
                                           text="Satış",
                                           bg=self.bg,
                                           fg="white",
                                           selectcolor="black",
                                           variable=self.secili_yonetici,
                                           font=self.widget_font,
                                           value=int(YoneticiTipi.SATIS),width=6,highlightthickness = 0, bd = 0,)
        
        self.servis_radio_btn = Radiobutton(self.frame_box,
                                            text="Servis",
                                            bg=self.bg,
                                            fg="white",
                                            selectcolor="black",
                                            variable=self.secili_yonetici,
                                            font=self.widget_font,
                                            value=int(YoneticiTipi.SERVIS),width=6,highlightthickness = 0, bd = 0)
       
        self.frame_box.pack(pady=50)
        self.title.grid(row=0,column=1,columnspan=2,pady=20)
        self.id_label.grid(row=1,column=1,columnspan=2,pady=20)
        self.Id_entry.grid(row=2,column=1,columnspan=2,pady=20)
        self.sifre_label.grid(row=3,column=1,columnspan=2,pady=20)
        self.sifre_entry.grid(row=4,column=1,columnspan=2,pady=20)
        self.giris_btn.grid(row=5,column=0,columnspan=2,pady=20)
        self.kayit_yap_btn.grid(row=5,column=2,columnspan=2,pady=20)
        self.satis_radio_btn.grid(row=6, column=0,columnspan=2,pady=20)
        self.servis_radio_btn.grid(row=6, column=2,columnspan=2,pady=20)

        """Sayfa yüklenince id girişinin yapılacağı kısıma tıklamadan giriş yapılabilir"""
        self.Id_entry.focus()
        """Enter tuşu ile giriş yapılması"""
        self.window.bind("<Return>", lambda event: self.giris_kontrol(self.Id_entry.get(),
                                                                self.sifre_entry.get()))
                         
        self.window.mainloop()
    @property
    def yonetici_Id(self):
        return self.__yonetici_Id
    
    @yonetici_Id.setter
    def yonetici_Id(self, Id_hash):
        self.__yonetici_Id = Id_hash
    
    @property
    def yonetici_sifre(self):
        return self.__yonetici_sifre
    
    @yonetici_sifre.setter
    def yonetici_sifre(self, yonetici_sifre_hash):
        self.__yonetici_sifre = yonetici_sifre_hash
    
    @property
    def giris_basarili(self):
        return self.__giris_basarili
    @giris_basarili.setter
    def giris_basarili(self, flag):
        self.__giris_basarili = flag
    
    def giris_kontrol(self, Id, sifre):
        """info -> "Giriş başarılı", "Şifre hatalı!", "Id ve/veya şifre hatalı!"""
        self.giris_basarili, info, self.yonetici_Id, self.yonetici_sifre = Yonetici.giris_kontrol_et(Id, sifre, self.secili_yonetici.get())
        
        if self.giris_basarili:
            self.giris_mesaji_label.config(text=info, fg="#00FF00")
            self.giris_mesaji_label.grid(row=7,column=1,columnspan=2,pady=20)
            """Giriş başarılı pencere yok edilebilir"""
            self.window.destroy()
        else:
            self.giris_mesaji_label.config(text=info, fg="#FF0000")
            self.giris_mesaji_label.grid(row=7, column=1,columnspan=2,pady=20)
    def kayit_yap(self):
        self.window.withdraw()#Pencere gizleme
        kayit_dialog = KayıtYapDialog()
        if kayit_dialog.geri_donulsun:
            self.window.deiconify()#Pencere görünür yapma
        else:
            self.window.destroy()#pencere yok edilir
            
