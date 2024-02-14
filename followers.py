import pandas as pd

# JSON dosyanızın doğru yolundan emin olun
file_path = "followers_1.json"

# JSON verilerini okuyun
data = pd.read_json(file_path)

# "string_list_data"dan "value"yu ayıklayın (her öğe için bir giriş varsayarak)
values = [item[0]["value"] for item in data["string_list_data"]]

# "Followers" sütunlu DataFrame oluşturun
df = pd.DataFrame(values, columns=["Followers"])

# Excel dosyası olarak kaydedin (netlik için index=False'i göz önünde bulundurun)
df.to_excel("followers.xlsx", index=False)