class Computador:
    def __init__(self, a_processador, a_gpu, a_ram):
        self.processador = a_processador
        self.gpu = a_gpu
        self.ram = a_ram

    def relatorio(self):
        print("O processador é um: " + str(self.getProcessador()) + " A GPU é uma: " + str(self.getGpu()) + " e a máquina tem " + str(self.getRam()) + " de RAM")

    def setProcessador(self, nome):
        self.processador = nome

    def getProcessador(self):
        return (self.processador)

    def setGpu(self, nome):
        self.gpu = nome

    def getGpu(self):
        return (self.gpu)

    def setRam(self, quantidade):
        self.ram = quantidade

    def getRam(self):
        return (self.ram)