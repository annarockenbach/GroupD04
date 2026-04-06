from puzzles import get_question, check_answer, get_hint, get_points, get_total_puzzles
from player import Player
from email_system import send_email

# Create 2 players
p1 = Player("Walaa")
p2 = Player("Anna")

players = [p1, p2]

print("🎮 Escape Room Simulation\n")

# Loop through puzzles
while True:
    finished_players = [p for p in players if p.finished]

    if len(finished_players) > 0:
        break

    for player in players:
        if player.finished:
            continue

        print(f"\n--- {player.name}'s Turn ---")
        print(get_question(player.stage))

        user_input = input("Enter answer (or type 'hint'): ")

        # Hint system
        if user_input.lower() == "hint":
            if player.hints_used < 2:
                print("💡 Hint:", get_hint(player.stage, player.hints_used))
                player.use_hint()
            else:
                print("⚠️ No more hints.")
            continue

        # Check answer
        if check_answer(player.stage, user_input):
            print("✅ Correct!")

            points = get_points(player.stage)
            player.add_score(points)
            player.next_stage()

            if player.stage == get_total_puzzles():
                player.finish_game()
                print(f"\n🏆 {player.name} ESCAPED THE ROOM!")
                break
        else:
            print("❌ Wrong!")

# Determine winner & loser
players.sort(key=lambda x: x.score, reverse=True)

winner = players[0]
loser = players[1]

print("\n📊 Final Results:")
for p in players:
    print(p.show_status())

# Send emails (EDIT EMAILS HERE)
winner_email = "your_email@gmail.com"
loser_email = "your_email@gmail.com"

send_email(
    winner_email,
    "Escape Room Winner",
    f"🎉 Congratulations {winner.name}! You won with {winner.score} points!"
)

send_email(
    loser_email,
    "Escape Room Result",
    f"Hello {loser.name}, you scored {loser.score}. Better luck next time!"
)
