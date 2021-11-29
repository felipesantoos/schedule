import schedule
import time

i = 1
def second_job():
    global i
    if i == 1: print(i, "segundo")
    else: print(i, "segundos")
    i = i + 1

def minute_job():
    print("Passou-se mais 1 minuto!")

def hour_job():
    print("Passou-se mais 1 hora!")

def lunch_job():
    print("Hora do almoço!")

def sunday_job():
    print("Hoje é domingo!")

def monday_job():
    print("Hoje é segunda!")

schedule.every(1).second.do(second_job)
schedule.every(1).minutes.do(minute_job)
schedule.every().hour.do(hour_job)
schedule.every().day.at("12:00").do(lunch_job)
schedule.every().sunday.do(monday_job)
schedule.every().monday.at("08:00").do(monday_job)

while True:
    schedule.run_pending()
    time.sleep(1)
    