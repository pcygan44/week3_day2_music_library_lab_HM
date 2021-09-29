from db.run_sql import run_sql
from models.album import Album



def save(album):
    sql = " INSERT INTO albums (album_title) VALUES (%s) RETURNING *"
    values = [album.album_title]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

# def delete_one(id):
#     sql = "DELETE FROM album WHERE id = %s"
#     values = [id]
#     run_sql(sql,values)

# def select(id):
#     task = None
#     sql ="SELECT * FROM albums WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]
#     if result is not None:
