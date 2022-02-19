from Arac import Arac
from Musteri import Musteri
class AracServis(Arac):
    def __init__(self,segment="", model="", kasa_tipi="", vites="", yil="", motor="", yakit_tipi="", renk="", km="", plaka="",giris_tarihi="",musteri_isim="",musteri__tel="",musteri_talep="",teslim_tarihi="",durum_raporu="",ucret=""):
        super().__init__(segment, model, kasa_tipi, vites, yil, motor, yakit_tipi, renk)
        self.__km = km
        self.__plaka = plaka
        self.__giris_tarihi = giris_tarihi
        self.__teslim_tarihi = teslim_tarihi
        self.__durum_raporu = durum_raporu
        
        self.__musteri = Musteri(musteri_isim,musteri__tel,musteri_talep)
        self.__ucret = ucret
        
    @property
    def km(self):
        return self.__km
    @km.setter
    def km(self, km):
        self.__km = km
    
    @property
    def plaka(self):
        return self.__plaka
    @plaka.setter
    def plaka(self, plaka):
        self.__plaka = plaka
    @property
    def giris_tarihi(self):
        return self.__giris_tarihi
    @giris_tarihi.setter
    def giris_tarihi(self, giris_tarihi):
        self.__giris_tarihi = giris_tarihi
    @property
    def teslim_tarihi(self):
        return self.__teslim_tarihi
    @teslim_tarihi.setter
    def teslim_tarihi(self, teslim_tarihi):
        self.__teslim_tarihi = teslim_tarihi
    @property
    def durum_raporu(self):
        return self.__durum_raporu
    @durum_raporu.setter
    def durum_raporu(self, durum_raporu):
        self.__durum_raporu = durum_raporu
    @property
    def musteri(self):
        return self.__musteri
    @musteri.setter
    def musteri(self, musteri):
        self.__musteri = musteri
    @property
    def ucret(self):
        return self.__ucret
    @ucret.setter
    def ucret(self, ucret):
        self.__ucret = ucret
        
    def arac_bilgisini_al(self):
        """Araç bilgisi sözlük olarak döndürülür"""
        arac_bilgisi = {"segment":self.segment, 
                        "model":self.model, 
                        "kasa_tipi":self.kasa_tipi, 
                        "vites":self.vites, 
                        "yil":self.yil, 
                        "motor":self.motor, 
                        "yakit_tipi":self.yakit_tipi,
                        "renk":self.renk, 
                        "km":self.km,
                        "plaka":self.plaka,
                        "giris_tarihi":self.giris_tarihi}
        arac_bilgisi.update(self.musteri.musteri_bilgisini_al())
        arac_bilgisi.update({"teslim_tarihi":self.teslim_tarihi,
                            "durum_raporu":self.durum_raporu,
                            "ucret":self.ucret})
        return arac_bilgisi
    def arac_bilgisini_guncelle(self, yeni_arac_bilgisi):
        """Mevcut aracın bilgisi sözlük olarak alınan araç bilgisi 
        ile güncellenir.
        """
        self.model = yeni_arac_bilgisi["model"]
        self.segment = yeni_arac_bilgisi["segment"]
        self.kasa_tipi = yeni_arac_bilgisi["kasa_tipi"]
        self.motor = yeni_arac_bilgisi["motor"]
        self.renk = yeni_arac_bilgisi["renk"]
        self.yakit_tipi = yeni_arac_bilgisi["yakit_tipi"]
        self.vites = yeni_arac_bilgisi["vites"]
        self.yil = yeni_arac_bilgisi["yil"]
        self.km = yeni_arac_bilgisi["km"]
        self.plaka = yeni_arac_bilgisi["plaka"]
        self.giris_tarihi = yeni_arac_bilgisi["giris_tarihi"]
        self.teslim_tarihi = yeni_arac_bilgisi["teslim_tarihi"]
        self.durum_raporu = yeni_arac_bilgisi["durum_raporu"]
        self.musteri.musteri_bilgisini_guncelle(yeni_arac_bilgisi["musteri_isim"],
                                                yeni_arac_bilgisi["musteri_tel"],
                                                yeni_arac_bilgisi["musteri_talep"])
        self.ucret = yeni_arac_bilgisi["ucret"]

    def __repr__(self):
        return (super().__repr__()+
                f'{self.__km}\n'+
                f'{self.__plaka}\n'+
                f'{self.__giris_tarihi}\n'+
                f'{self.__musteri}\n'+
                f'{self.__teslim_tarihi}\n'+
                f'{self.__durum_raporu}\n'+
                f'{self.__ucret}\n')
    