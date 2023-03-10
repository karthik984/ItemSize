import os, sys

def get_directory_size(path):
    total_size = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total_size += entry.stat().st_size
            elif entry.is_dir():
                total_size += get_directory_size(entry.path)
    return total_size

#directory_path = input("path:")
#if directory_path == '':

directory_path = os.getcwd() 

if not os.path.exists(directory_path):
    print("need a valid path to calclulate get the size")
    sys.exit()

file_name = 'item_size.txt'

if os.path.exists(file_name):
    os.remove(file_name)

f = open('item_size.txt', 'w')
type = ''
with os.scandir(directory_path) as it:
        for entry in it:
            size = 0
            if entry.is_file():
                size += entry.stat().st_size
                type = '(f)'
            elif entry.is_dir():
                size = get_directory_size(entry.path)
                type = '(D)'
            to_print = str((f"{type}{entry.name} =====> {size/(1000000 * 1073.74): .4f} GB || {size/1000000: .4f} MB || {size} bytes"))
            f.write(to_print)
            f.write('\n')

f.close()