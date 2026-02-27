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

```
---

## 🛠️ Kullanım Rehberi
Terminal üzerinden ihtiyacınıza uygun modu seçerek sistemi analiz edebilirsiniz:

- **📊 Standart Görünüm:** `botan-info` (Görsel barlar ve detaylı özet)
- **🍃 Minimal Mod:** `botan-info -m` (Sadece temel sistem metrikleri)
- **📋 JSON Çıktısı:** `botan-info -j` (Otomasyon ve scriptler için veri)
- **⚪ Renksiz Çıktı:** `botan-info --no-color` (Log dosyaları için uygun)

---

## ✨ Öne Çıkan Özellikler
Botan-Info, sadeliği modern sistem analiziyle birleştirir.

- **🚀 Hafif Mimari:** Python tabanlı yapısıyla sistem kaynaklarını yormaz.
- **🎨 Akıllı Renkler:** CPU ve RAM yüküne göre dinamik renk kodlaması.
- **📈 Görsel İstatistikler:** Terminal üzerinde şık ve anlaşılır doluluk barları.
- **🛡️ Tam Uyumluluk:** Arch Linux, CachyOS ve EndeavourOS sistemlerinde sorunsuz çalışır.

---

## 🏗️ Geliştirme Süreci

> **📢 Önemli Not:** Botan Linux ekosistemini güçlendirmek adına bu aracı aktif olarak güncelliyoruz. Önümüzdeki süreçte odak noktalarımız:
> - **Repo Optimizasyonu:** Paketlerimizi daha hızlı ve erişilebilir kılmak.
> - **Yeni Modüller:** GPU sıcaklık ve ağ trafiği analizi eklemek.
> - **Stabilite:** Farklı terminal emülatörlerinde kusursuz görünüm sağlamak.

---

## 🤝 Ekibimize Katılın!

Botan Linux'un geleceğini birlikte inşa edebiliriz! Eğer siz de geliştirici ekibine katılmak veya projeye destek olmak isterseniz Discord sunucumuza bekliyoruz:

👉 **[Botan Linux Discord Sunucusu](https://discord.gg/zB4NYTFj)**

---

<p align="center">
  <i>"Botanı daha iyi bir yere taşımak için çalışmaya devam ediyoruz."</i>
</p>
