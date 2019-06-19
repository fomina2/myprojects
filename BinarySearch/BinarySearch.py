print('Please enter numbers into list, press enter after each number')
print('To finish input - press enter')
a: int = int(input('-->>'))
mass = []
while True:
    try:
        mass.append(a)
        a = int(input('-->> '))
    except:
        break

print('Enter number for search in the list')
x: int = int(input('-->> '))
mass.sort()
left: int = 0
right: int = len(mass) - 1
mid = round((left + right) / 2)


if mass[mid] != x:
    while left <= right:
            mid = round((left + right) / 2)
            if mass[mid] == x:
                print('Number', mass[mid], 'was found in the list')
                break
            if mass[mid] != x:
                if mass[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            if left > right:
                print('Entered number was not found in the list')
else:
    print('Number', mass[mid], 'was found in the list')
