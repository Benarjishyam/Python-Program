from collections import defaultdict
from collections import Counter

def find_Sub_String(string): 
      
    n = len(string) 
    
    #To get no.of distinct characters
    a=Counter(list(string))
    distinct_count = len(a)
    
      
    curr_cnt = defaultdict(lambda: 0)
    count = 0
    start = 0
    min_len = n 
   
    #Sliding Window approach to solve the problem
    
    for i in range(n): 
        curr_cnt[string[i]] += 1
     
        if curr_cnt[string[i]] == 1: 
            count += 1
     
        if count == distinct_count: 
            while curr_cnt[string[start]] > 1: 
                if curr_cnt[string[start]] > 1: 
                    curr_cnt[string[start]] -= 1
                      
                start += 1
                  
          
            len_window = i - start + 1
              
            if min_len > len_window: 
                min_len = len_window 
                start_index = start 
  
    return len(str(string[start_index: start_index +min_len]))
                                   
# Driver code 
if __name__=='__main__': 
    
    s=raw_input()
    res= find_Sub_String(s)
    print(res)
