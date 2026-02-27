🌿 Botan-Info
Plaintext

  ____        _                    ___        __      
 | __ )  ___ | |_ __ _ _ __       |_ _|_ __  / _| ___  
 |  _ \ / _ \| __/ _` | '_ \ _____ | || '_ \| |_ / _ \ 
 | |_) | (_) | || (_| | | | |_____|| || | | |  _| (_) |
 |____/ \___/ \__\__,_|_| |_|     |___|_| |_|_|  \___/ 
                                          by Botan Linux

    Botan Linux için geliştirilmiş, hafif, hızlı ve görselliği ön planda tutan sistem analiz aracı.

botan-info, terminal üzerinden sisteminizin sağlığını anlık olarak izlemenizi sağlayan Python tabanlı bir yardımcı araçtır.
✨ Öne Çıkan Özellikler

    📊 Canlı Barlar: Bellek ve disk doluluğunu görsel ilerleme çubuklarıyla izleyin.

    🎨 Akıllı Renkler: Sistem yüküne göre değişen dinamik renk paleti (Yeşil, Sarı, Kırmızı).

    ⚙️ Donanım Detayı: CPU, Kernel, Uptime ve aktif kullanıcı bilgilerine anında erişim.

    🔌 JSON Desteği: -j bayrağı ile otomasyonlarınız için temiz veri çıktısı alın.

    🪶 Ultra Hafif: 4GB RAM'li sistemlerde bile kasmadan, anında çalışır.

🚀 Kurulum & Depo Ayarları

Diğer Arch tabanlı dağıtımlarda (CachyOS, EndeavourOS vb.) botan-info ve diğer araçlarımıza erişmek için /etc/pacman.conf dosyanıza aşağıdaki satırları ekleyin.

Not: En iyi deneyim ve kesintisiz bağlantı için iki sunucuyu da eklemeniz önerilir. Sistem, bir sunucuya ulaşılamazsa otomatik olarak diğerini deneyecektir.
Ini, TOML

[botan]
SigLevel = Optional TrustAll
# GitHub Mirror (Primary)
Server = https://raw.githubusercontent.com/Botan-linux/botan-repo/main/x86_64
# GitLab Mirror (Secondary)
Server = https://gitlab.com/zeke000p/botan-repo/-/raw/main/x86_64

Depoyu güncelleyin ve kurun:
Bash

sudo pacman -Syy botan-info

🛠️ Kullanım Rehberi
Komut	Açıklama
botan-info	Standart özet görünümü (Görsel barlar ile).
botan-info -m	Minimal: Sade, metin tabanlı özet.
botan-info -j	JSON: Scriptler için yapılandırılmış veri.
botan-info --no-color	Renksiz çıktı (Loglama için uygun).
🤝 Katkıda Bulunun

Bu araç Botan Linux topluluğu için geliştirilmiştir. Kodları çatallayarak (Fork) kendi dağıtımınıza göre optimize edebilir veya yeni özellikler ekleyebilirsiniz.

    Dipnot: "Bu araç sadece bir bilgi gösterici değil, sistemin nabzını tutan bir yapraktır." 🌱
