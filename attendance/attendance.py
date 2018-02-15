from xlsx.write_xlsx import WriteXLSX
from xlsx.read_xlsx import ReadXLSX


class Attendance:
    def __init__(self, students_file_name, attendance_file_name, week_name):
        self.__attendance_mark = "YES"
        self.__department = "Department"
        self.__section = "Section"
        self.__name = "Name"
        self.__scanner_output = "ScannerOutput"
        self.__students_file_name = students_file_name
        self.__attendance_file_name = attendance_file_name
        self.__week_name = week_name
        self.__attendance_info = self.__get_scanner_output()
        info, rows_counter = self.__get_students_info()
        if self.__attendance_info is not None and rows_counter != 0:
            self.__take_attendance(info, rows_counter)

    def __get_scanner_output(self):
        # Get ScannerOutput list
        attendance_info, attendance_rows_counter = ReadXLSX(self.__attendance_file_name).get_info()
        if self.__scanner_output in attendance_info:
            return attendance_info[self.__scanner_output]

    def __get_students_info(self):
        # Get Students Info to add attendance then save it
        info, rows_counter = ReadXLSX(self.__students_file_name).get_info()
        return info, rows_counter

    def __take_attendance(self, info, rows_counter):
        for row in range(0, rows_counter):
            data = ""
            if self.__department in info:
                department = info[self.__department][row]
                data += "[" + department + "]"
            if self.__section in info:
                section = info[self.__section][row]
                data += "[" + section + "]"
            if self.__name in info:
                name = info[self.__name][row]
                data += "[" + name + "]"

            if data in self.__attendance_info:
                info[self.__week_name][row] = self.__attendance_mark
            else:
                if info[self.__week_name][row] == 'nan':
                    info[self.__week_name][row] = ''

        WriteXLSX(self.__students_file_name, self.__week_name, info[self.__week_name])
