# Routine

**Routine** is a Python library for scheduling tasks (also known as schedules, crons, or jobs). With Routine, 
you can easily configure which days a function should run, set multiple executions per day, choose specific 
weekdays, and much more. Simple and intuitive, Routine allows anyone to schedule tasks quickly and 
efficiently—without any hassle. 

# How to use:

Let's use this function for example:

def functionTest():

    for x in range(0, 2):
        sleep_time = 1
        print(f"Function 1 {x} {datetime.now()}")
        time.sleep(sleep_time)
		
		
		
Let's create a job with the functionTest with **routine**

import routine

routineObj = routine.routine()
routineObj.newRoutine(functionTest,day=7)

while True:
    
    routineObj.start()
    time.sleep(2)
	
	
This way, your job will run every day, but there are more configuration options available for you to use with **Routine**.

routineObj.newRoutine(funcTeste,day=1) - just in monday
routineObj.newRoutine(funcTeste,day=1,at="14:50") - Setting a day with a specific time


Let's say you want to run a function every Thursday at 3:30 PM and 6:10 PM.


import routine

routineObj = routine.routine()
routineObj.newRoutine(funcTeste,day=4, at="15:30")
routineObj.newRoutine(funcTeste,day=4, at="18:10")

while True:
    
    routineObj.start()
    time.sleep(2)




