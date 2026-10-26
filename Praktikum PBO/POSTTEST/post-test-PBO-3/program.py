import datetime
from abc import ABC, abstractmethod


# Class pelatih (Superclass 1)
class pelatih:
    total_person = 0

    def __init__(self, nama, umur):
        pelatih.total_person += 1
        self.nama = nama
        self._umur = None
        self.umur = umur
        self.__tanggal_daftar = datetime.date.today().isoformat()

    @property
    def umur(self):
        return self._umur

    @umur.setter
    def umur(self, value):
        if not isinstance(value, int) or value <= 0:
            print(f'[GAGAL] Umur tidak valid: {value}. Harus bilangan bulat positif.')
            return
        self._umur = value

    @property
    def tanggal_daftar(self):
        return self.__tanggal_daftar

    def _info_dasar(self):
        return f'{self.nama} ({self._umur} th)'

    def peran(self):
        return 'pelatih'

    def tampilkan_profil(self):
        print(f'{self._info_dasar()} | Peran: {self.peran()} | Terdaftar: {self.__tanggal_daftar}')


# Class ProgressLog (Komposisi dengan User)
class ProgressLog:
    def __init__(self, tanggal, berat_badan, catatan=''):
        self.tanggal = tanggal
        self.berat_badan = berat_badan
        self.catatan = catatan

    def tampilkan(self):
        catatan = self.catatan or '-'
        print(f'  {self.tanggal} | {self.berat_badan}kg | {catatan}')

    # Duck typing
    def ringkasan(self):
        return f'ProgressLog {self.tanggal}: {self.berat_badan}kg'


# Class User (Subclass dari pelatih)
class User(pelatih):
    nama_aplikasi = 'FitTrack Pro'
    total_user = 0

    def __init__(self, nama, umur, berat_badan):
        super().__init__(nama, umur)
        User.total_user += 1
        self.__id_user = f'USR-{User.total_user:03d}'
        self.__berat_badan = None
        self.berat_badan = berat_badan
        self.__progress_log = []
        self.trainer = None

    @property
    def id_user(self):
        return self.__id_user

    @property
    def berat_badan(self):
        return self.__berat_badan

    @berat_badan.setter
    def berat_badan(self, value):
        if not User.validasi_berat(value):
            print(f'[GAGAL] Berat badan tidak valid: {value}. Harus angka positif.')
            return
        self.__berat_badan = value

    @property
    def riwayat_progress(self):
        return list(self.__progress_log)

    def catat_progres(self, berat_baru, catatan=''):
        if not User.validasi_berat(berat_baru):
            print(f'[GAGAL] Progres tidak dicatat, berat tidak valid: {berat_baru}')
            return
        self.__berat_badan = berat_baru
        # Komposisi
        log = ProgressLog(datetime.date.today().isoformat(), berat_baru, catatan)
        self.__progress_log.append(log)
        print(f'[INFO] Progres {self.nama} dicatat: {berat_baru}kg')

    def tampilkan_riwayat(self):
        print(f'Riwayat progres {self.nama}:')
        if not self.__progress_log:
            print('  (Belum ada catatan)')
        for log in self.__progress_log:
            log.tampilkan()

    # Override
    def peran(self):
        return 'Member'

    def tampilkan_profil(self):
        nama_trainer = self.trainer.nama if self.trainer else '-'
        print(f'{self.__id_user} | {self._info_dasar()} | Berat badan: {self.__berat_badan}kg '
              f'| Trainer: {nama_trainer}')

    # Operator overloading
    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.__id_user == other.id_user

    def __hash__(self):
        return hash(self.__id_user)

    def __str__(self):
        return f'User {self.__id_user} - {self.nama}'

    @classmethod
    def dari_dict(cls, data):
        return cls(data['nama'], data['umur'], data['berat_badan'])

    @classmethod
    def info_aplikasi(cls):
        print(f'{cls.nama_aplikasi} | Total user terdaftar: {cls.total_user}')

    @staticmethod
    def validasi_berat(value):
        return isinstance(value, (int, float)) and value > 0

    @staticmethod
    def kategori_bb(berat):
        if berat < 55:
            return 'Ringan'
        elif berat < 80:
            return 'Sedang'
        return 'Berat'


# Class Trainer (Subclass dari pelatih)
class Trainer(pelatih):
    total_trainer = 0

    def __init__(self, nama, umur, spesialisasi, pengalaman_tahun):
        super().__init__(nama, umur)
        Trainer.total_trainer += 1
        self.spesialisasi = spesialisasi
        self.pengalaman_tahun = pengalaman_tahun
        self.__daftar_user = []

    @property
    def jumlah_user(self):
        return len(self.__daftar_user)

    # Asosiasi
    def bimbing(self, user):
        if not isinstance(user, User):
            print('[GAGAL] Yang dibimbing harus objek User.')
            return
        if user in self.__daftar_user:
            print(f'[GAGAL] {user.nama} sudah dibimbing {self.nama}.')
            return
        self.__daftar_user.append(user)
        user.trainer = self
        print(f'{self.nama} sekarang membimbing {user.nama}.')

    def tampilkan_user_bimbingan(self):
        print(f'User bimbingan {self.nama}:')
        for u in self.__daftar_user:
            print(f'  - {u.id_user} {u.nama}')

    # Override
    def peran(self):
        return f'Trainer {self.spesialisasi}'

    def tampilkan_profil(self):
        print(f'{self._info_dasar()} | {self.peran()} | Pengalaman: {self.pengalaman_tahun} th '
              f'| User dibimbing: {self.jumlah_user}')


# Class Exercise (Abstract Base Class / Superclass 2)
class Exercise(ABC):
    satuan_berat = 'kg'
    total_exercise = 0
    kategori_tersedia = ['Dada', 'Punggung', 'Kaki', 'Bahu', 'Lengan', 'Core', 'Cardio']

    def __init__(self, nama_latihan, sets, reps, kategori='Dada'):
        Exercise.total_exercise += 1
        self.__id_exercise = f'EX-{Exercise.total_exercise:03d}'
        self.nama_latihan = nama_latihan
        self._sets = sets
        self._reps = reps
        self._kategori = kategori if kategori in Exercise.kategori_tersedia else 'Dada'

    @property
    def id_exercise(self):
        return self.__id_exercise

    @property
    def kategori(self):
        return self._kategori

    @property
    def sets(self):
        return self._sets

    @property
    def reps(self):
        return self._reps

    def _info_dasar(self):
        return f'{self.__id_exercise} | {self.nama_latihan} [{self._kategori}]'

    # Abstract method
    @abstractmethod
    def hitung_volume(self):
        pass

    @abstractmethod
    def hitung_kalori(self):
        pass

    @abstractmethod
    def detail_latihan(self):
        pass

    # Method konkret
    def tampilkan_info(self):
        print(f'{self._info_dasar()} {self.detail_latihan()} '
              f'| Volume: {self.hitung_volume()}{Exercise.satuan_berat} '
              f'| Kalori: ~{self.hitung_kalori()} kkal')

    # Operator overloading
    def __str__(self):
        return f'{self.nama_latihan} (~{self.hitung_kalori()} kkal)'

    def __lt__(self, other):
        if not isinstance(other, Exercise):
            return NotImplemented
        return self.hitung_kalori() < other.hitung_kalori()

    def __gt__(self, other):
        if not isinstance(other, Exercise):
            return NotImplemented
        return self.hitung_kalori() > other.hitung_kalori()

    @classmethod
    def ubah_satuan_berat(cls, satuan_baru):
        cls.satuan_berat = satuan_baru
        print(f'[INFO] Satuan berat sekarang: {cls.satuan_berat}')

    @staticmethod
    def validasi_nama_latihan(nama):
        return isinstance(nama, str) and nama.strip() != ''


# Class StrengthExercise (Subclass dari Exercise)
class StrengthExercise(Exercise):
    def __init__(self, nama_latihan, sets, reps, berat_beban, alat='Barbell', kategori='Dada'):
        super().__init__(nama_latihan, sets, reps, kategori)
        self.alat = alat                    # Atribut unik
        self._berat_beban = None
        self.berat_beban = berat_beban

    @property
    def berat_beban(self):
        return self._berat_beban

    @berat_beban.setter
    def berat_beban(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError('Berat beban harus berupa angka positif.')
        self._berat_beban = value

    def hitung_volume(self):
        return self._sets * self._reps * self._berat_beban

    def hitung_kalori(self):
        return round(self.hitung_volume() * 0.02, 1)

    def detail_latihan(self):
        return (f'({self.alat}) {self._sets}x{self._reps} '
                f'@ {self._berat_beban}{Exercise.satuan_berat}')


# Class BodyweightExercise (Subclass dari Exercise)
class BodyweightExercise(Exercise):
    faktor_kesulitan = {'Mudah': 0.3, 'Sedang': 0.6, 'Sulit': 0.9}

    def __init__(self, nama_latihan, sets, reps, berat_badan, tingkat_kesulitan='Sedang',
                 kategori='Dada'):
        super().__init__(nama_latihan, sets, reps, kategori)
        if tingkat_kesulitan not in BodyweightExercise.faktor_kesulitan:
            raise ValueError(f'Tingkat kesulitan harus salah satu dari '
                             f'{list(BodyweightExercise.faktor_kesulitan)}.')
        self.tingkat_kesulitan = tingkat_kesulitan   # Atribut unik
        self._berat_badan = berat_badan

    def hitung_volume(self):
        faktor = BodyweightExercise.faktor_kesulitan[self.tingkat_kesulitan]
        return round(self._sets * self._reps * self._berat_badan * faktor, 1)

    def hitung_kalori(self):
        faktor = BodyweightExercise.faktor_kesulitan[self.tingkat_kesulitan]
        return round(self._sets * self._reps * faktor, 1)

    def detail_latihan(self):
        return f'(Bodyweight, {self.tingkat_kesulitan}) {self._sets}x{self._reps}'


# Class CardioExercise (Subclass dari Exercise)
class CardioExercise(Exercise):
    kalori_per_menit = {'Rendah': 5, 'Sedang': 8, 'Tinggi': 12}

    def __init__(self, nama_latihan, durasi_menit, intensitas='Sedang'):
        super().__init__(nama_latihan, 1, 1, 'Cardio')
        if not isinstance(durasi_menit, (int, float)) or durasi_menit <= 0:
            raise ValueError('Durasi harus berupa angka positif.')
        if intensitas not in CardioExercise.kalori_per_menit:
            raise ValueError(f'Intensitas harus salah satu dari '
                             f'{list(CardioExercise.kalori_per_menit)}.')
        self.durasi_menit = durasi_menit        # Atribut unik
        self.intensitas = intensitas

    def hitung_volume(self):
        return 0

    def hitung_kalori(self):
        return round(self.durasi_menit * CardioExercise.kalori_per_menit[self.intensitas], 1)

    def detail_latihan(self):
        return f'{self.durasi_menit} menit, intensitas {self.intensitas}'


# Class StretchingExercise (Subclass dari Exercise) - OCP
class StretchingExercise(Exercise):
    def __init__(self, nama_latihan, sets, detik_tahan, kategori='Core'):
        super().__init__(nama_latihan, sets, 1, kategori)
        self.detik_tahan = detik_tahan          # Atribut unik

    def hitung_volume(self):
        return 0

    def hitung_kalori(self):
        return round(self._sets * self.detik_tahan * 0.05, 1)

    def detail_latihan(self):
        return f'(Stretching) {self._sets}x tahan {self.detik_tahan} detik'


# Class SesiLatihan (Komposisi dengan WorkoutRoutine)
class SesiLatihan:
    def __init__(self, nomor, nama_routine, total_volume, total_kalori):
        self.nomor = nomor
        self.tanggal = datetime.date.today().isoformat()
        self.nama_routine = nama_routine
        self.total_volume = total_volume
        self.total_kalori = total_kalori

    def tampilkan(self):
        print(f'  Sesi #{self.nomor} | {self.tanggal} | {self.nama_routine} '
              f'| Volume: {self.total_volume}{Exercise.satuan_berat} '
              f'| Kalori: ~{self.total_kalori} kkal')

    # Duck typing
    def ringkasan(self):
        return f'Sesi #{self.nomor} {self.nama_routine}: ~{self.total_kalori} kkal'


# Class WorkoutRoutine (Asosiasi ke User, Agregasi Exercise, Komposisi SesiLatihan)
class WorkoutRoutine:
    total_routine = 0
    kategori_valid = ['Push', 'Pull', 'Legs', 'Full Body']
    nama_instansi = 'FitTrack Studio'

    # Asosiasi ke User, Dependency injection (DIP)
    def __init__(self, nama_routine, user, kategori='Full Body'):
        WorkoutRoutine.total_routine += 1
        self.nama_routine = nama_routine
        self.user = user
        self.__daftar_latihan = []
        self.__riwayat_sesi = []
        self.__kategori = 'Full Body'
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

    @property
    def riwayat_sesi(self):
        return list(self.__riwayat_sesi)

    # Agregasi
    def tambah_latihan(self, exercise):
        if not isinstance(exercise, Exercise):
            print('[GAGAL] Objek yang ditambahkan bukan Exercise.')
            return
        self.__daftar_latihan.append(exercise)
        print(f"'{exercise.nama_latihan}' ditambahkan ke routine '{self.nama_routine}'.")

    def hitung_total_volume(self):
        return round(sum(ex.hitung_volume() for ex in self.__daftar_latihan), 1)

    def hitung_total_kalori(self):
        return round(sum(ex.hitung_kalori() for ex in self.__daftar_latihan), 1)

    def tampilkan_routine(self):
        print(f'Routine: {self.nama_routine} ({self.kategori}) milik {self.user.nama}')
        if not self.__daftar_latihan:
            print('  (Belum ada latihan)')
            return
        for ex in self.__daftar_latihan:
            print('  -', end=' ')
            ex.tampilkan_info()
        print(f'  Total volume routine: {self.hitung_total_volume()}{Exercise.satuan_berat}')
        print(f'  Total kalori routine: ~{self.hitung_total_kalori()} kkal')

    # Komposisi
    def mulai_sesi(self):
        nomor = len(self.__riwayat_sesi) + 1
        sesi = SesiLatihan(nomor, self.nama_routine, self.hitung_total_volume(), self.hitung_total_kalori())
        self.__riwayat_sesi.append(sesi)
        print(f"[INFO] Sesi #{nomor} routine '{self.nama_routine}' dicatat.")

    def tampilkan_riwayat_sesi(self):
        print(f"Riwayat sesi routine '{self.nama_routine}':")
        if not self.__riwayat_sesi:
            print('  (Belum ada sesi)')
        for sesi in self.__riwayat_sesi:
            sesi.tampilkan()

    # Operator overloading
    def __len__(self):
        return len(self.__daftar_latihan)

    def __add__(self, other):
        if not isinstance(other, WorkoutRoutine):
            return NotImplemented
        gabungan = WorkoutRoutine(f'{self.nama_routine} + {other.nama_routine}', self.user)
        for ex in self.__daftar_latihan + other.__daftar_latihan:
            gabungan.__daftar_latihan.append(ex)
        return gabungan

    def __str__(self):
        return f"Routine '{self.nama_routine}' ({self.kategori}, {len(self)} latihan)"

    # Duck typing
    def ringkasan(self):
        return f"Routine '{self.nama_routine}': {len(self)} latihan, ~{self.hitung_total_kalori()} kkal"

    @classmethod
    def tambah_kategori_baru(cls, kategori_baru):
        if kategori_baru not in cls.kategori_valid:
            cls.kategori_valid.append(kategori_baru)
            print(f"[INFO] Kategori '{kategori_baru}' ditambahkan ke daftar kategori valid.")

    @staticmethod
    def validasi_jumlah_latihan(jumlah, maksimal=10):
        return isinstance(jumlah, int) and 0 <= jumlah <= maksimal


# Class Gym (Agregasi dengan Trainer dan User)
class Gym:
    def __init__(self, nama):
        self.nama = nama
        self.__daftar_trainer = []
        self.__daftar_member = []

    # Agregasi
    def tambah_trainer(self, trainer):
        if not isinstance(trainer, Trainer):
            print('[GAGAL] Objek yang ditambahkan bukan Trainer.')
            return
        self.__daftar_trainer.append(trainer)
        print(f'Trainer {trainer.nama} bergabung di {self.nama}.')

    # Agregasi
    def tambah_member(self, user):
        if not isinstance(user, User):
            print('[GAGAL] Objek yang ditambahkan bukan User.')
            return
        self.__daftar_member.append(user)
        print(f'Member {user.nama} terdaftar di {self.nama}.')

    def tampilkan_info(self):
        print(f'Gym: {self.nama} | Trainer: {len(self.__daftar_trainer)} '
              f'| Member: {len(self.__daftar_member)}')
        for t in self.__daftar_trainer:
            print(f'  [Trainer] {t.nama}')
        for m in self.__daftar_member:
            print(f'  [Member]  {m.nama}')

    # Duck typing
    def ringkasan(self):
        return (f'Gym {self.nama}: {len(self.__daftar_trainer)} trainer, '
                f'{len(self.__daftar_member)} member')


# Duck typing
def cetak_ringkasan(*daftar_objek):
    for objek in daftar_objek:
        print(' ', objek.ringkasan())


def judul(teks):
    print(f'\n{teks}')


# Pengujian

judul('1. Pembuatan objek')
user1 = User("Prabowo", 21, 80)
trainer1 = Trainer("Joko", 30, "Strength", 7)
bench = StrengthExercise("Bench Press", 3, 8, 70)
pushup = BodyweightExercise("Push Up", 3, 15, user1.berat_badan)
lari = CardioExercise("Lari Treadmill", 30)
print('Objek User, Trainer, dan 3 Exercise berhasil dibuat.')

judul('2. Bukti abstract class tidak bisa diinstansiasi')
try:
    latihan = Exercise("Latihan Abstrak", 1, 1)
except TypeError as e:
    print("[TypeError]", e)

judul('3. Polimorfisme via pewarisan (satu loop, banyak subclass)')
print(user1.peran(), "|", trainer1.peran())
for orang in (user1, trainer1):
    orang.tampilkan_profil()
for ex in (bench, pushup, lari):
    ex.tampilkan_info()

judul('4. Validasi setter')
user1.berat_badan = -10
try:
    bench.berat_beban = 0
except ValueError as e:
    print("[GAGAL]", e)

judul('5. Asosiasi (Trainer <-> User)')
trainer1.bimbing(user1)
user1.tampilkan_profil()

judul('6. Agregasi (WorkoutRoutine o-- Exercise)')
routine = WorkoutRoutine("Upper Body", user1, "Push")
routine.tambah_latihan(bench)
routine.tambah_latihan(pushup)
routine.tampilkan_routine()

# Operator overloading
judul('7. Operator overloading')
routine2 = WorkoutRoutine("Cardio Day", user1, "Full Body")
routine2.tambah_latihan(lari)
routine2.tambah_latihan(StretchingExercise("Plank Hold", 3, 30))
gabungan = routine + routine2
print(gabungan)
print('len(gabungan) =', len(gabungan))
print('bench > pushup  :', bench > pushup)
print('bench < lari    :', bench < lari)
print('Urut kalori naik:', [str(ex) for ex in sorted([bench, pushup, lari])])
print('user1 == user1  :', user1 == user1)

judul('8. Duck typing (class tidak berhubungan, satu fungsi)')
gym = Gym("FitTrack Studio Gym")
gym.tambah_trainer(trainer1)
gym.tambah_member(user1)
user1.catat_progres(81, "Minggu 1")
routine.mulai_sesi()
cetak_ringkasan(gym, routine, routine.riwayat_sesi[0], user1.riwayat_progress[0])

judul('9. Agregasi: routine dihapus, Exercise tetap hidup')
del routine
bench.tampilkan_info()

judul('10. Komposisi (User *-- ProgressLog)')
user1.tampilkan_riwayat()