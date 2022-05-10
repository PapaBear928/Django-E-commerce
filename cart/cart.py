from store.models import Products
from django.conf import settings
from decimal import Decimal


class Cart():
	'''
	Nasza bazowa klasa wózka.Zapewnia pewne domyślne zachowania klasy, które w razie potrzeby będą mogły być dziedziczone
	lub zastępowane.
	'''

	def __init__(self, request):
		self.session = request.session
		cart = self.session.get('session_key')
		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}
		self.cart = cart

	def add(self, product, qty):
		'''
		Dodajemy odświeżanie koszyka naszego użytkownika podczas sesyji
		'''
		product_id = str(product.id)

		if product_id in self.cart:
			self.cart[product_id]['qty'] += qty
		else:
			self.cart[product_id] = {'price': str(product.price), 'qty': qty}

		self.save()

	def __iter__(self):
		'''
		Zbierze dane z product_id z sesji aby wysłać zapytanie do DB i zwrócić produkty
		'''
		product_ids = self.cart.keys()
		products = Products.products.filter(id__in=product_ids)
		cart = self.cart.copy()

		for product in products:
			cart[str(product.id)]['product'] = product

		for item in cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['qty']
			yield item

	def __len__(self):
		'''
		weź dane z koszyka i zachowaj liczbę QTY
		'''

		return sum(item['qty'] for item in self.cart.values())

	def get_subtotal_price(self):
		return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

	def get_total_price(self):

		before_delivery = sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

		if before_delivery == 0:
			shipping = Decimal(0.00)
		else:
			shipping = Decimal(14.49)

		total = before_delivery + Decimal(shipping)
		totalrounded = round(total, 2)
		return totalrounded

	def delete(self, product):
		'''
		Usuwanie rzeczy ze sesji
		'''
		product_id = str(product)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()

	def update(self, product, qty):
		'''
		Uaktualnianie rzeczy ze sesji
		'''

		product_id = str(product)
		if product_id in self.cart:
			self.cart[product_id]['qty'] += qty
		self.save()

	def save(self):
		self.session.modified = True

	def clear(self):
		# wymazujem koszyk
		del self.session[settings.CART_SESSION_ID]
		self.save()
