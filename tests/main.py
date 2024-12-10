import json
import asyncio
from pathlib import Path

from aiohttp import client
from asserts import assert_count_equal, assert_dict_equal, assert_equal

async def main():
    with open(Path(__file__).parent / "tests.json") as f:
        tests = json.load(f)
    tasks = []
    async with client.ClientSession() as session:
        for i, test in enumerate(tests):
            tasks.append(asyncio.create_task(run_test(i+1, test, session)))

        done, _ = await asyncio.wait(tasks)
        if all(task.exception() is None for task in done):
            print("All tests passed")

async def run_test(test_number: int, test: dict, session: client.ClientSession):
    async with session.post('http://localhost:8080/get_form', data=test["data"]) as response:
        assert_equal(response.status, test["response"]["status"])
        data = await response.json()
        # if isinstance(data, str):
        assert_equal(data, test["response"]["data"])
        # elif isinstance(data, dict):
        #     assert_dict_equal(data, test["response"]["data"])
    
    print(f"Test #{test_number} passed")

asyncio.run(main())