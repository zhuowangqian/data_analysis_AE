import pymysql

db = pymysql.connect(
    user='root',
    password='Qian1314',
    database='test'
)
cursor = db.cursor()

sql = 'select * from baidu_translate;'
cursor.execute(sql)
print(cursor.execute(sql))

# https://github.com/zhuowangqian/data_analysis_AE/tree/57275b2c3beefa22f5eb03ab5559a71a10983707
