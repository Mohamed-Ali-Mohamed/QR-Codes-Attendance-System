from generator.generator import Generator

data_folder = "../data/"

# Do u want to generate QR Codes to use them in attendance?
# 1. Go to "../data/StudentsInfo.xlsx" and fill students data
# 2. Rename it with your subject like "StudentsInfo_Theory"
# 3. Set the file name & Run

students_info_file_name = "StudentsInfo_Theory"
Generator(data_folder + students_info_file_name)

# 4. Go to "../generator/QR Codes/" and give the QR Codes to your students
