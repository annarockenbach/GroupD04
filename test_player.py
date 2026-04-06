from player import Player

p1 = Player("Walaa")

print("Starting player status:")
print(p1.show_status())

p1.add_score(10)
p1.use_hint()
p1.next_stage()

print("\nAfter one puzzle:")
print(p1.show_status())

p1.finish_game()

print("\nAfter finishing the game:")
print(p1.show_status())
