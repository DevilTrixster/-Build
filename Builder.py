import json

class ArticleBuilder:
    def __init__(self):
        self.title = None
        self.authors = None
        self.content = None
        self.hash_code = None

    def set_title(self, title):
        self.title = title.strip()
        return self

    def set_authors(self, authors_line):
        self.authors = [author.strip() for author in authors_line.split(',')]
        return self

    def set_content(self, content):
        self.content = content.strip()
        return self

    def set_hash(self, hash_code):
        self.hash_code = hash_code.strip()
        return self

    def build(self):
        if not all([self.title, self.authors, self.content, self.hash_code]):
            raise ValueError("Не все поля заполнены")

        return {
            "title": self.title,
            "authors": self.authors,
            "content": self.content,
            "hash": self.hash_code
        }


def parse_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if len(lines) < 3:
        raise ValueError("Файл должен содержать как минимум 3 строки: заголовок, авторы и хеш-код")

    # Предполагаем, что хеш-код находится в последней строке
    hash_line = lines[-1].strip()
    content = ''.join(lines[2:-1]).strip()  # Контент между авторами и хешем
    authors_line = lines[1].strip()
    title_line = lines[0].strip()

    builder = ArticleBuilder()
    article = (builder
               .set_title(title_line)
               .set_authors(authors_line)
               .set_content(content)
               .set_hash(hash_line)
               .build())
    return article

def save_to_json(article, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(article, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    input_file = "article.txt"
    output_file = "article.json"

    try:
        article = parse_txt_file(input_file)
        save_to_json(article, output_file)
        print("Конвертация завершена успешно!")
    except Exception as e:
        print(f"Ошибка: {e}")