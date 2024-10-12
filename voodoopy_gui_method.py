from voodoo.gui import Gui
import voodoo.gui.builder as vo
import voodoo.gui.state as st

text = "Hello voodist"
json_data = {"key": "value"}  # Replace with actual data you want to send
endpoint = "https://run.mocky.io/v3/2b72bff6-fabf-46e6-b561-a0e512c3f156"

# State nesnesi oluşturuluyor
state = st.State()

# Buton tıklandığında state güncelleniyor
state.update_state({
    'input1': 'Değer 1',
    'input2': 'Değer 2'
})

# Python tarafında state'in güncel değerlerine erişim
print(state.input1)  # Çıktı: Değer 1
print(state.input2)  # Çıktı: Değer 2
# voodoopy_gui_method.py

def process_data(state):
    print(f"Submit Data Called with: {state}")
    # state içinde input1 ve input2 gibi değerlere erişebiliriz
    print(f"Input 1: {state.get('input1')}, Input 2: {state.get('input2')}")
    Gui(vo.Page.consolewrite('Done')).run(debug=True)


with vo.Page() as page:
    page.text("Let's Make Some Voodoo !", mode="md")
    page.input(id="input1", text=state.input1)
    page.input(id="input2", text=state.input2)
    page.button("Send").submit_data(process_data, state)
 
    #page.button("Submit").text("Hi woodist!")
Gui(page).run(debug=True)
