#
# Database access functions for the web forum.
# 

import time
import psycopg2

## Database connection
DB = []

## Get posts from database.
def GetAllPosts():
    db = psycopg2.connect("dbname=forum")
    connection = db.cursor()
    connection.execute("SELECT time, content FROM posts ORDER BY time DESC")
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    posts = ({'content': str(row[1]), 'time': str(row[0])}
             for row in connection.fethcAll())
    db.close()
    return posts

## Add a post to the database.
def AddPost(content):
    db = psycopg2.connect("dbname=forum")
    connection = db.cursor()
    connection.execute("INSERT INTO posts (content) VALUES ('%s')" % content)
    
    db.commit()
    db.close()
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
