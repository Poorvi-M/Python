def calculate_love_score(name1, name2):
    count1=0
    count2=0
    count3=0
    count4=0
    love=['L','O', 'V', 'E', 'l', 'o', 'v', 'e']
    true=['T', 'R', 'U', 'E', 't', 'r', 'u', 'e']
    for char in name1:
        if char in love:
            count1+=1 
    for char in name2:
        if char in love:
            count2+=1 
    
    total=(count1+count2)
    
    
    for char in name1:
        if char in true:
            count3+=1 
    for char in name2:
        if char in true:
            count4+=1 
    total2= count3+count4
    final_total= str(total2)+ str(total)
    print(f"{final_total}")

calculate_love_score("", "")
