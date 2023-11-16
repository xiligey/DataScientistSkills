import asyncio
import time

import requests


async def test2(i):
    r = await other_test(i)
    print(i, r)


async def other_test(i):
    r = requests.get(i)
    print(i)
    await asyncio.sleep(4)
    print(time.time() - start)
    return r


url = ["https://segmentfault.com",
       "https://www.jianshu.com",
       "https://www.baidu.com"]

loop = asyncio.get_event_loop()
task = [asyncio.ensure_future(test2(i)) for i in url]
start = time.time()
loop.run_until_complete(asyncio.wait(task))
time_cost = time.time() - start
print(time_cost)
loop.close()
