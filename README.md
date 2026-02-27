# 🌿 Botan-Info

<p align="center">
  <img src="https://img.shields.io/badge/Version-2.0.0-00ff88?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Base-Arch_Linux-1793d1?style=for-the-badge&logo=arch-linux" />
</p>

<p align="center">
  <b>Sistemin nabzını tutan bir yaprak.</b><br>
  <i>Botan Linux için hafif sistem monitörü.</i>
</p>

---

### 🚀 Kurulum
`/etc/pacman.conf` sonuna ekle:

```ini
[botan]
SigLevel = Optional TrustAll
Server = [https://raw.githubusercontent.com/Botan-linux/botan-repo/main/x86_64](https://raw.githubusercontent.com/Botan-linux/botan-repo/main/x86_64)
Server = [https://gitlab.com/zeke000p/botan-repo/-/raw/main/x86_64](https://gitlab.com/zeke000p/botan-repo/-/raw/main/x86_64)

Ardından şu komutu çalıştırın:
Bash

sudo pacman -Syy botan-info

🛠️ Kullanım

    botan-info : Görsel sistem özeti.

    botan-info -m : Minimal mod.

    botan-info -j : JSON veri çıktısı.

🤝 İletişim & Destek

    Discord: https://discord.gg/zB4NYTFj

    Web: https://botan-linux.github.io/Botan-sprout/
