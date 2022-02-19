from AracDialog import AracDialog
from tkinter.ttk import Combobox
from ServisYoneticisi import ServisTipi
from Musteri import Musteri
from AracServis import AracServis
from tkinter import messagebox
from tkinter import *
class ServisBilgisiDialog(AracDialog):
    def __init__(self, servis_tipi, secili_arac_bilgisi):
        super().__init__("Servis Bilgisi Dialog")
        self.servis_tipi = servis_tipi
        
        self.kasa_tipi_label = Label(self.dialog_frame, text="Kasa Tipi ", 
                      font=("Arial", 18, "bold"),
                      fg="white",bg=self.bg)
        self.segment_label = Label(self.dialog_frame, text="Segment ", 
                      font=("Arial", 18, "bold"),
                      fg="white",bg=self.bg)
        self.model_label = Label(self.dialog_frame, text="Model ", 
                      font=("Arial", 18, "bold"),
                      fg="white",bg=self.bg)
        self.motor_label = Label(self.dialog_frame, text="Motor ", 
                      font=("Arial", 18, "bold"),
                      fg="white",bg=self.bg)
        self.renk_label = Label(self.dialog_frame, text="Renk ", 
                      font=("Arial", 18, "bold"),
                      fg="white",bg=self.bg)
        self.yakit_tipi_label = Label(self.dialog_frame, text="Yakıt Tipi ", 
                      font=("Arial", 18, "bold"),
                      fg="white",bg=self.bg)
        self.vites_label = Label(self.dialog_frame, text="Vites Türü ", 
                      font=("Arial", 18, "bold"),
                      fg="white",bg=self.bg)
        self.yil_label = Label(self.dialog_frame, text="Yıl ", 
                      font=("Arial", 18, "bold"),
                      fg="white",bg=self.bg)
        self.km_label = Label(self.dialog_frame, text="KM ", 
                      font=("Arial", 18, "bold"),
                      fg="white",bg=self.bg)
        self.plaka_label = Label(self.dialog_frame, text="Plaka ", 
                      font=("Arial", 18, "bold"),
                      fg="white",bg=self.bg)
        self.giris_tarihi_label = Label(self.dialog_frame, text="Giriş Tarihi ", 
                      font=("Arial", 18, "bold"),
                      fg="white",bg=self.bg)
        self.musteri_isim_label = Label(self.dialog_frame, text="Müşteri İsmi ", 
                      font=("Arial", 18, "bold"),
                      fg="white",bg=self.bg)
        self.musteri_tel_label = Label(self.dialog_frame, text="Müşteri Tel ", 
                      font=("Arial", 18, "bold"),
                      fg="white",bg=self.bg)
        self.musteri_talep_label = Label(self.dialog_frame, text="Müşteri Talebi ", 
                      font=("Arial", 18, "bold"),
                      fg="white",bg=self.bg)
        self.teslim_tarihi_label = Label(self.dialog_frame, text="Teslim Tarihi ", 
                        font=("Arial", 18, "bold"),
                        fg="white",bg=self.bg)
        self.durum_raporu_label = Label(self.dialog_frame, text="Durum Raporu ", 
                        font=("Arial", 18, "bold"),
                        fg="white",bg=self.bg)
        
        self.ucret_label = Label(self.dialog_frame, text="Ücret ", 
                        font=("Arial", 18, "bold"),
                        fg="white",bg=self.bg)
        self.kaydet_btn = Button(self.dialog_frame, text='Kaydet', 
                            command=self.kaydet, 
                            bg='black',
                            fg='white',highlightthickness = 0, bd = 0)
        self.iptal_btn = Button(self.dialog_frame, text='İptal', 
                            command=self.iptal, 
                            bg='black',
                            fg='white',highlightthickness = 0, bd = 0)
                
        self.segment_combobox  = Combobox(self.dialog_frame, font=("Arial",18)) 
        self.segment_combobox.insert(0,secili_arac_bilgisi["segment"])
        
        self.model_entry  = Entry(self.dialog_frame, font=("Arial",18))
        self.model_entry.insert(0,secili_arac_bilgisi["model"])
        
        self.kasa_tipi_combobox  = Combobox(self.dialog_frame, font=("Arial",18),)
        self.kasa_tipi_combobox.insert(0,secili_arac_bilgisi["kasa_tipi"])
        
        self.vites_combobox  = Combobox(self.dialog_frame, font=("Arial",18))
        self.vites_combobox.insert(0,secili_arac_bilgisi["vites"])
        
        self.yil_entry  = Entry(self.dialog_frame, font=("Arial",18))
        self.yil_entry.insert(0,secili_arac_bilgisi["yil"])
        
        self.motor_combobox  = Combobox(self.dialog_frame, font=("Arial",18))
        self.motor_combobox.insert(0,secili_arac_bilgisi["motor"])

        self.yakit_tipi_combobox  = Combobox(self.dialog_frame, font=("Arial",18))
        self.yakit_tipi_combobox.insert(0,secili_arac_bilgisi["yakit_tipi"])
        
        self.renk_combobox  = Combobox(self.dialog_frame, font=("Arial",18))
        self.renk_combobox.insert(0,secili_arac_bilgisi["renk"])        
        
        
        self.km_entry  = Entry(self.dialog_frame, font=("Arial",18))
        self.km_entry.insert(0,secili_arac_bilgisi["km"])
        
        self.plaka_entry  = Entry(self.dialog_frame, font=("Arial",18))
        self.plaka_entry.insert(0,secili_arac_bilgisi["plaka"])
        
        self.giris_tarihi_entry  = Entry(self.dialog_frame, font=("Arial",18))
        self.giris_tarihi_entry.insert(0,secili_arac_bilgisi["giris_tarihi"])
        
        self.musteri_isim_entry  = Entry(self.dialog_frame, font=("Arial",18))
        self.musteri_isim_entry.insert(0, secili_arac_bilgisi["musteri_isim"])
        
        self.musteri_tel_entry  = Entry(self.dialog_frame, font=("Arial",18))
        self.musteri_tel_entry.insert(0, secili_arac_bilgisi["musteri_tel"])
        
        self.musteri_talep_text  = Text(self.dialog_frame, font=("Arial",18),width=20, height=5)
        self.musteri_talep_text.insert(END, secili_arac_bilgisi["musteri_talep"])
        self.musteri_talep_text.bind("<Tab>", self.sonrakine_odaklan)

        self.teslim_tarihi_entry  = Entry(self.dialog_frame, font=("Arial",18))
        self.teslim_tarihi_entry.insert(0, secili_arac_bilgisi["teslim_tarihi"])
                    
        self.durum_raporu_text = Text(self.dialog_frame,font=("Arial",18), width=20, height=5)
        self.durum_raporu_text.insert(END, secili_arac_bilgisi["durum_raporu"])
        self.durum_raporu_text.bind("<Tab>", self.sonrakine_odaklan)
        
        self.ucret_entry  = Entry(self.dialog_frame, font=("Arial",18))
        self.ucret_entry.insert(0, secili_arac_bilgisi["ucret"])
        
        
        self.segment_combobox["values"]=("A","B","C","D","S","E","G")
        
        self.renk_combobox["values"]=("beyaz", "siyah", "kırmızı", "mavi", "yeşil", "kahverengi","turuncu","mor")

        self.kasa_tipi_combobox["values"]=("Cabrio","Sedan","Coupe","Hatchback","Station Vagon","SUV")
        
        self.vites_combobox["values"]=("manuel","yarı otomatik","tam otomatik")
                
        self.motor_combobox["values"]=("1301-1600","1601-1800","1801-2000","3001-4000", "yok")

        self.yakit_tipi_combobox["values"]=("dizel","hybrit","benzin","elektrik")
        
        #Pack
        self.segment_label.pack()
        self.segment_combobox.pack() 
        
        self.model_label.pack()
        self.model_entry.pack()
         
        self.kasa_tipi_label.pack() 
        self.kasa_tipi_combobox.pack()
        
        self.vites_label.pack()
        self.vites_combobox.pack()
        
        self.yil_label.pack()
        self.yil_entry.pack()
        
        self.motor_label.pack()
        self.motor_combobox.pack()
        
        self.yakit_tipi_label.pack()
        self.yakit_tipi_combobox.pack()
        
        self.renk_label.pack()
        self.renk_combobox.pack()
        
        self.km_label.pack()
        self.km_entry.pack()
        
        self.plaka_label.pack()
        self.plaka_entry.pack()
        
        self.giris_tarihi_label.pack()
        self.giris_tarihi_entry.pack()
        
        self.musteri_isim_label.pack()
        self.musteri_isim_entry.pack()
        
        self.musteri_tel_label.pack()
        self.musteri_tel_entry.pack()
        
        
        self.musteri_talep_label.pack()
        self.musteri_talep_text.pack()
        
        if self.servis_tipi == ServisTipi.SERVIS_GORMUS:
            self.teslim_tarihi_label.pack()
            self.teslim_tarihi_entry.pack()
            
            self.durum_raporu_label.pack()
            self.durum_raporu_text.pack()
            
            self.ucret_label.pack()
            self.ucret_entry.pack()
        
        elif self.servis_tipi == ServisTipi.SERVISTE:
            self.teslim_tarihi_label.pack_forget()
            self.teslim_tarihi_entry.pack_forget()
            
            self.durum_raporu_label.pack_forget()
            self.durum_raporu_text.pack_forget()
            
            self.ucret_label.pack_forget()
            self.ucret_entry.pack_forget()

        self.kaydet_btn.pack(padx=13,pady=13)
        self.iptal_btn.pack(padx=13, pady=13)
        
        """Başlangıçta en üstte yer alan entry widget'ına odaklanılır"""
        self.segment_combobox.focus()
        """ESC tuşu -> iptal"""
        self.dialog_window.bind("<Escape>", lambda event: self.iptal())
        """Width, Height"""
        self.dialog_window.resizable(False,True)
        self.dialog_window.mainloop()
    @property
    def servis_tipi(self):
        return self.__servis_tipi
    @servis_tipi.setter
    def servis_tipi(self, servis_tipi):
        self.__servis_tipi = servis_tipi
    def sonrakine_odaklan(self, event):
        event.widget.tk_focusNext().focus()
        return 'break'
    
    def sonlandir(self):
        """quit -> main loop dan çıkar.
        Yazılmaz ise sonsuz döngüde kalır Dialog un oluşturulduğu yerden çıkamaz."""
        self.dialog_window.quit()
        """window daki bütün widgetları yok eder."""
        self.dialog_window.destroy()
        
    def kaydet(self):
        if self.servis_tipi == ServisTipi.SERVIS_GORMUS and not self.degerler_gecerli_mi(self.degeri_duzenle(self.ucret_entry.get()),
                                        True,
                                        "Ücret bilgisi sıfırdan küçük olamaz!",
                                        "Ücret bilgisi ondalıklı sayı olmalıdır!"):
            return 
        self.kaydedilsin = True
        self.yeni_arac_bilgisi = self.yeni_arac_bilgisi_al()
        
        self.sonlandir()
        
    def yeni_arac_bilgisi_al(self):
        if self.servis_tipi == ServisTipi.SERVISTE:
            ucret = ""
        else:
            ucret = self.degistir_virgul_nokta(f"{float(self.degeri_duzenle(self.ucret_entry.get())):,}")
            
        """Yeni araç bilgisi sözlük olarak döndürülür"""
        return  {"segment":self.segment_combobox.get(),
                "model":self.model_entry.get(),
                "kasa_tipi":self.kasa_tipi_combobox.get(),
                "vites":self.vites_combobox.get(),
                "yil":self.yil_entry.get(),
                "motor":self.motor_combobox.get(),
                "yakit_tipi":self.yakit_tipi_combobox.get(),
                "renk":self.renk_combobox.get(),
                "km":self.km_entry.get(),
                #Plaka büyütülür ve boşluklar silinir
                "plaka":self.plaka_entry.get().upper().replace(' ', ''),
                "giris_tarihi":self.giris_tarihi_entry.get(),
                "musteri_isim":self.musteri_isim_entry.get(),
                "musteri_tel":self.musteri_tel_entry.get(),
                "musteri_talep":self.musteri_talep_text.get("1.0", "end-1c"),
                "teslim_tarihi":self.teslim_tarihi_entry.get(),
                "durum_raporu":self.durum_raporu_text.get("1.0", "end-1c"),
                #Ücret bilgisi başındaki sıfırlar atılarak üçerli şekilde güncellenir
                "ucret":ucret}
    
    def iptal(self):
        self.kaydedilsin = False
        self.sonlandir()
    