with open("SitRush.txt") as f:
    lines = list(map(float, f.read().replace(',', '.').splitlines()))
    print(*lines)