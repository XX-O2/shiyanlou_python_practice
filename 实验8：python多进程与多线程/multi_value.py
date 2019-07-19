import time
from multiprocessing import Process,Value,Lock

# 该函数运行在子进程中，参数val是一个Value对象，是全局变量
def func(val,lock):
    # 将val这个全局变量的值进行50次＋1操作
    for i in range(50):
        time.sleep(0.01)
        """
        lock.acquire()
        val.value += 1
        lock.release()
        """
        with lock:
            val.value +=1

def main():
    # 多进程无法使用全局变量，multiprocessing提供的Value是一个代理器
    # val是一个Value对象，它是全局变量，数据类型为int，初始值为0
    val = Value('i',0)
    # 创建10个任务，备用
    lock = Lock()
    processes = [Process(target=func,args=(val,lock)) for i in range(10)]
    # 启动10个子进程来运行 procs 中的任务，对 Value 对象进行＋1操作
    for p in processes:
        p.start()
    # join方法使主进程挂起，直至所有子进程运行完毕
    for p in processes:
        p.join()
    print(val.value)

if __name__ == "__main__":
    for i in range(5):
        main()
