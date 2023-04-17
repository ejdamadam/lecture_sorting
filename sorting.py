import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """

    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as soubor:
        data = csv.DictReader(soubor)
        slovnik = {}
        for row in data:
            for hlavicka, hodnota in row.items():
                if hlavicka not in slovnik:
                    slovnik[hlavicka] = [int(hodnota)]
                else:
                    slovnik[hlavicka].append(int(hodnota))
    return slovnik


def selection_sort(num_list, direction="vzestupne"):
    sorted_list = []
    while num_list:
        d = len(num_list)
        x = num_list[0]
        i = 1
        if direction == "vzestupne":
            while i < d:
                if num_list[i] < x:
                    x = num_list[i]
                i += 1
        elif direction == "sestupne":
            while i < d:
                if num_list[i] > x:
                    x = num_list[i]
                i += 1
        sorted_list.append(x)
        num_list.remove(x)
    return sorted_list


print(selection_sort(read_data("numbers.csv")["series_1"], "vzestupne"))



def main():
    pass


if __name__ == '__main__':
    main()
