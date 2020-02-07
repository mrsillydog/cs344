from gps import gps

################################
# Lab_3.py
# Written by Ian Adams for CS344 at Calvin University, Spring 2020
# 
# Problem specification for a GPS problem that GPS cannot solve, but a human easily can.
# Initial state: An orca, a seal, and a fish walk into a sandbar.
# Goal state: Only the orca walks out.
# Operations: The seal can only eat the fish. The orca can only eat the seal. The fish can't eat the orca or seal.
# Obvious human solution: Seal will eat fish. Orca then eats the seal.
# GPS' failure: Since the first goal state is "no seal", the program first looks for a way to remove the seal.
#   So, the orca immediately eats the seal, but then there's no seal left to eat the fish.
# Fix: there does not seem to be a way to fix it by changing op order or intermediate state. However,
#   reordering the goal states so "no fish" precedes "no seal" fixes it and GPS can solve it.
################################

problem = {
    "start1": ["orca", "seal", "fish"],
    "finish1": ["no seal", "no fish", "orca"],

    "ops": [
        {
            "action": "orca eats seal",
            "preconds": [
                "orca",
                "seal"
            ],
            "add": [
                "no seal"
            ],
            "delete": [
                "seal"
            ]
        },
        {
            "action": "seal eats fish",
            "preconds": [
                "fish",
                "seal"
            ],
            "add": [
                "no fish"
            ],
            "delete": [
                "fish"
            ]
        }
    ]
}
#
def main():
    start = problem['start1']
    finish = problem['finish1']
    ops = problem['ops']
    actionSequence = gps(start, finish, ops)
    if actionSequence is None:
        print("plan failure...")
        return
    for action in actionSequence:
        print(action)

if __name__ == '__main__':
    main()
