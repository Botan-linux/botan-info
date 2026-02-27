# Bu paket Botan Linux resmi depoları için derlenmiştir
pkgname=botan-info
pkgver=2.0.0
pkgrel=1
pkgdesc="Botan Linux sistem bilgisi ve monitör aracı"
arch=('any')
url="https://github.com/Botan-linux/botan-info"
license=('MIT')
depends=('python')
optdepends=(
    'jq: JSON çıktısını formatlamak için'
)
conflicts=('neofetch' 'screenfetch')  # Botan-info bu araçların yerini alır
provides=('system-info')
# Botan Linux iç paket - yerel kaynak kullan
source=("botan-info.py")
sha256sums=('SKIP')

# Paket versiyonu Botan Linux sürümüyle uyumlu
# pkgver() {
#     cat /etc/botan-version 2>/dev/null || echo "2.0.0"
# }

package() {
    # Doğrudan build dizininden kurulum
    install -Dm755 "$srcdir/botan-info.py" "$pkgdir/usr/bin/botan-info"
    
    # LICENSE ve README yoksa oluştur (minimal paket için)
    if [ -f "$srcdir/LICENSE" ]; then
        install -Dm644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    else
        # MIT License placeholder
        install -Dm644 /dev/stdin "$pkgdir/usr/share/licenses/$pkgname/LICENSE" <<'EOF'
MIT License - Botan Linux
EOF
    fi
    
    if [ -f "$srcdir/README.md" ]; then
        install -Dm644 "$srcdir/README.md" "$pkgdir/usr/share/doc/$pkgname/README.md"
    fi
    
    # Botan Linux spesifik: /etc/botan/ altına yapılandırma
    install -dm755 "$pkgdir/etc/botan"
    
    # Man sayfası (basit)
    install -Dm644 /dev/stdin "$pkgdir/usr/share/man/man1/botan-info.1" <<'EOF'
.TH BOTAN-INFO 1 "2024" "Botan Linux" "User Commands"
.SH NAME
botan-info \- Botan Linux sistem bilgisi görüntüleyici
.SH SYNOPSIS
.B botan-info
[\fIOPTIONS\fR]
.SH DESCRIPTION
Gelişmiş terminal tabanlı sistem monitörü.
.SH OPTIONS
.TP
.BR \-m ", " \-\-minimal
Minimal gösterim
.TP
.BR \-j ", " \-\-json
JSON formatında çıktı
.TP
.BR \-\-no\-color
Renksiz çıktı
.SH AUTHOR
Botan Linux Team
EOF
}
