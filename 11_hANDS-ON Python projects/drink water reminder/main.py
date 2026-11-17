import time
from notifypy import Notify

notification = Notify()
notification.title = "Reminder"
notification.message = "Please drink a sip of water!"

while True:
    notification.send()
    time.sleep(5)
