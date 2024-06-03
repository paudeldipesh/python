import multiprocessing
import os
from concurrent.futures import ProcessPoolExecutor

import requests


def download_file(url, name):
    print(f"image-{name} downloading...")
    response = requests.get(url)
    os.makedirs("images", exist_ok=True)
    open(f"images/image-{name}.jpg", "wb").write(response.content)
    print(f"image-{name} downloaded!")


random_image_url = "https://picsum.photos/600/500"

if __name__ == "__main__":
    # processes = []

    #     for index in range(5):
    #         # download_file(random_image_url, index + 1) # Use this for synchronous
    #         file = multiprocessing.Process(
    #             target=download_file, args=[random_image_url, index + 1]
    #         )
    #         file.start()
    #         processes.append(file)

    #     for file in processes:
    #         file.join()

    with ProcessPoolExecutor() as executor:
        number_list_one = [random_image_url for i in range(6)]
        number_list_two = [i for i in range(6)]
        results = executor.map(download_file, number_list_one, number_list_two)
        for result in results:
            print(result)
