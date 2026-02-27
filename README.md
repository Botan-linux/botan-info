🌿 Botan-Info
📊 Sistem Bilgisi

Botan Linux için hafif ve estetik sistem monitörü. Sistemin nabzını tutan bir yaprak.
🚀 Kurulum

/etc/pacman.conf dosyasının sonuna aşağıdakileri ekleyin:

[botan]
SigLevel = Optional TrustAll
Server = https://raw.githubusercontent.com/Botan-linux/botan-repo/main/x86_64
Server = https://gitlab.com/zeke000p/botan-repo/-/raw/main/x86_64
🛠️ Kullanım

Terminal üzerinden şu komutları kullanabilirsiniz:

    botan-info : Görsel sistem özeti.

    botan-info -m : Minimal mod.

    botan-info -j : JSON veri çıktısı.

✨ Öne Çıkanlar

    Görsel Güç: CPU, RAM ve Disk için dinamik barlar.

    Saf Performans: Python tabanlı düşük kaynak tüketimi.

    Geniş Uyumluluk: Arch, CachyOS ve EndeavourOS desteği.

🤝 İletişim & Destek

    Discord: https://discord.gg/zB4NYTFj

    Web: https://botan-linux.github.io/Botan-sprout/
