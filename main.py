import re
from pprint import pprint
import csv
def get_fullname_list(contacts_list):
  last_name = []
  full_name = []
  for i in range(1,len(contacts_list)):
        if contacts_list[i][0] != '' and contacts_list[i][1] != '' and contacts_list[i][2] != '':
          if contacts_list[i][0] not in last_name:
            last_name += [contacts_list[i][0]]
            full_name += [contacts_list[i][0],contacts_list[i][1],contacts_list[i][2]]
        elif contacts_list[i][0] != '' and contacts_list[i][1] != '':
          if contacts_list[i][0] not in last_name:
            full_name += [(f'{contacts_list[i][0]} {contacts_list[i][1]}').split()]
            last_name += [contacts_list[i][0]]
        elif contacts_list[i][0] != '':
          if contacts_list[i][0].split()[0] not in last_name:
            full_name += [contacts_list[i][0].split()]
            last_name += [contacts_list[i][0].split()[0]]
  return full_name

def get_list(contacts_list):
  phone_list = []
  fullname_list = get_fullname_list(contacts_list)
  fullname_list.insert(0,['lastname','firstname','surname','organization','position','phone','email'])
  for fullname in fullname_list:
    for i in range(1, len(contacts_list)):
      if fullname[0] in contacts_list[i][0]:
        if contacts_list[i][3] != '':
          fullname.append(contacts_list[i][3])
        if contacts_list[i][4] != '':
          fullname.append(contacts_list[i][4])
        if contacts_list[i][5] != '':
          fullname.append(format_phone(contacts_list[i][5]))
        if contacts_list[i][6] != '':
          fullname.append(contacts_list[i][6])
  phone_list += fullname_list
  return phone_list

def format_phone(number_phone):
  pattern1 = r"((\+7|8)495(\d{3})(\d{2})(\d{2}))|((\+7|8)?\s*(\((\d+)\)|)\s*(\d+)[-\s](\d+)[-\s](\d{2})(\d{2}))|((\+7|8)?\s*(\((\d+)\)|)\s*(\d+)[-\s](\d+)[-\s](\d+))"
  pattern2 = r"\(*доб.+((\d{4}))\)*"
  sub_text1 = r"+7(495)\18\11\3-\19\4\12-\20\5\13"
  sub_text2 = r'доб.\2'
  res = re.sub(pattern1, sub_text1, number_phone)
  number_phone = re.sub(pattern2, sub_text2, res)
  return number_phone

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# TODO 1: выполните пункты 1-3 ДЗ
contacts_list = get_list(contacts_list)
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)