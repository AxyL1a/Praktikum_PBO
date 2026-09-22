# class MesinATM:
#     def __init__[self, id_atm, lok]si, saldo_kas):
#         self.id_atm = id_atm
#         self.lokasi = lokasi
#         self.saldo_kas = saldo_kas
#     def proses_penarikan(self, nama_nasabah, jumlah):
#         if jumlah <= self.saldo_kas:
#             self.saldo_kas -= jumlah
#             print(f" [ATM {self.id_atm}] Penarikan Rp{jumlah:,} oleh {nama_nasabah} berhasil.")
#             print(f" Sisa kas di ATM {self.lokasi}: Rp{self.saldo_kas:,}")
#         else:
#             print(f" [ATM {self.id_atm}] Saldo kas mesin tidak mencukupi.")  

# class Nasabah:
#     def __init__(self, nama, nomor_rekening):
#         self.nama = nama
#         self.nomor_rekening = nomor_rekening
# # Tidak ada self.atm = ...
# # Nasabah tidak memiliki mesin ATM secara permanen.
#     def tarik_tunai(self, atm, jumlah):
#         print(f" {self.nama} memasukkan kartu ke ATM unit {atm.id_atm}({atm.lokasi})...") 
#         atm.proses_penarikan(self.nama, jumlah)

# # Kedua objek dibuat secara independen
# atm_pusat = MesinATM("ATM-01", "Kantor Cabang Sudirman", 50000000)
# budi = Nasabah("Budi Santoso", "101-220-334")
# siti = Nasabah("Siti Rahma", "101-445-889")
# # Asosiasi berjalan saat method dipanggil
# budi.tarik_tunai(atm_pusat, 500000)
# # Mesin ATM yang sama bisa digunakan oleh nasabah lain
# siti.tarik_tunai(atm_pusat, 1000000)


class shop:
    def __init__(self,name):
        self.name = name

    def proses_pebelian(self, hero, Item):
        if hero.gold >= Item.harga:
            hero.gold -= Item.harga
            print(f"{self.name} beli {Item.name}"
                    f"({Item.harga} gold), sissa gold{hero.gold}")
            return True
        print (f"[{self.name}] Gold {hero.name} tidak cukup untuk {Item.name}")
        return False


class Item:
    def __init__(self, name, harga, bonus_attack=0, bonus_armor=0):
        self.name = name
        self.harga = harga
        self.bonus_attack = bonus_attack
        self.bonus_armor = bonus_armor


class Skill:
    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    def __str__(self):
        return f"{self.name} ({self.damage} damage, {self.mana_cost} mana)"

# magic method
def __str__(self):
    return(f"Item: {self.name} | +{self.bonus_attack} attack | +{self.bonus_armor} armor")

class Hero:
    JumlahHero = 0
    MAKS_SlOT = 4

    def __init__(self, name, health, mana, armor, attack, gold, list_skill):
        self.name = name
        self.health = health
        self.mana = mana
        self.armor = armor
        self.attack = attack
        self.gold = gold
        #komposisi
        self._skills = [(name, dmg, mana)for name,dmg, mana in list_skill] 
        self._inventory = []

    # penggunaan asosiasi
    def beli_item(self, shop, item):
        if len(self._inventory) >= Hero.MAKS_SLOT:
            print(f"inventory {self.name} dah penuh brok")
            return
        if shop.proses_pembelian(self, item):
            self._inventory.append(item)

    # penggunaan agregasi
    def ambil_item(self, item):
        if len(self._inventory) < Hero.MAKS_SLOT:
            self._inventory.append(item)
            print(f"+ {self.name} mengambil {item.name}")

    def cast_skill(self,nomor_skill, lawan):
        skill = self._skills[nomor_skill- 1]
        if self.mana < skill.mana_cost:
            print(f"Mana {self.name} tidak cukup untuk {skill.name}")
            return
        self.mana -= skill.mana_cost
        lawan.health -= skill.damage
        print(f"{self.name} memakai {skill.name} ke {lawan.name},"
                f"sisa healt {lawan.name}: {lawan.health}")




brodi = Hero("Brodi", 3000, 30, 10, 100, 100, list_skill=[("tembak", 100,10), ("loncat", 70, 1)])
shop = shop("belanja Item")
bod = Item("BOD", 3100, bonus_attack=160)
winter = Item("Winter", 2140, bonus_attack=15, bonus_armor=45)


brodi.beli_item(shop, bod)
brodi.ambil_item(bod)
print()