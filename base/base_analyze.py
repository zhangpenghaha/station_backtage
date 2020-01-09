import os

import yaml


def analyze_file(file_name, key):

    with open(".%sdata%s%s" % (os.sep, os.sep, file_name), "r",encoding="utf-8") as f:
        case_data = yaml.load(f)[key]

        data_list = list()
        for i in case_data.values():
            data_list.append(i)
        print(data_list)
        return data_list

def mysql_file(file_name, key):

    with open("..%sdata%s%s" % (os.sep, os.sep, file_name), "r",encoding="utf-8") as f:
        case_data = yaml.load(f,Loader=yaml.FullLoader)[key]

        # data_list = list()
        # for i in case_data.values():
        #     data_list.append(i)
        # print(case_data)
        return case_data
