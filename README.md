# Web Teknoloji Parmak İzi Çıkarma Aracı

Web uygulamalarında kullanılan teknolojileri tespit eden, sürüm bilgilerini çıkaran ve olası güvenlik açıklarını belirleyen Python tabanlı bir analiz aracı.

Temel Bilgiler

-Proje Adı: Web Teknoloji Parmak İzi

-Öğrenci Adı ve Numarası: 2320191022 Samethan Kül

-Teslim Tarihi: 30.01.2025

## 🚀 Özellikler

- HTTP header detaylı analizi
- JavaScript kütüphane tespiti
- CMS ve framework sürüm tespiti
- Teknoloji stack güvenlik değerlendirmesi
- Detaylı JSON formatında raporlama

## 📋 Gereksinimler

- Python 3.7+
- pip (Python paket yöneticisi)
- İnternet bağlantısı

## 🛠 Kurulum

1. Repoyu klonlayın:
```bash
git clone (https://github.com/samethankull/Web-Teknoloji-Parmak-zi.git)
cd Web-Teknoloji-Parmak-zi.git
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## 📦 Gerekli Paketler

```
requests>=2.28.0
beautifulsoup4>=4.9.0
```

## 💻 Kullanım

### Basit Kullanım

```bash
python fingerprinter.py
```

### Kod İçinde Kullanım

```python
from web_tech_fingerprinter import WebTechFingerprinter

fingerprinter = WebTechFingerprinter("https://example.com")
report = fingerprinter.analyze()
print(report)
```

### Örnek Çıktı

```json
{
  "url": "https://example.com",
  "detected_technologies": {
    "jQuery": true,
    "WordPress": true
  },
  "potential_vulnerabilities": [
    "Header eksik: XSS koruması önerilir"
  ],
  "headers": {
    "Server": "Apache/2.4.41",
    "Content-Type": "text/html"
  }
}
```

## ⚙️ Konfigürasyon

### Zorunlu Parametreler

| Parametre | Açıklama | Örnek |
|-----------|----------|--------|
| url | Analiz edilecek web sitesinin URL'i | https://example.com |

### Opsiyonel Parametreler

| Parametre | Varsayılan Değer | Açıklama |
|-----------|------------------|-----------|
| timeout | 10 | İstek zaman aşımı süresi (saniye) |
| user_agent | WebTechFingerprinter/1.0 | Özel User-Agent tanımı |

## 🔍 Tespit Edilen Teknolojiler

- JavaScript Kütüphaneleri:
  - jQuery
  - React
  - Angular
  - Vue
- CMS Sistemleri:
  - WordPress
  - Drupal
  - Joomla
- Web Sunucuları:
  - Apache
  - Nginx
- Frameworkler:
  - Django
  - Laravel

## 🐛 Hata Ayıklama

Sık karşılaşılan hatalar ve çözümleri:

1. Bağlantı Hataları
   - URL formatını kontrol edin
   - İnternet bağlantınızı kontrol edin
   - Timeout süresini artırın

2. ModuleNotFoundError
   - Paketlerin yüklü olduğundan emin olun
   - Virtual environment'ın aktif olduğunu kontrol edin

## ⚠️ Güvenlik Notları

- Kullanım öncesi gerekli yasal izinleri alın
- Agresif taramalardan kaçının
- Rate limiting kullanın


## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'feat: Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

