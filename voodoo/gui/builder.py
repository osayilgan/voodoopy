import uuid
from voodoo.gui.state import State

class Page:
    def __enter__(self):
        self.content = ""
        self.event_list = {}  # Event list bir dictionary olarak tanımlandı
        self.state = State()  # State nesnesi ekleniyor
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def add_panel(self, panel):
        """Panele ait içerikleri sayfaya ekliyor."""
        self.content += panel.render()
        return self

    def Setup(self, title: str, width: str = "max-w-lg", shadow: bool = True, rounded: bool = True):
        shadow_class = "shadow-lg" if shadow else ""
        rounded_class = "rounded-lg" if rounded else ""

        # Sayfanın genel HTML yapısı
        self.content = f'''
        <html>
        <head>
            <title>{title}</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link href="/static/css/tailwind.min.css" rel="stylesheet" />
            <link href="/static/css/flowbite.min.css" rel="stylesheet" />
            <script src="/static/js/flowbite.min.js"></script>
        </head>
        <body class="bg-gray-50 p-10">
            <div class="{width} mx-auto">
                <div class="bg-white {shadow_class} {rounded_class} p-6 space-y-4">
                    <h5 class="text-2xl font-semibold leading-tight text-gray-900 mb-4">{title}</h5>
                    {self.content}
                </div>
            </div>
        '''
        return self

    def render(self):
        event_scripts = ""
        # Event'leri döngüyle işliyoruz
        for button_id, function_ref in self.event_list.items():
            event_scripts += f"""
            var button_{button_id} = document.getElementById('{button_id}');
            button_{button_id}.addEventListener('click', function() {{
                var state = {{}};  // HTML input'lardan state'i topluyoruz
                document.querySelectorAll('input, label').forEach(function(element) {{
                    state[element.id] = element.value;
                }});
                window.state = state;
                console.log("Güncel State:", window.state);

                // Backend fonksiyonunu tetikleme
                if ('{function_ref}' === 'process_data') {{
                    process_data(window.state);
                }} else if ('{function_ref}' === 'another_function') {{
                    another_function(window.state);
                }}
            }});
            """

        return self.content + f"""
            <script>
                {event_scripts}
                function process_data(state) {{
                    alert("Processing: " + JSON.stringify(state));
                }}

                function another_function(state) {{
                    alert("Another Function: " + JSON.stringify(state));
                }}
            </script>
        </body>
        </html>
        """


class Panel:
    def __enter__(self):
        self.content = ""
        self.event_list = {}
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def text(self, text, mode="normal"):
        if mode == "md":
            self.content += f'<h1 class="text-3xl font-bold text-gray-900">{text}</h1>'
        else:
            self.content += f'<p class="text-base text-gray-700">{text}</p>'
        return self

    def input(self, id=None, text=None):
        text_value = "" if text is None else str(text)
        id = str(uuid.uuid4()) if id is None else id
        self.content += f'<input id="{id}" class="border border-gray-300 p-2 rounded-md w-full" type="text" value="{text_value}">'
        return self

    def button(self, text, function_ref=None):
        # Benzersiz bir ID veriyoruz, eğer yoksa yeni bir GUID üretiyoruz
        button_id = str(uuid.uuid4())
        
        # Buton oluşturuyoruz
        self.content += f'<button id="{button_id}" class="mx-2 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">{text}</button>'

        # Butonun event'ini kaydediyoruz
        if function_ref is not None:
            self.event_list[button_id] = function_ref
        else:
            print(f"Geçilen fonksiyon referansı None: {function_ref}")
        return self

    def consolewrite(self, message):
        # Konsol çıktısı ekliyoruz
        if self.current_button is not None:
            self.event_list[self.current_button].append(f'console.log("{message}");')
        return self

    def render(self):
        return f'''
        <div class="w-full h-auto mx-auto">
            <div class="bg-pastel-blue shadow-lg rounded-lg p-6 space-y-4">
                {self.content}
            </div>
        </div>
        '''
