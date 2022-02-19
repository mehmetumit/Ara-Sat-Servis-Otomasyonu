from enum import Enum
from tkinter import ttk
from abc import ABC, abstractmethod
class AracMenu(ABC):
    def __init__(self):
        self.bg = '#123456'
        self.window_size = "1024x800"
        self.min_window_width = 1024
        self.min_window_height = 800
        self.giris_ekranina_donulsun = False
        
    @property
    def giris_ekranina_donulsun(self):
        return self.__giris_ekranina_donulsun
    
    @giris_ekranina_donulsun.setter
    def giris_ekranina_donulsun(self, flag):
        self.__giris_ekranina_donulsun = flag
    
    def satir_tiplerini_guncelle(self, tree_view:ttk.Treeview, item):
        """İşlem yapılacak tree view ve satır parametre olarak alınır
        Parametre oloarak verilen satırdan sonraki satırların renkleri değiştirilir"""
        sonraki_satir = tree_view.next(item)
        """sonraki_satir '' ise son satıra ulaşılmıştır """
        while sonraki_satir != '':
            satir_tipi = self.satir_tipini_al(tree_view.index(sonraki_satir) - 1)
            tree_view.item(sonraki_satir, tags=satir_tipi)
            sonraki_satir = tree_view.next(sonraki_satir)

    def satir_tipini_al(self, index):
        """Verilen index çift ise "cift_satir", tek ise "tek_satir" 
        stringi döndürülür"""
        return "cift_satir" if index % 2 == 0 else "tek_satir"