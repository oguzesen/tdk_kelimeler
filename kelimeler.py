import requests
import json
# URL ve istek başlıkları
url = "https://sozluk.gov.tr/autocomplete.json"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0) Firefox/131.0"}
# İstek gönder
response = requests.get(url, headers=headers)

# Daha önce eklenmiş kelimeleri saklamak için bir set oluştur
unique_words = set()

# Yanıtın başarılı olup olmadığını kontrol et
if response.status_code == 200:
    # gelen JSON verisini çöz
    data = response.json()
    dosya = "kelimeler.txt"
    unique_words = set()

    # Dosyaya yazmak için aç
    with open(dosya, "w", encoding="utf-8") as f:
        for item in data:
            madde = item["madde"]
            if madde not in unique_words: # Mükerrer kelimeleri atla
	            unique_words.add(madde)  # Kelimeyi kümeye ekle
	            f.write(madde + "\n")  # Dosyaya yaz
    print(f"TDK sözlükteki {len(unique_words)} adet kelime {dosya} dosyasına kaydedildi.")
else:
    print(f"İstek başarısız oldu. Durum kodu: {response.status_code}")
