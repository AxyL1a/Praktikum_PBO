class User:
    nama_aplikasi = "FitTrack Pro"
    total_user = 0

    def __init__(self, nama, umur, berat_badan):
        User.total_user += 1
        self.__id_user = f"USR-{User.total_user:03d}"
        self.nama = nama
        self.umur = umur
        self.__berat_badan = None
        self.berat_badan = berat_badan

    @property
    def id_user(self):
        return self.__id_user

    @property
    def berat_badan(self):
        return self.__berat_badan

    @berat_badan.setter
    def berat_badan(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            print(f"[GAGAL] Berat badan tidak valid: {value}. Harus angka positif.")
            return
        self.__berat_badan = value

    def tampilkan_profil(self):
        print(f"{self.__id_user} | {self.nama} ({self.umur} th) | Berat badan: {self.__berat_badan}kg")

    @classmethod
    def dari_dict(cls, data):
        return cls(data["nama"], data["umur"], data["berat_badan"])

    @classmethod
    def info_aplikasi(cls):
        print(f"{cls.nama_aplikasi} | Total user terdaftar: {cls.total_user}")

    @staticmethod
    def kategori_bb(berat):
        if berat < 55:
            return "Ringan"
        elif berat < 80:
            return "Sedang"
        return "Berat"


class Exercise:
    satuan_berat = "kg"
    total_exercise = 0
    kategori_tersedia = ["Dada", "Punggung", "Kaki", "Bahu", "Lengan", "Core"]

    def __init__(self, nama_latihan, sets, reps, berat_beban, kategori="Dada"):
        Exercise.total_exercise += 1
        self.nama_latihan = nama_latihan
        self.sets = sets
        self.reps = reps
        self.__berat_beban = None
        self.berat_beban = berat_beban
        self.kategori = kategori if kategori in Exercise.kategori_tersedia else "Dada"

    @property
    def berat_beban(self):
        return self.__berat_beban

    @berat_beban.setter
    def berat_beban(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Berat beban harus berupa angka positif.")
        self.__berat_beban = value

    def hitung_volume(self):
        return self.sets * self.reps * self.__berat_beban

    def tampilkan_info(self):
        print(f"{self.nama_latihan} [{self.kategori}] {self.sets}x{self.reps} "
                f"@ {self.__berat_beban}{Exercise.satuan_berat} "
                f"| Volume: {self.hitung_volume()}{Exercise.satuan_berat}")

    @classmethod
    def ubah_satuan_berat(cls, satuan_baru):
        cls.satuan_berat = satuan_baru
        print(f"[INFO] Satuan berat sekarang: {cls.satuan_berat}")

    @staticmethod
    def validasi_nama_latihan(nama):
        return isinstance(nama, str) and nama.strip() != ""


class WorkoutRoutine:
    total_routine = 0
    kategori_valid = ["Push", "Pull", "Legs", "Full Body"]
    nama_instansi = "FitTrack Studio"

    def __init__(self, nama_routine, user, kategori="Full Body"):
        WorkoutRoutine.total_routine += 1
        self.nama_routine = nama_routine
        self.user = user
        self.__daftar_latihan = []
        self.kategori = kategori

    @property
    def kategori(self):
        return self.__kategori

    @kategori.setter
    def kategori(self, value):
        if value not in WorkoutRoutine.kategori_valid:
            print(f"[GAGAL] Kategori '{value}' tidak valid. Pilihan: {WorkoutRoutine.kategori_valid}")
            return
        self.__kategori = value

    def tambah_latihan(self, exercise):
        if not isinstance(exercise, Exercise):
            print("[GAGAL] Objek yang ditambahkan bukan Exercise.")
            return
        self.__daftar_latihan.append(exercise)
        print(f"'{exercise.nama_latihan}' ditambahkan ke routine '{self.nama_routine}'.")

    def tampilkan_routine(self):
        print(f"Routine: {self.nama_routine} ({self.kategori}) milik {self.user.nama}")
        if not self.__daftar_latihan:
            print("  (Belum ada latihan)")
            return
        for ex in self.__daftar_latihan:
            print("  -", end=" ")
            ex.tampilkan_info()
        print(f"  Total volume routine: {self.hitung_total_volume()}{Exercise.satuan_berat}")

    def hitung_total_volume(self):
        return sum(ex.hitung_volume() for ex in self.__daftar_latihan)

    @classmethod
    def tambah_kategori_baru(cls, kategori_baru):
        if kategori_baru not in cls.kategori_valid:
            cls.kategori_valid.append(kategori_baru)
            print(f"[INFO] Kategori '{kategori_baru}' ditambahkan ke daftar kategori valid.")

    @staticmethod
    def validasi_jumlah_latihan(jumlah, maksimal=10):
        return isinstance(jumlah, int) and 0 <= jumlah <= maksimal


print("1. Membuat objek User")
user1 = User("Prabowo", 21, 80)
user2 = User.dari_dict({"nama": "Megawati", "umur": 20, "berat_badan": 58})
user1.tampilkan_profil()
user2.tampilkan_profil()
User.info_aplikasi()
print("Kategori BB Prabowo:", User.kategori_bb(user1.berat_badan))
print("Kategori BB Megawati:", User.kategori_bb(user2.berat_badan))


print("\n2. Membuat objek Exercise")
bench_press = Exercise("Bench Press", 3, 8, 70, kategori="Dada")
squat = Exercise("Barbell Squat", 3, 8, 40, kategori="Kaki")
bench_press.tampilkan_info()
squat.tampilkan_info()
print("Total exercise dibuat:", Exercise.total_exercise)
Exercise.ubah_satuan_berat("kg")
print("Validasi nama latihan kosong:", Exercise.validasi_nama_latihan(""))


print("\n3. Membuat objek WorkoutRoutine")
routine1 = WorkoutRoutine("Upper Body", user1, kategori="Push")
routine2 = WorkoutRoutine("Leg Day", user2, kategori="Legs")
routine1.tambah_latihan(bench_press)
routine2.tambah_latihan(squat)
routine1.tampilkan_routine()
routine2.tampilkan_routine()
print("Total routine dibuat:", WorkoutRoutine.total_routine)
WorkoutRoutine.tambah_kategori_baru("Cardio")
print("Validasi jumlah latihan:", WorkoutRoutine.validasi_jumlah_latihan(3))


print("\n4. Uji setter")
print("-> User.berat_badan")
user1.berat_badan = 82
user1.berat_badan = -10
user1.tampilkan_profil()


print("-> Exercise.berat_beban")
try:
    bench_press.berat_beban = 45
    print(f"[BERHASIL] berat_beban diubah -> {bench_press.berat_beban}kg")
    bench_press.berat_beban = 0
except ValueError as e:
    print(f"[GAGAL] {e}")


print("-> WorkoutRoutine.kategori")
routine2.kategori = "Full Body"
routine2.kategori = "Full Pantat"
print("Kategori routine2 sekarang:", routine2.kategori)