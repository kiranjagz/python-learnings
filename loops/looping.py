monday_temp = [9.1, 9.3, 5.3]

for temp in monday_temp:
    print(round(temp))
    print('Done')
    
for letter in 'hello':
    if letter == 'h':
        print(letter.title())
    else:
        print('<<>>')
        
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
    
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))