# 🌿 Botan Linux Sistem Bilgisi Aracı

Gelişmiş terminal tabanlı Linux sistem monitörü ve bilgi görüntüleyici.

## Özellikler

- 📊 Görsel bellek ve disk kullanım barları
- 🎨 Akıllı renk kodlaması (yeşil/sarı/kırmızı)
- ⚙️ Detaylı CPU bilgisi
- 💾 RAM, Swap ve Disk kullanımı
- 🌐 Ağ arayüzleri
- ⏱️ Sistem uptime'ı
- 👥 Aktif kullanıcı sayısı
- 📋 JSON çıktı desteği (scriptler için)

## Kurulum

### Botan Linux 
```bash
sudo pacman -S botan-info
## Kullanım
# Tam bilgi göster
botan-info

# Minimal mod (sadece temel bilgiler)
botan-info -m

# JSON çıktı
botan-info -j | jq .

# Renksiz çıktı (log dosyası için)
botan-info --no-color > sistem.log

# Yardım
botan-info --help

## Dipnot: bu araç botan linux ile geliştrilmiş  forkunu yapıp arch cachy os endavouros için oluşturabilirsiniz
