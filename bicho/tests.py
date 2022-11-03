from django.test import TestCase

# Create your tests here.
# myscript2.py
from schedule import every, repeat, run_pending
import time

@repeat(every(5).minutes)
def job():
    print("Job scheduled using decorator...")

while True:
    run_pending()
    time.sleep(1)