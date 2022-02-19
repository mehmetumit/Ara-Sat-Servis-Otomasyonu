from AracDialog import AracDialog
from SatisYoneticisi import SatisTipi
from Musteri import Musteri
from AracSatis import *
from tkinter import *
from tkinter import messagebox 
from tkinter import ttk
import sqlite3
class AracCesidiDialog(AracDialog):
    def __init__(self):
        super().__init__("Araç Çeşidi Dialog")
       
        #Labellar
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
        
          
        #entrylar
        self.segment_combobox = ttk.Combobox(self.dialog_frame,
                                             font=self.widget_font,
                                             )
         
        self.kasa_tipi_combobox = ttk.Combobox(self.dialog_frame,
                                               font=self.widget_font,
                                               )
        self.vites_combobox = ttk.Combobox(self.dialog_frame,
                                               font=self.widget_font,
                                               )
        self.yil_combobox = ttk.Combobox(self.dialog_frame,
                                               font=self.widget_font,
                                               )
        self.motor_combobox = ttk.Combobox(self.dialog_frame,
                                               font=self.widget_font,
                                               )
        self.yakit_tipi_combobox = ttk.Combobox(self.dialog_frame,
                                               font=self.widget_font,
                                               )


        self.model_entry = Entry(self.dialog_frame,
                                           font=self.widget_font,
                                           )
        
        self.segment_combobox["values"]=("A","B","C","D","S","E","G")
        
        self.kasa_tipi_combobox["values"]=("Cabrio","Sedan","Coupe","Hatchback","Station Vagon","SUV")
        
        self.vites_combobox["values"]=("manuel","yarı otomatik","tam otomatik")
        
        self.yil_combobox["values"]=("2019","2020","2021")
        
        self.motor_combobox["values"]=("1301-1600","1601-1800","1801-2000","3001-4000", "yok")

        self.yakit_tipi_combobox["values"]=("dizel","hybrit","benzin","elektrik")
        
        
        

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
        
        self.model_label.pack()
        self.model_entry.pack()
        
        self.kasa_tipi_label.pack()
        self.kasa_tipi_combobox.pack()
        
        self.vites_label.pack()
        self.vites_combobox.pack()
        
        self.yil_label.pack()
        self.yil_combobox.pack()
        
        self.motor_label.pack()
        self.motor_combobox.pack()
                
        self.yakit_tipi_label.pack()
        self.yakit_tipi_combobox.pack()
       
        self.kaydet_btn.pack(padx=13,pady=13)
        self.iptal_btn.pack(padx=13, pady=13)
        
        
       
        """ESC tuşu -> iptal"""
        self.dialog_window.bind("<Escape>", lambda event: self.iptal())
        """Width, Height"""
        self.dialog_window.resizable(False,True)
        self.dialog_window.mainloop()
        
   
   
    def sonlandir(self):
        
        """quit -> main loop dan çıkar.
        Yazılmaz ise sonsuz döngüde kalır Dialog un oluşturulduğu yerden çıkamaz."""
        self.dialog_window.quit()
        """window daki bütün widgetları yok eder."""
        self.dialog_window.destroy()

    def kaydet(self):
        
        self.yeni_arac_bilgisi = self.yeni_arac_bilgisi_al()
        for val in self.yeni_arac_bilgisi.values():
            if val == '':
                messagebox.showwarning(parent=self.dialog_frame,title="Hata",
                                     message="Araç çeşidi bilgileri boş olamaz!")
                return
        
        self.kaydedilsin = True
        self.sonlandir()
        
    def yeni_arac_bilgisi_al(self):
        """Yeni araç çeşidi bilgisi sözlük olarak döndürülür"""
        return  {"segment":self.segment_combobox.get(),
                "model":self.model_entry.get(),
                "kasa_tipi":self.kasa_tipi_combobox.get(),
                "vites":self.vites_combobox.get(),
                "yil":self.yil_combobox.get(),
                "motor":self.motor_combobox.get(),
                "yakit_tipi":self.yakit_tipi_combobox.get()}
        
    def iptal(self):
        self.kaydedilsin = False
        self.sonlandir()
    