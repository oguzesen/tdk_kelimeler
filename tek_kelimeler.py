import requests
import json
import re
url = "https://sozluk.gov.tr/autocomplete.json"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0) Firefox/131.0"}
response = requests.get(url, headers=headers)
unique_words = set()
if response.status_code == 200:
    data = response.json()
    dosya = "tek_kelimeler.txt"
    unique_words = set()
    with open(dosya, "w", encoding="utf-8") as f:
        for item in data:
            madde = item["madde"]
            if len(madde)==0: # içerik yoksa pas geç
                continue
            """
            # Şapkalı harfleri şapkasıza çevirme...
            madde = madde.replace("â", "a").replace("î", "ı").replace("û", "u")
            madde = madde.replace("Â", "A").replace("Î", "I").replace("Û", "U")

            # Tüm harfleri küçük harflere çevirme
            madde = madde.replace("İ","i").replace("I","ı").replace("Ş","ş").replace("Ğ","ğ").replace("Ü","ü").replace("Ö","ö").replace("Ç","ç")
            madde = madde.lower()
            """
            if madde not in unique_words:
	            if re.match(r'^[a-zA-ZçÇğĞıİöÖşŞüÜâÂîÎûÛ":]+$', madde):	            													
	                f.write(madde + "\n")  # Dosyaya yaz
	                unique_words.add(madde)  # Kelimeyi sete ekle

    print(f"TDK'da yer alan -tek- kelimeler ({len(unique_words)} adet) {dosya} dosyasına kaydedildi.")
else:
    print(f"İstek başarısız oldu. Durum kodu: {response.status_code}")
