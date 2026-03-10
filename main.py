from capsule.scheduler import check_unlocks
import schedule
import time

schedule.every(10).seconds.do(check_unlocks)

print("TimeCapsule daemon running...")

while True:
    schedule.run_pending()
    time.sleep(1)
