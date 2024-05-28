num_dig = int(input('how many digits: '))
numbers = {}
for num in range(num_dig):
    number = input('enter the numbers: ')
    try:
        numbers[number] +=1
    except:
        numbers[number] =1

print(numbers)