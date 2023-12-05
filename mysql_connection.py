import mysql.connector


# 파이썬으로 mysql에 접속할 수 있는 함수.
def get_connection() :
    connection = mysql.connector.connect(
        host = 'dbsample.cmuxpoe5idov.ap-northeast-2.rds.amazonaws.com',
        database = 'recipe_db',
        user = 'recipe_db_user',
        password = '1234'
    )
    return connection
