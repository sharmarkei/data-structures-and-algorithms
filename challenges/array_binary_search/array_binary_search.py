def array_binary_search(lst, key):
  start_idx = 0
  stop_idx = len(lst)
  
  try:
    while True:
      middle = (start_idx + stop_idx) // 2
      if lst[middle] == key:
        return middle
      elif lst[middle] > key:
        stop_idx = middle - 1
      elif lst[middle] < key:
        start_idx = middle + 1
  except:
    return -1


print(array_binary_search([1, 2, 3, 4, 5], 3))
