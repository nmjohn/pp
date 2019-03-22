import math
import random

# We set some hyper-parameters for deck creation, number of trials and opponent's deck sizes.
MAX_LAND = 60
NUMBER_OF_TRIALS_PER_DECK = 1000
CARDS_IN_OPPONENTS_DECK = 60

# Stores all the results of each run.
success = [ [-1] * NUMBER_OF_TRIALS_PER_DECK for _ in range(MAX_LAND+1) ]

# Build a deck that has number_of_islands lands in deck and the rest Persistent Petitioners.
for number_of_islands in range(0, MAX_LAND+1):
  for trial_number in range(0, NUMBER_OF_TRIALS_PER_DECK):
    number_of_islands_in_deck = number_of_islands
    number_of_petitioners_in_deck = MAX_LAND - number_of_islands
    cards_in_opponents_deck = CARDS_IN_OPPONENTS_DECK

    # Your cards in play
    islands_in_play = 0
    petitioners_in_play = 0

    # Your cards in hand
    islands_in_hand = 0
    petitioners_in_hand = 0

    turn = -1

    while (cards_in_opponents_deck > 0) and (number_of_petitioners_in_deck + number_of_islands_in_deck) > 0:
      turn += 1
      # Assume opponent plays first
      if turn == 0:
        cards_in_opponents_deck -= 7
      elif turn == 1:
        # Doesn't draw on turn 1
        pass
      else:
        cards_in_opponents_deck -= 1

      # If opponent had to draw this turn and lost, go to the break condition.
      if cards_in_opponents_deck < 0:
        break

      if turn == 0:
        cards_to_draw = 7
      else:
        cards_to_draw = 1
      # Your cards in hand
      for _ in range(cards_to_draw):
        card = random.randint(0, number_of_islands_in_deck + number_of_petitioners_in_deck - 1)
        if card < number_of_islands_in_deck:
          islands_in_hand += 1
          number_of_islands_in_deck -= 1
        else:
          petitioners_in_hand += 1
          number_of_petitioners_in_deck -= 1
      
      if turn == 0:
        continue
      
      #print('Turn number ' + str(turn))
      # Play logic:
      # Always play a land if you can.
      if islands_in_hand > 0:
        islands_in_hand -= 1
        islands_in_play += 1


      # The number of cards you can mill are 12 * floor(petitioners / 4) + (non just casted petitioners % 4)
      tappable_petitioners = petitioners_in_play
      untappable_petitioners = 0
      untapped_islands = islands_in_play
      while untapped_islands >= 2 and petitioners_in_hand >= 1:
        untapped_islands -= 2
        petitioners_in_hand -= 1
        petitioners_in_play += 1
        untappable_petitioners += 1
      
      # Try to tap 4 petitioners first
      while (tappable_petitioners + untappable_petitioners) >= 4:
        tapped = 0
        if untappable_petitioners >= 4:
          tapped = 4
          untappable_petitioners -= 4
        else:
          tapped = untappable_petitioners
          untappable_petitioners = 0
          
        if tapped < 4:
          left = 4 - tapped 
          tapped = 4
          tappable_petitioners -= left

        if tapped == 4:
          cards_in_opponents_deck -= 12
        else: 
          print('ERROR Tapped')
          raise Error()

      # With left over land, try to tap tappable petitioners.
      tapped_mills = min(tappable_petitioners, untapped_islands)
      cards_in_opponents_deck -= tapped_mills
    if cards_in_opponents_deck > 0:
      success[number_of_islands][trial_number] = -1
    else:
      success[number_of_islands][trial_number] = turn

print("Islands\tMin Turns\tMax Turns\tAverage\tLost")
for i in range(len(success)):
  minimum = min(success[i])
  maximum = max(success[i])
  average = float(sum(success[i])) / float(len(success[i]))
  lost = sum([1 if x == -1 else 0 for x in success[i]])
  print("%d\t%d\t\t%d\t\t%d\t%d" % (i, minimum, maximum, average, lost))
