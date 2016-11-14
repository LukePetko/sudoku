from tkinter import *

def vynulovanie():
	global b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9, bs
	bs = [b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9]
	for i in range(len(bs)):
		bs[i] = False

def miesto(event):
	global x, y
	x = event.x // 20
	y = event.y // 20
	print(y, x, riadky[y][x], pov_riadky[y][x])

def stlacenie(event):
	if pov_riadky[y][x] == "0" and event.char in "123456789":
		riadky[y][x] = event.char
		g.create_rectangle(x * 20 + 3, y * 20 + 3, x * 20 + 17, y * 20 + 17, fill = "white", outline = "")
		g.create_text(x * 20 + 10, y * 20 + 10, text = riadky[y][x])

def kontrola():
	global error_boolean
	error_boolean = False
	kontrolne_riadky_x = 9 * [""]
	kontrolne_riadky_y = 9 * [""]
	kontrolne_riadky_kocky = 9 * [""]

# test na číslo 0

	for i in range(len(riadky)):
		if error_boolean == True:
			break
		for j in range(len(riadky[i])):
			if riadky[i][j] == "0":
				error_boolean = True
				break
			else:
				kontrolne_riadky_x[i] += riadky[i][j]
				kontrolne_riadky_y[i] += riadky[j][i]

	for i in range(3):
		for j in range(i * 3, (i + 1) * 3):
			for k in range(9):
				if k < 3:
					kontrolne_riadky_kocky[j] += riadky[j][k]
				elif 3 <= k < 6:
					kontrolne_riadky_kocky[j] += riadky[j][k]
				elif 6 <= k < 9:
					kontrolne_riadky_kocky[j] += riadky[j][k]

	print(kontrolne_riadky_kocky)

	# for i in range(len(riadky)):
	#


# test v riadku a stlpci

	if error_boolean == False:
		for i in range(len(kontrolne_riadky_x)):
			if error_boolean == True:
				break
			for j in range(1, 10):
				if kontrolne_riadky_x[i].find(str(j)) == -1 or kontrolne_riadky_y[i].find(str(j)) == -1 or kontrolne_riadky_kocky[i].find(str(j)) == -1:
					error_boolean = True
					break
		print(error_boolean)

sub = open("sudoku_spravne.txt", "r")
riadky = sub.readlines()
pov_riadky = list()
print(pov_riadky)
for i in range(len(riadky)):
	riadky[i] = riadky[i].strip()
	pov_riadky.append(riadky[i])
	riadky[i] = list(riadky[i])

print(riadky)
plocha = Tk()

g = Canvas(plocha, width = 180, height = 180, bg = "white")
g.pack()
g.bind("<Button-1>", miesto)
g.bind_all("<Key>", stlacenie)
b = Button(plocha, text = "Ukonči", command = kontrola)
b.pack()

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
mainloop()
