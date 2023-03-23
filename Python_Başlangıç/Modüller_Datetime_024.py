"""
DATETİME MODÜLÜ 

date, time ve datetime

"""

from datetime import datetime

#print(dir(datetime))
#print(help(datetime))

şuan = datetime.now()
# Şu anki gün,ay,yıl,saat,dakika ve saniyeyi yazdırır.
print(şuan.year)
# Sadece yılı yazdırır.

tarih = datetime.ctime(şuan)
print(tarih)

okunaklı_tarih = datetime.strftime(şuan, "%c")
# Buradan alınan çıktı .ctime kullanılarak alınan çıktıyla aynı olur.
# %c ile tüm tarihin çıktısı alınır.

okunaklı_tarih2 = datetime.strftime(şuan, "%j")
# %j ile yılın kaçıncı günü olduğunun çıktısı alınır.

okunaklı_tarih3 = datetime.strftime(şuan, "%x")
# %x ile Ay/Gün/Yıl şeklinde çıktı alınır.

okunaklı_tarih4 = datetime.strftime(şuan, "%X")
# %X ile Saat:Dakika:Saniye şeklinde çıktı alınır.