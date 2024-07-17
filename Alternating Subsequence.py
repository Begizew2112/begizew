def max_alt_subsq_sum(t_cases):
    results = []
    for t in t_cases:
        n, a = t
        curr_max = a[0]
        max_sum = 0
        
        for i in range(1, n):
            if (a[i] > 0 and curr_max > 0) or (a[i] < 0 and curr_max < 0):
                curr_max = max(curr_max, a[i])
            else:
                max_sum += curr_max
                curr_max = a[i]
        
        max_sum += curr_max
        results.append(max_sum)
    
    return results

t = int(input())
t_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    t_cases.append((n, a))

results = max_alt_subsq_sum(t_cases)
for result in results:
    print(result)
