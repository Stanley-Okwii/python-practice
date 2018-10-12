def my_sort(number_list):
    odd_list = []
    even_list = []
    # results = []
    for i in number_list:
        if(i%2 == 1):
            odd_list.append(i)
        else:
            even_list.append(i)

    # results = odd_list.sort(reverse=True)
    odd_list.sort()
    even_list.sort()
    # print(results)
    return(odd_list + even_list)

print(my_sort([2,3,4,45,52,46,78,86,7]))
