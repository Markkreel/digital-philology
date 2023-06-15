class Tree:
    def __init__(self, leaves):
        self.leaves = leaves

    def set_season(self, season):
        try:
            if season == "Winter" or season == "Autumn":
                self.leaves = False
                print("Leaves have fallen off the tree.")
            else:
                self.leaves = True
                print("The tree has leaves.")
        except Exception as e:
            print("An error occurred:", e)


# Create an instance of Tree with leaves
my_tree = Tree(True)
print("Initial state of the tree:", my_tree.leaves)

# Set the season to Winter
my_tree.set_season("Winter")
print("Updated state of the tree:", my_tree.leaves)

# Set the season to Spring
my_tree.set_season("Spring")
print("Updated state of the tree:", my_tree.leaves)
