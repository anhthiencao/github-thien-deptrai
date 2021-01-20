import sqlite3 
import json


conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Employee_mana(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Age INT, Department TEXT, ROLE TEXT)")

with open('data.json', 'r') as json_file:
    emp_data = json.load(json_file)

def insert_employee(
        name: str,
        age: int,
        department: str,
        role: str
    ):
    """
    Helps to insert employee record to SQLite DB  
    Params:
        _id: id of employee
        name: name of employee
        department: department of employee
        role: role of employee
        mentor: mentor id of employee
    Return: N/A
    """
    try:
        cur.execute("""
                INSERT INTO Employee_mana 
                (Name, Age, Department, ROLE) 
                VALUES(
                    '{name}',
                    {age},
                    '{department}',
                    '{role}'
                )
            """.format(
            name=name,
            age=age,
            department=department,
            role=role,
        ))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
        exit(1)

def load_init_data(data):
    for item in data:
        name = item["name"]
        age = item["age"]
        department = item["department"]
        role = item["role"]
        insert_employee(name, age, department, role)



load_init_data(emp_data)
