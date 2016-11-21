from tkinter import *

def miesto(event):
	global x, y
	x = event.x // 40
	y = event.y // 40
	print(y, x, riadky[y][x], pov_riadky[y][x])

def stlacenie(event):
	if pov_riadky[y][x] == "0" and event.char in "123456789":
		riadky[y][x] = event.char
		g.create_rectangle(x * 40 + 3, y * 40 + 3, x * 40 + 37, y * 40 + 37, fill = "white", outline = "")
		g.create_text(x * 40 + 20, y * 40 + 20, text = riadky[y][x], font = ("Times New Roman", 30))

def vymazanie(event):
	x = event.x // 40
	y = event.y // 40
	if pov_riadky[y][x] == "0":
		riadky[y][x] = "0"
		g.create_rectangle(x * 40 + 3, y * 40 + 3, x * 40 + 37, y * 40 + 37, fill = "white", outline = "")

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

	if error_boolean == False:
		for i in range(len(kontrolne_riadky_x)):
			if error_boolean == True:
				break
			for j in range(1, 10):
				if kontrolne_riadky_x[i].find(str(j)) == -1 or kontrolne_riadky_y[i].find(str(j)) == -1 or kontrolne_riadky_kocky[i].find(str(j)) == -1:
					error_boolean = True
					break
		print(error_boolean)

	if error_boolean == True:
		txt = "Máš to zle, veľa šťastia nabudúce!"
	else:
		txt = "Gratulujem! Si najlepší"
	plocha_2 = Tk()
	Label(plocha_2, text = txt).pack()

def su0():
	global su
	su = "sudoku/sudoku_00"
def su1():
	global su
	su = "sudoku/sudoku_01"
def ries():
	global su
	if e.get() != "":
		su = "sudoku/" + e.get()
	if su != "":
		preplocha.destroy()
def nahlad():
	global riadky, su
	if e.get() != "":
		su = "sudoku/" + e.get()
	if su != "":
		sub = open("{}.txt".format(su), "r")
		riadky = sub.readlines()
		pov_riadky = list()
		print(pov_riadky)
		for i in range(len(riadky)):
			riadky[i] = riadky[i].strip()
			pov_riadky.append(riadky[i])
			riadky[i] = list(riadky[i])

		plocha = Tk()
		g = Canvas(plocha, width = 360, height = 360, bg = "white")
		g.pack()
		for i in range(10):
			for j in range(10):
				g.create_rectangle(i * 40 - 40, j * 40 - 40, i * 40, j * 40)
		for i in range(4):
			for j in range(4):
				g.create_rectangle(i * 120 - 120, j * 120 - 120, i * 120, j * 120, width = 2)


		for i in range(len(riadky)):
			print(su)
			for j in range(len(riadky[i])):
				if riadky[j][i] != "0":
					g.create_text(i * 40 + 20, j * 40 + 20, text = riadky[j][i], fill = "blue", font = ("Times New Roman", 30))
				else:
					continue

def save():
	global save_e, save_plocha
	save_plocha = Tk()
	Label(save_plocha, text = "Meno: ").grid(row = 0, column = 0, sticky = W)
	save_e = Entry(save_plocha)
	Label(save_plocha, text = ".txt").grid(row = 0, column = 2, sticky = E)
	save_e.grid(row = 0, column = 1, sticky = E)
	Button(save_plocha, text = "Ulož a ukonči!", command = save_file).grid(row = 1, column = 1, sticky = S)
	mainloop()

def save_file():
	save_riadky = list()
	if save_e.get() != "":
		save_txt = save_e.get()
		save_sub = open("saves/{}.txt".format(save_txt), "w")
		for i in range(len(riadky)):
			save_riadky.append("")
			for j in range(len(riadky[i])):
				save_riadky[i] += riadky[i][j]
			save_sub.write(save_riadky[i])
			save_sub.write("\n")
		save_sub.close()
		save_plocha.destroy()
		plocha.destroy()
preplocha = Tk()
b1 = Radiobutton(preplocha, text = "Sudoku 1", value = 0, command = su0).grid(row = 0, column = 0, sticky = W)
b2 = Radiobutton(preplocha, text = "Sudoku 2", value = 1, command = su1).grid(row = 1, column = 0, sticky = W)
e = Entry()
e.grid(row = 2, column = 0)
button_1 = Button(preplocha, text = "Rieš", command = ries).grid(row = 3, column = 0, sticky = W)
button_2 = Button(preplocha, text = "Náhlad", command = nahlad).grid(row = 3, column = 0, sticky = W, padx = 60)
preplocha.mainloop()

sub = open("{}.txt".format(su), "r")
riadky = sub.readlines()
pov_riadky = list()
print(pov_riadky)
for i in range(len(riadky)):
	riadky[i] = riadky[i].strip()
	pov_riadky.append(riadky[i])
	# riadky[i] = list(riadky[i])

plocha = Tk()

g = Canvas(plocha, width = 360, height = 360, bg = "white")
g.pack()
g.bind("<Button-1>", miesto)
g.bind("<Button-2>", vymazanie)
g.bind_all("<Key>", stlacenie)
Button(plocha, text = "Ukonči", command = kontrola).pack(side = "left")
Button(plocha, text = "Ulož", command = save).pack(side = "left")

for i in range(10):
	for j in range(10):
		g.create_rectangle(i * 40 - 40, j * 40 - 40, i * 40, j * 40)
for i in range(4):
	for j in range(4):
		g.create_rectangle(i * 120 - 120, j * 120 - 120, i * 120, j * 120, width = 2)


for i in range(len(riadky)):
	for j in range(len(riadky[i])):
		if riadky[j][i] != "0":
			g.create_text(i * 40 + 20, j * 40 + 20, text = riadky[j][i], fill = "blue", font = ("Times New Roman", 30))
		else:
			continue

mainloop()
