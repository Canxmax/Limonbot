import aiohttp

class Pokemon:
    def __init__(self, pokemon_number):
        self.pokemon_number = pokemon_number
        self.name = None
        self.types = []
        self.height = None
        self.weight = None
        self.stats = {}
        self.image_url = None

    async def load_data(self):
        # PokeAPI üzerinden Pokémon verilerini çekme
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    # API'den gelen verileri niteliklere aktarıyoruz
                    self.name = data.get('name')
                    self.height = data.get('height')
                    self.weight = data.get('weight')
                    self.types = [t['type']['name'] for t in data.get('types', [])]
                    self.stats = {s['stat']['name']: s['base_stat'] for s in data.get('stats', [])}
                    self.image_url = data.get('sprites', {}).get('front_default')
                else:
                    # İstek başarısız olursa varsayılan (Pikachu) değerler
                    self.name = "pikachu"
                    self.image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"

    # --- Getter Metotları (Niteliklere Erişim) ---
    def get_name(self):
        return self.name

    def get_types(self):
        return self.types

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_stats(self):
        return self.stats

    def get_img(self):
        return self.image_url

    # --- Setter Metod (Nitelikleri Değiştirme) ---
    async def change_pokemon(self, new_number):
        self.pokemon_number = new_number
        await self.load_data()  # Yeni Pokémon verilerini tekrar yükle
