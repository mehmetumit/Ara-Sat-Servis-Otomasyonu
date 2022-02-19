from tkinter import messagebox
from abc import ABC, abstractmethod
from tkinter import *
class AracDialog(ABC):
    def __init__(self, window_title):
        self.bg = '#123456'
        self.window_size = "768x1000"
        self.fg = 'white'
        self.widget_font = ("Arial",20)
        self.kaydedilsin = False
        
        self.dialog_window = Toplevel()
        self.dialog_window.geometry(self.window_size)
        self.dialog_window.title(window_title)
        self.dialog_window.config(background=self.bg)

        ############################################################################################
        self.dialog_canvas = Canvas(self.dialog_window,  bg=self.bg)
        self.dialog_frame = Frame(self.dialog_canvas,bg=self.bg)
        
        self.scroolbarY = Scrollbar(self.dialog_canvas, orient=VERTICAL,command=self.dialog_canvas.yview)
        self.scroolbarX = Scrollbar(self.dialog_canvas,orient=HORIZONTAL, command=self.dialog_canvas.xview)
        
        
        self.dialog_canvas.configure(yscrollcommand=self.scroolbarY.set)

        self.scroolbarY.pack(side = RIGHT, fill=BOTH)

        self.dialog_canvas.pack(expand=True, fill=BOTH)
        
        self.dialog_window.update()
        pos_x = (self.dialog_window.winfo_width()/2)
        """n -> north scrool'un en üstten başlaması için"""
        self.dialog_canvas.create_window((pos_x,0), window=self.dialog_frame, anchor="n")
        self.dialog_frame.bind('<Configure>', lambda e: self.dialog_canvas.configure(scrollregion=self.dialog_canvas.bbox("all")))
        
        ############################################################################################

    @property
    def yeni_arac_bilgisi(self):
        return self.__yeni_arac_bilgisi
    @yeni_arac_bilgisi.setter
    def yeni_arac_bilgisi(self, yeni_arac_bilgisi):
        self.__yeni_arac_bilgisi = yeni_arac_bilgisi

    @abstractmethod
    def kaydet(self):
        pass
    @abstractmethod
    def sonlandir(self):
        pass
    @abstractmethod
    def kaydet(self):
        pass
    @abstractmethod
    def yeni_arac_bilgisi_al(self):
        pass
    @abstractmethod
    def iptal(self):
        pass
    def degistir_virgul_nokta(self, s:str):
        """Verilen string içerisindeki noktaları virgül virgülleri nokta yapar"""
        """İlk önce virgülleri # işaretine çevirir daha sonra noktaları virgül işaretine
        ardından # işaretini noktaya çevirir böylece yer değiştirilmiş olurlar."""
        return s.replace(',', '#').replace('.', ',').replace('#', '.')
    def degeri_duzenle(self, s:str):
        return self.degistir_virgul_nokta(s.replace('.', '').lstrip('0'))
    def degerler_gecerli_mi(self, deger, ondalikli:bool,negatif_title, tam_sayi_title):
            """Değer bilgisinin geçerli olup olmadığı kontrol edilir"""

            try:
               
                """Değer bilgisi verilen ondalikli parametresine göre float yada int değilse ValueError verir"""
                deger = float(deger) if ondalikli else int(deger)
                """Değer bilgisi 0'dan küçükse hata verir"""
                if deger <= 0:
                    messagebox.showwarning(parent=self.dialog_frame,title="Sıfırdan Büyük Değil Hatası",message=negatif_title)
                    return False
            except ValueError:
                messagebox.showwarning(parent=self.dialog_frame,title="Sayı Hatası",message=tam_sayi_title)
                return False
            """Değer bilgisi geçerli"""
            return True