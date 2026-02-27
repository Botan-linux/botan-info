# 🌿 Botan-Info

<p align="center">
 <img src="https://img.shields.io/badge/Version-2.0.0-00ff88?style=for-the-badge" />
 <img src="https://img.shields.io/badge/Base-Arch_Linux-1793d1?style=for-the-badge&logo=arch-linux" />
 <img src="https://img.shields.io/badge/Language-Python-ffd343?style=for-the-badge&logo=python" />
</p>

<p align="center">
 <b>Sistemin nabzını tutan bir yaprak.</b><br>
 Botan Linux ekosistemi için hafif ve estetik sistem monitörü.
</p>

---

## 🌐 Resmi Depo

Botan-Info ve diğer Botan araçlarını kullanmak için resmi depomuzu ekleyin:

👉 **[Botan Linux Repo](https://github.com/Botan-linux/botan-repo)**

---

## 🚀 Hızlı Kurulum

`/etc/pacman.conf` dosyasının sonuna ekleyin:

```ini
[botan]
SigLevel = Optional TrustAll
Server = https://raw.githubusercontent.com/Botan-linux/botan-repo/main/x86_64
Server = https://gitlab.com/zeke000p/botan-repo/-/raw/main/x86_64


Kurulum:
```bash
sudo pacman -Syy botan-info
