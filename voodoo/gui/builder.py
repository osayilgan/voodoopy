import requests
import uuid

class Page:
    def __enter__(self):
        self.content = ""
        self.event_list = []  # Her bir butonun işlemlerini tutacak geçici hafıza
        self.current_button = None  # Şu anki buton
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def text(self, text, mode="normal"):
        if mode == "md":
            self.content += f'<h1 class="text-3xl font-bold text-gray-900">{text}</h1>'
        else:
            self.content += f'<p class="text-base text-gray-700">{text}</p>'
        return self  # Method chaining için self döndürülüyor

    def input(self, id=None, text=None):
        # Eğer text verilmemişse varsayılan bir değer atayalım (örneğin, boş string)
        if text is None:
            text_value = ""
        else:
            # text'i string'e dönüştürerek her veri tipini kabul edelim
            text_value = str(text)

        # Eğer id verilmemişse GUID üretelim
        if id is None:
            id = str(uuid.uuid4())

        # HTML input elementi oluşturuluyor
        self.content += f'<input id="{id}" class="border border-gray-300 p-2 rounded-md w-full" type="text" value="{text_value}">'
        return self  # Method chaining'e olanak sağlamak için self döndürülüyor

    def button(self, text):
        # Buton oluşturuluyor ve tıklama event'i sonradan eklenecek
        button_id = f"button-{len(self.event_list)}"  # Buton ID'si unique olmalı
        self.current_button = button_id  # Şu anki butonu set et
        # Her butona yatay margin (mx-2) ekleyerek butonlar arası boşluk bırakılıyor
        self.content += f'<button id="{button_id}" class="mx-2 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">{text}</button>'
        self.event_list.append([])  # Her buton için boş bir liste başlatıyoruz
        return self  # Method chaining için self döndürülüyor

    def consolewrite(self, message):
        # Şu anki butonun event listesine ekle
        if self.current_button is not None:
            self.event_list[int(self.current_button.split('-')[-1])].append(f'console.log("{message}");')
        return self  # Method chaining için self döndürülüyor
    
    def callendpoint(self, endpoint, data):
        # API çağrısını ilgili butonun event listesine ekle
        if self.current_button is not None:
            self.event_list[int(self.current_button.split('-')[-1])].append(f"""
                var inputValue = {data};
                fetch('{endpoint}', {{
                    method: 'POST',
                    headers: {{
                        'Content-Type': 'application/json'
                    }},
                    body: JSON.stringify(inputValue)
                }})
                .then(response => response.json())
                .then(data => {{
                    console.log('Success:', data);
                }})
                .catch((error) => {{
                    console.error('Error:', error);
                }});
            """)
        return self  # Method chaining için self döndürülüyor

    def render(self):
        # Render edilen HTML'de her butonun event listener'ı temp memory (self.event_list) ile dolacak
        event_scripts = ""
        for idx, events in enumerate(self.event_list):
            event_scripts += f"""
            var button_{idx} = document.getElementById('button-{idx}');
            button_{idx}.addEventListener('click', function() {{
                // Tüm input ve label elemanlarını toplayalım
                var state = {{}};
                document.querySelectorAll('input, label').forEach(function(element) {{
                    state[element.id] = element.value;
                }});

                // State'i global olarak kaydet (frontend'de)
                window.state = state;
                
                // State'i konsola yazdır (debug için)
                console.log("Güncel State:", window.state);
                
                // Event'leri çalıştır (önce state toplandı, sonra event'ler çalışacak)
                {''.join(events)}
            }});
            """
        
        # HTML yapısını döndür
        return f"""
        <html>
        <head>
            <title>Voodoo GUI</title>
            <!-- Tailwind CSS -->
            <link href="/static/css/tailwind.min.css" rel="stylesheet" />
            <!-- Flowbite -->
            <link href="/static/css/flowbite.min.css" rel="stylesheet" />
            <script src="/static/js/flowbite.min.js"></script>
        </head>
        <body class="bg-gray-50 p-10">
            <div class="max-w-lg mx-auto">
                <!-- 'space-y-4' eklenerek her öğe arasında dikey boşluk bırakılıyor -->
                <div class="bg-white shadow-lg rounded-lg p-6 space-y-4">
                    <h5 class="text-2xl font-semibold leading-tight text-gray-900 mb-4">Getting started with voodoo GUI</h5>
                    {self.content}
                </div>
            </div>
            <script>
                {event_scripts}
            </script>
        </body>
        </html>
        """
