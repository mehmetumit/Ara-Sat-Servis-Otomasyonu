import hashlib as hl
class HashAraci:
    """Id ve şifre hashlerinin oluşturulmasında kullanılmıştır"""
    @staticmethod
    def hash_yap(Id, sifre):
        """
        Unicode input utf-8 olarak encode edilmeli
        """
        data = {"Id":hl.sha256(Id.encode('utf-8')).hexdigest(),
                "sifre":hl.sha256(sifre.encode('utf-8')).hexdigest()}
        return data
