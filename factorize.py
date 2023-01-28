from datetime import datetime
from multiprocessing import Pool, cpu_count

list_res = []


def factorize(num: int) -> list:
    list_n = []
    count = 0
    while count < num:
        count += 1
        if not num % count:
            list_n.append(count)
    return list_n


def callback(result: list):
    list_res.append(result)


def pool_async(*n: int) -> tuple:
    with Pool(cpu_count()) as p:
        p.map_async(factorize, n, callback=callback)
        p.close()
        p.join()
    return tuple(list_res[0])


def linear(*n: int) -> tuple:
    result = []
    for number in n:
        result.append(factorize(number))
    return tuple(result)


if __name__ == '__main__':
    start = datetime.now()
    print(f'Count CPU: {cpu_count()}')
    res = linear(128, 255, 99999, 10651060, 128, 255, 99999, 10651060, 128, 255, 99999, 10651060)
    # a, b, c, d = linear(128, 255, 99999, 10651060)
    # # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
    # #              1521580, 2130212, 2662765, 5325530, 10651060]
    end = datetime.now()
    [print(i) for i in res]
    print(f'Time linear calculation: {end - start}')


    start_a = datetime.now()
    res_a = pool_async(128, 255, 99999, 10651060, 128, 255, 99999, 10651060, 128, 255, 99999, 10651060)
    # f, g, h, i = pool_async(128, 255, 99999, 10651060)
    # assert f == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert g == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert h == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert i == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
    #              1521580, 2130212, 2662765, 5325530, 10651060]
    end_a = datetime.now()
    [print(i) for i in res_a]
    print(f'Time async calculation : {end_a - start_a}')
