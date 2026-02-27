Anladım, kod bloklarını (```) kaldırdığımızda yazıların iç içe geçmesi engellendi ama bu sefer de görsellik kayboldu. GitHub özelliklerini (tablolar, kalın yazılar ve hizalamalar) kullanarak, yazıların birbirine girmesini engelleyen geniş boşluklu ve profesyonel tasarımı hazırladım.

Bunu direkt kopyalayıp README.md dosyasına yapıştırabilirsin:
🌿 Botan-Info

<p align="center">
<b>Sistemin nabzını tutan bir yaprak.</b>


<i>Botan Linux için hafif ve estetik sistem monitörü.</i>
</p>
🚀 Kurulum

/etc/pacman.conf dosyasının en altına şu satırları ekleyin:

[botan]


SigLevel = Optional TrustAll


Server = https://raw.githubusercontent.com/Botan-linux/botan-repo/main/x86_64


Server = https://gitlab.com/zeke000p/botan-repo/-/raw/main/x86_64
🛠️ Kullanım
Komut	Açıklama
botan-info	Görsel sistem özeti ve barlar.
botan-info -m	Minimal (sadece metin) modu.
botan-info -j	Scriptler için JSON veri çıktısı.
✨ Öne Çıkanlar

    📊 Görsel Güç: CPU, RAM ve Disk için dinamik renkli barlar.

    ⚡ Saf Performans: Python mimarisiyle düşük kaynak tüketimi.

    🛡️ Geniş Uyumluluk: Arch, CachyOS ve EndeavourOS desteği.

🤝 İletişim & Destek

    Discord: https://discord.gg/zB4NYTFj

    Web Sitesi: https://botan-linux.github.io/Botan-sprout/
