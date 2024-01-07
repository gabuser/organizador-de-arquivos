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

class deletar(usuario):

    def __init__(self,localiz):
        usuario.__init__(self, localiz)
    
    def apagar(self):
        self.remover=True
        self.arquivos=os.listdir()
        print(f'seus arquivos: {self.arquivos}')

        while self.remover:
            escolh=input('insira os arquivos:')
            for c in self.arquivos:
                if escolh == c: 
                    os.remove(f'{self.localiz}/{escolh}')
            if escolh == 'q':
                self.remover=False
            

esclh=input('o que deseja fazer a(apagar arquivos) c(copiar arquivos):')
caminho=input('insira o caminho de onde estão os arquivos:')

if esclh== 'c':
    try:
        mover=usuario(caminho)
        mover.copiar()
    except FileNotFoundError:
        print('diretório inexistente')

else:
    try:
        tirar=deletar(caminho)
        tirar.apagar()
    except FileNotFoundError:
        print('diretório inexistente')

#try:
#    mover=usuario(caminho)
#
#    mover.copiar()
#except FileNotFoundError:
#    
#    print('verifique se voce colocou o diretório corretamente: /home/user/...')