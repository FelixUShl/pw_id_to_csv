import os
from zipfile import ZipFile
import cv2
from pyzbar.pyzbar import decode

"""
Открыть проект в IDE
Подтянуть библиотеки командой "pip install -r requirements.txt"
Положить исходный архив в папку, Указать имя архива а переменную file, запустить скрипт
"""

file="PW-ID_223300-223327.zip"
def qr_read(img_path):
    img = cv2.imread(img_path)
    return decode(img)[0][0].decode('utf-8')


# Обработка QR кодов
def hex8b(qr_name: str) -> str:
    return qr_name[:-4].upper()


def generate_qr_list(qrs: list, path: str) -> list:
    data = list()
    for qr in qrs:
        data.append([hex8b(qr).upper(),
                     qr_read(f"{path}/{qr}")])
    return data


def zip_unpuck(zip_file_name):
    zip_f = f"{os.path.abspath(os.path.dirname(zip_file_name))}/{zip_file_name}"
    with ZipFile(zip_f, "r") as zip:
        zip.extractall(path="tmp")
    return zip_file_name[:-4]


def generate_csv(list):
    raw_data = ""
    for row in list:
        raw_data += f"{row[-1]};{row[0].lstrip()}\n"
    with open ("qr.csv", "w") as csv:
        csv.write(raw_data[:-1])

def do_csv(zip_file_name: str) -> str:
    # Распакуем полученный архив
    TEMP_FOLDER = zip_unpuck(zip_file_name)

    # Создадим список файлов в папке, проверим что они все изображения
    files = sorted(os.listdir("tmp"))
    qrs = []
    for item in files:
        if item[-4:] == ".png": qrs.append(item)
    data = generate_qr_list(qrs, "tmp")
    generate_csv(data)


do_csv(file)
