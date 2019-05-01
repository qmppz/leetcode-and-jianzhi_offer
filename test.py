

def get_no_repeat_substr(s):
    
    windows = []
    no_repeat_set = set()
    max_len = 0
    
    i=0
    for i in range(len(s)):
        if s[i] not in no_repeat_set:
            no_repeat_set.update(s[i])
            windows.append(s[i])
        else:
            max_len = max(max_len, len(no_repeat_set))
            windows = windows[ windows.index(s[i])+1 : ]
            
            no_repeat_set = set(windows)
        i+=1
    return max_len
            
        
a=[1,2,3,4,5,6,7]
print(a[:3],a[:111])


