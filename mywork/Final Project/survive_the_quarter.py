# Name: Mahika GODBOLE          Group: A        <-- TODO: write your own name
#
# FEATURE CHOSEN: (a) Streak bonus: three reputation gains in a row give 500 EUR.
#  Why?
#   It rewards the player for making good choices several days in a row,
#   and it only needs a counter that goes up or resets, so it was simple to add
#   without touching the rest of the game.
#
# ---- THE FOUR QUESTIONS (TODO: answer in your own words) ----
# 1. What goes in?
#    Separator: comma (,)
#    Columns: ID: A unique numeric identifier for each scenario.
#             Scenario: The text description of the situation or crisis the player faces.
#             OptionA,OptionB,OptionC: The text descriptions of the three choices available to the player for each scenario.
#             BudgetA,BudgetB,BudgetC: The monetary change (in EUR) to the player's budget when selecting option A, B, or C respectively.
#             ReputationA,ReputationB,ReputationC: The change to the player's reputation gauge when selecting option A, B, or C respectively.
#             FeedbackA,FeedbackB,FeedbackC: The narrative feedback text shown to the player explaining the outcome of their chosen action.
#    How the Numbers Are Written:
#             The numbers are written as standard integers (both positive and negative).
#             Negative values (e.g., -800, -5) represent costs, penalties, or losses.
#             Positive values (e.g., 15) represent financial gains or boosts to reputation.
#             Zero (0) indicates no change to that specific gauge.
#    How to Find the Impact of Option B:
#             To find the impact of Option B, you look up the specific row for the scenario and read BudgetB for its financial cost/gain and ReputationB for its effect on the player's reputation.
# 2. What happens? (one day, step by step)
#    1) Print the day number, both gauges, the situation and options A, B, C.
#    2) Ask for A, B or C, and ask again until the answer is valid
#       (lowercase accepted).
#    3) Apply the budget and reputation change; reputation is capped at 100.
#    4) Print the feedback line and the changes.
#    5) Update the streak counter; at 3 gains in a row, add 500 EUR.
#    6) Save the day in the history list as a tuple.
#    7) If budget or reputation is 0 or less, stop the game immediately.
# 3. What comes out?
#    The player sees either "You are fired" with the reason, or "Quarter
#    survived!" with the budget, reputation, score and title. Then the best
#    and worst move, and "Saved in results.csv". One line of results.csv looks like:
#    Lea,6350,100,CMO Material,2026-10-30
# 4. What could go wrong? (at least three)
#    - scenarios_A.csv is missing: the program prints a clear message and stops.
#    - A row has a broken number or missing column: that row is skipped and
#      the game continues with the others.
#    - The player types something other than A, B or C: the program asks again.
#    - The player types no name: the name "Player" is used.
#    - The input is closed (Ctrl+D): the program says bye instead of crashing.
#    - results.csv does not exist yet: it is created with a header line.
#
# What is missing / not finished: nothing

import csv
import random
from datetime import date

SCENARIO_FILE = "scenarios_A.csv"
RESULTS_FILE = "results.csv"
DAYS = 10
START_BUDGET = 10000
START_REPUTATION = 50
MAX_REPUTATION = 100
STREAK_LENGTH = 3
STREAK_BONUS = 500


def load_scenarios(filename):
    """Read the CSV and return a list of scenarios.
    Each scenario is (situation, {"A": option_tuple, "B": ..., "C": ...})
    and each option tuple is (text, budget_change, reputation_change, feedback)."""
    scenarios = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                options = {}
                for letter in ("A", "B", "C"):
                    option = (
                        row["Option" + letter],
                        int(row["Budget" + letter]),
                        int(row["Reputation" + letter]),
                        row["Feedback" + letter],
                    )
                    options[letter] = option
                scenarios.append((row["Scenario"], options))
            except (ValueError, KeyError, TypeError):
                # a broken row is skipped instead of crashing the game
                print("Skipping a broken row (ID " + str(row.get("ID")) + ")")
    return scenarios


def ask_name():
    """Ask the player's name; use a default if nothing is typed."""
    name = safe_input("What is your name? ").strip()
    if name == "":
        name = "Player"
    return name


def safe_input(prompt):
    """input() that ends the game politely if the input is closed (Ctrl+D)."""
    try:
        return input(prompt)
    except EOFError:
        print("\nInput closed. Bye!")
        raise SystemExit


def ask_choice():
    """Ask for A, B or C until the answer is valid. Returns 'A', 'B' or 'C'."""
    answer = safe_input("Your choice (A, B or C): ").strip().upper()
    while answer not in ("A", "B", "C"):
        answer = safe_input("Please type A, B or C: ").strip().upper()
    return answer


def apply_choice(budget, reputation, option):
    """Apply an option to the gauges. Returns the new (budget, reputation).
    Reputation can never go above 100."""
    text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = min(reputation + reputation_change, MAX_REPUTATION)
    return budget, reputation


def get_title(budget, reputation):
    """Return (score, title) for a player who survived."""
    score = reputation + budget // 200
    if score < 95:
        title = "Eternal Intern"
    elif score < 120:
        title = "Growth Hacker"
    elif score < 140:
        title = "CMO Material"
    else:
        title = "Viral Legend"
    return score, title


def find_best_and_worst(history):
    """history: list of (reputation_change, day, option_text) tuples.
    Python compares tuples element by element, starting with the first one,
    so max() and min() look at the reputation change first."""
    return max(history), min(history)


def save_result(name, budget, reputation, title):
    """Append one line to results.csv (add a header if the file is new)."""
    try:
        with open(RESULTS_FILE, "r", encoding="utf-8"):
            has_file = True
    except FileNotFoundError:
        has_file = False
    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not has_file:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([name, budget, reputation, title, date.today().isoformat()])


def show_move(label, move):
    """Print the best or worst move."""
    change, day, text = move
    print(label + ": day " + str(day) + ', "' + text + '" (' + format(change, "+d") + ")")


def play_game():
    try:
        scenarios = load_scenarios(SCENARIO_FILE)
    except FileNotFoundError:
        print("Cannot find " + SCENARIO_FILE + ". Put it in the same folder as this script.")
        return
    if len(scenarios) == 0:
        print("No usable scenario in " + SCENARIO_FILE + ".")
        return

    name = ask_name()
    random.shuffle(scenarios)

    budget = START_BUDGET
    reputation = START_REPUTATION
    history = []
    streak = 0
    fired_reason = ""

    for day in range(1, min(DAYS, len(scenarios)) + 1):
        situation, options = scenarios[day - 1]
        print("\n--- Day " + str(day) + " ---")
        print("[Budget: " + str(budget) + " EUR | Reputation: " + str(reputation) + "/100]")
        print(situation)
        for letter in ("A", "B", "C"):
            print("  " + letter + ": " + options[letter][0])

        letter = ask_choice()
        option = options[letter]
        budget, reputation = apply_choice(budget, reputation, option)
        print(option[3])
        print("Budget " + format(option[1], "+d") + " EUR, Reputation " + format(option[2], "+d"))

        # Feature (a): three reputation gains in a row give 500 EUR
        if option[2] > 0:
            streak += 1
        else:
            streak = 0
        if streak == STREAK_LENGTH:
            budget += STREAK_BONUS
            streak = 0
            print("Streak bonus! Three good days in a row: +" + str(STREAK_BONUS) + " EUR")

        history.append((option[2], day, option[0]))

        if budget <= 0:
            fired_reason = "the budget hit zero"
            break
        if reputation <= 0:
            fired_reason = "your reputation hit zero"
            break

    print("\n==============================")
    if fired_reason != "":
        title = "Fired"
        print("You are fired: " + fired_reason + ".")
        print("Budget: " + str(budget) + " EUR, reputation: " + str(reputation) + "/100")
    else:
        score, title = get_title(budget, reputation)
        print("Quarter survived!")
        print("Budget left: " + str(budget) + " EUR, reputation: " + str(reputation) + "/100")
        print("Final score: " + str(score))
        print(name + ", your title: " + title)

    best, worst = find_best_and_worst(history)
    show_move("Best move", best)
    show_move("Worst move", worst)

    save_result(name, budget, reputation, title)
    print("Saved in " + RESULTS_FILE)


play_game()
