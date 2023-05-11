# TODO: The code below will crash & return an IndexError. That is because the list of fruits is out of range.

fruits = ["Apple", "Pear", "Orange"]

# TODO: Catch the exception & make sure the code does not crash
def make_pie(index):
    try:
      fruit = fruits[index]
    except IndexError:
       print("Fruit pie")
    else:
      print(fruit + " pie")

make_pie(4)