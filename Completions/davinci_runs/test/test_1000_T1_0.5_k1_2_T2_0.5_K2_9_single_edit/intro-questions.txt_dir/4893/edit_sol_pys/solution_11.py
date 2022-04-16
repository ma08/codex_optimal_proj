
#-*-coding:utf-8-*-

def min_distance(n, p, distances):
	distances = sorted(distances) # 按照升序排序
	result = distances[0] # 起始位置
	for i in range(1, n):
		if distances[i] - distances[i-1] > result + p*i: # 计算距离
			result = distances[i] - p*i
	return result

n, p = map(int, raw_input().split()) # 输入个数和步长
distances = map(int, raw_input().split()) # 输入距离
print min_distance(n, p, distances) # 输出最小距离
