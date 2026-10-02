import helper
put=input("введите путь к асци БЕЗ РАЗШИРЕНИЯ: ")
a=helper.App_helper.loadApp(put,"asci")
if a == "":
	print("по данному местоположению нету файла")
	if input("создать файл?(y,N): ") == "y":
		v=open(put+".asci","w")
		v.write(" ")
	else:
		exit()
print("вводите асци, когда закончите введите 0 без пробелов")
asci_all=[]
asc=input()
while asc != "0":
	b=[]
	for i in range(len(asc)):
		b.append(asc[i])
	asci_all.append(b)
	asc=input()
helper.App_helper.saveApp(put,"asci",asci_all)