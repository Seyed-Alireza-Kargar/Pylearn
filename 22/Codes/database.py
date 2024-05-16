import sqlite3

def create_connection():
    conn = sqlite3.connect('tasks.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            time TEXT,
            priority TEXT,
            done BOOLEAN NOT NULL CHECK (done IN (0, 1))
        )
    ''')
    conn.commit()
    conn.close()

def add_task(title, description, time, priority):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, description, time, priority, done) VALUES (?, ?, ?, ?, 0)', (title, description, time, priority))
    conn.commit()
    conn.close()

def get_tasks():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks ORDER BY done, priority DESC')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task_done(task_id, done):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET done = ? WHERE id = ?', (done, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
