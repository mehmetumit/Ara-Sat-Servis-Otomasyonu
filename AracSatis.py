from Arac import Arac

class AracSatis(Arac):
    def __init__(self, segment="", model="", kasa_tipi="", vites="", yil="", motor="", yakit_tipi="", renk="", fiyat="", adet="", satis_tarihi="" ):
        super().__init__(segment,model,  kasa_tipi,vites, yil, motor, yakit_tipi, renk)
        self.__fiyat = fiyat
        self.__satis_tarihi = satis_tarihi
        self.__adet = adet
        
    @property
    def fiyat(self):
        return self.__fiyat
    @fiyat.setter
    def fiyat(self, fiyat):
        self.__fiyat = fiyat
    @property
    def satis_tarihi(self):
        return self.__satis_tarihi
    @satis_tarihi.setter
    def satis_tarihi(self, satis_tarihi):
        self.__satis_tarihi = satis_tarihi
    @property
    def adet(self):
        return self.__adet
    @adet.setter
    def adet(self, adet):
        self.__adet = adet
        
    def konfigure_et():
        return
    
    def arac_bilgisini_al(self):
        return {"segment":self.segment, 
                "model":self.model, 
                "kasa_tipi":self.kasa_tipi, 
                "vites":self.vites, 
                "yil":self.yil, 
                "motor":self.motor,
                "yakit_tipi":self.yakit_tipi,
                "renk":self.renk,
                "fiyat":self.fiyat,
                "adet":self.adet,
                "satis_tarihi":self.satis_tarihi}
    def arac_bilgisini_guncelle(self, yeni_arac_bilgisi):
        """Mevcut aracın bilgisi sözlük olarak alınan araç bilgisi 
        ile güncellenir.
        """
        self.segment = yeni_arac_bilgisi["segment"]
        self.kasa_tipi = yeni_arac_bilgisi["kasa_tipi"]
        self.model = yeni_arac_bilgisi["model"]
        self.vites = yeni_arac_bilgisi["vites"]
        self.yil = yeni_arac_bilgisi["yil"]
        self.motor = yeni_arac_bilgisi["motor"]
        self.yakit_tipi = yeni_arac_bilgisi["yakit_tipi"]
        self.satis_tarihi = yeni_arac_bilgisi["satis_tarihi"]
        self.renk = yeni_arac_bilgisi["renk"]
        self.fiyat = yeni_arac_bilgisi["fiyat"]
        self.adet = yeni_arac_bilgisi["adet"]
        
    def __repr__(self):
        return (super().__repr__() +
                f'renk: {self.__renk}\n'+
                f'fiyat: {self.__fiyat}\n'+
                f'adet: {self.adet}\n'+
                f'satis_tarihi: {self.satis_tarihi}\n')