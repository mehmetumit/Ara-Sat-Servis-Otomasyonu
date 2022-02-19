from AracServis import AracServis
from Yonetici import Yonetici
from AracServis import AracServis
from enum import Enum
import sqlite3
class ServisTipi(Enum):
    SERVISTE = 0
    SERVIS_GORMUS = 1

class ServisYoneticisi(Yonetici):
    def __init__(self, Id, sifre, data_servis:str):
        super().__init__(Id, sifre)
        self.__data_servis = data_servis
        self.__servisteki_araclar = list()
        self.__servis_gormus_araclar = list()
        self.__servisteki_araclar_plakalar = set()
        
        self.conn = sqlite3.connect(data_servis)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS servisteki_araclar(segment TEXT, model TEXT, kasa_tipi TEXT, vites TEXT, yil TEXT, motor TEXT, yakit_tipi TEXT, renk TEXT, km TEXT, plaka TEXT, giris_tarihi TEXT, musteri_isim TEXT, musteri_tel TEXT, musteri_talep TEXT, teslim_tarihi TEXT, durum_raporu TEXT, ucret TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS servis_gormus_araclar(segment TEXT, model TEXT, kasa_tipi TEXT, vites TEXT, yil TEXT, motor TEXT, yakit_tipi TEXT, renk TEXT, km TEXT, plaka TEXT, giris_tarihi TEXT, musteri_isim TEXT, musteri_tel TEXT, musteri_talep TEXT, teslim_tarihi TEXT, durum_raporu TEXT, ucret TEXT)")
    @property
    def servisteki_araclar(self):
        return self.__servisteki_araclar
    
    @property
    def servis_gormus_araclar(self):
        return self.__servis_gormus_araclar
    
    @property
    def data_servis(self):
        return self.__data_servis
    @property
    def servisteki_araclar_plakalar(self):
        return self.__servisteki_araclar_plakalar
        
    def arac_ekle(self, arac:AracServis, servis_tipi):
        """Parametre olarak verilen araç servis tipine göre
        servisteki araçlara ya da servis görmüş araçlara eklenir ardından
        araç dosyaya eklenir."""
        if servis_tipi == ServisTipi.SERVISTE:
            self.__servisteki_araclar.append(arac)
            """Araca ait plaka serviste bir kere bulunabileceğinden plakalara eklenir."""
            self.servisteki_araclar_plakalar.add(arac.plaka)            
        elif servis_tipi == ServisTipi.SERVIS_GORMUS:
            self.__servis_gormus_araclar.append(arac)
        else:
            return
        """Dosyaya araç eklenir"""
        self.dosyaya_arac_ekle(arac.arac_bilgisini_al(), servis_tipi)

    def dosyaya_arac_ekle(self, arac_bilgisi:dict, servis_tipi, index=-1):
        """Verilen servis tipine göre araç bilgisi dosyada uygun indexe atanır.
        İndex varsayılan değer yani -1 ise dosyanın sonuna eklenir."""
        if servis_tipi == ServisTipi.SERVISTE:
            data_tipi = "servisteki_araclar"
        elif servis_tipi == ServisTipi.SERVIS_GORMUS:
            data_tipi = "servis_gormus_araclar"
        else:
            return
        """rowID leri düzenler"""
        self.cur.execute("VACUUM")
        self.conn.commit()  
         
        if index == -1:
            self.cur.execute(f"INSERT INTO {data_tipi} VALUES(:segment, :model, :kasa_tipi, :vites, :yil, :motor, :yakit_tipi, :renk, :km, :plaka, :giris_tarihi, :musteri_isim, :musteri_tel, :musteri_talep, :teslim_tarihi, :durum_raporu, :ucret)",tuple(arac_bilgisi.values()))
            self.conn.commit()
        else:
            rowID = index + 1
            self.cur.execute(f"UPDATE {data_tipi} SET segment=?, model=?, kasa_tipi=?, vites=?, yil=?, motor=?, yakit_tipi=?, renk=?, km=?, plaka=?, giris_tarihi=?, musteri_isim=?, musteri_tel=?, musteri_talep=?, teslim_tarihi=?, durum_raporu=?, ucret=? WHERE rowid={rowID}",tuple(arac_bilgisi.values()))
            self.conn.commit()
        
    def arac_sil(self, index, servis_tipi):
        """Alınan indexteki araç servis tipine göre silinir"""
        if servis_tipi == ServisTipi.SERVISTE:
            """Silinecek aracın plakası plakalar kümesinden de silinir"""
            self.__servisteki_araclar_plakalar.remove(self.servisteki_araclar[index].plaka)
            self.__servisteki_araclar.pop(index)
        elif servis_tipi == ServisTipi.SERVIS_GORMUS:
            self.__servis_gormus_araclar.pop(index)
        else:
            return
        self.dosyadan_arac_sil(index, servis_tipi)
        
    def dosyadan_arac_sil(self,index, servis_tipi):
        """Alınan indexteki araç servis tipine göre dosyadan silinir"""
        if servis_tipi == ServisTipi.SERVISTE:
            data_tipi = 'servisteki_araclar'
        elif servis_tipi == ServisTipi.SERVIS_GORMUS:
            data_tipi = 'servis_gormus_araclar'
        else:
            return
        rowID = index + 1
        self.cur.execute(f"DELETE FROM {data_tipi} WHERE rowid={rowID}")
        self.conn.commit()
        self.cur.execute("VACUUM")
        self.conn.commit()

                
    def servis_islemini_tamamla(self, index):
        """Alınan indexteki araç servisteki_araclar listesinden ve dosyadan kaldırılır.
        Daha sonra servis_gormus_araclar listesine ve dosyaya eklenir""" 
        arac = self.__servisteki_araclar.pop(index)
        """Servis işlemi tamamlanan aracın plakası plakalar kümesinden kaldırılır"""
        self.servisteki_araclar_plakalar.remove(arac.plaka)
        self.dosyadan_arac_sil(index, ServisTipi.SERVISTE)
        self.__servis_gormus_araclar.append(arac)
        self.dosyaya_arac_ekle(arac.arac_bilgisini_al(), ServisTipi.SERVIS_GORMUS)
        
    def arac_bilgisini_guncelle(self, index, arac_bilgisi, servis_tipi):
        """Alınan indexteki araç bilgisi alınan araç bilgisi ile servis tipine göre güncellenir."""
        if servis_tipi == ServisTipi.SERVISTE:
            """Plakanın değişme durumu olabileceğinden eski plaka kaldırılır yenisi eklenir."""
            self.servisteki_araclar_plakalar.remove(self.__servisteki_araclar[index].plaka)
            self.__servisteki_araclar[index].arac_bilgisini_guncelle(arac_bilgisi)
            self.servisteki_araclar_plakalar.add(arac_bilgisi["plaka"])
        elif servis_tipi == ServisTipi.SERVIS_GORMUS:
            self.__servis_gormus_araclar[index].arac_bilgisini_guncelle(arac_bilgisi)
        else:
            return
        """Araç dosyaya eklenerek güncellenir."""
        self.dosyaya_arac_ekle(arac_bilgisi, servis_tipi, index)
        
    def arac_bilgisini_al(self, index, servis_tipi):
        """Alınan indexteki aracın bilgisi servis_tipine göre döndürülür."""
        if servis_tipi == ServisTipi.SERVISTE:
            return self.__servisteki_araclar[index].arac_bilgisini_al()
        elif servis_tipi == ServisTipi.SERVIS_GORMUS:
            return self.__servis_gormus_araclar[index].arac_bilgisini_al()
    
    def servis_listesi_al(self, servis_tipi):
        """Servis listesi servis_tipi'ne göre dosyadan alınıp uygun şekilde
        güncellenir."""

        self.cur.execute("VACUUM")
        if servis_tipi == ServisTipi.SERVISTE:
            self.cur.execute("SELECT * FROM servisteki_araclar")
            """Dosyadaki servisteki araçlar listeye aktarılır"""
            for row in self.cur.fetchall():
                arac = AracServis(*row)
                self.__servisteki_araclar.append(arac)
                self.__servisteki_araclar_plakalar.add(arac.plaka)
                        
           
        elif servis_tipi == ServisTipi.SERVIS_GORMUS:
            self.cur.execute("SELECT * FROM servis_gormus_araclar")

            """Dosyadaki servis görmüş araçlar listeye aktarılır."""
            for row in self.cur.fetchall():
                arac = AracServis(*row)
                self.__servis_gormus_araclar.append(arac)
                        
                    
        
    def __repr__(self):
        return (super().__repr__() +
                f'servisteki_araclar: {self.__servisteki_araclar}\n'+
                f'servis_gormus_araclar: {self.__servis_gormus_araclar}\n')