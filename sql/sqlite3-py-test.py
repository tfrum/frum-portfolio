import sqlite3
from queue import Queue
from threading import Thread
import time

# Create a sample database and export it into a Python object (a dictionary)
employees = [
    (1, 'John Doe', 30, 50000),
    (2, 'Jane Doe', 25, 60000),
    (3, 'Bob Smith', 40, 70000)
]
employee_dict = {emp[0]: {'name': emp[1], 'age': emp[2], 'salary': emp[3]} for emp in employees}

def create_db():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            salary REAL
        )
    ''')
    cursor.executemany('INSERT INTO employees VALUES (?, ?, ?, ?)', employees)
    conn.commit()
    return conn, cursor

# Create a queue for updates
update_queue = Queue()

# Define a function to process updates
def process_updates():
    conn, cursor = create_db()  # Create a new connection and cursor for this thread
    while True:
        update = update_queue.get()
        if update is None:
            break
        employee_id, column, value = update
        cursor.execute(f'UPDATE employees SET {column} = ? WHERE id = ?', (value, employee_id))
        conn.commit()
        employee_dict[employee_id][column] = value
        print(f'Updated employee {employee_id}\'s {column} to {value}')
    cursor.close()
    conn.close()

# Start the update processing thread
update_thread = Thread(target=process_updates)
update_thread.start()

# Simulate manual updates to the database
try:
    while True:
        employee_id = int(input('Enter employee ID: '))
        column = input('Enter column to update (name, age, or salary): ')
        value = input(f'Enter new {column} for employee {employee_id}: ')
        if column == 'age':
            value = int(value)
        elif column == 'salary':
            value = float(value)
        update_queue.put((employee_id, column, value))
        time.sleep(1)  # Simulate some delay between updates
except KeyboardInterrupt:
    pass  # Allow exit with Ctrl+C

# Stop the update processing thread
update_queue.put(None)
update_thread.join()
