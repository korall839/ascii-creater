import helper
put=input("введите путь к асци БЕЗ РАЗШИРЕНИЯ: ")
a=helper.App_helper.loadApp(put,"asci")
if a == "":
	print("по данному местоположению нету файла")
	input("нажмите enter для завершения")
else:
	data=helper.App_helper.loadApp(put,"asci")
	for i in range(len(data)):
		for k in range(len(data[i])):
			print(data[i][k],end="")
		print()
	input("нажмите enter для завершения")