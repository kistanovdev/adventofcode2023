def parse_rounds(lst: list[str]):

  res = {'red': 0,'green' : 0,'blue': 0}
  for line in lst:
    items = line.split(",")
    for item in items:
      count, color = item.strip().split(" ")
      res[color] = max(res[color], int(count))
  return res

def separate_input(line:str):
  game, inputs = line.split(":")
  rounds = inputs.strip().split(';')
  parsed_game = int(game.split(" ")[-1])
  parsed_rounds = parse_rounds(rounds)

  return (parsed_game, parsed_rounds)

def main():
  possible = {'red': 12,'green' : 13,'blue': 14}
  print(sum([game if all([count <= possible[color] for color, count in rounds.items()]) else 0 for game, rounds in [separate_input(line) for line in [line.strip() for line in open("input.txt")]] ]))

if __name__=="__main__":
  main()