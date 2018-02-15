import os
import qrcode


class GenerateQR:
    def __init__(self, data, output_path):
        self.__data = data
        self.__output_path = output_path
        # Create qr code instance
        self.__qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        self.__generate()

    def __generate(self):
        if self.__data is None or self.__data == "":
            return
        # Add data
        self.__qr.add_data(self.__data)
        self.__qr.make(fit=True)

        img = self.__qr.make_image()
        if not os.path.exists(self.__output_path):
            os.makedirs(self.__output_path)
        img.save(self.__output_path+self.__data+".png")
