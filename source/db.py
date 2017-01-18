import sqlite3
class Db():
    def __init__(self,debug,base):
        self.debug = debug
        self.mensagem="Metodo db"
        self.base = base
        if self.debug == 1:
            print(self.mensagem)
            print(self.base)
        conn = sqlite3.connect(self.base)
        c = conn.cursor()
        c.execute("create table IF NOT EXISTS hosts(endereco varchar(15) primary key, nome varchar(30),grupoid integer, up real, tryup real, lastlogin real,lastuser varchar(30) )")
        conn.commit()
        c.execute("create table IF NOT EXISTS grupo(groupid integer primary key, nome varchar(30))")
        conn.commit()
        conn.close()
    def listarHosts(self):
        conn = sqlite3.connect(self.base)
        c = conn.cursor()
        contador = 1
        for row in c.execute("select * from hosts"):
            print("(" + str(contador) + ") ip=" + row[0] + " " + "nome=\"" + row[1] + "\"")
            contador = contador + 1
        conn.commit()
        conn.close()
        return contador
    def procuraHost(self,hostname):
        conn = sqlite3.connect(self.base)
        c = conn.cursor()
        contador = 1
        for row in c.execute("select * from hosts where nome like \'%" + hostname + "%\' or endereco ==  \'" + hostname + "\'"):
            print("(" + str(contador) + ") ip=" + row[0] + " " + "nome=\"" + row[1] + "\"")
            contador = contador + 1
        conn.commit()
        conn.close()
        return contador
    def cadastraHost(self,hostname,endereco):
        conn = sqlite3.connect(self.base)
        c = conn.cursor()
        c.execute("insert into hosts values ('" + endereco + "','" + hostname + "','','','','','')")
        conn.commit()
        conn.close()
