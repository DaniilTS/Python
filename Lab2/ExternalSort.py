import tempfile
import os
from Sort import Sorting


class Exort(object):
    __temp_arr = []
    __file_names = []
    __num_of_lines = 10000
    __counter = 1

    def __read_file(self, file):
        with open(file, 'r') as n_file:
            for line in n_file:
                self.__temp_arr.append(int(line))
                self.__counter += 1
                if self.__counter > self.__num_of_lines:
                    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp:
                        list = Sorting.merge_sort(self.__temp_arr)
                        temp.writelines(f'{i}\n' for i in list)
                        self.__file_names.append(temp)

                    self.__temp_arr.clear()
                    self.__counter = 1

    def sort(self, file_name):
        self.__read_file(file_name)
        self.__sort_files()
        self.__res_file()

    def __sort_files(self):
        while len(self.__file_names) > 1:
            with open(self.__file_names[0].name, 'r') as first_file, open(self.__file_names[1].name,
                                                                          'r') as second_file:
                with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp:
                    self.__sort_lines(temp, [first_file, second_file])
                    self.__file_names.append(temp)
            self.__del_files(first_file)
            self.__del_files(second_file)

    def __sort_lines(self, temp, files):
        first_line = files[0].readlines()
        second_line = files[1].readlines()
        while first_line and second_line:
            if int(first_line) > int(second_line):
                temp.writelines(second_line)
                second_line = files.readline()
            else:
                temp.writelines(first_line)
                first_line = files[0].readlines()
        if first_line:
            self.__cont_fill(temp, files[0],first_line)
        else:
            self.__cont_fill(temp, files[1], second_line)

    def __cont_fill(self, temp, file, line):
        while line:
            temp.writelines(f'{line}')
            line = file.readline()

    def __res_file(self):
        temp = self.__file_names[0]
        with open('res_file.txt', 'w') as res_file, open(temp.name, 'r') as temp_file:
            for i in temp_file:
                res_file.writelines(i)
        self.__del_files(temp)

    def __del_files(self, file):
        if os.path.exists(file.name):
            self.__file_names.pop(0)
            os.remove(file.name)
