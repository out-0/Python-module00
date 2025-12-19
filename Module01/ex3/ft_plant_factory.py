class Plant:
    """Plant class represent initial information about plant"""
    def __init__(self, name: int, starting_height: int, starting_age: int):
        """Constructor for the base elements for a plant"""
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age
        print(f"Created: {self.name} ", end="")
        print(f"({self.starting_height}cm, {self.starting_age} days)")


def create_plants() -> None:
    """Create 5 plants objects and initial their status"""
    Plant("Rose", 25, 30)
    Plant("Oak", 200, 365)
    Plant("Cactus", 5, 90)
    Plant("Sunflower", 80, 45)
    Plant("Fern", 15, 120)
    print("\nTotal plants created: 5")


print("=== Plant Factory Output ===")
create_plants()
