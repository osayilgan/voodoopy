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


with vo.Page() as page:
    page.text("Let's Make Some Voodoo !", mode="md")
    page.text(f"My text: {text}")
    page.input(f"{text}")
    page.input(":)")
    page.button("Submit").callendpoint(endpoint=f"{endpoint}", data=json_data)
    page.button("Submit").consolewrite("Hello World").consolewrite("Hello Mars")
    page.button("Msg").consolewrite("Hello jubiter").consolewrite("hello saturn")
    page.button("Send").input(id='input1',text = state.input1).input(id='input2', text =  state.input2)
 
    #page.button("Submit").text("Hi woodist!")
Gui(page).run(debug=True)
