from AracMenu import AracMenu
from Arac import Arac
import tkinter
from AracServis import AracServis
from ServisYoneticisi import ServisTipi, ServisYoneticisi
from Musteri import Musteri
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ServisBilgisiDialog import ServisBilgisiDialog
from GirisEkrani import GirisEkrani
import json
import textwrap

class ServisMenu(AracMenu):
    def __init__(self, servis_yoneticisi:ServisYoneticisi):
        super().__init__()
        self.servis_yoneticisi = servis_yoneticisi
        self.servis_window = Tk()
        self.servis_window.geometry(self.window_size)
        self.servis_window.minsize(self.min_window_width,self.min_window_height)

        self.servis_window.title("Servis Menu")
        self.giris_ekranina_donulsun = False
       
        ########################################################################
        # Varsayılan temalar
        # ('aqua', 'step', 'clam', 'alt', 'default', 'classic')
        style = ttk.Style()

        style.theme_create('tema',settings={
            "TNotebook": {
                "configure": {
                    "background":"#123456", # Notebook widgetının margin rengi
                    "tabmargins": [5, 5, 0, 0], # sol, üst, sağ, alt
                }
            },
            "TNotebook.Tab": {
                "configure": {
                    "foreground": "#FFFFFF",# Seçili değilken tab yazı rengei
                    "background": '#4d4d4d', # Seçili değilken tab arkaplan rengi
                    "padding": [10, 2], # Yazı ile tab sınırı arasında kalan yatay dolgu, Yazı ile tab sınırı arasında kalan dikey dolgu
                    
                },
                "map": {
                    "foreground": [("selected", "#000000")], #Seçiliyken tab yazı rengi
                    "background": [("selected", '#bfbfbf')], #Seçiliyken tab arkaplan rengi
                    "expand": [("selected", [5, 5, 5, 0])] #Seçiliyken yazı marginlerinin genişletilmesi
                }
            },
            "Treeview":{
                "configure":{
                    "font":"Calibri 10",
                    "foreground":"black",
                    "background":"silver",
                    "fieldbackground":"silver",
                    "rowheight":40,
                },
                "map":{
                    "background": [("selected", "#3756bf")],
                    "foreground": [("selected", "white")]
                }
            },
            "Treeview.Heading":{
                "configure":{
                    "font":"Calibri 12 bold"
                },
            }
        })
        style.theme_use('tema')
        ########################################################################

        self.notebook = ttk.Notebook(self.servis_window)
        self.servistekiler_tab = Frame(self.notebook,bg=self.bg)
        self.servis_gormusler_tab = Frame(self.notebook, bg=self.bg)
        self.notebook.add(self.servistekiler_tab, text="Servisteki Araçlar")
        self.notebook.add(self.servis_gormusler_tab,text="Servis İşlemi Görmüş Araçlar")
        self.notebook.pack(expand=True, fill="both")#***************
        
        self.servis_window.iconbitmap("./logo.ico")
        self.servis_window.config(background=self.bg)
        
        self.servistekiler_label = Label(self.servistekiler_tab, 
                           text="Servisteki Araçlar", 
                           font=("Arial", 40, "bold"), 
                           fg="white",
                           bg=self.bg).pack()
        self.servis_gormusler_label = Label(self.servis_gormusler_tab, 
                           text="Servis Görmüş Araçlar", 
                           font=("Arial", 40, "bold"), 
                           fg="white",
                           bg=self.bg).pack()
        """
        'browse' -> birden fazla satır seçilemez
        'headings' -> #0 sütununun göstermez
        """
        self.servistekiler_treeview = ttk.Treeview(self.servistekiler_tab, selectmode="browse", show="headings")
        self.servis_gormusler_treeview = ttk.Treeview( self.servis_gormusler_tab, selectmode="browse", show="headings")
        
                                                  
        self.servistekiler_treeview['columns'] = ("segment",
                                                  "model",
                                                  "kasa_tipi",
                                                  "vites",
                                                  "yil",
                                                  "motor",
                                                  "yakit_tipi",
                                                  "renk",
                                                  "km",
                                                  "plaka",
                                                  "giris_tarihi",
                                                  "musteri_isim",
                                                  "musteri_tel",
                                                  "musteri_talep")
        self.servis_gormusler_treeview['columns'] = ("segment",
                                                    "model",
                                                    "kasa_tipi",
                                                    "vites",
                                                    "yil",
                                                    "motor",
                                                    "yakit_tipi",
                                                    "renk",
                                                    "km",
                                                    "plaka",
                                                    "giris_tarihi",
                                                    "musteri_isim",
                                                    "musteri_tel",
                                                    "musteri_talep",
                                                    "teslim_tarihi",
                                                    "durum_raporu",
                                                    "ucret")
        self.servistekiler_treeview.column("#0", width=0, minwidth=0)
        self.servistekiler_treeview.column("segment", anchor=CENTER, width=200, minwidth=200)
        self.servistekiler_treeview.column("model", anchor=CENTER, width=200, minwidth=200)
        self.servistekiler_treeview.column("kasa_tipi", anchor=CENTER, width=200, minwidth=200)
        self.servistekiler_treeview.column("vites", anchor=CENTER, width=200, minwidth=200)
        self.servistekiler_treeview.column("yil", anchor=CENTER, width=200, minwidth=200)
        self.servistekiler_treeview.column("motor", anchor=CENTER, width=200, minwidth=200)
        self.servistekiler_treeview.column("yakit_tipi", anchor=CENTER, width=200, minwidth=200)
        self.servistekiler_treeview.column("renk", anchor=CENTER, width=200, minwidth=200)        
        self.servistekiler_treeview.column("km", anchor=CENTER, width=200, minwidth=200)
        self.servistekiler_treeview.column("plaka", anchor=CENTER, width=200, minwidth=200)
        self.servistekiler_treeview.column("giris_tarihi", anchor=CENTER, width=200, minwidth=200)
        self.servistekiler_treeview.column("musteri_isim", anchor=CENTER, width=200, minwidth=200)
        self.servistekiler_treeview.column("musteri_tel", anchor=CENTER, width=200, minwidth=200)
        self.servistekiler_treeview.column("musteri_talep", anchor=CENTER, width=900, minwidth=900)
        
        self.servis_gormusler_treeview.column("#0", width=0, minwidth=0)
        self.servis_gormusler_treeview.column("segment", anchor=CENTER, width=200, minwidth=200)
        self.servis_gormusler_treeview.column("model", anchor=CENTER, width=200, minwidth=200)
        self.servis_gormusler_treeview.column("kasa_tipi", anchor=CENTER, width=200, minwidth=200)
        self.servis_gormusler_treeview.column("vites", anchor=CENTER, width=200, minwidth=200)
        self.servis_gormusler_treeview.column("yil", anchor=CENTER, width=200, minwidth=200)
        self.servis_gormusler_treeview.column("motor", anchor=CENTER, width=200, minwidth=200)
        self.servis_gormusler_treeview.column("yakit_tipi", anchor=CENTER, width=200, minwidth=200)
        self.servis_gormusler_treeview.column("renk", anchor=CENTER, width=200, minwidth=200)        
        self.servis_gormusler_treeview.column("km", anchor=CENTER, width=200, minwidth=200)
        self.servis_gormusler_treeview.column("plaka", anchor=CENTER, width=200, minwidth=200)
        self.servis_gormusler_treeview.column("giris_tarihi", anchor=CENTER, width=200, minwidth=200)
        self.servis_gormusler_treeview.column("musteri_isim", anchor=CENTER, width=200, minwidth=200)
        self.servis_gormusler_treeview.column("musteri_tel", anchor=CENTER)
        self.servis_gormusler_treeview.column("musteri_talep", anchor=CENTER, width=900, minwidth=900)
        self.servis_gormusler_treeview.column("teslim_tarihi", anchor=CENTER, width=200, minwidth=200)
        self.servis_gormusler_treeview.column("durum_raporu", anchor=CENTER, width=900, minwidth=900)
        self.servis_gormusler_treeview.column("ucret", anchor=CENTER, width=200, minwidth=200)
        
        self.servistekiler_treeview.heading("#0", text="")
        self.servistekiler_treeview.heading("segment",text="Segment", anchor=CENTER)
        self.servistekiler_treeview.heading("model",text="Model", anchor=CENTER)
        self.servistekiler_treeview.heading("kasa_tipi",text="Kasa Tipi", anchor=CENTER)
        self.servistekiler_treeview.heading("vites",text="Vites", anchor=CENTER)
        self.servistekiler_treeview.heading("yil",text="Yıl", anchor=CENTER)
        self.servistekiler_treeview.heading("motor",text="Motor", anchor=CENTER)
        self.servistekiler_treeview.heading("yakit_tipi",text="Yakıt Tipi", anchor=CENTER)
        self.servistekiler_treeview.heading("renk",text="Renk", anchor=CENTER)        
        self.servistekiler_treeview.heading("km",text="Km", anchor=CENTER)
        self.servistekiler_treeview.heading("plaka",text="Plaka", anchor=CENTER)
        self.servistekiler_treeview.heading("giris_tarihi",text="Giriş Tarihi", anchor=CENTER)
        self.servistekiler_treeview.heading("musteri_isim",text="Müşteri Ad Soyad", anchor=CENTER)
        self.servistekiler_treeview.heading("musteri_tel",text="Müşteri Tel", anchor=CENTER)
        self.servistekiler_treeview.heading("musteri_talep",text="Müşteri Talep", anchor=CENTER)
        
        self.servis_gormusler_treeview.heading("#0", text="")
        self.servis_gormusler_treeview.heading("segment",text="Segment", anchor=CENTER)
        self.servis_gormusler_treeview.heading("model",text="Model", anchor=CENTER)
        self.servis_gormusler_treeview.heading("kasa_tipi",text="Kasa Tipi", anchor=CENTER)
        self.servis_gormusler_treeview.heading("vites",text="Vites", anchor=CENTER)
        self.servis_gormusler_treeview.heading("yil",text="Yıl", anchor=CENTER)
        self.servis_gormusler_treeview.heading("motor",text="Motor", anchor=CENTER)
        self.servis_gormusler_treeview.heading("yakit_tipi",text="Yakıt Tipi", anchor=CENTER)
        self.servis_gormusler_treeview.heading("renk",text="Renk", anchor=CENTER)        
        self.servis_gormusler_treeview.heading("km",text="Km", anchor=CENTER)
        self.servis_gormusler_treeview.heading("plaka",text="Plaka", anchor=CENTER)
        self.servis_gormusler_treeview.heading("giris_tarihi",text="Giriş Tarihi", anchor=CENTER)
        self.servis_gormusler_treeview.heading("musteri_isim",text="Müşteri Ad Soyad", anchor=CENTER)
        self.servis_gormusler_treeview.heading("musteri_tel",text="Müşteri Tel", anchor=CENTER)
        self.servis_gormusler_treeview.heading("musteri_talep",text="Müşteri Talep", anchor=CENTER)
        self.servis_gormusler_treeview.heading("teslim_tarihi", text="Teslim Tarihi", anchor=CENTER)
        self.servis_gormusler_treeview.heading("durum_raporu", text="Durum Raporu", anchor=CENTER)        
        self.servis_gormusler_treeview.heading("ucret", text="Ücret")
        
        self.servistekiler_treeview.pack(expand=True, fill=BOTH)
        self.servis_gormusler_treeview.pack(expand=True, fill=BOTH)
        
        self.servistekiler_treeview_scroolbarY = Scrollbar(self.servistekiler_treeview)
        self.servistekiler_treeview_scroolbarX = Scrollbar(self.servistekiler_treeview,orient=HORIZONTAL)
        
        self.servis_gormusler_treeview_scroolbarY = Scrollbar(self.servis_gormusler_treeview)
        self.servis_gormusler_treeview_scroolbarX = Scrollbar(self.servis_gormusler_treeview,orient=HORIZONTAL)
        
        self.servistekiler_treeview_scroolbarY.pack(side = RIGHT, fill=BOTH)
        self.servistekiler_treeview_scroolbarX.pack(side=BOTTOM, fill=BOTH)
        self.servistekiler_treeview.config(xscrollcommand=self.servistekiler_treeview_scroolbarX.set,
                                          yscrollcommand = self.servistekiler_treeview_scroolbarY.set)
        self.servistekiler_treeview_scroolbarY.config(command= self.servistekiler_treeview.yview)
        self.servistekiler_treeview_scroolbarX.config(command=self.servistekiler_treeview.xview)
        
        self.servis_gormusler_treeview_scroolbarY.pack(side = RIGHT, fill=BOTH)
        self.servis_gormusler_treeview_scroolbarX.pack(side=BOTTOM, fill=BOTH)
        self.servis_gormusler_treeview.config(xscrollcommand=self.servis_gormusler_treeview_scroolbarX.set,
                                          yscrollcommand = self.servis_gormusler_treeview_scroolbarY.set)
        self.servis_gormusler_treeview_scroolbarY.config(command= self.servis_gormusler_treeview.yview)
        self.servis_gormusler_treeview_scroolbarX.config(command=self.servis_gormusler_treeview.xview)
        
        
        self.servistekiler_arac_ekle_btn = Button(self.servistekiler_tab,
                                    command= lambda: self.arac_ekle(self.servistekiler_treeview, ServisTipi.SERVISTE),
                                    text="Araç Ekle", fg="white", bg="black",highlightthickness = 0, bd = 0 ).pack(side=LEFT, padx=10,pady=10)
        
        self.servis_gormusler_arac_ekle_btn = Button(self.servis_gormusler_tab,
                                    command=lambda :self.arac_ekle(self.servis_gormusler_treeview, ServisTipi.SERVIS_GORMUS),
                                    text="Araç Ekle", fg="white", bg="black",highlightthickness = 0, bd = 0 ).pack(side=LEFT, padx=10,pady=10)
        
        self.servistekiler_arac_sil_btn = Button(self.servistekiler_tab,
                                    command= lambda: self.arac_sil(self.servistekiler_treeview, ServisTipi.SERVISTE),
                                    text="Araç Sil", fg="white", bg="black",highlightthickness = 0, bd = 0 ).pack(side=LEFT, padx=10,pady=10)
        
        self.servis_gormusler_arac_sil_btn = Button(self.servis_gormusler_tab,
                                    command= lambda: self.arac_sil(self.servis_gormusler_treeview, ServisTipi.SERVIS_GORMUS),
                                    text="Araç Sil", fg="white", bg="black",highlightthickness = 0, bd = 0 ).pack(side=LEFT, padx=10,pady=10)
        
        self.servistekiler_arac_bilgisini_degistir_btn = Button(self.servistekiler_tab,
                                            command= lambda: self.arac_bilgisini_degistir(self.servistekiler_treeview,
                                                                                 ServisTipi.SERVISTE),
                                            text="Araç Bilgisini Değiştir",
                                            fg="white", bg="black",highlightthickness = 0, bd = 0).pack(side=LEFT, padx=10,pady=10)
        
        self.servis_gormusler_arac_bilgisini_degistir_btn = Button(self.servis_gormusler_tab,
                                            command= lambda: self.arac_bilgisini_degistir(self.servis_gormusler_treeview,
                                                                                 ServisTipi.SERVIS_GORMUS),
                                            text="Araç Bilgisini Değiştir",
                                            fg="white", bg="black",highlightthickness = 0, bd = 0).pack(side=LEFT, padx=10,pady=10)
        
        self.servis_islemini_tamamla_btn = Button(self.servistekiler_tab,
                                                  command= self.servis_islemini_tamamla,
                                                  text="Servis İşlemini Tamamla",
                                                  fg="white", bg="black",highlightthickness = 0, bd = 0).pack(side=LEFT, padx=10,pady=10)

        back_icon = PhotoImage(file="./back_btn.png", height=20, width=25)
        self.giris_ekranina_don_btn = Button(self.servis_window,
                                             command=self.giris_ekranina_don,
                                             text="Giriş Ekranına Dön",
                                             image=back_icon,
                                             bg="white").pack(side=LEFT, padx=10,pady=10)

        self.servistekiler_treeview.tag_configure('tek_satir', background='#b6e2c1')
        self.servis_gormusler_treeview.tag_configure('tek_satir', background='#b6e2c1')

        self.servistekiler_treeview.tag_configure('cift_satir', background='#fcffd6')
        self.servis_gormusler_treeview.tag_configure('cift_satir', background='#fcffd6')
        
        self.data_yukle()
        
        self.servis_window.mainloop()
    
    def arac_ekle(self, tree_view:ttk.Treeview, servis_tipi):
        """
        Eklenecek arayüz ve eklenecek aracın servis tipi parametre olarak verilir.
        Ekranda açılan dialog penceresinden aracın bilgileri girilir ardından araç 
        yönetici nesnesine ve arayüze eklenir.
        """
        eklenecek_arac = AracServis()
        """Araç eklemek için boş bir araç nesnesi oluşturulur."""
        tree_count = len(tree_view.get_children())
        """Dialoga parametre olarak oluşturulan aracın varsayılan arac bilgisi verilir."""
        arac_bilgisi_dialog = ServisBilgisiDialog(servis_tipi, eklenecek_arac.arac_bilgisini_al())
        """Count çift ise index tek olur fakat arac
        henüz eklenmediği için aracın satır tipi çift oluyor."""
        satir_tipi = self.satir_tipini_al(tree_count)
        """Servisteki araçlar için ücret, durum raporu, teslim tarihi
        aracın servis işlemi tamamlandığında girilecek."""
        
        """Servis görmüş araçlar için mevcut olup olmama kontrolü yapılmasına gerek yok."""
        if arac_bilgisi_dialog.kaydedilsin :
            if servis_tipi == ServisTipi.SERVISTE and (arac_bilgisi_dialog.yeni_arac_bilgisi["plaka"] in 
                                                       self.servis_yoneticisi.servisteki_araclar_plakalar):
                """Araç mevcut ekleme yapılmaz"""
                messagebox.showwarning(title="Hata", message="Araç zaten mevcut!")

            else:
                """Eklenecek araç dialogda girilen bilgiler ile güncellenir."""
                eklenecek_arac.arac_bilgisini_guncelle(arac_bilgisi_dialog.yeni_arac_bilgisi)
                """Yönetici nesnesine eklenir."""
                self.servis_yoneticisi.arac_ekle(eklenecek_arac, servis_tipi)
                """Arayüze eklenir."""
                tree_view.insert(parent='', index=tree_count,
                                 tags=(satir_tipi,),
                                 values=self.arac_bilgisini_tuple_yap(arac_bilgisi_dialog.yeni_arac_bilgisi, servis_tipi))
        """İptale basılırsa eklenmez."""
    
    def arac_sil(self, tree_view:ttk.Treeview, servis_tipi):
        """
        Verilen arayüze ve servis tipine göre seçili satır arayüzden ve 
        seçili araç yönetici nesnesinden silinir.
        """
        selected_item = tree_view.selection()
        selected_index = tree_view.index(selected_item)
        
        if selected_item == ():
                messagebox.showwarning(title="Hata", message="Araç seçilmedi!")
        else:
            if messagebox.askokcancel(title="Araç Sil",
                                    message="Araç silmek istediğinizden emin misiniz?",
                                    ):
                """selected_item boş tuple ise satır seçilmemiş demektir.""" 
                if selected_item == ():
                    messagebox.showwarning(title="Hata", message="Araç seçilmedi!")
                else:
                    """Arayüzdeki satırlar güncellenir."""
                    self.satir_tiplerini_guncelle(tree_view, selected_item)
                    """Arayüzden seçili satır silinir."""
                    tree_view.delete(selected_item)                
                    """Yönetici nesnesinden servis tipine göre seçili araç silinir."""
                    self.servis_yoneticisi.arac_sil(int(selected_index), servis_tipi)
            """İptale basılırsa silinmez."""
    def arac_bilgisini_degistir(self, tree_view:ttk.Treeview, servis_tipi):
        """
        Verilen arayüze ve servis tipine göre seçili satır arayüzden ve 
        seçili araç yönetici nesnesinden değiştirilir.
        """
        selected_item = tree_view.selection()
        selected_index = tree_view.index(selected_item)
        satir_tipi = self.satir_tipini_al(selected_index)
        """selected_item boş tuple ise satır seçilmemiş demektir.""" 
        if selected_item == ():
                messagebox.showwarning(title="Hata", message="Araç seçilmedi!")
        else:
            """Değiştirilecek olan aracın bilgisi ve servis tipi dialog a gönderilir""" 
            eski_arac_bilgisi = self.servis_yoneticisi.arac_bilgisini_al(selected_index,servis_tipi)
            arac_bilgisi_dialog = ServisBilgisiDialog(servis_tipi, eski_arac_bilgisi)
            
            if arac_bilgisi_dialog.kaydedilsin :
                """
                Servis tipi SERVISTE olan araç için plakası değiştirilmeden önceki kendi plakasına eşit olabilir ama 
                diğer araçların plakasına eşit olamaz.
                """
                if servis_tipi == ServisTipi.SERVISTE and ((arac_bilgisi_dialog.yeni_arac_bilgisi["plaka"] !=eski_arac_bilgisi["plaka"])
                                                           and 
                                                           (arac_bilgisi_dialog.yeni_arac_bilgisi["plaka"] in 
                                                            self.servis_yoneticisi.servisteki_araclar_plakalar)):
                    
                    """Araç zaten mevcut ekleme yapılmaz."""
                    messagebox.showwarning(title="Hata", message="Araç zaten mevcut!")
                else:
                    """Yeni aracın bilgileri yönetici aracılığıyla güncellenir."""
                    self.servis_yoneticisi.arac_bilgisini_guncelle(int(selected_index), 
                                                                   arac_bilgisi_dialog.yeni_arac_bilgisi, 
                                                                   servis_tipi)
                    """Arayüzden eski araç silinir ve yenisi yerleştirilir."""
                    tree_view.delete(selected_item)
                    tree_view.insert(parent="",tags=satir_tipi,
                                     index=selected_index, values=self.arac_bilgisini_tuple_yap(
                                         arac_bilgisi_dialog.yeni_arac_bilgisi,
                                         servis_tipi))
    def servis_islemini_tamamla(self):
        """
        Seçili servisteki aracın servis işlemleri tamamlanır, bunun için açılan dialog 
        penceresinden aracın ücret durum, durum raporu gibi bilgileri girilir ardından
        araç servis görmüş araçlar arayüzüne taşınır.
        """
        selected_item = self.servistekiler_treeview.selection()
        selected_index = self.servistekiler_treeview.index(selected_item)
        tree_count = len(self.servis_gormusler_treeview.get_children())
        """Count çift ise index tek olur fakat arac
        henüz eklenmediği için aracın satır tipi çift oluyor."""
        satir_tipi = self.satir_tipini_al(tree_count)
        
        """selected_item boş tuple ise satır seçilmemiş demektir.""" 
        if selected_item == ():
                messagebox.showwarning(title="Hata", message="Araç seçilmedi!")
        else:
            """Araç servis görmüş araçlar arayüzüne taşınacağından 
            ücret, durum raporu gibi bilgileri girilmesi gerekir bunun için dialog
            servis tipi SERVIS_GORMUS olarak ayarlanır
            """
            arac_bilgisi_dialog = ServisBilgisiDialog(ServisTipi.SERVIS_GORMUS,
                                                    self.servis_yoneticisi.arac_bilgisini_al(int(selected_index),
                                                                                             ServisTipi.SERVISTE))
            if arac_bilgisi_dialog.kaydedilsin:
                self.servis_yoneticisi.arac_bilgisini_guncelle(int(selected_index), 
                                                               arac_bilgisi_dialog.yeni_arac_bilgisi, 
                                                               ServisTipi.SERVISTE)
                """Yönetici nesnesinde aracın servis işlemi tamamlanır"""
                self.servis_yoneticisi.servis_islemini_tamamla(int(selected_index))
                """Servistekiler arayüzünün satır tipleri güncellenir"""
                self.satir_tiplerini_guncelle(self.servistekiler_treeview, selected_item)
                """Servistekiler arayüzünden araç silinir"""
                self.servistekiler_treeview.delete(selected_item)
                """Servis görmüşler arayüzüne araç eklenir"""
                self.servis_gormusler_treeview.insert(parent="", tags=satir_tipi,
                                                      index=tree_count, 
                                                      values=self.arac_bilgisini_tuple_yap(
                                                          arac_bilgisi_dialog.yeni_arac_bilgisi, 
                                                          ServisTipi.SERVIS_GORMUS))
    def data_yukle(self):
        """Servis yöneticisinin araç listesi dosyadan okunup güncellenir
        ardından uygun servis tipine göre araçların bilgileri arayüze eklenir."""
        self.servis_yoneticisi.servis_listesi_al(ServisTipi.SERVISTE)
        self.servis_yoneticisi.servis_listesi_al(ServisTipi.SERVIS_GORMUS)
        self.arayuzu_guncelle(ServisTipi.SERVISTE)
        self.arayuzu_guncelle(ServisTipi.SERVIS_GORMUS)
        
    def arayuzu_guncelle(self, servis_tipi):
        """
        Uygun servis tipine göre yöneticinin araçları arayüze eklenir.
        """
        if servis_tipi == ServisTipi.SERVISTE:
            tree_view = self.servistekiler_treeview
            araclar = self.servis_yoneticisi.servisteki_araclar
        elif servis_tipi == ServisTipi.SERVIS_GORMUS:
            tree_view = self.servis_gormusler_treeview
            araclar = self.servis_yoneticisi.servis_gormus_araclar
        else:
            return
        
        index_count = 0
        for arac in araclar:
            """Satır tipine göre satırın rengi belirlenir."""
            satir_tipi = self.satir_tipini_al(index_count)
            index_count += 1
            tree_view.insert(parent="", index='end', 
                             tags=(satir_tipi),
                             values=self.arac_bilgisini_tuple_yap(arac.arac_bilgisini_al(), servis_tipi))

    def arac_bilgisini_tuple_yap(self, arac_bilgisi, servis_tipi:ServisTipi):
        """
        Araç bilgisi arayüzün başlık yapısına göre uygun bir biçimde tuple'a çevrilir.
        """
        arac_bilgisi_tuple = (arac_bilgisi["segment"],
                              arac_bilgisi["model"],
                              arac_bilgisi["kasa_tipi"],
                              arac_bilgisi["vites"],
                              arac_bilgisi["yil"],
                              arac_bilgisi["motor"],
                              arac_bilgisi["yakit_tipi"],
                              arac_bilgisi["renk"],
                              arac_bilgisi["km"],
                              arac_bilgisi["plaka"],
                              arac_bilgisi["giris_tarihi"],
                              arac_bilgisi["musteri_isim"],
                              arac_bilgisi["musteri_tel"],
                              textwrap.fill(arac_bilgisi["musteri_talep"],100)
                              )
        """
        Servis tipi SERVIS_GORMUS ise diğer servis tipinde dikkate alınmayan teslim_tarihi,
        durum_raporu ve ucret bilgileri tuple içerisine dahil edilir
        """
        if servis_tipi == ServisTipi.SERVIS_GORMUS:
            arac_bilgisi_tuple += (arac_bilgisi["teslim_tarihi"],
                                   textwrap.fill(arac_bilgisi["durum_raporu"],100),
                                   arac_bilgisi["ucret"]+'₺')

        return arac_bilgisi_tuple
        
    

    def giris_ekranina_don(self):
        """
        ServisMenu sonlandırılır ve giris_ekranina_donulsun değişkeni 
        True yapılarak ServisMenu nün kapatıldığının mı yoksa giriş ekranına dönülmek
        istendiğinin mi bilgisi öğrenilmiş olur.
        """
        
        """window.quit() -> mainloop sonlandırılır"""
        self.servis_window.quit()
        """window.destroy() -> pencere yok edilir"""
        self.servis_window.destroy()
        self.giris_ekranina_donulsun = True
