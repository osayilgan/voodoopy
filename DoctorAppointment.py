from voodoo.gui import Gui
import voodoo.gui.builder as vo

def process_data(state):
    print(f"Process Data State: {state['input1']} , {state['input2']}")

def another_function(state):
    print(f"Another : Process Data State: {state['input1']} , {state['input2']}")

# Bu blok GUI'yi yalnızca dosya doğrudan çalıştırıldığında başlatacak
if __name__ == "__main__":
    with vo.Page() as page:
        page.text("Let's Make Some Voodoo!", mode="md")
        page.input(id="input1", text="Değer 1")
        page.input(id="input2", text="Değer 2")
        
        # Her buton farklı fonksiyon referansı alıyor
        page.button("Submit", "process_data").consolewrite(f'submit:{page.state}')
        page.button("Another Button", "another_function").consolewrite(f'Another button: {page.state}')
        
    
        Gui(page).run(debug=True)
