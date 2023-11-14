from database import student_collection

ans = student_collection.find()

async def fun():
    async for i in ans:
        print(i)
fun()

import asyncio
asyncio.run(fun())