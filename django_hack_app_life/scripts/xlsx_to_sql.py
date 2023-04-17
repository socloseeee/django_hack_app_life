import os
import sqlite3
import pandas as pd
from pathlib import Path
import warnings
from transliterate import translit


warnings.simplefilter("ignore")

def checkTableExists(dbcon, tablename):
    listOfTables = dbcon.cursor().execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table' AND name='{0}'
        """.format(tablename))
    return True if listOfTables else False

cnn = None
db_file: str = '../db.sqlite3'
table_name = 'Userdata'

try:
    cnn = sqlite3.connect(db_file)
    print('database connected..')
    for file_path in (Path('../xlsx_files').iterdir()):
        df = pd.read_excel(Path(file_path))
        print(df.head(10), '\n')
        df.columns = map(lambda x: translit(x.replace('"', ''), language_code='ru', reversed=True), df.columns)
        add_or_create = 'append' if checkTableExists(cnn, table_name) else 'create'
        print(checkTableExists(cnn, table_name))
        df.to_sql(name=table_name, con=cnn, if_exists=add_or_create)
        sql = "Select * From Userdata"
        df_read = pd.read_sql(sql, cnn)
        print(df_read.head(10))
except Exception as e:
    print(e)
finally:
    if cnn:
        cnn.close()

os.system('python ../manage.py inspectdb > ../app/models.py')
os.system('python ../manage.py makemigrations')
os.system('python ../manage.py migrate')
