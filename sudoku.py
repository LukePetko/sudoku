from tkinter import *

def miesto(event):
	global x, y
	x = event.x // 20
	y = event.y // 20
	print(y, x, riadky[y][x], pov_riadky[y][x])
	# g.create_text(x * 20 + 10, y * 20 + 10, text = int(riadky[y][x]) + 1)
	# riadky[y][x] = "{}".format(int(riadky[y][x]) + 1)

def stlacenie(event):
	if pov_riadky[y][x] == "0":
		riadky[y][x] = event.char
		g.create_rectangle(x * 20 + 3, y * 20 + 3, x * 20 + 17, y * 20 + 17, fill = "white", outline = "")
		g.create_text(x * 20 + 10, y * 20 + 10, text = riadky[y][x])

sub = open("sudoku.txt", "r")
riadky = sub.readlines()
pov_riadky = list()
print(pov_riadky)
for i in range(len(riadky)):
	riadky[i] = riadky[i].strip()
	pov_riadky.append(riadky[i])
	riadky[i] = list(riadky[i])

g = Canvas(width = 180, height = 180, bg = "white")
g.pack()
g.bind("<Button-1>", miesto)
g.bind_all("<Key>", stlacenie)

for i in range(10):
	for j in range(10):
		g.create_rectangle(i * 20 - 20, j * 20 - 20, i * 20, j * 20)
for i in range(4):
	for j in range(4):
		g.create_rectangle(i * 60 - 60, j * 60 - 60, i * 60, j * 60, width = 2)


for i in range(len(riadky)):
	for j in range(len(riadky[i])):
		if riadky[j][i] != "0":
			g.create_text(i * 20 + 10, j * 20 + 10, text = riadky[j][i], fill = "gold")
		else:
			continue

g.mainloop()
