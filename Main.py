from SatisYoneticisi import SatisYoneticisi
from SatisMenu import SatisMenu
from GirisEkrani import GirisEkrani
from Yonetici import Yonetici, YoneticiTipi
from SatisMenu import *
from ServisMenu import *

if __name__ == "__main__":
    while True:
        ge = GirisEkrani()

        if ge.giris_basarili:
            yonetici = Yonetici(ge.yonetici_Id,ge.yonetici_sifre)
            if ge.secili_yonetici.get() == YoneticiTipi.SATIS:
                menu = SatisMenu(SatisYoneticisi(yonetici.Id, yonetici.sifre, "satis.db"))
                if menu.giris_ekranina_donulsun:
                    continue
                else:
                    break
            elif ge.secili_yonetici.get() == YoneticiTipi.SERVIS:
                menu = ServisMenu(ServisYoneticisi(yonetici.Id, yonetici.sifre, "servis.db"))
                if menu.giris_ekranina_donulsun:
                    continue
                else:
                    break
        else:
            """Giriş başarısız ve ekran kapatılmış"""
            break
