# 规范操作应该是固定数组大小，对索引进行循环操作（取余计数）
# 判空判满实现：1. 循环计数器 2. 牺牲一个存储位置 3. 设置标志位(比较不好想到）


class MyCircularQueue:


    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.maxlen = k
        # 在Python中这样的操作可以提高效率吗（空间或者时间）? leetcode 提交是一样的
        self.circular = [None] * k
        self.front = 0
        self.rear = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.maxlen
            self.circular[self.rear] = value
            self.size += 1
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1) % self.maxlen
            self.size -= 1
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.circular[self.front] if self.size else -1
        # if self.size:
        #     return self.cicular[self.front]
        # else:
        #     return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.circular[self.rear] if self.size else -1
        # if self.size:
        #     return self.circular[-1]
        #     # return self.circular[self.rear]
        # else:
        #     return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return not self.size

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.maxlen

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
