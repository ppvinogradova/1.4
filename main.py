import csv

flats_list = list()

with open('output.csv', encoding='utf-8', newline='') as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)

#можете посмотреть содержимое файла с квартирами через print, можете - на вкладке output.csv
#print (flats_list)


#TODO 1:
# 1) Напишите цикл, который проходит по всем квартирам, и показывает только новостройки
#и их порядковые номера в файле. Подсказка - вам нужно изменить этот код:
new_flat = []
for flat in flats_list:
  if "новостройка" in flat: 
    print("Новостройка номер {}".format(flat[0]))
    new_flat.append(flat)
print(len(new_flat))
# 2) добавьте в код подсчет количества новостроек


#TODO 2:
# 1) Сделайте описание квартиры в виде словаря, а не списка. Используйте следующие поля из файла output.csv: ID, Количество комнат;Новостройка/вторичка, Цена (руб). У вас должно получиться примерно так:
flat_info = {"id":flat[0], "rooms":flat[1], "type":flat[2], "price":flat[11]}
# 2) Измените код, который создавал словарь для поиска квартир по метро так, чтобы значением словаря был не список ID квартир, а список описаний квартир в виде словаря, который вы сделали в п.1 
subway_dict = {}
for flat in flats_list:
  subway = flat[3].replace("м.", "")
  if subway not in subway_dict.keys():
    subway_dict[subway] = list()
  subway_dict[subway].append(list(flat_info.items()))
print(subway_dict)

discription = subway_dict.values()
for one_subway in discription:
  subway_list = []
  subway_list.append(one_subway)
  print(len(subway_list[0]))
# 3) Самостоятельно напишите код, который подсчитывает и выводит, сколько квартир нашлось у каждого метро.