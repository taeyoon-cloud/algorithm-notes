def hanoi(num_disk, start, target):
    if num_disk == 0:
        return
    
    hanoi(num_disk-1, start, 6-start-target)
    move_disk(num_disk, start, target)
    hanoi(num_disk-1, 6-start-target,target)


def move_disk(num, start, target):
    print(start, target)
    

num = int(input())
print(2**num - 1)
hanoi(num, 1, 3)