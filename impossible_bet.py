import random


def play_bet(participants=100, times=1000, checks=50):
    """Simulate the bet x times with x participants."""
    wins = 0
    losses = 0
    for time in range(times):
        boxes = list(range(1, participants + 1))
        random.shuffle(boxes)
        for participant in range(1, participants + 1):
            found = False
            count = 0
            to_open = participant
            while found == False and count < checks:
                if boxes[to_open - 1] == participant:
                    found = True
                else:
                    to_open = boxes[to_open - 1]

                count += 1
            if found == False:
                losses += 1
                break
            elif found == True and participant == participants:
                wins += 1
    return (wins, losses)

def results(wins, losses):
    total = wins + losses
    win_percentage = (wins / total) * 100
    lose_percentage = (losses / total) * 100
    return win_percentage, lose_percentage



if __name__ == '__main__':
    participants = int(input(print('participants')))
    times = int(input(print('times')))
    checks = int(input(print('checks')))

    print(results(*play_bet(participants=participants, times=times, checks=checks)))
