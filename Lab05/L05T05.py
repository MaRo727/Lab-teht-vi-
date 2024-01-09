def get_cost(x, y, z):
    return str(round((y * x / 100 * z), 2)) + " €"
print(get_cost(100,7.5,1.88))
print(get_cost(220,6.9,1.88))