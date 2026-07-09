import json
import os

FAVORITES_PATH = os.path.join("data", "favorites.json")


def load_favorites():
    if not os.path.exists(FAVORITES_PATH):
        return []

    with open(FAVORITES_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def save_favorites(favorites):
    os.makedirs("data", exist_ok=True)

    with open(FAVORITES_PATH, "w", encoding="utf-8") as file:
        json.dump(favorites, file, ensure_ascii=False, indent=4)


def add_favorite(ticker):
    favorites = load_favorites()

    if ticker not in favorites:
        favorites.append(ticker)
        save_favorites(favorites)

    return favorites


def remove_favorite(ticker):
    favorites = load_favorites()
    favorites = [item for item in favorites if item != ticker]
    save_favorites(favorites)

    return favorites


def is_favorite(ticker):
    favorites = load_favorites()
    return ticker in favorites