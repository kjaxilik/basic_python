import pandas as pd
import numpy as np
import os
import shutil
import mmap
import sys

#####################################################################################


path = os.getcwd()
# 'C:\\test'

path = 'C:\\Users\\lmv\\'
os.chdir(path)
os.getcwd()


#####################################################################################

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

#####################################################################################

path = 'C:\\test\\'
os.chdir(path)

directory = os.path.join(os.getcwd(), 'data')
create_dir_if_not_exist(directory)

#os.chdir(directory)

#####################################################################################

path1 = os.path.join(os.getcwd(), 'data1')
path2 = os.path.join(os.getcwd(), 'data2')
create_dir_if_not_exist(path1)
create_dir_if_not_exist(path2)


files = [x for x in os.listdir(os.getcwd()) ]
for i in range(len(files)):
    file = files[i]
    print(file, file[-3:])

# dirs = [x for x in os.listdir(path) if os.path.isdir(x)]
# files = [x for x in os.listdir(path) if os.path.isfile(x)]



files = [x for x in os.listdir(path) if x[-3:] == 'txt']
for i in range(len(files)):
    file = files[i]
    p = shutil.copy2(os.path.join(os.getcwd(), file), os.path.join(path2, file))

delete_dir(path1)
delete_dir(path2)


content = os.listdir(path=".")
print(content)

content = os.listdir(path="..")
print(content)



#####################################################################################


staff = pd.DataFrame({
    'ID':[1,2,3,4,5], 
    'ID_LEAD': [2,2,3,4,2],
    'ID_DEP': [1,1,3,4,1],
    'NAME': ['ИВАН', 'МАКСИМ', 'АЛЕКСАНДРА', 'МАРИЯ', 'АЛЕНА'],
    'SALARY': [94000.00, 138000.33, 192003.22, 57800, 200000],
})



staff.to_csv('staff1.csv', sep=';', encoding = 'cp1251')
staff.to_csv('staff0.csv', sep=';', encoding = 'utf-8')

with pd.ExcelWriter(os.path.join(path, 'staff.xlsx')) as writer:
    staff.to_excel(writer, sheet_name = 'first')

#####################################################################################


dbcsv1 = pd.read_csv('staff1.csv', encoding = 'cp1251', sep = ';')


dbcsv2 = pd.read_csv('staff2.csv', encoding = 'utf-8', sep = ';')


dbxlsx = pd.read_excel('staff.xlsx')



dbxlsx.fillna('',inplace=True)



c2 = 'SALARY'
c1 = 'ID_LEAD'
dbxlsx[c1] = dbxlsx[c1].apply(str)
dbxlsx['1'] = dbxlsx[c2].apply(lambda x: 'big' if int(x) > np.mean(dbxlsx[c2]) else 'small' )





#####################################################################################

my_f = open("Student.txt", "r", encoding = 'utf-8')
content = my_f.read()
print(len(content))
my_f.close()


my_f = open("Student.txt", "r", encoding = 'utf-8')
content = my_f.readline()
print(len(content))
my_f.close()


my_f = open("Student.txt", "r", encoding = 'utf-8')
content = my_f.readlines()
print(len(content))
my_f.close()


with open("test.txt", encoding = 'utf-8') as file:
    for line in file:
        print(line)


#####################################################################################



out_f = open("test2.txt", "w")
out_f.write("String string string")
out_f.close()


out_f = open("test3.txt", "w")
out_f.write("String string string\n")
out_f.write("String string string\n")
out_f.write("String string string\n")
out_f.close()

out_f = open("test4.txt", "w")
str_list = ['stroka_1\n', 'stroka_2\n', 'stroka_3\n']
out_f.writelines(str_list)
out_f.close()


with open("test5.txt", "w") as f_obj:
    print("Необычная работа функции print", file=f_obj)


#####################################################################################


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


#####################################################################################






os.rename("test5.txt", "test6.txt")
os.remove("test6.txt")


#####################################################################################

pth = os.path.join(os.getcwd(), 'test1.txt')
print(pth)
os.path.basename(pth)
os.path.dirname(pth)
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


def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines


def processing(s):
    s = s.lower()
    return s

def proc_file(file_path_from, file_path_to):
    N = get_num_lines(file_path_from) 
    with open(file_path_to, mode = 'w', encoding='UTF-8') as fileto:
        with open(file_path_from, encoding='UTF-8') as filefrom:
            for k in (range(N)):
                line = filefrom.readline()
                if line == '': break
                s = processing(line)
                if s != '': fileto.write(s)
    filefrom.close()
    fileto.close()
    
    

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



