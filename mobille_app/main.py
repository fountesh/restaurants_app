from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import requests


class Restaurant_App(App):

    promotions = []

    def answer(self):
        print('Натиснув')
        respones = requests.get('http://127.0.0.1:8000/api/promotions/')
        if respones.status_code == 200:
            self.promotions = respones.json()
            for promotion in self.promotions:
                print(promotion)
                app.root.add_widget(Button(text = promotion['title']))
        else:
            print('Error')      


    def build(self):
        box = BoxLayout()
        button = Button(text='Кнопка')
        box.add_widget(button)
        button.on_press = self.answer
        return box


app = Restaurant_App()

app.run()