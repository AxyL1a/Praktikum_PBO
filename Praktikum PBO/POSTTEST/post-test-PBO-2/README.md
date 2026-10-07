Nama : Denny Mulia
kelas : A1'25
NIM : 2509106011


# FitTrack Pro : Sistem Monitoring Progres Otot dan Management Workout

## Penjelasan Program

Program ini punya sebelas class yang berinteraksi lewat pewarisan
(inheritance) dan relasi antar objek (asosiasi, agregasi, komposisi).
Ada dua hierarki pewarisan. Yang pertama class pelatih sebagai induk
dari User dan Trainer. Yang kedua class Exercise sebagai induk dari
StrengthExercise, BodyweightExercise, dan CardioExercise. Class
WorkoutRoutine menghubungkan User, Exercise, dan SesiLatihan, sementara
ProgressLog dan Gym jadi class pendukungnya.

### Class pelatih

Ini superclass pertama, nyimpen data dasar seseorang di aplikasi. Setiap
objek baru bikin total_person otomatis nambah. Atribut nama sifatnya
public, _umur sifatnya protected karena perlu diakses subclass, dan
__tanggal_daftar sifatnya private karena cuma urusan class ini, jadi
dibaca lewat property tanggal_daftar.

Khusus umur, ada validasi di setter-nya. Kalau nilainya bukan bilangan
bulat positif, perubahan ditolak dan program mencetak pesan gagal, nilai
lama tetap dipertahankan.

Method-nya ada _info_dasar (protected, dipakai subclass), peran, dan
tampilkan_profil. Dua method terakhir di-override oleh subclass.

### Class User

Subclass dari pelatih yang nyimpen data pengguna aplikasi. Konstruktornya
manggil super().__init__ buat ngirim nama dan umur ke induknya. Ada
atribut kelas total_user dan nama_aplikasi. Atribut id_user, berat_badan,
dan daftar progress sifatnya private, sedangkan atribut trainer sifatnya
public dan awalnya kosong.

Setter berat_badan punya validasi, kalau nilainya bukan angka positif
maka ditolak dengan pesan gagal. Method catat_progres dipakai buat
nyimpen riwayat berat badan, dan tampilkan_riwayat buat nampilinnya.
Method peran dan tampilkan_profil di-override. Classmethod-nya dari_dict
dan info_aplikasi, sedangkan staticmethod-nya validasi_berat dan
kategori_bb.

### Class Trainer

Subclass kedua dari pelatih. Atribut uniknya spesialisasi dan
pengalaman_tahun, ditambah daftar user bimbingan yang sifatnya private.
Method bimbing dipakai buat masukin user ke daftar bimbingan sekaligus
ngisi atribut trainer milik user tersebut. Kalau user yang sama
dimasukkan dua kali, program nolak dengan pesan gagal. Method peran dan
tampilkan_profil di-override.

### Class Exercise

Superclass kedua yang nyimpen data dasar satu latihan. Ada tiga atribut
kelas, yaitu satuan_berat, total_exercise, dan kategori_tersedia. Atribut
nama_latihan sifatnya public, _sets, _reps, dan _kategori sifatnya
protected, sedangkan __id_exercise sifatnya private dan dibaca lewat
property id_exercise.

Instance method-nya ada hitung_volume (hasil dasarnya 0), hitung_kalori,
dan tampilkan_info. Classmethod-nya ubah_satuan_berat dan staticmethod-nya
validasi_nama_latihan, keduanya otomatis diwarisi semua subclass.

### Class StrengthExercise

Subclass Exercise buat latihan beban. Atribut uniknya alat dan
_berat_beban. Kalau berat_beban diisi nilai yang gak valid, program
langsung memunculkan ValueError. Method hitung_volume, hitung_kalori, dan
tampilkan_info di-override dengan rumus volume set x repetisi x beban.

### Class BodyweightExercise

Subclass Exercise buat latihan pakai berat badan sendiri seperti push up.
Atribut uniknya tingkat_kesulitan (Mudah, Sedang, atau Sulit) yang
menentukan faktor pengali. Kalau tingkat kesulitannya di luar pilihan,
muncul ValueError. Method hitung_volume, hitung_kalori, dan
tampilkan_info di-override.

### Class CardioExercise

Subclass Exercise buat latihan kardio. Atribut uniknya durasi_menit dan
intensitas (Rendah, Sedang, atau Tinggi). Set dan repetisi diisi 1 dan
kategorinya dikunci "Cardio". Durasi yang gak positif atau intensitas
yang gak ada di pilihan memunculkan ValueError. Method hitung_kalori dan
tampilkan_info di-override, sedangkan hitung_volume memakai versi induk.

### Class WorkoutRoutine

Class yang menghubungkan User, Exercise, dan SesiLatihan. Setiap routine
punya satu user pemiliknya dan bisa diisi banyak latihan dari jenis apa
pun. Atribut kelasnya total_routine, kategori_valid, dan nama_instansi.
Daftar latihan, riwayat sesi, dan kategori sifatnya private. Kalau
kategori yang dimasukkan gak ada di kategori_valid, perubahan ditolak
dan muncul pesan gagal.

Instance method-nya ada tambah_latihan, hitung_total_volume,
hitung_total_kalori, tampilkan_routine, mulai_sesi, dan
tampilkan_riwayat_sesi. Classmethod-nya tambah_kategori_baru dan
staticmethod-nya validasi_jumlah_latihan.

### Class ProgressLog, SesiLatihan, dan Gym

ProgressLog nyimpen tanggal, berat badan, dan catatan satu kali
pencatatan progres. SesiLatihan nyimpen nomor sesi, tanggal, nama
routine, total volume, dan total kalori. Gym nampung banyak Trainer dan
User lewat tambah_trainer dan tambah_member, dan nolak objek yang bukan
tipenya.

## Penerapan Inheritance

Program ini punya dua superclass dan lima subclass. Semua subclass
manggil konstruktor induknya lewat super().__init__ dan punya atribut
unik yang gak dimiliki induk maupun saudaranya, misalnya spesialisasi
di Trainer, alat di StrengthExercise, tingkat_kesulitan di
BodyweightExercise, dan durasi_menit di CardioExercise.

Method overriding dipakai di banyak tempat. peran dan tampilkan_profil
di-override oleh User dan Trainer. hitung_volume, hitung_kalori, dan
tampilkan_info di-override oleh subclass Exercise dengan rumus
masing-masing. Karena namanya sama, WorkoutRoutine bisa manggil method
itu ke semua jenis latihan tanpa perlu ngecek tipenya.

Untuk tingkat akses, atribut protected (satu garis bawah) dipakai buat
data yang perlu diakses langsung subclass, seperti _umur, _sets, dan
_reps. Atribut private (garis bawah ganda) dipakai buat data eksklusif
superclass, yaitu __tanggal_daftar dan __id_exercise, yang cuma bisa
dibaca subclass lewat property.

## Penerapan Relasi UML

Asosiasi dipakai antara Trainer dan User yang saling kenal dua arah lewat
method bimbing, serta antara WorkoutRoutine dan User lewat atribut user
sebagai pemilik routine. Kedua objek tetap hidup sendiri-sendiri.

Agregasi dipakai antara WorkoutRoutine dan Exercise, serta antara Gym
dengan Trainer dan User. Objek bagiannya dibuat di luar lalu
dimasukkan, jadi tetap hidup walau induknya dihapus.

Komposisi dipakai antara User dan ProgressLog, serta antara
WorkoutRoutine dan SesiLatihan. Objek bagiannya dibuat di dalam
method catat_progres dan mulai_sesi, bukan dari luar, jadi nasibnya
ikut induknya.

## Soal Validasi Data

Semua atribut private di program ini diakses lewat property, jadi ada
fungsi getter buat baca nilainya dan fungsi setter buat ubah nilainya.
Nama fungsi setter sengaja dibuat sama persis dengan nama fungsi
getter-nya, sesuai aturan penulisan Python yang benar.

Tiap kali ada percobaan mengubah data lewat setter, program bakal
mengecek dulu apakah nilainya masuk akal. Kalau enggak, ada dua cara
program menolaknya, bisa dengan mencetak pesan peringatan terus nilai
lama tetap dipakai (umur, berat badan, kategori routine), atau dengan
memunculkan error yang bisa ditangkap pakai try except (berat beban,
tingkat kesulitan, durasi, dan intensitas).

## Panduan Pengujian

Buat nguji programnya, cukup jalankan file program.py terus perhatikan
output yang muncul secara berurutan.

Bagian pertama nunjukin pembuatan objek User bernama Prabowo, Trainer
bernama Joko, serta tiga jenis Exercise, yaitu Bench Press, Push Up, dan
Lari Treadmill. Hasil method peran dan tampilkan_info dicetak, jadi
kelihatan kalau method yang sama menghasilkan format dan rumus yang
berbeda di tiap class, itu tandanya inheritance dan overriding jalan.

Bagian kedua nguji setter. Berat badan Prabowo dicoba diisi -10 dan
ditolak dengan pesan gagal, lalu berat beban Bench Press dicoba diisi 0
dan ditolak dengan ValueError.

Bagian ketiga nunjukin asosiasi, yaitu Joko membimbing Prabowo, lalu
profil Prabowo menampilkan nama trainernya.

Bagian keempat nunjukin agregasi. Bench Press dan Push Up dimasukkan ke
routine Upper Body, lalu routine dihapus pakai del. Setelah itu Bench
Press tetap bisa dipakai, itu tandanya objek latihan hidup mandiri.

Bagian terakhir nunjukin komposisi, yaitu progres berat badan Prabowo
dicatat lalu riwayatnya ditampilkan.
