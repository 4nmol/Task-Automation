import schedule
import time
from datetime import datetime

print("Task Automation started......")
print("This is Task Automation scheduler")
print("Python Task of internship in Code aplha")

# Function defination of the Task Automation function 

def Task_automation():
    now = datetime.now().time()
    print("This Task Automation will Automatically notify you after every 10 seconds")
    print(f"Current time and date: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("Current time: ", now)
    print("10 seconds Task scheduler executed completely")
    
# Additional task functions for different time intervals

# Task Automation for 1 minute interval (using scheduler)

def Task_automation1():
    print("This Task Automation will Automatically notify you after every 1 minute")
    print(f"Current time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("1 minute Task scheduler executed completely")

# Task Automation for 5 seconds interval

def Task_automation2():
    print("This Task Automation will Automatically notify you after every 5 seconds")
    print(f"Current time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("5 seconds Task scheduler executed completely")


# Task Automation for 15 seconds interval

def Task_automation3():
    print("This Task Automation will Automatically notify you after every 15 seconds")
    print(f"Current time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("15 seconds Task scheduler executed completely")

# Task Automation for 20 seconds interval

def Task_automation4():
    print("This Task Automation will Automatically notify you after every 20 seconds")
    print(f"Current time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("20 seconds Task scheduler executed completely")
    
    
# Task Automation for 30 seconds interval

def Task_automation5():
    print("This Task Automation will Automatically notify you after every 30 seconds")
    print(f"Current time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("30 seconds Task scheduler executed completely")

# Schedule the tasks for different time intervals

schedule.every(10).seconds.do(Task_automation)
schedule.every(1).minute.do(Task_automation1)
schedule.every(5).seconds.do(Task_automation2)
schedule.every(15).seconds.do(Task_automation3)
schedule.every(20).seconds.do(Task_automation4)
schedule.every(30).seconds.do(Task_automation5)


while True:
    schedule.run_pending()  # Check and run pending tasks
    time.sleep(1)  # Sleep for 1 second before checking again
