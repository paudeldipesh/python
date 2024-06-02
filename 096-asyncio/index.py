import asyncio

import requests


async def async_function_one():
    url = "https://images.pexels.com/photos/1820563/pexels-photo-1820563.jpeg"
    response = requests.get(url)
    with open("road.jpeg", "wb") as file:
        file.write(response.content)
    print("Road Image!")
    return "Road"


async def async_function_two():
    url = "https://images.pexels.com/photos/3201580/pexels-photo-3201580.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    response = requests.get(url)
    with open("developer.jpeg", "wb") as file:
        file.write(response.content)
    print("Developer Image!")
    return "Developer"


async def async_function_three():
    url = "https://images.pexels.com/photos/2421467/pexels-photo-2421467.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    response = requests.get(url)
    with open("monk.jpeg", "wb") as file:
        file.write(response.content)
    print("Monk Image!")
    return "Monk"


async def main_function():
    # Download images synchronously
    # await async_function_one()
    # await async_function_two()
    # await async_function_three()

    # Download images asynchronously
    run_task = await asyncio.gather(
        async_function_one(), async_function_two(), async_function_three()
    )

    print(run_task)


asyncio.run(main_function())
