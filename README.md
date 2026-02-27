<h1 align="center">🌿 Botan-Info</h1>

<p align="center">
  <b>Sistemin nabzını tutan bir yaprak.</b><br>
  <i>Botan Linux için hafif ve estetik sistem monitörü.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-green?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="License"/>
  <img src="https://img.shields.io/badge/platform-Linux-yellow?style=flat-square&logo=linux" alt="Platform"/>
</p>

---

## 🚀 Kurulum

`/etc/pacman.conf` dosyasının en altına şu satırları ekleyin:

```ini
[botan]
SigLevel = Optional TrustAll
Server = https://raw.githubusercontent.com/Botan-linux/botan-repo/main/x86_64
Server = https://gitlab.com/zeke000p/botan-repo/-/raw/main/x86_64


sudo pacman -Syy
sudo pacman -S botan-info

🛠️ Kullanım
Table
Copy
Komut	Açıklama
botan-info	Görsel sistem özeti ve barlar
botan-info -m	Minimal (sadece metin) modu
botan-info -j	Scriptler için JSON veri çıktısı
✨ Öne Çıkanlar

    📊 Görsel Güç: CPU, RAM ve Disk için dinamik renkli barlar
    ⚡ Saf Performans: Python mimarisiyle düşük kaynak tüketimi
    🛡️ Geniş Uyumluluk: Arch, CachyOS ve EndeavourOS desteği

🤝 İletişim & Destek

    💬 Discord: https://discord.gg/zB4NYTFj
    🌐 Web Sitesi: https://botan-linux.github.io/Botan-sprout/

