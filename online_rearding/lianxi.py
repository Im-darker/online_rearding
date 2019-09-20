import redis

r = redis.Redis(host="127.0.0.1", port=6379, db=0, charset="utf8", decode_responses=True)
r.set("name", "xwh")
r.expire("name", 2)
import time
time.sleep(1)

print(r.get("name"))