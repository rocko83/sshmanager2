class Log:
    def __init__(self,debug,logpath,loggeral):
        self.debug = debug
        self.mensagem="Metodo log"
        self.logdir = logpath
        self.loggeral = logpath + "/" + loggeral
        if self.debug == 1:
            print(self.mensagem)
            print(self.logdir)
            print(self.loggeral)
