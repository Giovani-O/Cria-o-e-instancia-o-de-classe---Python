from ComputerClass import Computador

estoque = []

pc1 = Computador('Ryzen 7', 'RTX 3070Ti', '32Gb')
pc2 = Computador('Core i9', 'RX 6900XT', '32Gb')
pc3 = Computador('Athlon 200GE', 'Vega 3', '8Gb')

estoque.append(pc1)
estoque.append(pc2)
estoque.append(pc3)

for objeto in estoque:
    objeto.relatorio()