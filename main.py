from openai import OpenAI

api_key = ""  # Podaj swój klucz API tutaj
client = OpenAI(api_key=api_key)

# Funkcja do komunikacji z API OpenAI
def generate_html_from_article(article_text, api_key):
    prompt = (
        "Przekształć ten tekst artykułu w strukturę HTML z użyciem odpowiednich tagów, "
        "zachowując dokładny, oryginalny tekst bez zmian. Główny tytuł artykułu oznacz jako <h1> (jeden raz), a główne sekcje "
        "artykułu jako <h2>. Zadbaj, aby zwykły tekst akapitowy nie był oznaczany jako nagłówek. "
        "Dodaj tagi <img src='image_placeholder.jpg' alt='prompt do generowania grafiki'> w kilku miejscach, gdzie "
        "sensownie pasują obrazy (np. przy głównych sekcjach), i dodaj odpowiednie podpisy pod obrazkami. "
        "Wynikowy kod HTML powinien zawierać tylko zawartość sekcji <body>, bez <html> i <head>."
    )


    try:
        # Wysłanie żądania do API przy użyciu odpowiedniej metody
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Jesteś pomocnym asystentem do przekształcania tekstu na HTML."},
            {"role": "user", "content": prompt + "\n\n" + article_text}
        ],
        max_tokens=3000,
        temperature=0.7)
        # Zwrócenie wygenerowanego HTML-a
        return response.choices[0].message.content.strip()

    except Exception as e:
        print("Błąd podczas generowania HTML-a:", e)
        return None

def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def save_html(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


# Funkcja do czyszczenia tagów <body> i wyrównywania tabulacji
def clean_html_body_tags(html_content):
    # Usuwamy tagi <body> oraz </body>
    html_content = html_content.replace("<body>", "").replace("</body>", "")

    # Podział na linie i usunięcie zbędnych wcięć
    lines = html_content.splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]  # Usuwanie pustych linii

    if cleaned_lines:
        first_line = cleaned_lines[0].strip() 
        remaining_lines = ["        " + line for line in cleaned_lines[1:]]

    # Składanie oczyszczonego HTML z jednolitym wcięciem 
    return "\n".join([first_line] + remaining_lines)


# Funkcja do wstawienia zawartości do szablonu
def insert_into_template(template_path, output_path, content):
    cleaned_content = clean_html_body_tags(content)  # Czyszczenie HTML-a
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template = template_file.read()

    # Wstawienie oczyszczonego HTML-a do szablonu
    final_content = template.replace("<!-- Zawartość artykułu zostanie tutaj automatycznie dodana -->", cleaned_content)

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(final_content)


def main():
    article_path = "tresc artykulu.txt"
    article_html_path = "artykul.html"
    template_path = "szablon.html"
    preview_path = "podglad.html"

    article_text = read_article(article_path)
    article_html = generate_html_from_article(article_text, api_key)

    if article_html:
        save_html(article_html_path, article_html)
        print("Wygenerowany kod HTML zapisany do pliku artykul.html")

        # Wstawienie wygenerowanego HTML-a do podglądu
        insert_into_template(template_path, preview_path, article_html)
        print("Podgląd artykułu zapisany do pliku podglad.html")
    else:
        print("Nie udało się wygenerować kodu HTML.")


if __name__ == "__main__":
    main()
