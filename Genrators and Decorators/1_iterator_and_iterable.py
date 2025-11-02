my_foods = ['apple', 'bannana', 'cherry']

for food in my_foods:
    for food2 in my_foods:
        if food == food2:
            print(f"Skipping food {food}")
            continue
        print(f"Cooking {food} with {food2}")




class CountTOIterator:
    def __init__(self, max_vaalue):
        self.max = max_vaalue
        self.current = 1


    def __iter__(self):
        return self
    

    def __next__(self):
        if self.current <= self.max:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration
        

counter  = CountTOIterator(5)

for count in counter:
    print(count)