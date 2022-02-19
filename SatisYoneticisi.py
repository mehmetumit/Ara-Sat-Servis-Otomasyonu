from Yonetici import Yonetici
from AracSatis import AracSatis
from enum import Enum
import sqlite3

class SatisTipi(Enum):
    STOK= 0
    SATILMIS = 1

class SatisYoneticisi(Yonetici):
    def __init__(self, Id, sifre, data_satis:str):
        super().__init__(Id, sifre)
        self.__data_satis = data_satis
        self.__stoktaki_araclar = list()
        self.__satilmis_araclar = list()
        
        self.conn = sqlite3.connect(data_satis)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS stoktaki_araclar(segment TEXT, model TEXT, kasa_tipi TEXT, vites TEXT, yil TEXT, motor TEXT, yakit_tipi TEXT, renk TEXT, fiyat TEXT, adet TEXT, satis_tarihi TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS satilmis_araclar(segment TEXT, model TEXT, kasa_tipi TEXT, vites TEXT, yil TEXT, motor TEXT, yakit_tipi TEXT, renk TEXT, fiyat TEXT, adet TEXT, satis_tarihi TEXT)")

        
    @property
    def stoktaki_araclar(self):
        return self.__stoktaki_araclar
    @property
    def satilmis_araclar(self):
        return self.__satilmis_araclar
    @property
    def data_satis(self):
        return self.__data_satis
    
    def arac_ekle(self, arac, satis_tipi):
        """Parametre olarak verilen araç satış tipine göre
        satılmış araçlara ya da stoktaki araçlara eklenir ardından
        araç dosyaya eklenir."""
        if satis_tipi == SatisTipi.SATILMIS:
            self.__satilmis_araclar.append(arac)
        elif satis_tipi == SatisTipi.STOK:
            self.__stoktaki_araclar.append(arac)
        else:
            return
        """Dosyanın sonuna araç eklenir."""
        self.dosyaya_arac_ekle(arac.arac_bilgisini_al(), satis_tipi)
        
    def arac_sil(self, index, satis_tipi):
        if satis_tipi == SatisTipi.STOK:
            silinen_arac = self.__stoktaki_araclar.pop(index)
        elif satis_tipi == SatisTipi.SATILMIS:
            silinen_arac = self.__satilmis_araclar.pop(index)
        self.dosyadan_arac_sil(index, satis_tipi)
        return silinen_arac
    
    def arac_sat(self, index, satis_adedi, satis_tarihi):
        """index teki aracı satış adedi kadar satar"""
        
        arac_stok_bilgisi = self.arac_bilgisini_al(index, SatisTipi.STOK)
        """Satış adedi stoktakinden fazla ya da eşit ise stoktaki araç silinip
        satılmış araçlara eklenir"""
        if satis_adedi >= int(arac_stok_bilgisi["adet"]):
            satilmis_arac = self.arac_sil(index, SatisTipi.STOK)
            satilmis_arac.satis_tarihi = satis_tarihi
            self.arac_ekle(satilmis_arac, SatisTipi.SATILMIS)
            
        else:
            """
            Satılacak adet stoktaki adetden az ise stoktaki aracın adet bilgisi satılan 
            arac adedi kadar azaltılır ve stoktaki aracın bilgisindeki adet güncellenerek
            yeni araç oluşturulur. Ardından bu araç satılmış olarak eklenir
            """ 
            arac_stok_bilgisi["adet"] = str(int(arac_stok_bilgisi["adet"]) - satis_adedi)
            arac_stok_bilgisi["satis_tarihi"] = satis_tarihi
            self.arac_bilgisini_guncelle(index, arac_stok_bilgisi, SatisTipi.STOK)
            satilmis_arac = AracSatis()
            satilmis_arac.arac_bilgisini_guncelle(arac_stok_bilgisi)
            satilmis_arac.adet = satis_adedi
            self.arac_ekle(satilmis_arac,SatisTipi.SATILMIS)
            
    
    def arac_bilgisini_guncelle(self, index, arac_bilgisi, satis_tipi):
        """Alınan indexteki araç bilgisi alınan araç bilgisi ile satış tipine göre güncellenir."""
        if satis_tipi == SatisTipi.STOK:
            self.__stoktaki_araclar[index].arac_bilgisini_guncelle(arac_bilgisi)
        elif satis_tipi == SatisTipi.SATILMIS:
            self.__satilmis_araclar[index].arac_bilgisini_guncelle(arac_bilgisi)
        else:
            return
        """Araç dosyaya eklenerek güncellenir."""
        self.dosyaya_arac_ekle(arac_bilgisi, satis_tipi, index)
        
    def dosyaya_arac_ekle(self, arac_bilgisi:dict, satis_tipi, index=-1):
        """Verilen araç tipine göre araç bilgisi dosyada uygun indexe atanır.
        İndex varsayılan değer yani -1 ise dosyanın sonuna eklenir."""
        if satis_tipi == SatisTipi.STOK:
            data_tipi = "stoktaki_araclar"
        elif satis_tipi == SatisTipi.SATILMIS:
            data_tipi = "satilmis_araclar"
        else:
            return
        """rowID leri düzenler"""
        self.cur.execute("VACUUM")
        self.conn.commit()
        if index == -1:
            self.cur.execute(f"INSERT INTO {data_tipi} VALUES(:segment, :model, :kasa_tipi, :vites, :yil, :motor, :yakit_tipi, :renk, :fiyat, :adet, :satis_tarihi)",tuple(arac_bilgisi.values()))
            self.conn.commit()
        else:
            rowID = index + 1
            self.cur.execute(f"UPDATE {data_tipi} SET segment=?, model=?, kasa_tipi=?, vites=?, yil=?, motor=?, yakit_tipi=?, renk=? ,fiyat=?, adet=?, satis_tarihi=? WHERE rowid={rowID}",tuple(arac_bilgisi.values()))
            self.conn.commit()
                    
        
            
    def dosyadan_arac_sil(self, index, satis_tipi):
        """Alınan indexteki araç satış tipine göre dosyadan silinir"""
        if satis_tipi == SatisTipi.STOK:
            data_tipi = 'stoktaki_araclar'
        elif satis_tipi == SatisTipi.SATILMIS:
            data_tipi = 'satilmis_araclar'
        else:
            return
        
        self.cur.execute(f"DELETE FROM {data_tipi} LIMIT 1 OFFSET ?", str(index))
        self.conn.commit()
        self.cur.execute("VACUUM")
        self.conn.commit()
    
    def satis_listesi_al(self, satis_tipi):
        """Satış listesi satis_tipi'ne göre dosyadan alınıp uygun şekilde
        güncellenir."""
        self.cur.execute("VACUUM")
        if satis_tipi == SatisTipi.STOK:   
            self.cur.execute("SELECT * FROM stoktaki_araclar")
            for row in self.cur.fetchall():
                arac = AracSatis(*row)
                self.stoktaki_araclar.append(arac)
        elif satis_tipi == SatisTipi.SATILMIS:
            self.cur.execute("SELECT * FROM satilmis_araclar")
            """Dosyadaki satılmış araçlar listeye aktarılır."""
            for row in self.cur.fetchall():
                arac = AracSatis(*row)
                self.satilmis_araclar.append(arac)
                        
                   
    def arac_bilgisini_al(self, index, satis_tipi):
        """Alınan indexteki aracın bilgisi satis_tipi'ne göre döndürülür."""
        if satis_tipi == SatisTipi.SATILMIS :
            return self.__satilmis_araclar[index].arac_bilgisini_al()
        elif satis_tipi== SatisTipi.STOK:
            return self.__stoktaki_araclar[index].arac_bilgisini_al()
    def arac_bilgisi_mevcut_mu(self, arac_bilgisi:dict, satis_tipi, bakilmayacak_index=-1):
        """Parametre olarak verilen araç bilgisinin satış tipine göre ait olduğu araçlar içerisinde 
        mevcut olup olmadığını kontrol eder.Bakılmayacak index değeri istenirse atanabilir."""
        if satis_tipi == SatisTipi.SATILMIS:
            araclar = self.satilmis_araclar
        elif satis_tipi == SatisTipi.STOK:
            araclar = self.stoktaki_araclar
        else:
            return
        
        bakilacak_arac_bilgisi = arac_bilgisi.copy()
        bakilacak_arac_bilgisi.pop("fiyat")
        bakilacak_arac_bilgisi.pop("adet")
        if satis_tipi != SatisTipi.SATILMIS:
            bakilacak_arac_bilgisi.pop("satis_tarihi")
        for index in range(len(araclar)):
            hedef_arac_bilgisi = araclar[index].arac_bilgisini_al()
            hedef_arac_bilgisi.pop("fiyat")
            hedef_arac_bilgisi.pop("adet")
            if satis_tipi != SatisTipi.SATILMIS:
                hedef_arac_bilgisi.pop("satis_tarihi")
            if index == bakilmayacak_index:
                continue
            elif bakilacak_arac_bilgisi == hedef_arac_bilgisi:
                return True
        return False
    
    def __repr__(self):
        return (super().__repr__()+
                f'stoktaki_araclar: {self.__stoktaki_araclar}\n'+
                f'satilmis_araclar: {self.__satilmis_araclar}\n')