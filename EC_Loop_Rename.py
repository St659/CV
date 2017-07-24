from Meth_blue_06_09 import get_data_paths
import os
directory = 'E:\Google Drive\Cell Chamber Ref Test 02-12-16'

paths = get_data_paths(directory)


path = paths[0]


for path in paths:
    split_string = path.split('_')


    loop_string = split_string[-1]


    new_string = "".join(split_string)
    print(new_string)
    new_path = directory + "\\" + loop_string

    os.rename(path,new_path)