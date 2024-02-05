import re
import utils

day = 2

def getGameNumber(line: str) -> int:
    gamePattern = r"Game (\d+):"
    if re.match(gamePattern, line):
        return int(re.match(gamePattern, line).group(1))
    return -1

def getBags(game: str):
    bagPattern = r"(\d+) (red|blue|green)"
    bags = {"red": 0, "green": 0, "blue": 0}
    for match in re.finditer(bagPattern, game):
        value, color = match.groups()
        bags[color] += int(value)
    return bags

def parseInputLinePart1(line: str) -> dict[int, dict[str, int]]:
    ALLOWED_RED = 12
    ALLOWED_GREEN = 13
    ALLOWED_BLUE = 14

    gameNumber = getGameNumber(line)
    if gameNumber == -1:
        return {}

    games = line.split(";")
    bags = {"red": 0, "green": 0, "blue": 0}
    for game in games:
        t_bags = getBags(game)
        if t_bags["red"] <= ALLOWED_RED and t_bags["green"] <= ALLOWED_GREEN and t_bags["blue"] <= ALLOWED_BLUE:
            bags["red"] += t_bags["red"]
            bags["green"] += t_bags["green"]
            bags["blue"] += t_bags["blue"]
        else :
            return {}
        
    if bags != {"red": 0, "green": 0, "blue": 0}:
        return {gameNumber: bags}

def parseInputLinePart2(line: str) -> dict[int, dict[str, int]]:
    gameNumber = getGameNumber(line)
    if gameNumber == -1:
        return {}

    games = line.split(";")
    bags = {"red": 0, "green": 0, "blue": 0}
    for game in games:
        t_bags = getBags(game)
        bags["red"] = max(t_bags["red"], bags["red"])
        bags["green"] = max(t_bags["green"], bags["green"])
        bags["blue"] = max(t_bags["blue"], bags["blue"])
        
    if bags != {"red": 0, "green": 0, "blue": 0}:
        return bags

def part1(data: list[str]) -> int:
    games = {}
    for line in data:
        games.update(parseInputLinePart1(line))

    s = 0
    for id, _ in games.items():
        s += id

    return s

def part2(data: list[str]) -> int:
    games = []
    for line in data:
        game = parseInputLinePart2(line)
        if game != {}:
            games.append(game)
    
    s = 0
    for game in games:
        s += game["red"] * game["green"] * game["blue"]

    return s

def main():
    data = utils.readInput(day=day)
    # data = utils.readTestInput(day=day)

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))

if __name__ == "__main__":
    main()
