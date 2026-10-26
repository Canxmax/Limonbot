import aiohttp  # Eşzamansız HTTP istekleri için bir kütüphane
import random

class Pokemon:
    pokemons = {}
    # Nesne başlatma (kurucu)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.power = random.randint(1, 100)
        self.health = random.randint(1, 100)
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def get_name(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için asenktron metot
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API
        async with aiohttp.ClientSession() as session:  #  HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve çözümlenmesi
                    return data['forms'][0]['name']  #  Pokémon adını döndürme
                else:
                    return "Pikachu"  # İstek başarısız olursa varsayılan adı döndürür

    async def info(self):
        # Pokémon hakkında bilgi döndüren bir metot
        if not self.name:
            self.name = await self.get_name()
            self.power  # Henüz yüklenmemişse bir adın geri alınması
        return (f"Pokémonunuzun ismi: {self.name}"  # Pokémon adını içeren dizeyi döndürür
                        f"Can (health): {self.hp}\n"
                        f"Güç (power): {self.power}")
    async def show_img(self):
        # PokeAPI aracılığıyla bir pokémon görüntüsünün URL'sini almak için asenktron metot

    async def attack(self, enemy):
            if enemy.hp > self.power:
                enemy.hp -= self.power
                return f"Pokémon eğitmeni @{self.pokemon_trainer} @{enemy.pokemon_trainer}'ne saldırdı\n@{enemy.pokemon_trainer}'nin sağlık durumu {enemy.hp}"
            else:
                enemy.hp = 0
                return f"Pokémon eğitmeni @{self.pokemon_trainer} @{enemy.pokemon_trainer}'ni yendi!"

class Wizard(Pokemon):
    async def attack(self, enemy):

        extra_magic = random.randint(10, 30)
        total_damage = self.power + extra_magic
        
        if enemy.hp > total_damage:
            enemy.hp -= total_damage
            return f" @{self.pokemon_trainer} büyü gücünü kullandı ve @{enemy.pokemon_trainer}'ne {total_damage} hasar vurdu!\n@{enemy.pokemon_trainer}'nin kalan sağlığı: {enemy.hp}"
        else:
            enemy.hp = 0
            return f"@{self.pokemon_trainer} büyü ile @{enemy.pokemon_trainer}'ni alt etti!"


class Fighter(Pokemon):
    async def attack(self, enemy):

        critical_hit = self.power * 2
        
        if enemy.hp > critical_hit:
            enemy.hp -= critical_hit
            return f" @{self.pokemon_trainer} güçlü bir savaş hamlesi (Kritik) yaptı ve @{enemy.pokemon_trainer}'ne {critical_hit} hasar vurdu!\n@{enemy.pokemon_trainer}'nin kalan sağlığı: {enemy.hp}"
        else:
            enemy.hp = 0
            return f" @{self.pokemon_trainer} ezici bir darbe ile @{enemy.pokemon_trainer}'ni yendi!"