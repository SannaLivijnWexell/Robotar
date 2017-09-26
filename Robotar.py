# # nedan är exempel på variables
# robot_price = 900
# robot_count = 2
# robot_tax = 1.25
# book_price = 100
# book_count = 1
# book_tax = 1.06

# print(robot_price * robot_count * robot_tax + book_price * book_count * book_tax)

# # nedan är exempel på dictionaries

# robot = {"price": 900, "count": 2, "tax": 1.25}
# book = {"price": 100, "count": 1, "tax": 1.06}

# print(robot["price"] * robot["count"] * robot["tax"] + book["price"] * book["tax"]) 

# # Customers med dictionaries nedan:

# all_customers = [22, 32, 52]
# print(all_customers[1])






# # Nedan är exempel på klasser: större behållare och mer flexibla än dictionaries

# class Product:
# 	price = 0
# 	count = 0
# 	tax = 0

# robot = Product()
# robot.price = 900
# robot.count = 2
# robot.tax = 1.25

# book = Product()
# book.price = 100
# book.count = 1
# book.tax = 1.06

# print(robot.price * robot.count * robot.tax + book.price * book.count * book.tax)






# Nedan är en omskrivning som metod och klass. En metod är en behållare för kod som en vill köra flera gånger och "anropar".
# här är taxen inkluderat

# class Product:
# 	price = 0
# 	count = 0
# 	tax = 1.25

# 	def price_with_tax(self):
# 		return self.price * self.count * self.tax

# robot = Product()
# robot.price = 900
# robot.count = 2

# book = Product()
# book.price = 100
# book.count = 1
# book.tax = 1.06

# print(robot.price_with_tax() + book.price_with_tax())






# nedan är exempel på klass med konstruktor:

# class Product:
# 	price=0
# 	count=0
# 	tax=1.25
# # en konstruktor (magiska metod) som gör det lättare att definiera produkter:
# 	def __init__(self, price, count, tax): 
# 		self.price = price
# 		self.count = count
# 		self.tax = tax

# 	def price_with_tax(self):
# 		return self.price * self.count * self.tax

# robot = Product(price=900, count=2, tax=1.25)
# book = Product(price=100, count=1, tax=1.06)

# print(robot.price_with_tax() + book.price_with_tax())






# Nedan är exempel på lista med produkter istället för variabler

# class Product:
# 	price=0
# 	count=0
# 	tax= 0

# # en konstruktor (magiska metod) som gör det lättare att definiera produkter:
# 	def __init__(self, price, count, tax): 
# 		self.price = price
# 		self.count = count
# 		self.tax = tax

# 	def price_with_tax(self):
# 		return self.price * self.count * self.tax

# products = [Product(price=900, count=2, tax=1.25), Product(price=100, count=1, tax=1.06)]

# total_price = products[0].price_with_tax() + products[1].price_with_tax()

# print(total_price)






# Nedan är exempel på hur man räknar ut summan av varorna:

# class Product:

# # en konstruktor (magiska metod) som gör det lättare att definiera produkter:
# 	def __init__(self, price, count, tax): 
# 		self.price = price
# 		self.count = count
# 		self.tax = tax

# products = [Product(price=900, count=2, tax=1.25), Product(price=100, count=1, tax=1.06)]
# total_count = products[0].count + products[1].count
# print(total_count)






# Nedan är exmpel på for-loop

# class Product:
# 	price=0
# 	count=0
# 	tax= 0

# # en konstruktor (magiska metod) som gör det lättare att definiera produkter:
# 	def __init__(self, price, count, tax): 
# 		self.price = price
# 		self.count = count
# 		self.tax = tax

# 	def price_with_tax(self):
# 		return self.price * self.count * self.tax

# products = [Product(price=900, count=2, tax=1.25), Product(price=100, count=1, tax=1.06)]

# total_price = 0
# for product in products:
# 	total_price = total_price + product.price_with_tax()

# print(total_price)






# nedan är exempel på en If-sats. Om en vara är kostar mer än en viss summa t.ex.
# I detta fall får du 10% rabatt på varor som kostar mer än 500:-

# class Product:
# 	price=0
# 	count=0
# 	tax= 0

# en konstruktor (magiska metod) som gör det lättare att definiera produkter:
# 	def __init__(self, price, count, tax): 
# 		self.price = price
# 		self.count = count
# 		self.tax = tax

# 	def price_with_tax(self):
# 		total = self.price * self.count * self.tax
# 		if total > 500:
# 			return 0.9 * total
# 		else:
# 			return total

# products = [Product(price=900, count=2, tax=1.25), Product(price=100, count=1, tax=1.06)]

# total_price = 0
# for product in products:
# 	total_price = total_price + product.price_with_tax()

# print(total_price)







# NY PRODUKT: bananer 5:- (Tax 12%) & banankokbok 55:- (Tax 6%)

# Om du köper bananer för mer än 120 kr får du 10% rabatt på bananerna

class Product:
	price=0
	count=0
	tax= 0

	def __init__(self, price, count, tax): 
		self.price = price
		self.count = count
		self.tax = tax

	def price_with_tax(self):
		total = self.price * self.count * self.tax
		if total > 120:
			return 0.9 * total
		else:
			return total

products = [Product(price=5, count=55, tax=1.12), Product(price=55, count=1, tax=1.06), Product(price=5, count=55, tax=1.12), Product(price=55, count=1, tax=1.06)]

total_price = 0
for product in products:
	total_price = total_price + product.price_with_tax()

	print(total_price)















