from attendance.attendance import Attendance

data_folder = "../data/"
# Do you want to write the attendance in StudentsInfo file?
# 1. Scan students QR Codes with any app like "LoMag barcode scanner for Android"
# 2. Go to "../data/ScannerOutput.xlsx" and fill scanner output
# 3. Rename it with your subject like "ScannerOutput_Theory"
scanner_output_file_name = "ScannerOutput_Theory"
# 4. Write the week value like "Week2"
week_name = "Week2"
# 5. Set students info file name & Run
students_info_file_name = "StudentsInfo_Theory"

Attendance(data_folder + students_info_file_name, data_folder + scanner_output_file_name, week_name)

# 6. Go to "../data/students_info_file_name". You will find the attendance in "week_name" column
