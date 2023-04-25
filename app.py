import toga
from toga.style.pack import *

class App(toga.App):

    def select_first_file(self, widget):
        def after(widget, filepath):
            if filepath:
                self.first_route = filepath
                self.first_file_textInput.value = filepath
        self.main_window.open_file_dialog(title='select_first_file', on_result = after)

    def secound_first_file(self, widget):
        def after(widget, filepath):
            if filepath:
                self.secound_route = filepath
                self.secound_file_textInput.value = filepath
        self.main_window.open_file_dialog(title='select_secound_file', on_result = after)

    def comparing(self, widget):
        with open(self.first_route ,'rb') as f:
            f1 = str(list(f))
        with open(self.secound_route ,'rb') as f:
            f2 = str(list(f))
        if f1 == f2:
            self.result.text = "Same"
        else:
            self.result.text = "Not Same"


    def startup(self):
        self.main_window = toga.MainWindow(title=self.name)

        self.first_file_label = toga.Label("Choose the first file:", style=Pack(padding=3))
        self.first_file_textInput = toga.TextInput(placeholder='enter route', style=Pack(width=300, padding=3))
        self.first_file_button = toga.Button("...", on_press=self.select_first_file, style=Pack(width=50, padding=3),)

        self.secound_file_label = toga.Label("Choose the secound file:", style=Pack(padding=3))
        self.secound_file_textInput = toga.TextInput(placeholder='enter route', style=Pack(width=300, padding=3))
        self.secound_file_button = toga.Button("...", on_press=self.secound_first_file, style=Pack(width=50, padding=3),)

        self.result = toga.Label("", style=Pack(padding=3))

        box = toga.Box(
            children=[
                toga.Box(
                    children=[self.first_file_label, self.first_file_textInput, self.first_file_button],
                    style=Pack(direction=ROW, alignment=CENTER, padding=5)
                ),
                toga.Box(
                    children=[self.secound_file_label, self.secound_file_textInput, self.secound_file_button],
                    style=Pack(direction=ROW, alignment=CENTER, padding=5)
                ),
                toga.Box(
                    children=[toga.Button("start comparing", on_press=self.comparing, style=Pack(width=100, padding=5))],
                ),
                self.result
            ],
            style=Pack(direction=COLUMN),
        )

        self.main_window.content = box
        self.main_window.show()

def main():
    return App(formal_name="fileComparison-tool", app_id="org.seaotter.filecomparisontool")

if __name__ == "__main__":
    main().main_loop()