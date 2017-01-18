import json
class Config:
    def __init__(self):
        self.mensagem="Metodo Config"
        self.conffile = "etc/conf.json"
        self.dados = json.loads(open(self.conffile).read())
        self.dbfile = self.dados["dbfile"]
        self.logdir = self.dados["logdir"]
        self.loggeral = self.dados["loggeral"]
        self.defuser = self.dados["defuser"]
        self.debug = int(self.dados["debug"])
        if self.debug == 1:
            print(self.mensagem)
            print(self.dbfile)
            print(self.logdir)
            print(self.loggeral)
    def atualizaJson(self,variavel,valor):
        self.dados[variavel] = valor
        with open(self.conffile, 'w') as confsaida:
            json.dump(self.dados,confsaida)
