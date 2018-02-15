import pandas as pd
from openpyxl import load_workbook


class WriteXLSX:
    def __init__(self, file_name, column_name, column_data):
        self.__column_name = column_name
        self.__column_data = column_data
        self.__file = file_name + '.xlsx'
        self.__prepare_file()
        self.__write()

    def __prepare_file(self):
        xl = pd.ExcelFile(self.__file)
        self.__file_sheet_name = xl.sheet_names[0]
        self.__df = pd.read_excel(self.__file)
        if self.__column_name not in self.__df.columns:
            return
        self.__column_number = [i for i, x in enumerate(self.__df.columns) if x == self.__column_name][0]

    def __write(self):
        df2 = pd.DataFrame({self.__column_name: self.__column_data})

        writer = pd.ExcelWriter(self.__file, engine='openpyxl')
        book = load_workbook(self.__file)
        writer.book = book
        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

        self.__df.to_excel(writer, sheet_name=self.__file_sheet_name, index=False)
        df2.to_excel(writer, sheet_name=self.__file_sheet_name, index=False, startcol=self.__column_number)

        writer.save()
