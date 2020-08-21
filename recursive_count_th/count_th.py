'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    th_string = "th"

    n1 = len(word); 
    n2 = len(th_string); 
      
    # Base Case 
    if (n1 == 0 or n1 < n2): 
        return 0; 
  
    # Recursive Case 
    # Checking if the first 
    # substring matches 
    if (word[0 : n2] == th_string): 
        return count_th(word[n2 - 1:]) + 1; 
  
    # Otherwise, return the count  
    # from the remaining index 
    return count_th(word[n2 - 1:]); 












    # if (len(word) == 0 or len(word) < len('th')):
    #     return 0
    
    # if (word[0: len('th')] == 'th'):
    #     return count_th(word[len(word) -1:]) + 1
    
    # return count_th(word[len('th') - 1:])








    # if word == None:
    #     return None
    
    # cur_ind = 0
    # count = 0
    # cur_ind = word.find('th')
    # if cur_ind == -1:
    #     return count
    # count += 1
    # count_th(word[cur_ind+1:])