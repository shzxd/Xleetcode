from collections import deque

def ladderLength(beginword: str, endword: str, wordlist: list[str]) -> int:
    # # 1. 超时 原始思路，与最小基因变化433一样的做法，但是候选单词列表太长，导致搜索超时
    # wordlist = set(wordlist)
    # queue = deque([(beginword, 1)])
    # wordlength = len(beginword)
    # while queue:
    #     tmp = queue.popleft()
    #     if tmp[0] == endword:
    #         return tmp[1]
    #     wordlist.discard(tmp[0])
    #     # 这里要多次遍历wordlist，即使每次筛掉一个也太耗时，每次遍历得到的信息没有充分利用
    #     for w in wordlist:
    #         if sum(tmp[0][i] != w[i] for i in range(wordlength)) == 1:
    #             queue.append((w, tmp[1]+1))
    # return 0

    # 2. 把对wordlist的搜索转换到，word的搜索上，依赖于单词长度不会太长的前提
    wordlist = set(wordlist)
    queue = deque([(beginword, 1)])
    wordlength = len(beginword)
    while queue:
        word, step = queue.popleft()
        if word == endword:
            return step
        for i in range(wordlength):
            # 对当前单词逐个字符替换，验证是否在单词列表中，如果在就更新状态后放入搜索队列
            # 这里对26个字母用了ascii去处理，也可以用标准库
            # from string import ascii_lowercase as ASCII_LOWERCASE
            for c in range(26):
                candidate = word[:i] + chr(97+c) + word[i+1:]
                if candidate in wordlist:
                    wordlist.remove(candidate)
                    queue.append((candidate, step+1))
    return 0

    # 3. todo: 双向bfs
