# PlaceXML
Тестовое задание<br> 
1. Был проведен анализ XML документа и на основе его структуры была спроектирована база данных<br>
2. Диаграмма базы данных на изображении Pictures/1NF соответсвует первой нормальной форме, так как каждое значение в ячейке базы данных атомарно. Диаграмма базы данных на изображении Pictures/2NF соответствует нормальной форме таблиц, все аттрибуты таблиц зависят только от ключевого элемента. При этом в таблице Category первичный ключ является составным из двух полей - CategoryId и PlaceId, что связано со связью M:N между таблицами.<br>
3. Py-скрипт для перевода данных ParsingXMLtoCSV.py<br>
4. Если честно, не совсем понял задание с автотестами, поэтому не сделал его. Необходимо повторить операцию 3, но другим способом для всех данных, или только по конкретным правилам в документе?<br>
5. CSV со статистическими данными - PlacesXML/stats.csv<br>
6. База данных находится в DB/PlaceXML<br>Была выбрана СУДБ MySQL. В процессе была обнаружена проблема - MySQL не поддерживает домены значений, и пришлось использовать varchar для ContactType, BaseTest и CategoryType.<br>Запросы по правилам пункта 6:<br>
SELECT AdminName1,AdminName2,AdminName3,BaseName,HouseNumber FROM Admin INNER JOIN Location ON Admin.AdminId=Location.AdminId INNER JOIN Places ON Location.PlaceId=Places.PlaceId INNER JOIN Caegory ON Places.PlaceId=Category.PlaceId WHERE CategorySystem=“poi“ AND CategoryId=9567;<br>
SELECT BaseText FROM Name INNER JOIN Location ON Location.PlaceId=Name.PlaceId INNER JOIN Contacts ON Location.PlaceId=Contacts.PlaceId WHERE Contacts.ContactType="WEBADDRESS" AND Contacts.ContactString IS NOT NULL AND Location.CountryCode="RUS";<br>
Результаты запросов в папке Pictures.<br>
Тест кейс в документе Test_case.odt

