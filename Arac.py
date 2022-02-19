from abc import abstractmethod
class Arac:
    def __init__(self, segment="", model="",  kasa_tipi="", vites="", yil="", motor="",  yakit_tipi="", renk=""):
        self.__model = model
        self.__segment = segment
        self.__kasa_tipi = kasa_tipi
        self.__motor = motor
        self.__renk = renk
        self.__yakit_tipi = yakit_tipi
        self.__vites = vites
        self.__yil = yil
        
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model):
        self.__model = model
        
    @property
    def segment(self):
        return self.__segment
    @segment.setter
    def segment(self, segment):
        self.__segment = segment
        
    @property
    def kasa_tipi(self):
        return self.__kasa_tipi
    @kasa_tipi.setter
    def kasa_tipi(self, kasa_tipi):
        self.__kasa_tipi = kasa_tipi
        
    @property
    def motor(self):
        return self.__motor
    @motor.setter
    def motor(self, motor):
        self.__motor = motor
    
    @property
    def renk(self):
        return self.__renk
    @renk.setter
    def renk(self, renk):
        self.__renk = renk
        
    @property
    def yakit_tipi(self):
        return self.__yakit_tipi
    @yakit_tipi.setter
    def yakit_tipi(self, yakit_tipi):
        self.__yakit_tipi = yakit_tipi
    
    @property
    def vites(self):
        return self.__vites
    @vites.setter
    def vites(self, vites):
        self.__vites = vites
        
    @property
    def yil(self):
        return self.__yil
    @yil.setter
    def yil(self, yil):
        self.__yil = yil
        
    @abstractmethod
    def arac_bilgisini_al():
        raise NotImplementedError()
    
    def __repr__(self):
        return (f'{self.__model}\n'+
                f'{self.__segment}\n'+
                f'{self.__kasa_tipi}\n'+
                f'{self.__motor}\n'+
                f'{self.__renk}\n'+
                f'{self.__yakit_tipi}\n'+
                f'{self.__vites}\n'+
                f'{self.__yil}\n'
                )
    