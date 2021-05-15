from datetime import datetime
from assetshandler import AssetFile, Assets
import random


def make_uuid():
    return ''.join([random.choice('0123456789ABCDEF') for j in range(20)])


def createdAt(conn, file):
    sql = """select min( createdAt )
                 from assets_prod where post='%s'""" % str(file)
    cursor = conn.execute(sql)

    now = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    fetched = cursor.fetchall()[0][0]

    if fetched is None:
        output = now
    else:
        output = fetched
    return output


def posts_write(conn, file, title, header, now):
    sql = f"""INSERT INTO assets_prod
            (datestr,
             post,
             UUID,
             createdAt,
             title,
             header)
VALUES      ("%s",
             "%s",
             "%s",
             "%s",
             "%s",
             "%s")  """ % (now,
                           file,
                           make_uuid(),
                           createdAt(conn, file),
                           title,
                           header
                           )
    conn.execute(sql)
    conn.commit()


def posts_update1():
    asset = Assets()
    for i in asset.files_list:
        file = AssetFile(i)
        posts_write(conn, file.file, file.title, file.header)


def posts_update(conn, post):
    now = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    file = AssetFile(post)
    posts_write(conn, file.file, file.title, file.header, now)
