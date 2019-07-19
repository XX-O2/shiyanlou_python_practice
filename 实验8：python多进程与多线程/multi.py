import os
from multiprocessing import Process

def hello(name):
    # os.getpid()用来获取当前进程ID
    print('child process: {}'.format(os.getpid()))
    print('Hello '+name)

# 当我们运行一个 Python 程序，系统会创建一个进程来运行程序，被称为主进程或父进程
# 前面课程中，我们写的程序都是单进程程序，即所有代码都运行在一个主进程中
# 下面的 main() 函数就运行在主进程中
def main():
    # 打印当前进程即主进程ID
    print('parent process:　{}'.format(os.getpid()))
    # Process 对象只是一个子人物，运行该任务时系统会自动创建一个子进程
    # 主义args参数要以tuple方式传入
    p = Process(target=hello,args=('shiyanlou',))
    print('child process start')
    # 启动一个子进程来运行子任务，该进程运行的是hello()函数中的代码
    p.start()
    p.join()
    # 子进程完成后，继续运行主进程
    print('child process stop')
    print('parent process: {}'.format(os.getpid()))

if __name__ == "__main__":
    main()
