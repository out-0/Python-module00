def ft_garden_intro() -> None:
    """Display garden introduction with Rose plant details."""

    print("=== Welcome to My Garden ===")

    name: str = "Rose"
    height: int = 25
    age: int = 30

    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days\n")

    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
