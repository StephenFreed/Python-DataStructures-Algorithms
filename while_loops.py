def delete_starting_evens(lst):
  while len(lst) >= 0:
    if len(lst) > 0 and lst[0] % 2 == 0:
      lst = lst[1:]
      continue
    elif lst == None:
      lst = []
      return lst
    else:
      return lst