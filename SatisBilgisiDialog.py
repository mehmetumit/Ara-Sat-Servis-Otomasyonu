from AracDialog import AracDialog
from SatisYoneticisi import SatisTipi
from Musteri import Musteri
from AracSatis import *
from tkinter import *
from tkinter import messagebox 
from tkinter import ttk
import sqlite3
class SatisBilgisiDialog(AracDialog):
    def __init__(self, satis_tipi, secili_arac_bilgisi):
        super().__init__("Satış Bilgisi Dialog")
        self.combobox_listesi = list()
        self.satis_tipi = satis_tipi

        self.kasa_tipi_label = Label(self.dialog_frame,
                                        text="Kasa Tipi",
                                        bg=self.bg,
                                        fg=self.fg,
                                        font= self.widget_font)
        self.segment_label = Label(self.dialog_frame,
                                   text="Segment",
                                   bg=self.bg,
                                   fg=self.fg,
                                   font=self.widget_font)
        self.yil_label = Label(self.dialog_frame,
                               text="Yıl",
                               bg=self.bg,
                               fg=self.fg,
                               font=self.widget_font)
        
        self.motor_label = Label(self.dialog_frame,
                                 text="Motor",
                                 bg=self.bg,
                                 fg=self.fg,
                                 font=self.widget_font)
        
        self.vites_label = Label(self.dialog_frame,
                                 text="Vites",
                                 bg=self.bg,
                                 fg=self.fg,
                                 font=self.widget_font)
        
        self.model_label = Label(self.dialog_frame,
                                 text="Araç Modeli",
                                 bg=self.bg,
                                 fg=self.fg,
                                 font=self.widget_font)
        self.yakit_tipi_label = Label(self.dialog_frame,
                                 text="Yakıt Tipi",
                                 bg=self.bg,
                                 fg=self.fg,
                                 font=self.widget_font)
        self.fiyat_label = Label(self.dialog_frame,
                                 text="Fiyat",
                                 bg=self.bg,
                                 fg=self.fg,
                                 font=self.widget_font)
        self.adet_label = Label(self.dialog_frame,
                                 text="Adet",
                                 bg=self.bg,
                                 fg=self.fg,
                                 font=self.widget_font)
        self.renk_label = Label(self.dialog_frame,
                                 text="Renk",
                                 bg=self.bg,
                                 fg=self.fg,
                                 font=self.widget_font)
        self.satis_tarihi_label = Label(self.dialog_frame,
                                 text="Satış Tarihi",
                                 bg=self.bg,
                                 fg=self.fg,
                                 font=self.widget_font)
        
        #Comboboxlar
        self.segment_combobox = ttk.Combobox(self.dialog_frame,
                                             font=self.widget_font,
                                             state="readonly")
        self.segment_combobox.bind('<<ComboboxSelected>>', lambda e: self.sonrakini_aktiflestir(0))

        self.model_combobox = ttk.Combobox(self.dialog_frame,
                                               font=self.widget_font,
                                               state="disabled")
        self.model_combobox.bind('<<ComboboxSelected>>', lambda e: self.sonrakini_aktiflestir(1))

        self.kasa_tipi_combobox = ttk.Combobox(self.dialog_frame,
                                           font=self.widget_font,
                                           state="disabled")
        self.kasa_tipi_combobox.bind('<<ComboboxSelected>>', lambda e: self.sonrakini_aktiflestir(2))

        self.vites_combobox = ttk.Combobox(self.dialog_frame,
                                           font=self.widget_font,
                                           state="disabled")
        self.vites_combobox.bind('<<ComboboxSelected>>', lambda e: self.sonrakini_aktiflestir(3))

        self.yil_combobox = ttk.Combobox(self.dialog_frame,
                                         font=self.widget_font,
                                         state="disabled")
        self.yil_combobox.bind('<<ComboboxSelected>>', lambda e: self.sonrakini_aktiflestir(4))

        self.motor_combobox = ttk.Combobox(self.dialog_frame,
                                           font=self.widget_font,
                                           state="disabled")
        self.motor_combobox.bind('<<ComboboxSelected>>', lambda e: self.sonrakini_aktiflestir(5))

        self.yakit_tipi_combobox = ttk.Combobox(self.dialog_frame,
                                                font=self.widget_font,
                                                state="disabled")

        self.yakit_tipi_combobox.bind('<<ComboboxSelected>>', lambda e: self.sonrakini_aktiflestir(6))

        self.renk_combobox = ttk.Combobox(self.dialog_frame,
                                         font=self.widget_font,
                                         state="readonly")
        
        self.fiyat_entry  = Entry(self.dialog_frame, font=self.widget_font) 
        self.fiyat_entry.insert(0,secili_arac_bilgisi["fiyat"])
        
        self.adet_entry  = Entry(self.dialog_frame, font=self.widget_font) 
        self.adet_entry.insert(0,secili_arac_bilgisi["adet"])
        
        self.satis_tarihi_entry  = Entry(self.dialog_frame, font=self.widget_font) 
        self.satis_tarihi_entry.insert(0,secili_arac_bilgisi["satis_tarihi"])
       
        #default renkler
        self.renk_combobox["values"]=("beyaz", "siyah", "kırmızı", "mavi", "yeşil", "kahverengi","turuncu","mor")

        self.kasa_tipi_combobox.set(secili_arac_bilgisi["kasa_tipi"])
        self.segment_combobox.set(secili_arac_bilgisi["segment"])
        self.vites_combobox.set(secili_arac_bilgisi["vites"])
        self.motor_combobox.set(secili_arac_bilgisi["motor"])
        self.model_combobox.set(secili_arac_bilgisi["model"])
        self.yakit_tipi_combobox.set(secili_arac_bilgisi["yakit_tipi"])
        self.renk_combobox.set(secili_arac_bilgisi["renk"])
        self.yil_combobox.set(secili_arac_bilgisi["yil"])


        self.kaydet_btn = Button(self.dialog_frame, text='Kaydet', 
                            command=self.kaydet, 
                            bg='black',
                            fg='white',highlightthickness = 0, bd = 0)
        self.iptal_btn = Button(self.dialog_frame, text='İptal', 
                            command=self.iptal, 
                            bg='black',
                            fg='white',highlightthickness = 0, bd = 0)
                
        #Pack
        self.segment_label.pack()
        self.segment_combobox.pack()
        self.combobox_listesi.append(("segment",self.segment_combobox))
        
        
        
        self.model_label.pack()
        self.model_combobox.pack()
        self.combobox_listesi.append(("model",self.model_combobox))
        
        self.kasa_tipi_label.pack()
        self.kasa_tipi_combobox.pack()
        self.combobox_listesi.append(("kasa_tipi",self.kasa_tipi_combobox))
        
        self.vites_label.pack()
        self.vites_combobox.pack()
        self.combobox_listesi.append(("vites",self.vites_combobox))
        
        self.yil_label.pack()
        self.yil_combobox.pack()
        self.combobox_listesi.append(("yil",self.yil_combobox))
        
        self.motor_label.pack()
        self.motor_combobox.pack()
        self.combobox_listesi.append(("motor",self.motor_combobox))
                
        self.yakit_tipi_label.pack()
        self.yakit_tipi_combobox.pack()
        self.combobox_listesi.append(("yakit_tipi",self.yakit_tipi_combobox))
        
        self.renk_label.pack()
        self.renk_combobox.pack()
        
        self.fiyat_label.pack()
        self.fiyat_entry.pack()
        
        self.adet_label.pack()
        self.adet_entry.pack()
        
        """Satış tipine göre satis_tarihi gösterilir veya gizlenir"""
        if self.satis_tipi == SatisTipi.SATILMIS:
            
            self.satis_tarihi_label.pack()
            self.satis_tarihi_entry.pack()
            
        elif self.satis_tipi == SatisTipi.STOK:
           
            self.satis_tarihi_label.forget()
            self.satis_tarihi_entry.forget()

        self.kaydet_btn.pack(padx=13,pady=13)
        self.iptal_btn.pack(padx=13, pady=13)
        
        
        self.veri_tabanina_baglan("arac_cesidi.db")
        """ESC tuşu -> iptal"""
        self.dialog_window.bind("<Escape>", lambda event: self.iptal())
        """Width, Height"""
        self.dialog_window.resizable(False,True)
        self.dialog_window.mainloop()
    @property
    def satis_tipi(self):
        return self.__satis_tipi
    @satis_tipi.setter
    def satis_tipi(self, satis_tipi):
        self.__satis_tipi = satis_tipi
   
    def sonrakini_aktiflestir(self, index):
        """
        indexi verilen comboboxtan sonraki comboboxların state i disable yapılır
        ve içeriği temizlenir.Ardından bir sonraki comboboxın değerleri sonraki_degerleri_al 
        methodu ile içerisine yerleştirilir.
        """
        liste_uzunlugu = len(self.combobox_listesi)
        """combobox tupledır ve 0. indexi ismini 1. indexi o isem ait
        combobox nesnesini temsil eder."""
        for combobox in self.combobox_listesi[index+1:]:
            combobox[1].configure(state="disable")
            combobox[1].set("")
        """index son combobox ise sonraki comboboxın değerleri alınmaz ve state i değiştirilmez"""
        if index != liste_uzunlugu - 1:
            self.combobox_listesi[index+1][1].config(state="readonly")
            self.combobox_listesi[index+1][1]["values"] = self.sonraki_degerleri_al(index)
    def sonlandir(self):
        """Veritabanı bağlantısı ve pencere sonlandırılır"""
        self.cur.close()
        self.conn.close()
        """quit -> main loop dan çıkar.
        Yazılmaz ise sonsuz döngüde kalır Dialog un oluşturulduğu yerden çıkamaz."""
        self.dialog_window.quit()
        """window daki bütün widgetları yok eder."""
        self.dialog_window.destroy()
    def sonraki_degerleri_al(self, index):
        """
        indexi alınan comboboxtan sonraki comboboxın değerleri belirlenir.
        İlk index için segmente göre diğer indexlerde ise modele göre değerler alınır.
        """
        if index == 0:
            """Segment sütunu"""
            simdiki_sutun = self.combobox_listesi[0][0]
            """Segmentin şimdiki değeri"""
            simdiki_sutun_degeri = self.combobox_listesi[0][1].get()
            
        else:
            """Model sütunu"""
            simdiki_sutun = self.combobox_listesi[1][0]
            """Modelin şimdiki değeri"""
            simdiki_sutun_degeri = self.combobox_listesi[1][1].get()
        
        """sonraki combobox"""
        aranan_sonraki_sutun = self.combobox_listesi[index+1][0]
        
        """DISTINCT -> aynı değerlerin 1 kere alınması için kullanılır"""
        self.cur.execute(f'SELECT DISTINCT {aranan_sonraki_sutun} FROM arac_cesidi WHERE {simdiki_sutun} == ?',(simdiki_sutun_degeri,))
        """satir tuple olduğu için ilk indexi alınır böylece text olarak elde edilmiş olur"""
        """ satir = (metin,) -> satir[0] = metin"""
        degerler = [satir[0] for satir in self.cur.fetchall()]
        
        return degerler
    def kaydet(self):#1.345,678,54 -> 1345,678,54 -> 1345.678.54 ->532,345,465.456
        """Kaydetmeden önce adet bilgisinin geçerliliği kontrol edilir"""
        if not self.degerler_gecerli_mi(self.degeri_duzenle(self.adet_entry.get()),
                                        False,
                                        "Adet bilgisi sıfırdan küçük olamaz!",
                                        "Adet bilgisi tam sayı olmalıdır!"):
            return
        if not self.degerler_gecerli_mi(self.degeri_duzenle(self.fiyat_entry.get()),
                                        True, 
                                        "Fiyat bilgisi sıfırdan küçük olamaz!",
                                        "Fiyat bilgisi ondalıklı sayı olmalıdır!"):
            return
                         
        self.kaydedilsin = True
        self.yeni_arac_bilgisi = self.yeni_arac_bilgisi_al()
        self.sonlandir()
    def veri_tabanina_baglan(self, dosya_adi):
        """
        Araç çeşidi veri tabanı ile bağlantı kurulur ardından ilk combobbox ın değerleri
        veritabanından alınıp comboboxa yerleştirilir
        """
        self.conn = sqlite3.connect(dosya_adi)
        self.cur = self.conn.cursor()
        """aranan_sutun -> ilk combobox"""
        aranan_sutun = self.combobox_listesi[0][0]
        """DISTINCT -> aynı değerlerin 1 kere alınması için kullanılır"""
        self.cur.execute(f"SELECT DISTINCT {aranan_sutun} FROM arac_cesidi")
        """Aranan sütunun aynı olmayan verileri comboboxa eklenir"""
        self.combobox_listesi[0][1]["values"]=[satir for satir in self.cur.fetchall()]
    def yeni_arac_bilgisi_al(self):
        """Yeni araç bilgisi sözlük olarak döndürülür"""
        return  {"segment":self.segment_combobox.get(),
                "model":self.model_combobox.get(),
                "kasa_tipi":self.kasa_tipi_combobox.get(),
                "vites":self.vites_combobox.get(),
                "yil":self.yil_combobox.get(),
                "motor":self.motor_combobox.get(),
                "yakit_tipi":self.yakit_tipi_combobox.get(),
                "renk":self.renk_combobox.get(),
                #Fiyat bilgisi başındaki sıfırlar atılarak üçerli şekilde güncellenir
                #Ardından virgül ile noktalar yer değiştirilir 
                "fiyat":self.degistir_virgul_nokta(f"{float(self.degeri_duzenle(self.fiyat_entry.get())):,}"),
                #Adedin başına girilen sıfırlar silinir
                "adet":self.degistir_virgul_nokta(f"{int(self.degeri_duzenle(self.adet_entry.get())):,}"),
                "satis_tarihi":self.satis_tarihi_entry.get()}

    def iptal(self):
        self.kaydedilsin = False
        self.sonlandir()
    