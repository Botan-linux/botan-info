#!/usr/bin/env python3
"""
Botan Linux Sistem Bilgisi Aracı
Gelişmiş sistem monitörü ve bilgi görüntüleyici
"""

import os
import sys
import platform
import json
import argparse
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

# Renk kodları
class Colors:
    GREEN = "\033[1;32m"    # Botan Yeşili
    CYAN = "\033[1;36m"     # Açık Mavi
    YELLOW = "\033[1;33m"   # Sarı
    RED = "\033[1;31m"      # Kırmızı
    MAGENTA = "\033[1;35m"  # Mor
    WHITE = "\033[1;37m"    # Beyaz
    DIM = "\033[2m"         # Soluk
    RESET = "\033[0m"       # Sıfırla

    @classmethod
    def disable(cls):
        """Renkleri devre dışı bırak (pipe/redirect için)"""
        for attr in dir(cls):
            if not attr.startswith('_'):
                setattr(cls, attr, '')

class BotanInfo:
    def __init__(self, no_color=False):
        if no_color or not sys.stdout.isatty():
            Colors.disable()
        self.C = Colors
    
    def _read_file(self, path, default="N/A"):
        """Güvenli dosya okuyucu"""
        try:
            with open(path, "r") as f:
                return f.read().strip()
        except (FileNotFoundError, PermissionError):
            return default
    
    def _run_cmd(self, cmd, default="N/A"):
        """Komut çalıştırıcı"""
        try:
            return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL).strip()
        except subprocess.CalledProcessError:
            return default
    
    def get_load(self):
        """Sistem yükü"""
        load = self._read_file("/proc/loadavg", "0.00 0.00 0.00").split()[:3]
        return {
            "1min": float(load[0]),
            "5min": float(load[1]),
            "15min": float(load[2])
        }
    
    def get_memory(self):
        """Detaylı bellek bilgisi"""
        meminfo = self._read_file("/proc/meminfo", "")
        if not meminfo:
            return {}
        
        mem = {}
        for line in meminfo.split('\n')[:5]:
            if ':' in line:
                key, value = line.split(':')
                mem[key.strip()] = int(value.split()[0]) // 1024  # MB'a çevir
        
        total = mem.get('MemTotal', 0)
        available = mem.get('MemAvailable', mem.get('MemFree', 0))
        used = total - available
        
        return {
            "total": total,
            "used": used,
            "available": available,
            "percent": round((used / total * 100), 1) if total else 0
        }
    
    def get_swap(self):
        """Swap bilgisi"""
        meminfo = self._read_file("/proc/meminfo", "")
        swap_total = 0
        swap_free = 0
        
        for line in meminfo.split('\n'):
            if line.startswith('SwapTotal:'):
                swap_total = int(line.split()[1]) // 1024
            elif line.startswith('SwapFree:'):
                swap_free = int(line.split()[1]) // 1024
        
        used = swap_total - swap_free
        return {
            "total": swap_total,
            "used": used,
            "percent": round((used / swap_total * 100), 1) if swap_total else 0
        }
    
    def get_cpu_info(self):
        """CPU bilgisi"""
        cpuinfo = self._read_file("/proc/cpuinfo", "")
        model = "Unknown"
        cores = 0
        
        for line in cpuinfo.split('\n'):
            if 'model name' in line and model == "Unknown":
                model = line.split(':')[1].strip()
            if line.startswith('processor'):
                cores += 1
        
        # Kısaltma
        model = model.replace('Intel(R) Core(TM)', 'Intel Core')
        model = model.replace('AMD', self.C.CYAN + 'AMD' + self.C.RESET)
        model = model.replace('Intel', self.C.CYAN + 'Intel' + self.C.RESET)
        
        return {"model": model, "cores": cores or os.cpu_count()}
    
    def get_disk_usage(self):
        """Disk kullanımı"""
        try:
            stat = os.statvfs('/')
            total = (stat.f_blocks * stat.f_frsize) // (1024**3)  # GB
            free = (stat.f_bavail * stat.f_frsize) // (1024**3)
            used = total - free
            percent = round((used / total * 100), 1) if total else 0
            return {"total": total, "used": used, "free": free, "percent": percent}
        except Exception:
            return {}
    
    def get_uptime(self):
        """Sistem çalışma süresi"""
        uptime_sec = float(self._read_file("/proc/uptime", "0 0").split()[0])
        return str(timedelta(seconds=int(uptime_sec)))
    
    def get_hostname(self):
        """Hostname"""
        return platform.node()
    
    def get_network(self):
        """Ağ arayüzleri (basit)"""
        try:
            with open("/proc/net/dev", "r") as f:
                lines = f.readlines()[2:]  # Header'ları atla
            
            interfaces = []
            for line in lines:
                if ':' in line:
                    iface = line.split(':')[0].strip()
                    if iface != 'lo':  # Loopback hariç
                        interfaces.append(iface)
            return interfaces[:3]  # İlk 3 arayüz
        except Exception:
            return []
    
    def get_users(self):
        """Aktif kullanıcılar"""
        try:
            who = subprocess.check_output("who | wc -l", shell=True, text=True).strip()
            return int(who)
        except Exception:
            return 0
    
    def _color_percent(self, percent):
        """Yüzdeye göre renk seç"""
        if percent < 50:
            return self.C.GREEN
        elif percent < 80:
            return self.C.YELLOW
        else:
            return self.C.RED
    
    def display(self, minimal=False):
        """Ekrana yazdır"""
        C = self.C
        
        # Header
        print(f"\n{C.GREEN}🌿 Botan Linux Sistem Bilgisi{C.RESET}")
        print(f"{C.DIM}{'─' * 50}{C.RESET}")
        
        # Temel Bilgiler
        print(f"{C.GREEN}Hostname:{C.RESET}  {self.get_hostname()}")
        print(f"{C.GREEN}OS:{C.RESET}        {platform.system()} {platform.release()} ({platform.machine()})")
        print(f"{C.GREEN}Uptime:{C.RESET}    {self.get_uptime()}")
        print(f"{C.GREEN}Users:{C.RESET}     {self.get_users()} aktif")
        
        if not minimal:
            # CPU
            cpu = self.get_cpu_info()
            print(f"\n{C.CYAN}⚙️  İşlemci{C.RESET}")
            print(f"   {cpu['model']}")
            print(f"   Çekirdek: {cpu['cores']}")
            
            # Bellek
            mem = self.get_memory()
            if mem:
                mem_color = self._color_percent(mem['percent'])
                bar = self._make_bar(mem['percent'])
                print(f"\n{C.CYAN}💾 Bellek{C.RESET}")
                print(f"   Toplam: {mem['total']} MB | Kullanılan: {mem['used']} MB")
                print(f"   [{mem_color}{bar}{C.RESET}] {mem['percent']}%")
            
            # Swap
            swap = self.get_swap()
            if swap['total'] > 0:
                swap_color = self._color_percent(swap['percent'])
                print(f"\n{C.CYAN}💿 Swap{C.RESET}")
                print(f"   Kullanım: {swap['used']}/{swap['total']} MB ({swap_color}{swap['percent']}%{C.RESET})")
            
            # Disk
            disk = self.get_disk_usage()
            if disk:
                disk_color = self._color_percent(disk['percent'])
                bar = self._make_bar(disk['percent'])
                print(f"\n{C.CYAN}💽 Disk (/) {C.RESET}")
                print(f"   Toplam: {disk['total']} GB | Boş: {disk['free']} GB")
                print(f"   [{disk_color}{bar}{C.RESET}] {disk['percent']}%")
        
        # Yük (Her zaman göster)
        load = self.get_load()
        load_avg = (load['1min'] + load['5min'] + load['15min']) / 3
        load_color = C.GREEN if load_avg < 1 else C.YELLOW if load_avg < 2 else C.RED
        
        print(f"\n{C.CYAN}📊 Sistem Yükü{C.RESET}")
        print(f"   1dk:  {load_color}{load['1min']}{C.RESET}")
        print(f"   5dk:  {load_color}{load['5min']}{C.RESET}")
        print(f"   15dk: {load_color}{load['15min']}{C.RESET}")
        
        if not minimal:
            # Ağ
            net = self.get_network()
            if net:
                print(f"\n{C.CYAN}🌐 Ağ Arayüzleri{C.RESET}")
                print(f"   {', '.join(net)}")
        
        print(f"{C.DIM}{'─' * 50}{C.RESET}")
        print(f"{C.DIM}Botan v2.0 | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{C.RESET}\n")
    
    def _make_bar(self, percent, width=20):
        """İlerleme çubuğu oluştur"""
        filled = int(width * percent / 100)
        return '█' * filled + '░' * (width - filled)
    
    def to_json(self):
        """JSON formatında döndür"""
        return json.dumps({
            "hostname": self.get_hostname(),
            "platform": {
                "system": platform.system(),
                "release": platform.release(),
                "machine": platform.machine()
            },
            "uptime": self.get_uptime(),
            "cpu": self.get_cpu_info(),
            "memory": self.get_memory(),
            "swap": self.get_swap(),
            "disk": self.get_disk_usage(),
            "load": self.get_load(),
            "timestamp": datetime.now().isoformat()
        }, indent=2, ensure_ascii=False)

def check_linux():
    """Linux kontrolü"""
    if platform.system() != "Linux":
        print("❌ Bu araç sadece Linux sistemlerde çalışır!")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="🌿 Botan Linux Sistem Bilgisi Aracı",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Örnekler:
  %(prog)s              # Tam bilgi göster
  %(prog)s -m           # Minimal mod (sadece temel bilgiler)
  %(prog)s -j           # JSON çıktı
  %(prog)s --no-color   # Renksiz çıktı (pipe için)
        """
    )
    parser.add_argument("-m", "--minimal", action="store_true", help="Minimal gösterim")
    parser.add_argument("-j", "--json", action="store_true", help="JSON formatında çıktı")
    parser.add_argument("--no-color", action="store_true", help="Renkleri kapat")
    
    args = parser.parse_args()
    
    check_linux()
    
    botan = BotanInfo(no_color=args.no_color)
    
    if args.json:
        print(botan.to_json())
    else:
        botan.display(minimal=args.minimal)

if __name__ == "__main__":
    main()
