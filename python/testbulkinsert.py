#__author__ = 'Administrator'
import mysql.connector

def bulkinsert(dataarray):
    stmt='insert into test (classname, url) values (%s,%s)'
    cnn = mysql.connector.connect(user='root',passwd='12345',database='classspiderdb')

    cursor=cnn.cursor()
    try:
        cursor.executemany(stmt,dataarray)
    except mysql.connector.Error as e:
        print('query error!{}'.format(e))
    finally:
        cursor.close()

    cnn.commit()
    cnn.close()


if __name__ == '__main__':
    #test()
    data=[('Lucy','21'),
     ('Tom3',22),
     ('Lily4',21)]
    bulkinsert(data)
