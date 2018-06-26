def pancakesorting(stack):
    for i in reversed(range(len(stack))):
        stack = flip(stack,findlargestpancake(stack,i))
        print("Flip Up", stack)
        stack = flip(stack, i)
        print("Flip Down", stack)
    return stack

def findlargestpancake(stack,index):
    largest_pancake = stack[index]
    largest_index = index
    for i in range(index):
        if stack[i] > largest_pancake:
            largest_pancake = stack[i]
            largest_index = i

    print("Insert Spatula in index", largest_index, "Size", largest_pancake)
    return largest_index

def flip(stack,index):
    newstack = stack[:(index+1)]
    newstack.reverse()
    newstack += stack[(index+1):]
    return newstack

stack = [1, 4, 5, 2, 3, 8, 6, 7, 9, 0]
print(pancakesorting(stack))