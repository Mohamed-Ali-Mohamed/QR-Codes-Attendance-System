import pandas as pd


class ReadXLSX:
    def __init__(self, file_name):
        self.__file = file_name + '.xlsx'
        self.__info = {}
        self.__rows_counter = 0
        self.__prepare_file()

    def __prepare_file(self):
        try:
            xl = pd.ExcelFile(self.__file)
            df1 = xl.parse(xl.sheet_names[0])
            for column in df1.columns:
                self.__info[column] = []
            for column in df1.columns:
                for x in df1.get(column):
                    self.__info[column].append(str(x))
            if len(df1.columns) > 0:
                self.__rows_counter = len(self.__info[df1.columns[0]])
        except Exception as inst:
            print(type(inst))  # the exception instance
            print(inst.args)  # arguments stored in .args
            print(inst)  # __str__ allows args to be printed directly

    def get_info(self):
        return self.__info, self.__rows_counter
