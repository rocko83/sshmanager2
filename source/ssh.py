class Ssh:
    def __init__(self,debug):
        self.debug = debug
        self.mensagem="Metodo ssh"
        if self.debug == 1:
            print(self.mensagem)
