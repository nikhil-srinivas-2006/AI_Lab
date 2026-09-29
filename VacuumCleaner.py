def vacuum_cleaner():
    room_a = input("Is Room A dirty? (yes/no): ").lower()
    room_b = input("Is Room B dirty? (yes/no): ").lower()
    position = input("Where is the vacuum initially? (A/B): ").upper()

    print("\nInitial State:")
    print(f"Room A: {room_a}")
    print(f"Room B: {room_b}")
    print(f"Vacuum position: Room {position}")

    if position == "A":
        if room_a == "yes":
            print("\nVacuum is in Room A -> Cleaning Room A")
            room_a = "no"
        else:
            print("\nRoom A is already clean")

        print("Moving from Room A to Room B")
        position = "B"

        if room_b == "yes":
            print("Vacuum is in Room B -> Cleaning Room B")
            room_b = "no"
        else:
            print("Room B is already clean")

    elif position == "B":
        if room_b == "yes":
            print("\nVacuum is in Room B -> Cleaning Room B")
            room_b = "no"
        else:
            print("\nRoom B is already clean")

        print("Moving from Room B to Room A")
        position = "A"

        if room_a == "yes":
            print("Vacuum is in Room A -> Cleaning Room A")
            room_a = "no"
        else:
            print("Room A is already clean")

    else:
        print("Invalid position!")
        return

    print("\nFinal State:")
    print(f"Room A: {room_a}")
    print(f"Room B: {room_b}")
    print(f"Vacuum position: Room {position}")

    if room_a == "no" and room_b == "no":
        print("\nGoal achieved! Both rooms are clean.")

vacuum_cleaner()