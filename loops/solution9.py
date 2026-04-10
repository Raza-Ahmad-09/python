items = ["apple","bnana","orange","apple","mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate", item)
        break
    unique_item.add(item)



# | Iteration | item   | unique_item (before)       | Action                             |
# | --------- | ------ | -------------------------- | ---------------------------------- |
# | 1         | apple  | {}                         | Add → {"apple"}                    |
# | 2         | bnana  | {"apple"}                  | Add → {"apple","bnana"}            |
# | 3         | orange | {"apple","bnana"}          | Add → {"apple","bnana","orange"}   |
# | 4         | apple  | {"apple","bnana","orange"} | ❌ Already exists → Duplicate found |
