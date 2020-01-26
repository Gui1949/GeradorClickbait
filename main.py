import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from random import randint

kvfile = Builder.load_file('style.kv')

print('hello world')

class Main(Screen):

    def frase(self):
        frase_num = randint(1,10)
        
        if frase_num == 1:
            frase_tela = 'Caguei na pia e olha no que deu'

        if frase_num == 2:
            frase_tela = '24 Horas algemado com o meu cachorro'  

        if frase_num == 3:
            frase_tela = 'Reagindo as minhas inscritas dançando funk (12 ANOS!!)'     

        if frase_num == 4:
            frase_tela = 'Minha mãe reagindo a funks pesados (Apanhei??)'

        if frase_num == 5:
            frase_tela = 'Gastei R$6000 em materiais escolares'                               

        if frase_num == 6:
            frase_tela = 'Enganei a Interesseira da XJ6 (FICOU PUTA!)'

        if frase_num == 7:
            frase_tela = 'Fiquei no supermercado de madrugada (FUI PRESO?)'

        if frase_num == 8:
            frase_tela = 'Reagindo a gostosas dançando funk (+18)'

        if frase_num == 9:
            frase_tela = 'Como ganhar dinheiro fácil na internet sem sair de casa'            

        if frase_num == 10:
            frase_tela = 'A cada kill uma peça de roupa a menos (FREE FIRE)'            

        frase_tela = frase_tela.upper()
        self.manager.get_screen('frase_gerada').ids.lbl_frase.text = frase_tela
        self.manager.current = 'frase_gerada'                     

class frase_gerada(Screen):
        pass     

sm = ScreenManager()
sm.add_widget(Main(name='main'))
sm.add_widget(frase_gerada(name='frase_gerada'))

class app(App):

    def build(self):
        return sm

app().run()        
