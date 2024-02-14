import pandas as pd

# Excel dosyalarını oku
followers_df = pd.read_excel("followers.xlsx")
following_df = pd.read_excel("following.xlsx")

# Takip ettiğiniz kişilerin listesini oluştur
followers_list = followers_df["Followers"].to_list()

# Takip ettiklerinizden takipçileri çıkar
non_followers = []
for following in following_df["Following"]:
    if following not in followers_list:
        non_followers.append(following)

# Sonuçları yazdır veya kaydet
for follower in non_followers:
    print(follower)

# Non-followers'ı Excel'e kaydet (isteğe bağlı)
non_followers_df = pd.DataFrame(non_followers, columns=["Non-Followers"])
non_followers_df.to_excel("non_followers.xlsx", index=False)