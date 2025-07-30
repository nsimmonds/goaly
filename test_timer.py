import sqlite3
import time

DB_NAME = 'tasks.db'
WORK_SECONDS = 5  # Just 5 seconds for testing
BREAK_SECONDS = 3  # Just 3 seconds for testing

def get_random_task():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT id, description FROM tasks WHERE completed = 0 ORDER BY RANDOM() LIMIT 1')
    task = c.fetchone()
    conn.close()
    return task

def test_timer():
    print("\n=== Goaly Pomodoro Timer (Test Mode) ===")
    print("This is a quick test - real timer uses 25min work / 5min break\n")
    
    # Get a random incomplete task
    task = get_random_task()
    if task:
        task_id, task_desc = task
        print(f"🎯 Current task: [{task_id}] {task_desc}")
    else:
        print("🎯 No tasks available - time to add some!")
    
    # Work session (shortened for testing)
    print(f"\n⏰ Work session ({WORK_SECONDS} seconds)")
    for second in range(WORK_SECONDS):
        if task:
            print(f"Work on: {task_desc} ({second + 1}/{WORK_SECONDS})")
        else:
            print(f"Work! ({second + 1}/{WORK_SECONDS})")
        time.sleep(1)
    
    print("\n✅ Work session complete!")
    
    # Break session (shortened for testing)
    print(f"\n🎮 Break session ({BREAK_SECONDS} seconds)")
    for second in range(BREAK_SECONDS):
        print(f"Play! ({second + 1}/{BREAK_SECONDS})")
        time.sleep(1)
    
    print("\n🎉 Break complete! Ready for next round?\n")

if __name__ == '__main__':
    test_timer() 