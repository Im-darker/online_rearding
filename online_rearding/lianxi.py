# import redis
#
# r = redis.Redis(host="127.0.0.1", port=6379, db=0, charset="utf8", decode_responses=True)
# r.set("name", "xwh")
# r.expire("name", 2)
# import time
# time.sleep(1)
#
# print(r.get("name"))
# from itertools import product
#
# a = [1,2,3]
# b = [4,5,6]
# c =product(a, b)
# print(list(c))
#
# c = zip(a, b)
# print(list(c))