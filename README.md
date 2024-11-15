# README
## Opis aplikacji

Aplikacja umożliwia przekształcenie tekstu artykułu na strukturę HTML, przy zachowaniu oryginalnej treści. Wygenerowany kod HTML zawiera odpowiednie tagi `<h1>` dla tytułu, `<h2>` dla nagłówków sekcji oraz `<p>` dla zwykłego tekstu. 

Dodatkowo aplikacja umieszcza placeholdery obrazów w miejscach, gdzie mogą one sensownie pasować do treści i generuje odpowiedni podpis pod obrazkami, który można później wykorzystać do stworzenia grafik.

Aplikacja współpracuje z OpenAI API, wykorzystując model `gpt-3.5-turbo`, aby przekształcić artykuł w HTML.

## Główne funkcje aplikacji:
* Generowanie HTML z artykułu: Funkcja `generate_html_from_article()` przesyła tekst artykułu do API OpenAI, aby uzyskać odpowiednią strukturę HTML.
* Czytanie artykułu z pliku: Funkcja `read_article()` odczytuje treść artykułu z pliku tekstowego.
* Zapis HTML: Funkcja `save_html()` zapisuje wygenerowany HTML do pliku.
* Czyszczenie HTML: Funkcja `clean_html_body_tags()` usuwa tagi `<body>` i wyrównuje tabulację kodu HTML.
* Wstawienie HTML do szablonu: Funkcja `insert_into_template()` wstawia wygenerowany HTML do szablonu strony, tworząc podgląd artykułu.

## Instrukcja uruchomienia

### 1. Zainstaluj wymagane biblioteki
Aplikacja korzysta z biblioteki openai, którą należy zainstalować:
`pip install openai`

### 2. Uzyskaj klucz API OpenAI
Aby korzystać z OpenAI API, musisz posiadać klucz API. Możesz go uzyskać na stronie: https://platform.openai.com/.

Po uzyskaniu klucza, wprowadź go w kodzie w miejscu, gdzie znajduje się pusty ciąg (api_key = "").
`api_key = "Twój_klucz_API"`

### 3. Przygotowanie plików wejściowych
Aplikacja wymaga kilku plików wejściowych:

* `tresc artykulu.txt` – Plik zawierający tekst artykułu, który ma zostać przekształcony na HTML.
* `szablon.html` – Szablon HTML, w który zostanie wstawiona zawartość wygenerowanego HTML.
* Możesz stworzyć własny plik szablonu lub użyć domyślnego, który musi zawierać w odpowiednim miejscu komentarz:
`<!-- Zawartość artykułu zostanie tutaj automatycznie dodana -->`

### 4. Uruchomienie aplikacji
Po skonfigurowaniu wszystkich wymaganych plików, uruchom aplikację:

`python main.py`

Program odczyta artykuł z pliku `tresc artykulu.txt`, przekształci go na HTML, zapisze wygenerowany kod do pliku `artykul.html` i utworzy podgląd w pliku `podglad.html`.

### 5. Pliki wyjściowe
Po zakończeniu działania aplikacji, zostaną wygenerowane następujące pliki:

* `artykul.html` – Plik zawierający wygenerowany kod HTML z artykułem.
* `podglad.html` – Plik HTML z podglądem artykułu, w którym wstawiono wygenerowaną zawartość.

### Uwaga
Pamiętaj, aby wprowadzić prawidłowy klucz API w zmiennej api_key.

Możesz modyfikować szablon HTML, aby dostosować wygląd wygenerowanej strony do własnych potrzeb.
