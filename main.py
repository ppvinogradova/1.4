import csv

flats_list = list()

with open('output.csv', encoding='utf-8', newline='') as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv) 
#print (flats_list)

#TODO 1:ВЫПОЛНЕНО
new_flat = []
for flat in flats_list:
  if "новостройка" in flat: 
    print("Новостройка номер {}".format(flat[0]))
    new_flat.append(flat)
print(len(new_flat))

#TODO 2:
# 1) Сделайте описание квартиры в виде словаря, а не списка. Используйте следующие поля из файла output.csv: ID, Количество комнат;Новостройка/вторичка, Цена (руб). У вас должно получиться примерно так:
# 2) Измените код, который создавал словарь для поиска квартир по метро так, чтобы значением словаря был не список ID квартир, а список описаний квартир в виде словаря, который вы сделали в п.1 
subway_dict = {}
for flat in flats_list:
  flat_info = {"id":flat[0], "rooms":flat[1], "type":flat[2], "price":flat[11]}
  print(flat_info)
  subway = flat[3].replace("м.", "")
  if subway not in subway_dict.keys():
    subway_dict[subway] = list()
  subway_dict[subway].append(dict(flat_info.items()))
print(subway_dict)
# 3) Самостоятельно напишите код, который подсчитывает и выводит, сколько квартир нашлось у каждого метро.
for subways in subway_dict:
  print('У станции метро {}: {} квартир(а)'.format(subways, len(subway_dict[subways])))
  
