from tkinter import *
from os import remove # na vymazanie súboru po dokončení ak nejaký jestvuje
import platform

load_bool = False


# UDALOSTI V SUDOKU

def miesto(event):
	global x, y
	x = event.x // 40
	y = event.y // 40

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



# KONTROLA

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

	if error_boolean == True:
		txt = "Máš to zle, veľa šťastia nabudúce!"
	else:
		txt = "Gratulujem! Si najlepší"
		if load_bool == True:
			remove(load_sub_name)
	plocha_2 = Tk()
	Label(plocha_2, text = txt).pack()



# SPÚŠŤANIE

def sudoku_choise(num):
	global su
	su = "sudoku/sudoku_" + num

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
			for j in range(len(riadky[i])):
				if riadky[j][i] != "0":
					g.create_text(i * 40 + 20, j * 40 + 20, text = riadky[j][i], fill = "blue", font = ("Times New Roman", 30))
				else:
					continue



# UKLADANIE

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
		save_sub.write("{}".format(su))
		save_sub.close()
		save_plocha.destroy()
		plocha.destroy()



# NAČÍTAVANIE

def load():
	global load_e, load_plocha
	load_plocha = Tk()
	Label(load_plocha, text = "Napíš názov uloženého súboru: ").grid(row = 0, column = 0)
	load_e = Entry(load_plocha)
	load_e.grid(row = 0, column = 1)
	Label(load_plocha, text = ".txt").grid(row = 0, column = 2)
	Button(load_plocha, text = "Hraj!", command = load_file).grid(row = 1, column = 0, sticky = W)

def load_file():
	global load_bool, load_riadky, load_sub_name
	if load_e.get() != "":
		load_bool = True
		load_sub_name = "saves/" + load_e.get() + ".txt"
		load_sub = open("saves/{}.txt".format(load_e.get()), "r")
		load_riadky = load_sub.readlines()
		load_plocha.destroy()
		preplocha.destroy()


# FARBY

def zmena_farieb():
	color_plocha = Tk()
	Label(color_plocha, text = "Zmena farieb!").grid(row = 0, column = 0, sticky = W)

# MENU

preplocha = Tk()
preplocha.title("Menu")
b1 = Radiobutton(preplocha, text = "Sudoku 1", value = 0, command = lambda: sudoku_choise("00")).grid(row = 0, column = 0, sticky = W)
b2 = Radiobutton(preplocha, text = "Sudoku 2", value = 1, command = lambda: sudoku_choise("01")).grid(row = 1, column = 0, sticky = W)
e = Entry()
e.grid(row = 2, column = 0)
button_1 = Button(preplocha, text = "Rieš", command = ries).grid(row = 3, column = 0, sticky = W)
button_2 = Button(preplocha, text = "Náhlad", command = nahlad).grid(row = 3, column = 0, sticky = W, padx = 52)
button_3 = Button(preplocha, text = "Farby", command = zmena_farieb).grid(row = 3, column = 1, sticky = E)
menu = Menu(preplocha)

file_menu = Menu(menu, tearoff = 0)
file_menu.add_command(label = "Načítaj", command = load, accelerator = "Command+O")
menu.add_cascade(label = "Súbor", menu = file_menu)

preplocha.bind_all("Command-O", load)
preplocha.config(menu = menu)
preplocha.mainloop()


# ČÍTANIE
if load_bool == False:
	sub = open("{}.txt".format(su), "r")
elif load_bool == True:
	sub = open("{}.txt".format(load_riadky[9]), "r")
	su = load_riadky[9]
riadky = sub.readlines()
pov_riadky = list()
for i in range(len(riadky)):
	riadky[i] = riadky[i].strip()
	pov_riadky.append(riadky[i])
	riadky[i] = list(riadky[i])


plocha = Tk()
plocha.title("Sudoku")

g = Canvas(plocha, width = 360, height = 360, bg = "white")
g.pack()
g.bind("<Button-1>", miesto)
g.bind("<Button-2>", vymazanie)
g.bind_all("<Key>", stlacenie)
g.bind("<Command-s>", save)
# Button(plocha, text = "Ukonči", command = kontrola).pack(side = "left")
# Button(plocha, text = "Ulož", command = save).pack(side = "left")

game_menu = Menu(plocha)

game_file_menu = Menu(game_menu)
game_file_menu.add_command(label = "Ulož", command = save, accelerator = "Command+S")
game_file_menu.add_command(label = "Skontroluj", command = kontrola)
game_file_menu.add_command(label = "Ukonči bez kontroly", command = lambda: exit(), accelerator = "Command+Q")
game_menu.add_cascade(label = "Súbor", menu = game_file_menu)

plocha.config(menu = game_menu)
g.bind("<Command-s>", save)

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

if load_bool == True:
	for i in range(9):
		for j in range(9):
			if load_riadky[j][i] != "0" and riadky[j][i] == "0":
				g.create_text(i * 40 + 20, j * 40 + 20, text = load_riadky[j][i], fill = "black", font = ("Times New Roman", 30))
			else:
				continue
	for i in range(len(riadky)):
		load_riadky[i] = load_riadky[i].strip()
		riadky[i] = list(load_riadky[i])

mainloop()
