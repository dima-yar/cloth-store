import os

folder_path = r"C:/images"
list_of_files = os.listdir(folder_path)

print(list_of_files)
f = open(r"C:/Users/Артур/PycharmProjects/cloth-store/tempdata", 'w', encoding="utf-8")
for i in list_of_files:
    file_path = folder_path + '/' + i
    file_id = i[0:-4]
    f.write(f"INSERT INTO store_ProductImages (id, product_image) VALUES ({file_id}, lo_import('{str(file_path)}'));\n")

f.close()
