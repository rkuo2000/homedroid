# Goldbach Hypothesis verificaiton
import time
from multiprocessing import cpu_count
from multiprocessing import Pool
from Goldbach import goldbach

def subRanges(N, CPU_COUNT):
    list = [[ i+1, i+N // CPU_COUNT] for i in range(4, N, N // CPU_COUNT)]
    list[0][0] = 4
    if list[CPU_COUNT -1][1] > N:
        list[CPU_COUNT -1][1] = N
    return list

def main():
    N = 10**6
    print(N)
    CPU_COUNT= cpu_count()
    print(CPU_COUNT)

    print("Single-Processing")
    start = time.process_time()
    results = goldbach([4,N])
    for sample in results:
        print("%d=%d+%d" % sample)
    print("  Single-Processing computation time: %d s" % (time.process_time() - start)) 

    print(" Muliti-Processing")
    pool = Pool(CPU_COUNT)
    sepList = subRanges(N, CPU_COUNT)
    start = time.process_time()
    results = pool.map(goldbach, sepList)
    pool.close()
    pool.join()
    for result in results:
        for sample in result:
            print("%d=%d+%d" % sample)
    print("  Multi-Processing computation time: %d s" % (time.process_time() - start))

if __name__ == "__main__":
    main()
    
