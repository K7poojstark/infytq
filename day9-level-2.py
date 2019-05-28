
#PF-Prac-13
import math

def close_number(num1,num2,num3):
    if math.fabs(num1-num2)==1 and math.fabs(num3-num2)>=2 and math.fabs(num3-num1)>=2:
        return True
    elif math.fabs(num3-num2)==1 and math.fabs(num1-num2)>=2 and math.fabs(num3-num1)>=2:
        return True
    elif math.fabs(num1-num3)==1 and math.fabs(num3-num2)>=2 and math.fabs(num2-num1)>=2:
        return True
    else:
        return False
    
print(close_number(5,4,2))


#PF-Prac-16
def rotate_list(input_list,n):
    output_list=[]
    for i in range(len(input_list)-n,len(input_list)):
        output_list.append(input_list[i])
    for i in range(0,len(input_list)-n):
        output_list.append(input_list[i])
    return output_list

input_list= [1,2,3,4,5,6]
output_list=rotate_list(input_list,4)
print(output_list)


#PF-Prac-21
def check_numbers(num1,num2):
    #start writing your code here
    num_list=[]
    for i in range(num1,num2+1):
        for j in range(num1,num2+1):
            if(i%j==0 and i not in num_list and i!=j):
                num_list.append(i)
    count=len(num_list)
    return [num_list,count]

num1=2
num2=20
print(check_numbers(num1, num2))



#PF-Prac-32
def check_squares(number):
    for i in range(1,10000):
        for j in range(i+1,10000):
            if(i*i + j*j ==number):
                return True
    return False


number=68
print(check_squares(number))

#PF-Prac-36
def find_target_positions(input_string, target_word):
    target_list=[]
    temp_list = input_string.split(" ")
    for i in range(0,len(temp_list)):
        if(temp_list[i]==target_word):
            target_list.append(i)

    return target_list

def find_inverted_index(input_string):
    target_dict={}
    old_list = input_string.split(" ")
    for i in old_list:
        dict = {i:find_target_positions(input_string,i)}
        target_dict.update(dict)

    return target_dict
    
    
input_string="we dont need no education we dont need no thought control no we dont"
result_dict=find_inverted_index(input_string)
print(result_dict)


#PF-Prac-39
def max_populated_state(cities_dict,state):
    max_pop = 0
    for items in cities_dict:
        if items['State'] == state:
            if int(items['Population'] > max_pop):
                index1 = cities_dict.index(items)
                max_pop = items['Population']
            
    max_populated_city = cities_dict[index1]
    
    return max_populated_city
    
cities_dict = [
{'Name':'Vancouver','State':'WA','Population':161791},
{'Name':'Salem','State':'OR','Population':154637},
{'Name':'Seattle','State':'WA','Population':608660},
{'Name':'Spokane','State':'WA','Population':208916},
 ]
state="WA"
print("The city details are:",cities_dict)
print("State:",state)
output=max_populated_state(cities_dict,state)
print("The highest populated city in the given state is:",output)




      
