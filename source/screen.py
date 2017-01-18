class Screen:
    def __init__(self,debug):
        self.debug = debug
        self.mensagem="Metodo screen"
        if self.debug == 1:
            print(self.mensagem)
