def reverse_num(number):
    res = ""
#     for i in range(len(str(number))-1,-1,-1):
#         res += str(number)[i]
    res += "".join([str(number)[i] for i in range(len(str(number))-1,-1,-1)])
    return int(res)

def descend_num(number):
    res = ""
    number_str = list(str(number))
    while len(number_str) > 0:
        max_num = str(max(number_str))
        res += max_num
        number_str.remove(max_num)
    return int(res)
            
        
    
    
def is_kaprekar(number):
    descend_number = descend_num(number)
    reversed_number = reverse_num(descend_number)
    difference = descend_number - reversed_number
    flag = False
    if difference == number:
        flag= True
    if flag:
        return (f'{number} is Kaprekar')
    else:
        return (f'{number} is not Kaprekar')

# Enter a number
number = int(input("Enter Number: "))
print(is_kaprekar(number))
