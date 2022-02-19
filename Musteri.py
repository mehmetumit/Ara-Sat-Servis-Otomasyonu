class Musteri:
    def __init__(self,isim="",tel="",talep=""):
        self.__isim = isim
        self.__tel = tel
        self.__talep = talep

    @property
    def isim(self):
        return self.__isim
    @isim.setter
    def isim(self, isim):
        self.__isim = isim
        
    @property
    def tel(self):
        return self.__tel 
    @tel.setter
    def tel(self, tel):
        self.__tel = tel
    
    @property     
    def talep(self):
        return self.__talep
    @talep.setter
    def talep(self, talep):
        self.__talep = talep
    
    def musteri_bilgisini_al(self):
        return {"musteri_isim":self.isim,
                "musteri_tel":self.tel,
                "musteri_talep":self.talep}
    def musteri_bilgisini_guncelle(self, isim, tel, talep):
        self.isim = isim
        self.tel = tel 
        self.talep = talep
    def __repr__(self):
        return (f'{self.__isim}'+
                f'{self.__tel}'+
                f'{self.__talep}'
                )
    