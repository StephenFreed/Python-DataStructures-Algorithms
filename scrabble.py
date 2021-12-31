letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {
  key:value 
  for key, value 
  in zip(letters, points)
}
letter_to_points[' '] = 0
# Dict of letter and points
print(letter_to_points)

# Function to get points for word.
def score_word(word):
  point_total = 0
  for letter in word:
      point_total += letter_to_points.get(letter,0)
  return point_total

brownie_points = score_word('BROWnIE')
print(brownie_points)

player_to_words = {
  'player1': ['BLUE','TENNIS','EXIT'], 
  'wordNerd':['EARTH', 'EYES', 'MACHINE'], 
  'Lexi Con':['ERASER', 'BELLY','HUSKY'], 
  'Prof Reader':['ZAP','COMA','PERIOD']}
print(player_to_words)
print()
# Dict of player and total points

def update_point_totals():
  player_to_points = {}
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  print(player_to_points)

player_to_words['Test Player'] = [""]
print(player_to_words)
print()
update_point_totals()
# Appends word to player key if there. If not adds player, value. 
def play_word(player, word):
  if player in player_to_words:
    player_to_words[player].append(word)
  else:
    player_to_words[player] = word

letters += [letters.lower() for letter in letters]
points *= 2