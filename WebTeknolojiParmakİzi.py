import requests
import re
import json
from typing import Dict, List, Optional
from bs4 import BeautifulSoup
from urllib.parse import urlparse

#Bu sınıf analiz yapılacak bir web sitesinin URL'sini alır ve gerekli analiz sonuçlarını saklamak için bazı değişkenleri başlatır
class WebTechFingerprinter:
    def __init__(self, url: str):
        self.url = url
        self.headers = {}
        self.technologies = {}
        self.potential_vulnerabilities = []

#Analiz sürecini başlatır ve üç temel adımda gerçekleştirir
    def analyze(self) -> Dict:
        self._fetch_headers()
        self._detect_technologies()
        self._evaluate_security()
        return self.generate_report()

#HTTP GET İSTEĞİ GÖNDERİR VE HTTP BAŞLIKLARINI ÇEKER
    def _fetch_headers(self):
        try:
            response = requests.get(self.url, 
                headers={'User-Agent': 'WebTechFingerprinter/1.0'},
                timeout=10)
            self.headers = dict(response.headers)
            self.content = response.text
        except requests.RequestException as e:
            print(f"Bağlantı hatası: {e}")

#WEB Sitesinde Kullanılan WEB Teknolojilerini Analiz Eder
    def _detect_technologies(self):
        # JavaScript kütüphane tespiti
        js_libs = {
            'jQuery': r'jquery(?:\.min)?\.js',
            'React': r'react(?:\.production\.min)?\.js',
            'Angular': r'angular(?:\.min)?\.js',
            'Vue': r'vue(?:\.runtime\.min)?\.js'
        }
        for lib, pattern in js_libs.items():
            if re.search(pattern, self.content):
                self.technologies[lib] = True

        # CMS ve Framework tespiti
        cms_patterns = {
            'WordPress': r'wp-content',
            'Drupal': r'drupal\.js',
            'Joomla': r'joomla',
            'Django': r'Django/\d+\.\d+',
            'Laravel': r'Laravel'
        }

        for cms, pattern in cms_patterns.items():
            if re.search(pattern, self.content, re.IGNORECASE):
                self.technologies[cms] = True

        # Server ve teknoloji tespiti
        server_tech = self.headers.get('Server', '')
        tech_mappings = {
            'Apache': 'Apache Web Server',
            'Nginx': 'Nginx Web Server',
            'PHP': 'PHP',
            'ASP.NET': 'Microsoft ASP.NET'
        }

        for key, value in tech_mappings.items():
            if key in server_tech:
                self.technologies[value] = True
#WEB sitesinde olası güvenlik açıklarının tespitini yapar
    def _evaluate_security(self):
        security_checks = [
            ('X-XSS-Protection', 'Header eksik: XSS koruması önerilir'),
            ('X-Frame-Options', 'Header eksik: Clickjacking riski'),
            ('Content-Security-Policy', 'Header eksik: İçerik güvenliği zayıf')
        ]

        for header, warning in security_checks:
            if header not in self.headers:
                self.potential_vulnerabilities.append(warning)

        # Açık teknolojiler için bilinen zaafiyetler
        vulnerable_techs = {
            'WordPress': 'Bilinen WordPress güvenlik açıkları mevcut',
            'Joomla': 'Kritik Joomla güvenlik açıkları tespit edildi'
        }

        for tech in self.technologies:
            if tech in vulnerable_techs:
                self.potential_vulnerabilities.append(vulnerable_techs[tech])

#Analiz Raporu Oluşturma
    def generate_report(self) -> Dict:
        return {
            'url': self.url,
            'detected_technologies': self.technologies,
            'potential_vulnerabilities': self.potential_vulnerabilities,
            'headers': self.headers
        }

#Kullanıcıdan web url girişi istenir ve analiz metodunu çalıştırır
#Sonuçları jSON Formatında yazdırır

def main():
    url = input("Analiz edilecek web sitesi URL'sini girin: ")
    fingerprinter = WebTechFingerprinter(url)
    report = fingerprinter.analyze()
    
    print(json.dumps(report, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()