import mysql.connector
import json
import datetime


class API():
    """
    API class with functions to interact with db
    """

    def __init__(self):
        with open("connection.json") as file:
            connection_json = json.loads(file.read())
        self.connection = mysql.connector.connect(**connection_json )
        self.connection.autocommit = True
        self.status_dict = [{"key":'Open', "val":1}, {"key":'In Progress', "val":2}, {"key":'Closed', "val":3}]


    def list_stories(self):
        cur = self.connection.cursor(dictionary=True)
        cur.execute("select * from app.stories")
        return cur.fetchall()

    
    def get_story(self, id):
        cur = self.connection.cursor(dictionary=True)
        cur.execute("select * from app.stories where id = %s", (id,))
        return cur.fetchone()


    def create_story(self, header, story_description=None, start_date=datetime.datetime.today(), 
                    end_date=datetime.datetime.today() + datetime.timedelta(days=1)):
        cur = self.connection.cursor(dictionary=True)
        cur.execute("insert into app.stories(header, story_description, start_date, end_date) values (%s,%s,%s,%s)",
                    (header, story_description, start_date, end_date))
        return cur.rowcount


    def modify_story(self, id, header, story_description=None, start_date=datetime.datetime.today(), 
                    end_date=datetime.datetime.today() + datetime.timedelta(days=1)):
        cur = self.connection.cursor(dictionary=True)
        cur.execute("""Update app.stories set header = %s, story_description=%s, start_date=%s, end_date=%s
                        where id = %s """,(header,story_description,start_date,end_date, id))
        return cur.rowcount


    def delete_story(self, id):
        cur = self.connection.cursor(dictionary=True)
        cur.execute("""Delete FROM app.stories where id =%s""", (id,))
        return cur.rowcount


    def list_todos(self, id):
        cur = self.connection.cursor(dictionary=True)
        cur.execute("""select t.id, t.header, t.to_do_description, t.to_do_status, t.start_date, t.end_date 
                        from app.to_dos t where t.story_id = %s """, (id,))
        return cur.fetchall()


    def get_todo(self, id):
        cur = self.connection.cursor(dictionary=True)
        cur.execute("select * from app.to_dos where id = %s", (id,))
        return cur.fetchone()


    def create_to_do(self, story_id, header, to_do_status=1, to_do_description=None, start_date=datetime.datetime.today(),
                    end_date=datetime.datetime.today() + datetime.timedelta(days=1)):
        cur = self.connection.cursor(dictionary=True)
        cur.execute("""insert into app.to_dos(story_id,header,to_do_description,to_do_status,start_date,end_date) values (%s,%s,%s,%s,%s,%s)""",
                    (story_id,header, to_do_description, to_do_status, start_date, end_date))
        return cur.rowcount


    def modify_to_do(self, id, header, to_do_description, to_do_status=1, start_date=datetime.datetime.today(), 
                    end_date=datetime.datetime.today() + datetime.timedelta(days=1)):
        cur = self.connection.cursor(dictionary=True)
        cur.execute("""Update app.to_dos set header = %s, to_do_description=%s, to_do_status=%s, start_date=%s,
                        end_date=%s where id = %s """,(header,to_do_description,to_do_status,start_date,end_date, id))
        return cur.rowcount


    def delete_to_do(self, id):
        cur = self.connection.cursor(dictionary=True)
        cur.execute("""Delete FROM app.to_dos where id =%s""", (id,))
        return cur.rowcount
    
    
     

