def numWaterBottles(numBottles: int, numExchange: int) -> int:
	ans = 0
	mod = 0 # 空酒瓶
	# 只要手里还有酒就执行“喝酒-换酒”流程
	while numBottles:
	    ans += numBottles # 手里的酒喝掉
	    # 用喝掉的酒瓶 numBottles 以及上次留下的空酒瓶 mod 去换酒
	    numBottles, mod = divmod(numBottles+mod, numExchange)
	return ans
