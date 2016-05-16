import simpleguitk as simplegui

store = 0
operand = 0
def output():
	pass
	print "Store   = ",store
	print "Operand = ",operand
	print ""

def swap():
	global store, operand
	operand, store=store, operand
	output()

def add():
	global store, operand
	store=store+operand
	output()

def sub():
	global store, operand
	store=store-operand
	output()

def mul():
	global store, operand
	store=store*operand
	output()

def div():
	global store, operand
	store=float(store)/float(operand)
	output()

def modst(text_input):
	global store
	store=float(text_input)
	output()

def modop(text_input):
	global operand
	operand=float(text_input)
	output()


frame=simplegui.create_frame("Calc",200,200)
frame.add_button("Print",output,100)
frame.add_button("Swap",swap,100)
frame.add_button("Add",add,100)
frame.add_button("Subtract",sub,100)
frame.add_button("Multiply",mul,100)
frame.add_button("Divide",div,100)
frame.add_input("Store",modst,50)
frame.add_input("Operand",modop,50)



frame.start()