from sage.all import *

x = var('x')
print(solve(x**2 == 4, x))

# Симметрическая группа S_4
G = SymmetricGroup(4)

print("Порядок группы:", G.order())
print("Абелева ли:", G.is_abelian())
print("Простая ли:", G.is_simple())
print("Центр группы:", G.center())

# Элементы группы (перестановки в циклической записи)
g = G("(1,2,3)")
h = G("(1,2)")
print("Произведение g * h:", g * h)
print("Порядок элемента:", g.order())

# Классы сопряженности
print("Число классов сопряженности:", len(G.conjugacy_classes()))