from client import Client
from category import Category
from product import Product
from order import Order
from orderitem import Orderitem

#Cliente
rogerim = Client("Rogerim", "python", "Rua thurusbango thurusbago", "(51) 99999999", "Rogerim@gmail.com", "M")
print(f"\n{rogerim.first_name} {rogerim.last_name}, se cadastrou na loja.\n")

#Categorias dos produtos
tenis = Category("0001", "Tenis", "Categorias de tenis")
print(f"Categiria {tenis.name} foi cadastrada!\n")

#Produtos
nike_sb = Product("Tenis Nike SB", "Tenis nike sb, muito bom!", "01/01/1980", 1, tenis) #1 = Ativo, #2 Inativo
print(f"Produto {nike_sb.name} foi cadastrado!\n")

#Ordem de compra
Rogerim_que_compra = Order(1, rogerim)#1 = Ativo, #2 Inativo
print(f"Cliente: {Rogerim_que_compra.client.first_name}, realizou uma ordem de compra de um produto produto no valor de {Rogerim_que_compra.total_price}\n")

#Comprando item
Rogerim_ta_comprando = Orderitem(2, 200, Rogerim_que_compra, tenis)
print(f"Rogerim ta comprando o produto: {Rogerim_ta_comprando.product.name}")

Rogerim_que_compra.total_price(Rogerim_ta_comprando)

print(Rogerim_que_compra.total_price)