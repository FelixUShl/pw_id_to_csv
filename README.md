# pq_qr_to_csv
### Скрипт создающий csv из архива с qr кодами идентификаторов
В переменной < file > в качестве строки указываем имя zip архива, помещенного в папку со скриптом и запускаем скрипт
Результат работы скрипта: файл "qr.csv" со строками в формате "< url >;< HEX 8b >\n" и папка tmp с распакованными qr.\
<b>QR должны быть в формате png и файлы должны лежать в корне архива!!!! Остальные файлы в архиве будут проигнорированы
