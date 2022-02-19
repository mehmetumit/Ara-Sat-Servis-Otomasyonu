from AracCesidiDialog import AracCesidiDialog
import sqlite3
from AracSatis import AracSatis
from SatisBilgisiDialog import SatisBilgisiDialog
from AracMenu import AracMenu
from ServisYoneticisi import ServisTipi
from SatisYoneticisi import SatisTipi, SatisYoneticisi
from tkinter import * 
import tkinter
from tkinter import ttk
from tkinter import messagebox

class SatisMenu(AracMenu):
    def __init__(self, satis_yoneticisi:SatisYoneticisi):
        super().__init__()
        self.satis_yoneticisi = satis_yoneticisi
        self.fg = '#00FF00'
        self.widget_font = ("Arial",20)
        self.satis_window = Tk()
        
        
        self.satis_window.geometry(self.window_size)
        self.satis_window.title("Satis Menu")
        
        
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
                    "fieldbackground":"silver", #Boş kısımların arka plan rengi
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
        self.notebook = ttk.Notebook(self.satis_window)
        self.stoktakiler_tab = Frame(self.notebook,bg=self.bg)
        self.satilmislar_tab = Frame(self.notebook, bg=self.bg)
        self.arac_cesitleri_tab = Frame(self.notebook,bg=self.bg)
        
        self.notebook.add(self.stoktakiler_tab, text="Stoktaki Araçlar")
        self.notebook.add(self.satilmislar_tab,text="Satılmış Araçlar")
        self.notebook.add(self.arac_cesitleri_tab, text="Araç Çeşitleri")
        self.notebook.pack(expand=True, fill="both")
        
        self.satis_window.iconbitmap("./logo.ico")
        self.satis_window.config(bg=self.bg)
        self.satis_window.minsize(self.min_window_width,self.min_window_height)
        
        self.stoktakiler_label = Label(self.stoktakiler_tab, 
                           text="Stoktaki Araçlar", 
                           font=("Arial", 40, "bold"), 
                           fg="white",
                           bg=self.bg).pack()
        
        self.satilmislar_label = Label(self.satilmislar_tab, 
                           text="Satılmış Araçlar", 
                           font=("Arial", 40, "bold"), 
                           fg="white",
                           bg=self.bg).pack()
        self.arac_cesitleri_label = Label(self.arac_cesitleri_tab, 
                           text="Araç Çeşitleri", 
                           font=("Arial", 40, "bold"), 
                           fg="white",
                           bg=self.bg).pack()
        """
        'browse' -> birden fazla satır seçilemez
        'headings' -> #0 sütununun göstermez
        """
        self.satilmislar_treeview = ttk.Treeview( self.satilmislar_tab, selectmode="browse", show="headings")
        self.stoktakiler_treeview = ttk.Treeview( self.stoktakiler_tab, selectmode="browse", show="headings")
        self.arac_cesitleri_treeview = ttk.Treeview( self.arac_cesitleri_tab, selectmode="browse", show="headings")

        self.satilmislar_treeview['columns'] = ("segment",
                                                  "model",
                                                  "kasa_tipi",
                                                  "vites",
                                                  "yil",
                                                  "motor",
                                                  "yakit_tipi",
                                                  "renk",
                                                  "fiyat",
                                                  "adet",
                                                  "satis_tarihi")
        self.stoktakiler_treeview['columns'] = ("segment",
                                                  "model",
                                                  "kasa_tipi",
                                                  "vites",
                                                  "yil",
                                                  "motor",
                                                  "yakit_tipi",
                                                  "renk",
                                                  "fiyat",
                                                  "adet")
        self.arac_cesitleri_treeview['columns'] = ("segment",
                                                  "model",
                                                  "kasa_tipi",
                                                  "vites",
                                                  "yil",
                                                  "motor",
                                                  "yakit_tipi")
        
        self.satilmislar_treeview.column("#0", width=0)
        self.satilmislar_treeview.column("segment", anchor=CENTER, width=200, minwidth=200)
        self.satilmislar_treeview.column("model", anchor=CENTER, width=200, minwidth=200)
        self.satilmislar_treeview.column("kasa_tipi", anchor=CENTER, width=200, minwidth=200)
        self.satilmislar_treeview.column("vites", anchor=CENTER, width=200, minwidth=200)
        self.satilmislar_treeview.column("yil", anchor=CENTER, width=200, minwidth=200)
        self.satilmislar_treeview.column("motor", anchor=CENTER, width=200, minwidth=200)
        self.satilmislar_treeview.column("yakit_tipi", anchor=CENTER, width=200, minwidth=200)
        self.satilmislar_treeview.column("renk", anchor=CENTER, width=200, minwidth=200)        
        self.satilmislar_treeview.column("fiyat", anchor=CENTER, width=200, minwidth=200)
        self.satilmislar_treeview.column("adet", anchor=CENTER, width=200, minwidth=200)        
        self.satilmislar_treeview.column("satis_tarihi", anchor=CENTER, width=200, minwidth=200)        
        
        self.stoktakiler_treeview.column("#0", width=0)
        self.stoktakiler_treeview.column("segment", anchor=CENTER, width=200, minwidth=200)
        self.stoktakiler_treeview.column("model", anchor=CENTER, width=200, minwidth=200)
        self.stoktakiler_treeview.column("kasa_tipi", anchor=CENTER, width=200, minwidth=200)
        self.stoktakiler_treeview.column("vites", anchor=CENTER, width=200, minwidth=200)
        self.stoktakiler_treeview.column("yil", anchor=CENTER, width=200, minwidth=200)
        self.stoktakiler_treeview.column("motor", anchor=CENTER, width=200, minwidth=200)
        self.stoktakiler_treeview.column("yakit_tipi", anchor=CENTER, width=200, minwidth=200)
        self.stoktakiler_treeview.column("renk", anchor=CENTER, width=200, minwidth=200)       
        self.stoktakiler_treeview.column("fiyat", anchor=CENTER, width=200, minwidth=200)       
        self.stoktakiler_treeview.column("adet", anchor=CENTER, width=200, minwidth=200)       
        
        self.arac_cesitleri_treeview.column("#0", width=0)
        self.arac_cesitleri_treeview.column("segment", anchor=CENTER, width=200, minwidth=200)
        self.arac_cesitleri_treeview.column("model", anchor=CENTER, width=200, minwidth=200)
        self.arac_cesitleri_treeview.column("kasa_tipi", anchor=CENTER, width=200, minwidth=200)
        self.arac_cesitleri_treeview.column("vites", anchor=CENTER, width=200, minwidth=200)
        self.arac_cesitleri_treeview.column("yil", anchor=CENTER, width=200, minwidth=200)
        self.arac_cesitleri_treeview.column("motor", anchor=CENTER, width=200, minwidth=200)
        self.arac_cesitleri_treeview.column("yakit_tipi", anchor=CENTER, width=200, minwidth=200)
        
        self.satilmislar_treeview.heading("#0", text="")
        self.satilmislar_treeview.heading("segment",text="Segment", anchor=CENTER)
        self.satilmislar_treeview.heading("model",text="Model", anchor=CENTER)
        self.satilmislar_treeview.heading("kasa_tipi",text="Kasa Tipi", anchor=CENTER)
        self.satilmislar_treeview.heading("vites",text="Vites", anchor=CENTER)
        self.satilmislar_treeview.heading("yil",text="Yıl", anchor=CENTER)
        self.satilmislar_treeview.heading("motor",text="Motor", anchor=CENTER)
        self.satilmislar_treeview.heading("yakit_tipi",text="Yakıt Tipi", anchor=CENTER)
        self.satilmislar_treeview.heading("renk",text="Renk", anchor=CENTER)        
        self.satilmislar_treeview.heading("fiyat",text="Fiyat", anchor=CENTER)
        self.satilmislar_treeview.heading("adet",text="Adet", anchor=CENTER)
        self.satilmislar_treeview.heading("satis_tarihi",text="Satış Tarihi", anchor=CENTER)
        
        self.stoktakiler_treeview.heading("#0", text="")
        self.stoktakiler_treeview.heading("segment",text="Segment", anchor=CENTER)
        self.stoktakiler_treeview.heading("model",text="Model", anchor=CENTER)
        self.stoktakiler_treeview.heading("kasa_tipi",text="Kasa Tipi", anchor=CENTER)
        self.stoktakiler_treeview.heading("vites",text="Vites", anchor=CENTER)
        self.stoktakiler_treeview.heading("yil",text="Yıl", anchor=CENTER)
        self.stoktakiler_treeview.heading("motor",text="Motor", anchor=CENTER)
        self.stoktakiler_treeview.heading("yakit_tipi",text="Yakıt Tipi", anchor=CENTER)
        self.stoktakiler_treeview.heading("renk",text="Renk", anchor=CENTER)        
        self.stoktakiler_treeview.heading("fiyat",text="Fiyat", anchor=CENTER)
        self.stoktakiler_treeview.heading("adet",text="Adet", anchor=CENTER)        
        
        self.arac_cesitleri_treeview.heading("#0", text="")
        self.arac_cesitleri_treeview.heading("segment",text="Segment", anchor=CENTER)
        self.arac_cesitleri_treeview.heading("model",text="Model", anchor=CENTER)
        self.arac_cesitleri_treeview.heading("kasa_tipi",text="Kasa Tipi", anchor=CENTER)
        self.arac_cesitleri_treeview.heading("vites",text="Vites", anchor=CENTER)
        self.arac_cesitleri_treeview.heading("yil",text="Yıl", anchor=CENTER)
        self.arac_cesitleri_treeview.heading("motor",text="Motor", anchor=CENTER)
        self.arac_cesitleri_treeview.heading("yakit_tipi",text="Yakıt Tipi", anchor=CENTER)
        
        """Treeview arayüzlerine scrool bar atanma işlemleri."""
        self.satilmislar_treeview.pack(expand=True, fill=BOTH)
        self.satilmislar_treeview_scroolbarY = Scrollbar(self.satilmislar_treeview)
        self.satilmislar_treeview_scroolbarX = Scrollbar(self.satilmislar_treeview,orient=HORIZONTAL)
        self.satilmislar_treeview_scroolbarY.pack(side = RIGHT, fill=BOTH)
        self.satilmislar_treeview_scroolbarX.pack(side=BOTTOM, fill=BOTH)
        self.satilmislar_treeview.config(xscrollcommand=self.satilmislar_treeview_scroolbarX.set,
                                          yscrollcommand = self.satilmislar_treeview_scroolbarY.set)
        self.satilmislar_treeview_scroolbarY.config(command= self.satilmislar_treeview.yview)
        self.satilmislar_treeview_scroolbarX.config(command=self.satilmislar_treeview.xview)
        
        self.stoktakiler_treeview.pack(expand=True, fill=BOTH)
        self.stoktakiler_treeview_scroolbarY = Scrollbar(self.stoktakiler_treeview)
        self.stoktakiler_treeview_scroolbarX = Scrollbar(self.stoktakiler_treeview,orient=HORIZONTAL)
        self.stoktakiler_treeview_scroolbarY.pack(side = RIGHT, fill=BOTH)
        self.stoktakiler_treeview_scroolbarX.pack(side=BOTTOM, fill=BOTH)
        self.stoktakiler_treeview.config(xscrollcommand=self.stoktakiler_treeview_scroolbarX.set,
                                          yscrollcommand = self.stoktakiler_treeview_scroolbarY.set)
        self.stoktakiler_treeview_scroolbarY.config(command= self.stoktakiler_treeview.yview)
        self.stoktakiler_treeview_scroolbarX.config(command=self.stoktakiler_treeview.xview)
        
        self.arac_cesitleri_treeview.pack(expand=True, fill=BOTH)
        self.arac_cesitleri_treeview_scroolbarY = Scrollbar(self.arac_cesitleri_treeview)
        self.arac_cesitleri_treeview_scroolbarX = Scrollbar(self.arac_cesitleri_treeview,orient=HORIZONTAL)
        self.arac_cesitleri_treeview_scroolbarY.pack(side = RIGHT, fill=BOTH)
        self.arac_cesitleri_treeview_scroolbarX.pack(side=BOTTOM, fill=BOTH)
        self.arac_cesitleri_treeview.config(xscrollcommand=self.arac_cesitleri_treeview_scroolbarX.set,
                                          yscrollcommand = self.arac_cesitleri_treeview_scroolbarY.set)
        self.arac_cesitleri_treeview_scroolbarY.config(command= self.arac_cesitleri_treeview.yview)
        self.arac_cesitleri_treeview_scroolbarX.config(command=self.arac_cesitleri_treeview.xview)
        
        
        """Stripe(şerit) deseni oluşturmak için kullanılacak tagler"""
        self.satilmislar_treeview.tag_configure('tek_satir', background='#b6e2c1')
        self.stoktakiler_treeview.tag_configure('tek_satir', background='#b6e2c1')
        self.arac_cesitleri_treeview.tag_configure('tek_satir', background='#b6e2c1')
        
        self.satilmislar_treeview.tag_configure('cift_satir', background='#fcffd6')
        self.stoktakiler_treeview.tag_configure('cift_satir', background='#fcffd6')
        self.arac_cesitleri_treeview.tag_configure('cift_satir', background='#fcffd6')

                
        self.stoktakiler_arac_ekle_btn = Button(self.stoktakiler_tab,
                                    command= lambda: self.arac_ekle(tree_view=self.stoktakiler_treeview
                                                                    ,satis_tipi=SatisTipi.STOK),
                                    text="Araç Ekle", fg="white", bg="black",highlightthickness = 0, bd = 0 ).pack(side=LEFT, padx=10,pady=10)
        
        self.satilmislar_arac_ekle_btn = Button(self.satilmislar_tab,
                                    command= lambda: self.arac_ekle(tree_view=self.satilmislar_treeview,
                                                                    satis_tipi=SatisTipi.SATILMIS),
                                    text="Araç Ekle", fg="white", bg="black",highlightthickness = 0, bd = 0 ).pack(side=LEFT, padx=10,pady=10)
        
        self.stoktakiler_arac_sil_btn = Button(self.stoktakiler_tab,
                                    command= lambda: self.arac_sil(tree_view=self.stoktakiler_treeview,
                                                                   satis_tipi=SatisTipi.STOK),
                                    text="Araç Sil", fg="white", bg="black" ,highlightthickness = 0, bd = 0).pack(side=LEFT, padx=10,pady=10)
        self.satilmislar_arac_sil_btn = Button(self.satilmislar_tab,
                                    command= lambda: self.arac_sil(self.satilmislar_treeview,
                                                                   SatisTipi.SATILMIS),
                                    text="Araç Sil", fg="white", bg="black",highlightthickness = 0, bd = 0 ).pack(side=LEFT, padx=10,pady=10)

        self.stoktakiler_arac_bilgisini_degistir_btn = Button(self.stoktakiler_tab,
                                            command= lambda: self.arac_bilgisini_degistir(tree_view=self.stoktakiler_treeview,
                                                                                 satis_tipi=SatisTipi.STOK),
                                            text="Araç Bilgisini Değiştir",
                                            fg="white", bg="black",highlightthickness = 0, bd = 0).pack(side=LEFT, padx=10,pady=10)
        
        self.satilmislar_arac_bilgisini_degistir_btn = Button(self.satilmislar_tab,
                                            command= lambda: self.arac_bilgisini_degistir(tree_view=self.satilmislar_treeview,
                                                                                 satis_tipi=SatisTipi.SATILMIS),
                                            text="Araç Bilgisini Değiştir",
                                            fg="white", bg="black",highlightthickness = 0, bd = 0).pack(side=LEFT, padx=10,pady=10)
        
        self.arac_sat_btn = Button(self.stoktakiler_tab,
                                   text="Arac Sat",
                                   fg='white',
                                   bg='black',
                                   command=self.arac_sat,highlightthickness = 0, bd = 0).pack(side=LEFT, padx=10,pady=10)
        self.arac_cesidi_ekle_btn = Button(self.arac_cesitleri_tab,
                                   text="Arac Çeşidi Ekle",
                                   fg='white',
                                   bg='black',
                                   command=self.arac_cesidi_ekle,highlightthickness = 0, bd = 0).pack(side=LEFT, padx=10,pady=10)
        self.arac_cesidi_sil_btn = Button(self.arac_cesitleri_tab,
                                   text="Arac Çeşidi Sil",
                                   fg='white',
                                   bg='black',
                                   command=self.arac_cesidi_sil,highlightthickness = 0, bd = 0).pack(side=LEFT, padx=10,pady=10)
        back_icon = PhotoImage(file="./back_btn.png", height=20, width=25)
        self.giris_ekranina_don_btn = Button(self.satis_window,
                                             command=self.giris_ekranina_don,
                                             text="Giriş Ekranına Dön",
                                             image=back_icon,
                                             bg="white").pack(side=LEFT, padx=10,pady=10)
        
        self.data_yukle()
        self.satis_window.mainloop()
        
    def giris_ekranina_don(self):
        """
        Pencere yok edilir ve pencerenin kapatılma ihtimali olduğu için 
        giris_ekranina_donulsun bilgisi True yapılır
        """
        self.satis_window.quit()
        self.satis_window.destroy()
        self.giris_ekranina_donulsun = True

    def arac_sat(self):
        """
        Seçili araç satılı dialog penceresindeki adedi kadar satılır 
        """
        selected_item = self.stoktakiler_treeview.selection()
        selected_index = self.stoktakiler_treeview.index(selected_item)
        
        tree_count = len(self.satilmislar_treeview.get_children())
        
        """Count çift ise index tek olur fakat arac
        henüz eklenmediği için aracın satır tipi çift oluyor."""
        satir_tipi = self.satir_tipini_al(tree_count)
        
        """selected_item boş tuple ise satır seçilmemiş demektir.""" 
        if selected_item == ():
                messagebox.showwarning(title="Hata", message="Araç seçilmedi!")
        else:
            """Satılan araç satılmış araçlar arayüzüne ekleneceğinden 
            satis_tarihi bilgisi girilmesi gerekir bunun için dialog
            satış tipi SATILMIŞ olarak ayarlanır
            """
            satis_bilgisi_dialog = SatisBilgisiDialog(SatisTipi.SATILMIS,
                                                    self.satis_yoneticisi.arac_bilgisini_al(int(selected_index),
                                                                                             SatisTipi.STOK))
            if satis_bilgisi_dialog.kaydedilsin:
                satis_adedi = satis_bilgisi_dialog.yeni_arac_bilgisi["adet"]
                stok_adedi = self.satis_yoneticisi.arac_bilgisini_al(selected_index, SatisTipi.STOK)["adet"]
                
                """Stok adedi ve satılmak istenen adet miktarına göre arayüzde işlem yapılır."""
                if int(satis_adedi) >= int(stok_adedi):
                    """Arayüzdeki satırlar güncellenir."""
                    self.satir_tiplerini_guncelle(self.stoktakiler_treeview, selected_item)
                    """Yönetici nesnesinde araç satılır"""
                    self.satis_yoneticisi.arac_sat(int(selected_index), int(satis_adedi), satis_bilgisi_dialog.yeni_arac_bilgisi["satis_tarihi"])
                    """Stoktakiler arayüzünden araç silinir"""
                    self.stoktakiler_treeview.delete(selected_item)
                    """Daha sonradan satılmış araç arayüzüne eklenecek olana 
                    aracın adet bilgisi güncellenir."""
                    satis_bilgisi_dialog.yeni_arac_bilgisi["adet"] = stok_adedi
                else:
                    """Yonetici aracılığı ile araç satılır."""
                    self.satis_yoneticisi.arac_sat(int(selected_index), int(satis_adedi), satis_bilgisi_dialog.yeni_arac_bilgisi["satis_tarihi"])
                    
                    """Arayüzden eski stoktaki araç silinir ve yenisi yerleştirilir."""
                    self.stoktakiler_treeview.delete(selected_item)
                    self.stoktakiler_treeview.insert(parent="",tags=self.satir_tipini_al(selected_index),
                                     index=selected_index, values=self.arac_bilgisini_tuple_yap(
                                         self.satis_yoneticisi.arac_bilgisini_al(selected_index, SatisTipi.STOK),
                                         SatisTipi.STOK))
                    
                """Satılmış araçlar arayüzüne satılan araç eklenir"""
                self.satilmislar_treeview.insert(parent="", tags=satir_tipi,
                                                    index=tree_count, 
                                                    values=self.arac_bilgisini_tuple_yap(
                                                        satis_bilgisi_dialog.yeni_arac_bilgisi, 
                                                        SatisTipi.SATILMIS))
                    
    def arac_ekle(self, tree_view, satis_tipi):
        """
        Eklenecek arayüz ve eklenecek aracın satış tipi parametre olarak verilir.
        Ekranda açılan dialog penceresinden aracın bilgileri girilir ardından araç 
        yönetici nesnesine ve arayüze eklenir.
        """
        eklenecek_arac = AracSatis()
        """Araç eklemek için boş bir araç nesnesi oluşturulur."""
        tree_count = len(tree_view.get_children())
        """Dialoga parametre olarak oluşturulan aracın varsayılan arac bilgisi verilir."""
        satis_bilgisi_dialog = SatisBilgisiDialog(satis_tipi, eklenecek_arac.arac_bilgisini_al())
        """Count çift ise index tek olur fakat arac
        henüz eklenmediği için aracın satır tipi çift oluyor."""
        satir_tipi = self.satir_tipini_al(tree_count)
        

        if satis_bilgisi_dialog.kaydedilsin :
            arac_bilgisi_mevcut = self.satis_yoneticisi.arac_bilgisi_mevcut_mu(satis_bilgisi_dialog.yeni_arac_bilgisi,
                                                                               satis_tipi)
            if satis_tipi == SatisTipi.STOK and arac_bilgisi_mevcut:
                """Araç mevcut ekleme yapılmaz"""
                messagebox.showwarning(title="Hata", message="Araç zaten mevcut!")

            else:
                """Eklenecek araç dialogda girilen bilgiler ile güncellenir."""
                eklenecek_arac.arac_bilgisini_guncelle(satis_bilgisi_dialog.yeni_arac_bilgisi)
                """Yönetici nesnesine eklenir."""
                self.satis_yoneticisi.arac_ekle(eklenecek_arac, satis_tipi)
                """Arayüze eklenir."""
                tree_view.insert(parent='', index=tree_count,
                                 tags=(satir_tipi,),
                                 values=self.arac_bilgisini_tuple_yap(satis_bilgisi_dialog.yeni_arac_bilgisi, satis_tipi))
        """İptale basılırsa eklenmez."""
        
    def arac_bilgisini_degistir(self, tree_view:ttk.Treeview, satis_tipi):
        """
        Verilen arayüze ve satış tipine göre seçili satır arayüzden, 
        seçili araç yönetici nesnesinden değiştirilir.
        """
        selected_item = tree_view.selection()
        selected_index = tree_view.index(selected_item)
        satir_tipi = self.satir_tipini_al(selected_index)
        """selected_item boş tuple ise satır seçilmemiş demektir.""" 
        if selected_item == ():
                messagebox.showwarning(title="Hata", message="Araç seçilmedi!")
        else:
            """Değiştirilecek olan aracın bilgisi ve satış tipi dialog a gönderilir""" 
            eski_arac_bilgisi = self.satis_yoneticisi.arac_bilgisini_al(selected_index,satis_tipi)
            satis_bilgisi_dialog = SatisBilgisiDialog(satis_tipi, eski_arac_bilgisi)
              
            if satis_bilgisi_dialog.kaydedilsin :
                
                arac_bilgisi_mevcut = self.satis_yoneticisi.arac_bilgisi_mevcut_mu(satis_bilgisi_dialog.yeni_arac_bilgisi,
                                                                                   satis_tipi, 
                                                                                   bakilmayacak_index=selected_index)
                
                if satis_tipi == SatisTipi.STOK and arac_bilgisi_mevcut:
                    
                    """Araç zaten mevcut ekleme yapılmaz."""
                    messagebox.showwarning(title="Hata", message="Araç zaten mevcut!")
                else:
                    """Yeni aracın bilgileri yönetici aracılığıyla güncellenir."""
                    self.satis_yoneticisi.arac_bilgisini_guncelle(int(selected_index), 
                                                                   satis_bilgisi_dialog.yeni_arac_bilgisi, 
                                                                   satis_tipi)
                    """Arayüzden eski araç silinir ve yenisi yerleştirilir."""
                    tree_view.delete(selected_item)
                    tree_view.insert(parent="",tags=satir_tipi,
                                     index=selected_index, values=self.arac_bilgisini_tuple_yap(
                                         satis_bilgisi_dialog.yeni_arac_bilgisi,
                                         satis_tipi))
    
    def arac_sil(self, tree_view:ttk.Treeview, satis_tipi):
        """
        Verilen arayüze ve satış tipine göre seçili satır arayüzden ve 
        seçili araç yönetici nesnesinden silinir.
        """
        selected_item = tree_view.selection()
        selected_index = tree_view.index(selected_item)
        
        """selected_item boş tuple ise satır seçilmemiş demektir.""" 
        if selected_item == ():
            messagebox.showwarning(title="Hata", message="Araç seçilmedi!")
        else:
            if messagebox.askokcancel(title="Araç Sil",
                                    message="Araç silmek istediğinizden emin misiniz?",
                                    ):
                
                """Arayüzdeki satırlar güncellenir."""
                self.satir_tiplerini_guncelle(tree_view, selected_item)
                """Arayüzden seçili satır silinir."""
                tree_view.delete(selected_item)                
                """Yönetici nesnesinden servis tipine göre seçili araç silinir."""
                self.satis_yoneticisi.arac_sil(int(selected_index), satis_tipi)
            else:
                print("Silme işlemi iptal edildi!")
            
    def data_yukle(self):
        """
        Satış yöneticisinin araç listesi dosyadan okunup güncellenir, 
        uygun satış tipine göre araçların bilgileri arayüze eklenir ve araç çeşidi listesi dosyadan
        okunup arayüze eklenir.
        """
        self.satis_yoneticisi.satis_listesi_al(SatisTipi.STOK)
        self.satis_yoneticisi.satis_listesi_al(SatisTipi.SATILMIS)
        self.arayuzu_guncelle()        
    
    def arac_cesidi_arayuzunu_guncelle(self):
        """Araç çeşidi arayüzünün bilgileri dosyadan alınıp güncellenir"""
        self.conn = sqlite3.connect("arac_cesidi.db")
        self.cur = self.conn.cursor()
       
        self.cur.execute("CREATE TABLE IF NOT EXISTS arac_cesidi(segment TEXT, model TEXT, kasa_tipi TEXT, vites TEXT, yil TEXT, motor TEXT, yakit_tipi TEXT)")
        self.cur.execute("SELECT * FROM arac_cesidi")
        index = 0
        for satir in self.cur.fetchall():
            self.arac_cesitleri_treeview.insert(parent="", index=END,
                                                tags=self.satir_tipini_al(index),
                                                values=satir)
            index += 1
    def arac_cesidi_ekle(self):
        """Açılan dialog penceresinden yeni araç çeşidinin bilgileri elle girilebilir ya da 
        istenirse var olan bilgiler seçilebilir"""
        arac_cesidi_dialog = AracCesidiDialog()
        if arac_cesidi_dialog.kaydedilsin :
            self.cur.execute("INSERT INTO arac_cesidi VALUES(:segment, :model, :kasa_tipi, :vites, :yil, :motor, :yakit_tipi)",arac_cesidi_dialog.yeni_arac_cesidi_bilgisi)
            self.conn.commit()
            satir_tipi = self.satir_tipini_al(len(self.arac_cesitleri_treeview.get_children()))
            self.arac_cesitleri_treeview.insert(parent="", index=END, 
                                                tags=satir_tipi,
                                                values=self.arac_bilgisini_tuple_yap(arac_cesidi_dialog.yeni_arac_cesidi_bilgisi))
        """İptale basılırsa eklenmez."""
    def arac_cesidi_sil(self):
        """Seçilen araç çeşidi arayüzden ve dosyadan silinir"""
        selected_item = self.arac_cesitleri_treeview.selection()
        selected_index = self.arac_cesitleri_treeview.index(selected_item)

        """selected_item boş tuple ise satır seçilmemiş demektir.""" 

        if selected_item == ():
                messagebox.showwarning(title="Hata", message="Araç seçilmedi!")
        else:
            if  messagebox.askokcancel(title="Araç Çeşidini Sil",
                                    message="Araç çeşidini silmek istediğinizden emin misiniz?"): 
                self.satir_tiplerini_guncelle(self.arac_cesitleri_treeview, selected_item)
                self.cur.execute(f"DELETE FROM arac_cesidi WHERE rowid={selected_index+1}")
                self.arac_cesitleri_treeview.delete(selected_item)
                self.conn.commit()
            """İptale basılırsa silinmez."""
    
    def arayuzu_guncelle(self):
        """Bütün arayüzlerin bilgileri güncellenir."""
        self.araclar_arayuzunu_guncelle(SatisTipi.SATILMIS)
        self.araclar_arayuzunu_guncelle(SatisTipi.STOK)
        self.arac_cesidi_arayuzunu_guncelle()

    def araclar_arayuzunu_guncelle(self, satis_tipi):
        """Parametre olarak alınan satış tipine göre satış tipinin
        ait olduğu arayüzü günceller."""
        if satis_tipi == SatisTipi.SATILMIS:
            tree_view = self.satilmislar_treeview
            araclar = self.satis_yoneticisi.satilmis_araclar
        elif satis_tipi == SatisTipi.STOK:
            tree_view = self.stoktakiler_treeview
            araclar = self.satis_yoneticisi.stoktaki_araclar
            
        index_count = 0
        for arac in araclar:
            """Satır tipine göre satırın rengi belirlenir."""
            satir_tipi = self.satir_tipini_al(index_count)
            index_count += 1
            tree_view.insert(parent="", index='end', 
                             tags=(satir_tipi),
                             values=self.arac_bilgisini_tuple_yap(arac.arac_bilgisini_al(), satis_tipi))
    
    def arac_bilgisini_tuple_yap(self, arac_bilgisi, satis_tipi=NONE):
        """
        Araç bilgisi arayüzün başlık yapısına uygun bir biçimde tuple'a çevrilir.
        """
        arac_bilgisi_tuple = (arac_bilgisi["segment"],
                              arac_bilgisi["model"],
                              arac_bilgisi["kasa_tipi"],
                              arac_bilgisi["vites"],
                              arac_bilgisi["yil"],
                              arac_bilgisi["motor"],
                              arac_bilgisi["yakit_tipi"])
        """Satış tipi yok ise diğer kısımlar eklenmez"""
        if satis_tipi != NONE:
            arac_bilgisi_tuple += (arac_bilgisi["renk"],arac_bilgisi["fiyat"] + '₺',arac_bilgisi["adet"])
            
        """
        Satış tipi SATILMIS ise diğer satış tipinde dikkate alınmayan renk ve 
        satis_tarihi tuple içerisine dahil edilir
        """
        if satis_tipi == SatisTipi.SATILMIS:
            arac_bilgisi_tuple += (arac_bilgisi["satis_tarihi"],)
        return arac_bilgisi_tuple
