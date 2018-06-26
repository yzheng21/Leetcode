import queue, subprocess, threading
import time
from queue import PriorityQueue
# q = queue.Queue()
#
# #FIFO队列先进先出
# q.put(2)
# q.put(1)
# q.put(3)
#
# while not q.empty():
#     next_item = q.get()
#     print(next_item)
#     time.sleep(1)

# q = queue.LifoQueue()
#
# #LIFO队列后进先出
# q.put(2)
# q.put(1)
# q.put(3)
#
# while not q.empty():
#     next_item = q.get()
#     print(next_item)
#     time.sleep(1)

# q = queue.Queue(maxsize=2)
#
# #将q队列填满
# q.put('python')
# q.put('linux')
#
# print(time.ctime())    #打印当前时间
# try:    #捕获queue.Full异常
#     #q.put('shell', timeout=3)    #默认block=True
#     #q.put('shell', True, timeout=3)    #可以省略block=；直接写True；timeout=可以省略直接写3
#     q.put('shell', block=True, timeout=3)    #q队列已满，再次将数据放入q中，将阻塞3s后抛出异常queue.Full
# except queue.Full:
#     print('queue is full!')
#     print(time.ctime())

# q = PriorityQueue()
#
# q.put((2, 'code'))
# q.put((1, 'eat'))
# q.put((3, 'sleep'))
#
# while not q.empty():
#     next_item = q.get()
#     print(next_item)
#     time.sleep(3)

q = queue.Queue()
hosts = ['192.168.1.68', '192.168.1.118', '192.168.1.101', '192.168.1.250', '192.168.1.133']

def run():
    while True:    #防止线程少于len(hosts)时卡死，不用while循环线程数少时就会导致队列数据无法全部取完，就会造成queue.join()一直阻塞状态
        host = q.get()
        if host == '192.168.1.118':    #如果ip等于192.168.1.118就休眠10S，用于判读queue.join()是否阻塞直到queue.task_doen()通知后接触阻塞
            time.sleep(10)
        print('host ip is:%s'% host)
        q.task_done()    #当前线程任务完成

def main():
    for i in range(10):
        t = threading.Thread(target=run)
        t.setDaemon(True)
        t.start()

    for item in hosts:
        q.put(item)

    q.join()    #阻塞直至所有线程queue.task_done()返回

start = time.time()
main()
print("Elapsed Time: %s" % (time.time() - start))