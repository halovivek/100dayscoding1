def addtoInventory(inventory, addItems):
    inv = {'Gol coin': 42, 'rope': 12}
    dragonloot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addtoInventory(inv, dragonloot)
    displayInventory(inv)
    