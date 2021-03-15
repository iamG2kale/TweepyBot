import os
CONSUMER_KEY = os.getenv("tweepybotck")
CONSUMER_SECRET = os.getenv("tweepybotcs")
ACCESS_TOKEN = os.getenv("tweepybotat")
ACCESS_SECRET = os.getenv("tweepybotas")
print(os.getenv("tweepybotat"))
print(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)