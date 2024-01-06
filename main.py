#o script precisa fornecer qual caminho deve se mover os arquivos
# o script precisa conter a função de mover mais de um arquivo ou e permitir que o script possa 
#mover todos da estrutura de uma vez
# o script precisa verificar se  os arquivos mencionados estão dentro do repositório e retornar 
#uma msg de erro caso não
#repetir o preocesso


#será perguntado ao usuário qual diretório os arquivos estão 
#em seguida iremo usar o os module para mover o usuário para o local onde estão os arquivos
#a classe irá herdar esse atributos e instanciar ao objeto
#
#a próxima função chamada copiar irá herdar esse atributos e usar o while para permitir que 
#cada loop o usuário possa mover os arquivos para um destino desejado
#
#vamos usar um for loop para fazer uma busca sequencial e verificar se os itens estão dentro 
#de uma variável que iremos criar para armazenar todos os arquivos listados
#
#vamos usar o if statment, o if stament permite que o computador possa tomar uma decisão de acordo 
#com os dados de entrada.
#
#e retornar uma msg de erro caso não esteja dentro e se caso estiver perdir para o usuário 
#colocar o novo destino


import os, shutil 

class usuario:
    def __init__(self, localiz):
        self.localiz=localiz
        os.chdir(self.localiz)

    def copiar(self): 
        self.rodar=True
        self.arquivos= os.listdir()

        print(f'seus arquivos: {self.arquivos}')
        destino=input('insira o destino:')
        
        while (self.rodar):
            arquivo=input('insira os arquivos ou q para sair:')
           
            for c in self.arquivos:
                if arquivo == c:
                    #destino=input('insira o destino:')
                    shutil.copy(src=arquivo, dst=destino)
            
            if arquivo == 'q':
                self.rodar=False
    
caminho=input('insira o caminho de onde estão os arquivos:')

try:
    mover=usuario(caminho)

    mover.copiar()
except FileNotFoundError:
    
    print('verifique se voce colocou o diretório corretamente: /home/user/...')