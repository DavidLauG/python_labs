#Creating function min_max
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError ("List can not be empty")
    return(min(nums), max(nums))
    
#Creating function unique_sorted
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

#Creating the flatten funcion
def flatten(mat: list[list | tuple]) -> list:
    flat_list=[]
    for element in mat:
        if isinstance(element, (list,tuple)):
            flat_list.extend(element)
        else:
            raise TypeError('The element or line is not a list or tuple')
    return flat_list

print(min_max([42])) # (1, 5)
print(unique_sorted([-1, -1, 0, 2, 2,4])) # [1, 2, 3]
print(flatten([[1,2],(3,4),[5]])) # [1, 2, 3, 4, 5]