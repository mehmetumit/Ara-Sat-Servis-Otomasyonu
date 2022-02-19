from HashAraci import HashAraci
from abc import abstractmethod
from enum import IntEnum
import hashlib as hl
import sqlite3

class YoneticiTipi(IntEnum):
    SATIS = 0
    SERVIS = 1
    
class Yonetici:
    def __init__(self,Id,sifre):
        self.__Id = Id
        self.__sifre = sifre

    @property
    def Id(self):
        return self.__Id

    @property
    def sifre(self):
        return self.__sifre

    @abstractmethod
    def arac_ekle(self):
        pass

    @abstractmethod
    def arac_sil(self):
        pass
    @abstractmethod
    def arac_bilgisini_guncelle(self):
        pass

    @staticmethod
    def giris_kontrol_et(Id, sifre, yonetici_tipi):
        """
        Yönetici tipine göre uygun dosyadan 
        Id ve sifre nin hash değerlerini sha256 ya göre bulup
        dosyada var olup olmadığına bakılır.Tuple olarak
        (giriş başarılı mı, giriş bilgisi, id hash, şifre hash)
        bilgilerinin karşılıklarını döndürür.
        """
        conn = sqlite3.connect("yonetici.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS servis_yoneticisi(Id TEXT, sifre TEXT)")
        cur.execute("CREATE TABLE IF NOT EXISTS satis_yoneticisi(Id TEXT, sifre TEXT)")
        
        conn.commit()

        if yonetici_tipi == YoneticiTipi.SATIS:
            yonetici_tipi_data = "satis_yoneticisi"
        elif yonetici_tipi == YoneticiTipi.SERVIS:
            yonetici_tipi_data = "servis_yoneticisi"
        yonetici_hash = HashAraci.hash_yap(Id, sifre)
        
        cur.execute(f"SELECT * FROM {yonetici_tipi_data}")
        Id_flag = False
        sifre_flag = False
        for row in cur.fetchall():
            if yonetici_hash["Id"] == row[0]:
                Id_flag = True
            if yonetici_hash["sifre"] == row[1]:
                sifre_flag = True
        if Id_flag:
            if sifre_flag:
                return (True,"Giriş başarılı", yonetici_hash["Id"], yonetici_hash["sifre"])
            else:
                return (False,"Şifre hatalı!", yonetici_hash["Id"], yonetici_hash["sifre"])
        else:
            return (False,"Id ve/veya şifre hatalı!", yonetici_hash["Id"], yonetici_hash["sifre"])

        #if id_hash in jsonObject[yonetici_tipi_data]:
        #    if sifre_hash == jsonObject[yonetici_tipi_data][id_hash]:
        #        return (True,"Giriş başarılı", id_hash, sifre_hash)
        #    return (False,"Şifre hatalı!", id_hash, sifre_hash)
        #return (False,"Id ve/veya şifre hatalı!", id_hash, sifre_hash)

    def __repr__(self):
        return (f'Id: {self.__Id}\n'+
                f'Şifre: {self.__sifre}\n')