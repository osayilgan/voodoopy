from voodoo.gui import Gui
import voodoo.gui.builder as vo

text = "Hello voodist"
json_data = {"key": "value"}  # Replace with actual data you want to send
endpoint = "https://run.mocky.io/v3/2b72bff6-fabf-46e6-b561-a0e512c3f156"

with vo.Page() as page:
    page.text("Let's Make Some Voodoo !", mode="md")
    page.text(f"My text: {text}")
    page.input(f"{text}")
    page.input(":)")
    page.button("Submit").callendpoint(endpoint=f"{endpoint}", data=json_data)
    page.button("Submit").consolewrite("Hello World").consolewrite("Hello Mars")
    page.button("Msg").consolewrite("Hello jubiter").consolewrite("hello saturn")
    page.button("Send").input(id='input1').input(id='input2')
 
    #page.button("Submit").text("Hi woodist!")
Gui(page).run(debug=True)
