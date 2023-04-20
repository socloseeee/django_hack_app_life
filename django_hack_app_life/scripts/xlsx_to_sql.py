import os
import sqlite3
import pandas as pd
from pathlib import Path
import warnings
from transliterate import translit


warnings.simplefilter("ignore")


cnn = None
db_file: str = '../db.sqlite3'
table_name = 'Userdata'

try:
    cnn = sqlite3.connect(db_file)
    print('database connected..')
    i = 0
    print(list(str(path) for path in Path('../xlsx_files').iterdir()))
    for file_path in (Path('../xlsx_files').iterdir()):
        try:
            print(str(file_path))
            i += 1
            df = pd.read_excel(Path(file_path))
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            df['date'] = ((str(file_path)[::-1])[5:13])[::-1]
            print(df.head(10), '\n')
            df.columns = map(lambda x: translit(x.replace('"', '').replace('*', '').replace('№ ', '').replace('<span style="color: red;padding:2px">', '').replace('</span>', ''), language_code='ru', reversed=True), df.columns)
            df = df.loc[:, ~df.columns.str.contains('^Zajavki MZ-BDZ')]
            print(checkTableExists(cnn, table_name))
            df.to_sql(name=table_name, con=cnn, if_exists='append')
            sql = "Select * From Userdata"
            df_read = pd.read_sql(sql, cnn)
            print(df_read.head(10))
        except Exception as e:
            print(e)
except Exception as e:
    print(e)
finally:
    if cnn:
        cnn.close()
print(i)
os.system('python ../manage.py inspectdb > ../app/models.py')
os.system('python ../manage.py makemigrations')
os.system('python ../manage.py migrate')
