import pandas as pd

data = {
    "Book_Title": [
        "Thirukkural",
        "Panchali Sabatham",
        "Kallikattu Ithikasam",
        "Vekkai",
        "Kuyil Pattu",
        "To Kill a Mockingbird",
        "The White Tiger",
        "1984",
        "The God of Small Things",
        "Train to Pakistan",
    ],
    "Author": [
        "Thiruvalluvar",
        "Subramania Bharathiyar",
        "Poomani",
        "Poomani",
        "Subramania Bharathiyar",
        "Harper Lee",
        "Aravind Adiga",
        "George Orwell",
        "Arundhati Roy",
        "Khushwant Singh",
    ],
    "Genre": [
        "Ethics, Philosophy, Tamil Classic",
        "Mythology, Feminism",
        "Social, Drama",
        "Fiction, Social Justice",
        "Poetry, Society",
        "Fiction, Social Injustice",
        "Fiction, Society",
        "Dystopian, Political",
        "Fiction, Family Drama",
        "Historical Fiction",
    ],
    "Language": [
        "Tamil",
        "Tamil",
        "Tamil",
        "Tamil",
        "Tamil",
        "English",
        "English",
        "English",
        "English",
        "English",
    ],
}

df = pd.DataFrame(data)


def get_books_by_language(language, num_books=5):
    books = df[df["Language"].str.lower() == language.lower()].head(num_books)
    return books[["Book_Title", "Author", "Genre"]].to_dict(orient="records")



language_input = input("Enter the language (Tamil/English): ").strip()

if language_input.lower() in ["tamil", "english"]:
    selected_books = get_books_by_language(language_input)
    print(f"\nTop 5 {language_input.capitalize()} Books with  Themes:")
    for book in selected_books:
        print(f"- {book['Book_Title']} by {book['Author']} (Genre: {book['Genre']})")
else:
    print("Invalid language input. Please enter 'Tamil' or 'English'.")
