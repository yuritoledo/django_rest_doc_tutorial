from datetime import datetime

FMT = "%H:%M"

h1 = input("Digite a hora de início: ")
h2 = input("Digite a hora de término: ")

h1 = datetime.strptime(h1, FMT)
h2 = datetime.strptime(h2, FMT)

diff = h2 - h1

print(diff)
