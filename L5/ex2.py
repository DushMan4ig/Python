mark = [5, 5, 4, 3, 2, 1, 4]
maxim = max(mark)
minim = min(mark)
for i in range(len(mark)):
    if mark[i] == maxim:
        mark[i] = minim
print(mark)
        
    
    