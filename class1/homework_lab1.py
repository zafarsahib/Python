# Homework Lab 1: Playlist Class

class Playlist:
    def __init__(self, name):
        self.name = name
        self.song_count = 0
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        self.song_count += 1
        print(f'"{song}" added to playlist.')

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            self.song_count -= 1
            print(f'"{song}" removed from playlist.')
        else:
            print(f'"{song}" not found in playlist.')

    def show_info(self):
        print(f"Playlist Name: {self.name}")
        print(f"Total Songs: {self.song_count}")
        print("Songs List:", self.songs)

mysongs_playlist = Playlist("My Favorite English Songs")

mysongs_playlist.add_song("Shape of You")
mysongs_playlist.add_song("Blinding Lights")
mysongs_playlist.add_song("Someone Like You")
mysongs_playlist.add_song("Bohemian Rhapsody")

mysongs_playlist.remove_song("Shape of You")

mysongs_playlist.show_info()

# Homework Lab 1: Shopping Cart Class
class ShoppingCart:
    def __init__(self, owner):
        self.owner = owner
        self.item_count = 0

    def add_item(self, quantity):
        if quantity > 0:
            self.item_count += quantity
            print(f"{quantity} items added to cart.")
        else:
            print("Please enter a valid quantity.")

    def remove_item(self, quantity):
        if quantity > 0:
            if quantity <= self.item_count:
                self.item_count -= quantity
                print(f"{quantity} items removed from cart.")
            else:
                print("Cannot remove more items, cart is empty.")
        else:
            print("Please enter a valid quantity.")

    def show_cart(self):
        print(f"Owner: {self.owner}")
        print(f"Total items in cart: {self.item_count}")

shopping_cart = ShoppingCart("Muhammad Zafar Kamran")

shopping_cart.add_item(4)
shopping_cart.remove_item(2)
shopping_cart.show_cart()

# Homework Lab 1: Bank user Account Class
class UserAccount:
    def __init__(self, username):
        self.username = username
        self.active = False
        self.login_count = 0

    def activate(self):
        self.active = True
        print(f"{self.username} account activated.")

    def deactivate(self):
        self.active = False
        print(f"{self.username} account deactivated.")

    def login(self):
        if self.active:
            self.login_count += 1
            print(f"{self.username} logged in successfully.")
        else:
            print(f"{self.username} account is inactive. Please activate account first.")

    def show_status(self):
        print(f"Username: {self.username}")
        print(f"Active: {self.active}")
        print(f"Login Count: {self.login_count}")

user_account = UserAccount("Zafar")

user_account.show_status()
user_account.activate()
user_account.login()
user_account.deactivate()
user_account.login()
user_account.show_status()