import pandas as pd

# JSON dosyasının yolunu değiştir:
dosya_yolu = "following.json"

# JSON dosyasını oku
data = pd.read_json(dosya_yolu)

# following değerlerini listeye at
following_values = []
for item in data["relationships_following"]:
    # Listeye dönüştürme yöntemi 1
    following_values.append(item["string_list_data"][0]["value"])

    # Doğrudan erişim yöntemi 2
    # following_values.append(item["string_list_data"][0]["value"])

# Listeyi ekrana yazdır
for value in following_values:
    print(value)

# Listeyi excel dosyasına yazdır
df = pd.DataFrame(following_values, columns=["Following"])
df.to_excel("following.xlsx", index=False)