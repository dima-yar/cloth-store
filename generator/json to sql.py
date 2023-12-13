import json
f = open(r'C:\Users\Артур\PycharmProjects\cloth-store\tempdata\styles.json')

data = json.load(f)

print(data)

f.close()
f = open(r"C:\temp\data.sql", 'w')
for i in data:
    id = i["id"]
    gender = i['gender']
    mastercategory = i["masterCategory"]
    subcategory = i["subCategory"]
    articleType = i["articleType"]
    baseColour = i["baseColour"]
    season = i["season"]
    year = i["year"]
    usage = i["usage"]
    productDisplayName = i["productDisplayName"]
    f.write(f'''\'\'INSERT INTO store_Products (id, gender, master_category, sub_category, article_type, base_color, season, year, usage, name, is_available) VALUES (\"{id}\", \"{gender}\", \"{mastercategory}\", \"{subcategory}\", \"{articleType}\", \"{baseColour}\", \"{season}\", {year}, \"{usage}\", \"{productDisplayName}\");\n''')

f.close()

