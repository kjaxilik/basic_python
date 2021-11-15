# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 17:45:52 2021

@author: KaiJax
"""

import pandas as pd
import numpy as np
import os
import shutil
import mmap
import sys

###############################################################################

# для выбора текущей директории в path
path = os.getcwd()
# 'C:\\test'
print(path)

# чтобы изменить текущую рабочую директорию 
os.chdir('adress directorii')

###############################################################################

def create_dir_if_not_exist(directory):
   try:
       os.mkdir(directory)
   except:
       pass

def delete_dir(directory):
    try:
        shutil.rmtree(directory, ignore_errors = True)
    except:
        pass

###############################################################################


path = 'C:\\test\\'
os.chdir(path)

directory = os.path.join(os.getcwd(), 'data')
create_dir_if_not_exist(directory)

os.chdir(path)


path1 = os.path.join(os.getcwd(), 'data1')
path2 = os.path.join(os.getcwd(), 'data2')
create_dir_if_not_exist(path1)
create_dir_if_not_exist(path2)

# копировать все эелементы в лист (только названия с расширением)
files = [x for x in os.listdir(os.getcwd())]

# копировать только файлы без директорий
files = [x for x in os.listdir(path) if os.path.isfile(x)]
dirs = [x for x in os.listdir(path) if os.path.isdir(x)]



# копировать только txt файлы
files = [x for x in os.listdir(path) if x[-3:] == 'txt']
for i in range(len(files)):
    file = files[i]
    _ = shutil.copy2(os.path.join(os.getcwd(), file), os.path.join(path2, file))


delete_dir(path1)
delete_dir(path2)

# вывод файлов в текущей папке
content = os.listdir(path=".")
print(content)

# вывод файлов в родительской папке
content = os.listdir(path="..")
print(content)


staff = pd.DataFrame({
    'ID':[1,2,3,4,5],
     'ID_LEAD':[2,2,3,4,2],
     'ID_DEP': [1,1,3,4,1],
     'NAME': ['ИВАН','МАКСИМ','АЛЕКСАНДРА','МАРИЯ','ЕЛЕНА'],
     'SALARY': [94000.00,138000.33,192003.22,57800,200000]
})

# записать csv файл
staff.to_csv('staff0.csv', sep=';', encoding='cp1251')
staff.to_csv('staff1.csv', sep=';', encoding='utf-8')
staff.to_csv('staff2.csv', sep=';')



# записать Excel файл
with pd.ExcelWriter(os.path.join(path, 'staff.xlsx')) as writer:
    staff.to_excel(writer, sheet_name='first')

# чтение файлов
dbcsv1 = pd.read_csv('staff0.csv', encoding='cp1251', sep=';')

dbcsv2 = pd.read_csv('staff1.csv', encoding='utf-8', sep=';')

dbxlsx = pd.read_excel('staff.xlsx')

# заполнить nan на 0
dbxlsx.fillna('0',inplace=True)


c2 = 'SALARY'
c1 = 'ID_LEAD'
dbxlsx[c1] = dbxlsx[c1].apply(str)
dbxlsx['1'] = dbxlsx[c2].apply(lambda x: 'big' if int(x) > np.mean(dbxlsx[c2]) else 'small')

dbxlsx.to_csv('staff3.csv', sep=';', encoding='cp1251')


############################################################################################

# открыть полностью файл
my_f = open("Student.txt", "r", encoding='utf-8')
content = my_f.read()
print(len(content))
my_f.close()


# открыть файл только первой строки, если файл очень большой
my_f = open("Student.txt", "r", encoding='utf-8')
content = my_f.readline()
print(len(content))
my_f.close()


# открыть файл по строчно, если файл очень большой
my_f = open("Student.txt", "r", encoding='utf-8')
content = my_f.readlines()
print(len(content))
my_f.close()

v = []
with open("test.txt", encoding='utf-8') as file:
    for line in file:
        v.append(line)



##########################################################################################
# запись в файл
out_f = open("test2.txt", "w")
out_f.write("String string string")
out_f.close()


out_f = open("test3.txt", "w")
out_f.write("String string string\n")
out_f.write("String string string\n")
out_f.write("String string string\n")
out_f.close()

out_f = open("test4.txt", "w")
str_list = ['stroke_1\n', 'stroka_2\n', 'stroka_3\n']
out_f.writelines(str_list)
out_f.close()


# запись в файл через print
with open("test5.txt", "w") as f_obj:
    print("Необычная работа функции print", file=f_obj)


##########################################################################################

"""
Режим 	Описание
r	Открыть файл на чтение (режим по умолчанию)
w	Открыть на запись. При этом удалить содержимое файла. Если файла нет, создать новый.
x	Открыть файл на запись, если его нет. Если файл есть, он не будет создан.
a	Открыть файл на дозапись. Добавить информацию в конец файла.
b	Открыть файл в двоичном формате.
t	Открыть файл в текстовом формате (режим по умолчанию)
+	Открыть файл на чтение и запись
"""

##########################################################################################

# переименовывание и удаление файла

os.rename("test4.txt", "text4.txt")
os.remove("text4.txt")


##########################################################################################


pth = os.path.join(os.getcwd(), 'data', 'test1.txt')
print(pth)




# название файла
os.path.basename(pth)

# название папки
os.path.dirname(pth)

# проверка есть ли файл или нет
os.path.exists(pth)



#os.path.isdir()
#os.path.isfile()
#os.path.split()



dirs = [x for x in os.listdir(path) if os.path.isdir(x)]
files = [x for x in os.listdir(path) if os.path.isfile(x)]

print(os.path.split(pth))


#####################################################################################



print(sys.executable)
print(sys.path)
print(sys.platform)

#####################################################################################

# чтение только необходимых столбцов из файла в excel
def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines

# извенить в нижний регистр
def processing(s):
    s = s.lower()
    return s

def sokr_stolb(t):
    t = ';'.join(t.split(';')[:3])
    return t

file_path_from = 'staff3.csv'
file_path_to = 'staff4,.csv'

# функция записывает первые 3 столбца из файла1 в файл2
def proc_file(file_path_from, file_path_to):
    N = get_num_lines(file_path_from) 
    with open(file_path_to, mode = 'w', encoding='UTF-8') as fileto:
        with open(file_path_from, encoding='UTF-8') as filefrom:
            for k in (range(N)):
                line = filefrom.readline()
                # if line == '': break
                s = processing(line)
                #if s != '': fileto.write(s)
                fileto.write(s+'\n')
    filefrom.close()
    fileto.close()
    
proc_file(file_path_from, file_path_to)

# если файлов несколько то переюираем их
files = [x for x in os.listdir(os.getwcs())]
for i in range(len(files)):
    file = files[i]
    proc_file(file, file_path_to)


def proc_file2(file_path_from, foldername_to, filename):
    N = get_num_lines(file_path_from) 
    with open(file_path_from, encoding='UTF-8') as filefrom:
        for k in (range(N)):
            line = filefrom.readline()
            if line == '': break
            s = line.replace('\n','').split(';')
            if len(s) > 3:
                file_path_to = os.path.join(foldername_to, filename+'_'+s[-1]+'.csv')
                with open(file_path_to, mode = 'a', encoding='UTF-8') as fileto:
                    fileto.write(line)
                fileto.close()
    filefrom.close()



#####################################################################################





data = pd.read_csv( 'Student.csv', sep=';', encoding = 'utf-8')
data.fillna('',inplace=True)








    