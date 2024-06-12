"""
1. Create a Movie class
2. Create Multiple movie objects
3. Add these objects to list
4. Try to get objects one by one from list and print data
"""


class Movie(object):

    def __init__(self, title, min, hero):
        self.title = title
        self.runtime = min
        self.hero = hero

    def printer(self):
        print(
            f"""TItle is: {self.title}\nRuntime is: {self.runtime}\n
        hero is: {self.hero}"""
        )


list_of_movies = []

while True:
    title = input("Enter the tittle of movie: ")
    min = input("Enter the length of the movie: ")
    hero = input("Enter the name of hero: ")
    obj = Movie(title, min, hero)
    list_of_movies.append(obj)
    print("\n\nMovie added into the list")
    ans = input("Do you want to add another movie?")
    if ans != "y":
        break

print("All movies information")
for obj in list_of_movies:
    obj.printer()
