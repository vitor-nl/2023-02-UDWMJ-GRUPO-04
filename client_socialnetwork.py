from client import Client

class Client_socialnetwork():
    def __init__(self, client: Client, socialnetwork, senha):
        self.client = client
        self.socialnetwork = socialnetwork
        self.senha = senha
    
    def getEmail(self):
        return self.client.email
    
    def recuperaSenha(self, senhaAtual, senhaNova):
        if senhaAtual == self.senha:
            self.senha = senhaNova
            print("Sua senha foi alterada!")
        else:
            print("Ops.. A senha informado nao condiz com a atual.")