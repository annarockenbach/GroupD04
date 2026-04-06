from puzzles import get_question, check_answer, get_hint, get_points, get_total_puzzles
from player import Player

# Create a player
player = Player("Walaa")

print("🎮 Welcome to Escape Room Test\n")

# Loop through all puzzles
while player.stage < get_total_puzzles():

    print(f"\n--- Puzzle {player.stage + 1} ---")
    print(get_question(player.stage))

    while True:
        user_input = input("Enter answer (or type 'hint'): ")

        # If user asks for hint
        if user_input.lower() == "hint":
            if player.hints_used < 2:
                print("💡 Hint:", get_hint(player.stage, player.hints_used))
                player.use_hint()
            else:
                print("⚠️ No more hints available.")
            continue

        # Check answer
        if check_answer(player.stage, user_input):
            print("✅ Correct!")

            # Add points
            points = get_points(player.stage)
            player.add_score(points)

            # Move to next puzzle
            player.next_stage()
            break
        else:
            print("❌ Wrong answer, try again.")

# Game finished
player.finish_game()

print("\n🏆 Game Finished!")
print(player.show_status())
