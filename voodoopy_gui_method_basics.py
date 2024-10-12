from voodoo.gui import Gui
import voodoo.gui.builder as vo

# Burada yeniden state oluşturmuyoruz, builder.py'deki Page sınıfındaki state'i kullanıyoruz

# Backend'de verileri işleyen fonksiyon
def process_data(state):
    print(f"Submit Data Called with: {state.get_state()}")
    print(f"Input 1: {state.get('input1')}, Input 2: {state.get('input2')}")
    
    # Stateleri güncelliyoruz
    state.update_state({
        'input1': 'Değer 3',
        'input2': 'Değer 4'
    })
    
    # Frontend'e yeni statelerin yansıtılması için
    return state.get_state()

# GUI oluşturma
with vo.Page() as page:
    # Page içindeki state'i kullanıyoruz, dışarıdan yeniden state oluşturmuyoruz
    page.text("Let's Make Some Voodoo!", mode="md")
    page.input(id="input1", text=page.state.get('input1'))  # Page'deki state kullanılıyor
    page.input(id="input2", text=page.state.get('input2'))  # Page'deki state kullanılıyor
    
    # Butona tıklandığında process_data çalıştırılıyor
    page.button("Submit").method(process_data, page.state).consolewrite("Done")
    Gui(page).run(debug=True)
