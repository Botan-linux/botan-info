🌿 Botan-Info

    ____        __        __           
   / __ )____ _/ /_____ _/ /___  ____ _
  / __  / __ `/ __/ __ `/ / __ \/ __ `/
 / /_/ / /_/ / /_/ /_/ / / / / / /_/ / 
/_____/\__,_/\__/\__,_/_/_/ /_/\__,_/  
                                       
Botan Linux için geliştirilmiş, hafif, hızlı ve görselliği ön planda tutan sistem analiz aracı.

botan-info, terminal üzerinden sisteminizin sağlığını anlık olarak izlemenizi sağlayan, Python tabanlı bir yardımcı araçtır. Sadece veri göstermekle kalmaz, kritik eşikleri (CPU/RAM) renk kodlarıyla görselleştirir.

✨ Öne Çıkan Özellikler

📊 Canlı Barlar: Bellek ve disk doluluğunu % bazlı ilerleme çubuklarıyla görün.
🎨 Akıllı Renkler: Sistem yüküne göre değişen dinamik renk paleti (Yeşil: Rahat, Sarı: Yoğun, Kırmızı: Kritik).
⚙️ Donanım Detayı: CPU modelinden Kernel sürümüne, Uptime süresinden aktif kullanıcı sayısına kadar her şey.
🔌 JSON Entegrasyonu: -j bayrağı ile verileri JSON formatında alın; kendi dashboard projelerinizde kullanın.
🪶 Ultra Hafif: Minimum bağımlılık, maksimum performans.

🚀 Kurulum

1. Botan Linux Kullanıcıları (Resmi Repo)

sudo pacman -S botan-info

2. Diğer Arch Tabanlı Dağıtımlar (CachyOS, EndeavourOS vb.)

Botan araçlarını kullanmak için depomuzu sisteminize ekleyin:

/etc/pacman.conf dosyasını düzenleyin:

[botan]
SigLevel = Optional TrustAll
# Birincil Sunucu (GitHub)
Server = https://raw.githubusercontent.com/Botan-linux/botan-repo/main/x86_64
# Yedek Sunucu (GitLab) - En iyi deneyim için her ikisini de ekleyin
Server = https://gitlab.com/zeke000p/botan-repo/-/raw/main/x86_64

Depoyu senkronize edin ve kurun:

sudo pacman -Syy botan-info

💡 Not: İki sunucu da aynı içeriği sağlar. Birincisi yanıt vermezse otomatik olarak diğerine geçilir.

🛠️ Kullanım Rehberi

Komut	                Açıklama
botan-info	        Standart özet görünümü.
botan-info -m	        Minimal: Sadece en temel verileri gösterir.
botan-info -j	        Scripting: Otomasyonlar için JSON çıktısı verir.
botan-info --no-color	Renksiz çıktı (Düşük bitli terminaller veya loglar için).

🖼️ Örnek Çıktı

🌿 Botan Linux Sistem Bilgisi
──────────────────────────────────────────────────
Hostname:  botan-pc
OS:        Linux 6.7.4-arch1-1 (x86_64)
Uptime:    3 days, 14:22:11
Users:     2 aktif

⚙️  İşlemci
   AMD Ryzen 5 5600X
   Çekirdek: 12

💾 Bellek
   Toplam: 32012 MB | Kullanılan: 8456 MB
   [████████████████░░░░░░░░░░░░░░░░░░░░] 26.4%

💽 Disk (/) 
   Toplam: 512 GB | Boş: 423 GB
   [████████████░░░░░░░░░░░░░░░░░░░░░░░░] 17.4%

📊 Sistem Yükü
   1dk:  0.45
   5dk:  0.52
   15dk: 0.38
──────────────────────────────────────────────────
Botan v2.0 | 2026-02-27 14:30:15

🤝 Katkıda Bulunun (Fork & Support)

Bu araç Botan Linux topluluğu tarafından geliştirilmiştir. Kodları çatallayabilir (Fork), kendi dağıtımınıza göre optimize edebilir veya yeni özellikler ekleyerek bize destek olabilirsiniz.

🔗 GitHub: https://github.com/Botan-linux/botan-info
🔗 GitLab: https://gitlab.com/zeke000p/botan-info

Dipnot: "Bu araç sadece bir bilgi gösterici değil, sistemin nabzını tutan bir yapraktır." 🌱
