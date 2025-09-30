from abc import ABC, abstractmethod

class SoundTrack(ABC):
    @abstractmethod
    def play(self):
        pass

class Subtitles(ABC):
    @abstractmethod
    def display(self):
        pass

# Конкретные реализации продуктов для разных языков
class EnglishSoundTrack(SoundTrack):
    def play(self):
        return "Playing English sound track"

class EnglishSubtitles(Subtitles):
    def display(self):
        return "Displaying English subtitles"

class RussianSoundTrack(SoundTrack):
    def play(self):
        return "Воспроизведение русской звуковой дорожки"

class RussianSubtitles(Subtitles):
    def display(self):
        return "Отображение русских субтитров"

class SpanishSoundTrack(SoundTrack):
    def play(self):
        return "Reproduciendo pista de audio en español"

class SpanishSubtitles(Subtitles):
    def display(self):
        return "Mostrando subtítulos en español"

class FilmFactory(ABC):
    @abstractmethod
    def create_sound_track(self) -> SoundTrack:
        pass

    @abstractmethod
    def create_subtitles(self) -> Subtitles:
        pass

# Конкретные фабрики для разных языков
class EnglishFilmFactory(FilmFactory):
    def create_sound_track(self) -> SoundTrack:
        return EnglishSoundTrack()

    def create_subtitles(self) -> Subtitles:
        return EnglishSubtitles()


class RussianFilmFactory(FilmFactory):
    def create_sound_track(self) -> SoundTrack:
        return RussianSoundTrack()

    def create_subtitles(self) -> Subtitles:
        return RussianSubtitles()

class SpanishFilmFactory(FilmFactory):
    def create_sound_track(self) -> SoundTrack:
        return SpanishSoundTrack()

    def create_subtitles(self) -> Subtitles:
        return SpanishSubtitles()

# Класс фильма
class Film:
    def __init__(self, title: str, factory: FilmFactory):
        self.title = title
        self.sound_track = factory.create_sound_track()
        self.subtitles = factory.create_subtitles()

    def play(self):
        return f"{self.title}: {self.sound_track.play()} & {self.subtitles.display()}"

# Система кинопроката
class FilmRentalSystem:
    def __init__(self):
        self.factories = {
            'english': EnglishFilmFactory(),
            'russian': RussianFilmFactory(),
            'spanish': SpanishFilmFactory()
        }
        self.films = {
            'matrix': 'The Matrix',
            'inception': 'Inception',
            'avatar': 'Avatar'
        }

    def rent_film(self, film_key: str, language: str) -> Film:
        if film_key not in self.films:
            raise ValueError(f"Film {film_key} not available")

        if language not in self.factories:
            raise ValueError(f"Language {language} not supported")

        factory = self.factories[language]
        return Film(self.films[film_key], factory)

if __name__ == "__main__":
    system = FilmRentalSystem()

    # Аренда фильмов с разными языковыми дорожками
    film1 = system.rent_film('matrix', 'english')
    film2 = system.rent_film('inception', 'russian')
    film3 = system.rent_film('avatar', 'spanish')

    # Воспроизведение фильмов
    print(film1.play())
    print(film2.play())
    print(film3.play())

    # Попытка аренды с неподдерживаемым языком
    try:
        film4 = system.rent_film('matrix', 'french')
    except ValueError as e:
        print(f"Error: {e}")