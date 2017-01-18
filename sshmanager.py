#!/usr/bin/env python
import sys
import os
import time
import source.db
import source.log
import source.screen
import source.ssh
import source.config
import argparse
#import optparse
sys.path.insert(0,'./source')
class SshManager():


    def __init__(self):
        #DECLARA AS CARIAVEIS DE MAIN
        self.mensagem="Metodo SshManager"
        self.home = os.environ['HOME']
        self.pwd = os.environ['PWD']
        self.user = os.environ['USER']
        self.bin = sys.argv[0]
        self.args = len(sys.argv)
        #INSTANCIA AS CLASSES QUE SERAO USADAS
        self.config = source.config.Config()
        self.debug = self.config.debug
        self.defuser = self.config.defuser
        self.ssh = source.ssh.Ssh(self.debug)
        self.screen = source.screen.Screen(self.debug)
        self.log = source.log.Log(self.debug,self.config.logdir,self.config.loggeral)
        self.db = source.db.Db(self.debug,self.pwd + "/" + self.config.dbfile)
        if self.debug == 1:
            print(self.mensagem)
            print("home = \"" + self.home + "\"")
            print("pwd = \"" + self.pwd + "\"")
            print("user = \"" + self.user + "\"")
            print("bin = \"" + self.bin + "\"")
            print("argumentos = \"" + str(self.args) + "\"")
    def procuraHost(self,hostname):
        self.db.procuraHost(hostname)
    def conectarHost(self,hostname,enderecoIp,usuario):
        retorno = 0
        return retorno
    def selecionarUsuario(self,hostname):
        self.usuario = "root"
        return self.usuario
    def atualizaHost(self,hostname,usuario):
        self.data = time.strftime("%Y%m%d%H%M%S")
        self.retorno = 0
        return self.retorno
    def cadastraUsuario(self,usuario):
        self.retorno = 0
        return self.retorno
    def cadastraHost(self,hostname,enderecoIp):
        self.db.cadastraHost(hostname,enderecoIp)
        retorno = 0
        return retorno
    def alterarUsuarioPadrao(self,usuario):
        self.config.atualizaJson("defuser",usuario)
    def usuarioPadrao(self):
        usuario = self.config.defuser
        print(usuario)
    def listarHosts(self):
        self.db.listarHosts()
    def apagaTudo(self):
        apagar="nao implementado"
        return apagar
    def ajuda(self):
        print("help")


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print args.accumulate(args.integers)

'''
sessao = SshManager()
optionParser = optparse.OptionParser(usage="usage: %prog [options] arg1 arg2")
groupParser = optparse.OptionGroup(optionParser, "Conectar","Use para conectar a um host")
groupParser.add_option('-u', '--usuario', help='Usuario para conexao',default='root', dest='usuario')
groupParser.add_option('-s','--senha', help='Senha para conexao',default='123mudar', dest='senha')
groupParser.add_option('-n','--hostname', help='hostname',default="localhost", dest='hostname')
groupParser.add_option('-e','--endereco', help='Endereco ip do host',default='127.0.0.1',dest='endereco')
optionParser.add_option_group(groupParser)
groupParser = optparse.OptionGroup(optionParser, "Pesquisar","Pesquisa por um host ou IP na base")
groupParser.add_option('-p', '--pesquisa', help='pesquisa',default='root', dest='pesquisa')
groupParser.add_option('-l', '--listar', action="store_true", dest="verbose", default=True)
optionParser.add_option_group(groupParser)
groupParser = optparse.OptionGroup(optionParser, "Cadastrar","Cadastra um host ou IP na base")
groupParser.add_option('-c', '--cadastrar', help='cadastrar',default='root', dest='cadastrar')
optionParser.add_option_group(groupParser)
groupParser = optparse.OptionGroup(optionParser, "Apagar","Apaga um host ou IP da base")
groupParser.add_option('-a', '--apagar', help='apagar',default='root', dest='apagar')
optionParser.add_option_group(groupParser)
groupParser = optparse.OptionGroup(optionParser, "DEBUG",'Habilita o DEBUG da aplicacao')
groupParser.add_option('-d', '--debug',default='true')
optionParser.add_option_group(groupParser)
(options, args) = optionParser.parse_args()

if options.l == True:
    print("True")
'''