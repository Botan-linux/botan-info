# 🌿 Botan-Info

<p align="center">
  <img src="https://img.shields.io/badge/Version-2.0.0-00ff88?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Base-Arch_Linux-1793d1?style=for-the-badge&logo=arch-linux" />
  <img src="https://img.shields.io/badge/Language-Python-ffd343?style=for-the-badge&logo=python" />
</p>

<p align="center">
  <b>Sistemin nabzını tutan bir yaprak.</b><br>
  <i>Botan Linux ekosistemi için hafif ve estetik sistem monitörü.</i>
</p>

---

## 🚀 Hızlı Kurulum

`/etc/pacman.conf` dosyasının sonuna ekleyin:

```ini
[botan]
SigLevel = Optional TrustAll
Server = https://raw.githubusercontent.com/Botan-linux/botan-repo/main/x86_64
Server = https://gitlab.com/zeke000p/botan-repo/-/raw/main/x86_64

Kurulum: 
vurmak
Kopyala

sudo pacman -Syy botan-info

🛠️ Kullanım
Masa
Kopyala
Komut 	Açıklama
botan-info	Tam Özet: Görsel barlar ve detaylı analiz
botan-info -m	Minimal: Sadece temel sistem metrikleri
botan-info -j	JSON: Otomasyonlar için
✨ Öne Çıkanlar

    📊  Görsel Güç:  CPU, RAM ve Disk kullanımı için dinamik renkli barlar 
    ⚡  Saf Performans:  Python mimarisi sayesinde düşük kaynak tüketimi
    🛡️  Geniş Uyumluluk:  Arch, CachyOS ve EndeavourOS ile tam uyumlu yapı 

🤝 İletişim & Katkı
Bu araç Botan Linux topluluğu tarafından tutkuyla geliştirilmiştir. 
👉 **[Botan Linux Discord Sunucusu]( Botan Linux Discord Sunucusu
