import sqlite3
from queue import Queue
from threading import Thread
import time

# Create a sample database
conn = sqlite3.connect(':memory:')  # Still using in-memory for the example
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        salary REAL
    )
''')
employees = [
    (1, 'John Doe', 30, 50000),
    (2, 'Jane Doe', 25, 60000),
    (3, 'Bob Smith', 40, 70000)
]
cursor.executemany('INSERT INTO employees VALUES (?, ?, ?, ?)', employees)
conn.commit()

# Export the database into a Python object (a dictionary)
cursor.execute('SELECT * FROM employees')
employee_dict = {row[0]: {'name': row[1], 'age': row[2], 'salary': row[3]} for row in cursor.fetchall()}

# Create a queue for updates
update_queue = Queue()

# Define a function to process updates (now with a new connection for each update)
def process_updates():
    while True:
        update = update_queue.get()
        if update is None:
            break
        employee_id, column, value = update

        # Create a new connection and cursor for each update
        with sqlite3.connect(':memory:') as update_conn: 
            update_cursor = update_conn.cursor()
            update_cursor.execute(f'UPDATE employees SET {column} = ? WHERE id = ?', (value, employee_id))
            update_conn.commit()
            
            # Re-fetch updated row from database using the new connection
            update_cursor.execute('SELECT * FROM employees WHERE id = ?', (employee_id,))
            row = update_cursor.fetchone()
            employee_dict[employee_id] = {'name': row[1], 'age': row[2], 'salary': row[3]} 
            print(f'Updated employee {employee_id}\'s {column} to {value}')

# Start the update processing thread
update_thread = Thread(target=process_updates)
update_thread.start()

# Simulate manual updates to the database
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

# Stop the update processing thread
update_queue.put(None)
update_thread.join()

# Close the database connection
conn.close()
