import sys
from pathlib import Path


def get_base_dir() -> Path:
    """Возвращает папку запуска приложения или папку собранного .exe."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


def insure_save_file() -> Path:
    """Создаёт файл сохранения при первом запуске, если его ещё нет."""
    save_path = get_base_dir() / "save.txt"
    if not save_path.exists():
        save_path.write_text("Приложение запущено впервые.\n", encoding="utf-8")
    return save_path


def main() -> None:
    save_path = insure_save_file()
    print("Проект успешно запущен!")
    print(f"Папка приложения: {get_base_dir()}")
    print(f"Файл сохранения: {save_path}")


if __name__ == "__main__":
    main()
