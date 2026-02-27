🌿 Botan-Info

<p align="center">
<img src="https://img.shields.io/badge/Version-2.0.0-00ff88?style=for-the-badge" />
<img src="https://img.shields.io/badge/Base-Arch_Linux-1793d1?style=for-the-badge&logo=arch-linux" />
<img src="https://img.shields.io/badge/Language-Python-ffd343?style=for-the-badge&logo=python" />
</p>

<p align="center">
<code>

| __ )  ___ | |_ __ _ _ __       |_ | __  / | ___

|  _ \ / _ | / ` | ' \ _____ | || ' | | / _ \

| |) | () | || (| | | | ||| || | | |  | () |
|____/ _/ __,|| ||     ||| ||_|  __/
</code>



<b>Sistemin nabzını tutan bir yaprak.</b>


Gelişmiş terminal tabanlı Linux sistem monitörü ve bilgi görüntüleyici.
</p>
🌟 Özellikler

Botan-Info, sistem sağlığınızı anlık olarak izlemeniz için tasarlanmış hafif bir araçtır.

    📊 Görsel Barlar: Bellek ve disk kullanımını % bazlı ilerleme çubuklarıyla görün.

    🎨 Akıllı Renkler: Sistem yüküne göre yeşil, sarı ve kırmızı renk kodlaması.

    ⚙️ Detaylı Donanım: CPU bilgisi, RAM, Swap ve ağ arayüzleri tek ekranda.

    ⏱️ Sistem Durumu: Uptime süresi ve aktif kullanıcı sayısı.

    📋 JSON Desteği: Scriptleriniz ve otomasyonlarınız için temiz çıktı desteği.

🚀 Kurulum (Repo Ayarları)

Botan-Info'yu kurmak için aşağıdaki sunuculardan birini seçebilir ya da en iyi deneyim için iki sunucuyu birden ekleyebilirsiniz.

    /etc/pacman.conf dosyasını düzenleyin:

Ini, TOML

[botan]
SigLevel = Optional TrustAll
# GitHub Mirror (Hızlı)
Server = https://raw.githubusercontent.com/Botan-linux/botan-repo/main/x86_64
# GitLab Mirror (Alternatif)
Server = https://gitlab.com/zeke000p/botan-repo/-/raw/main/x86_64

    Paketi kurun:

Bash

sudo pacman -Syy botan-info

🛠️ Kullanım Rehberi

Aracı ihtiyacınıza göre farklı modlarda çalıştırabilirsiniz:

    Tam Bilgi: botan-info

    Minimal Mod: botan-info -m

    JSON Çıktı: botan-info -j | jq .

    Renksiz Çıktı: botan-info --no-color > sistem.log

    Yardım: botan-info --help

🏗️ Geliştirme ve Katkı

    📢 Önemli Not: Bu araç Botan Linux ile geliştirilmiştir. Kodları çatallayıp (Fork) Arch Linux, CachyOS veya EndeavourOS sistemleriniz için optimize edebilirsiniz.

    Gelecek planlarımızda, paket depolarımızı (Botan-Repo) daha da güçlendirmek ve botan-info verilerini web dashboard'larına entegre etmek yer alıyor.

🤝 Ekibimize Katılın!

Botan Linux'un bir parçası olun! Geliştirici ekibine katılmak veya projeye destek olmak isterseniz Discord sunucumuza bekliyoruz:

👉 Botan Linux Discord Sunucusu
