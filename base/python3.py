def printall(message, item):
	print (message, end="")
	print(item)
def dict_func():
	dict = {}
	dict['1'] = "tom"
	dict['2'] = "jerry"
	printall("init result:", dict)
	dict['2'] = "jake"
	printall("change value:",dict)
def  turbe_func():
	turbe = ()
	printall("init turbe:", turbe)

dict_func()

