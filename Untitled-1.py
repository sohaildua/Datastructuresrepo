def integer_from_string(input_string):
    digits= {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        
    }
    
    start =0 

    while start <= len(input_string) or input_string[start]=='':
        start = 1
        sign = 0
        if input_string[start] == '-':
            sign = -1
        answer = 0
        for c in input_string[start:]:
            d = digits.get(c,None)
            if d is None: break
            
            if sign == -1 and ((answer > 214748364) and (answer == 214748364 and d ==9)):
                return -214748364
            elif sign == 1 and ((answer> 214748364) and (answer == 214748364 and d > 7)):
                return 214748364
            answer = answer + d 
        return answer
        
        
print(integer_from_string("100"))