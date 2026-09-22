# FitTrack Pro : Sistem Monitoring Progres Otot dan Management Workout

## Penjelasan Program

Program ini punya tiga class utama yang saling berdiri sendiri tapi bisa
berinteraksi lewat objek, tanpa pakai pewarisan sama sekali. Class pertama
namanya User, class kedua Exercise, dan class ketiga WorkoutRoutine yang
menghubungkan keduanya.

### Class User

Class ini nyimpen data seorang pengguna aplikasi. Setiap kali objek baru
dibuat, jumlah total user otomatis nambah lewat atribut kelas total_user.
Ada juga atribut kelas nama_aplikasi yang isinya sama buat semua objek,
jadi bukan milik satu user doang.

Atribut nama dan umur sifatnya public, bisa langsung diakses dan diubah
dari luar. Sementara id_user dan berat_badan sifatnya private, ditandai
pakai garis bawah ganda di depan namanya. Karena private, dua atribut ini
cuma bisa diakses lewat property yang sudah disediakan.

Khusus berat_badan, ada validasi di bagian setter-nya. Kalau nilai yang
dimasukkan bukan angka atau angkanya nol ke bawah, perubahan bakal ditolak
dan program mencetak pesan gagal, nilai lama tetap dipertahankan.

Method yang tersedia di class ini ada tiga jenis. Yang pertama
tampilkan_profil, ini instance method biasa buat nampilin data user ke
layar. Yang kedua ada dua classmethod, dari_dict buat bikin objek User
langsung dari data dictionary, dan info_aplikasi buat nampilin info
aplikasi beserta jumlah user yang sudah terdaftar. Terakhir ada
kategori_bb, ini staticmethod yang tugasnya cuma mengelompokkan berat
badan jadi ringan, sedang, atau berat, tanpa perlu data dari objek
tertentu.

### Class Exercise

Class ini nyimpen data satu latihan, mulai dari nama latihan, jumlah set,
jumlah repetisi, berat beban, sampai kategorinya. Ada tiga atribut kelas
di sini, satuan_berat buat nentuin satuan berat yang dipakai,
total_exercise buat ngitung berapa banyak latihan yang sudah dibuat, dan
kategori_tersedia yang isinya daftar kategori yang boleh dipakai.

Atribut nama_latihan, sets, reps, dan kategori sifatnya public. Sementara
berat_beban sifatnya private dan cuma bisa diubah lewat property. Bedanya
sama User, kalau berat_beban diisi dengan nilai yang gak valid, program
bakal langsung memunculkan error ValueError, bukan cuma nampilin pesan
doang.

Instance method di class ini ada hitung_volume yang ngitung total volume
latihan dari perkalian set, repetisi, dan berat beban, sama
tampilkan_info buat nampilin semua info latihan sekaligus hasil
volumenya. Classmethod-nya namanya ubah_satuan_berat, dipakai buat ganti
satuan berat yang berlaku untuk semua objek Exercise. Terakhir ada
staticmethod validasi_nama_latihan yang ngecek apakah nama latihan yang
dimasukkan kosong atau enggak.

### Class WorkoutRoutine

Nah class ini yang menghubungkan User sama Exercise. Setiap routine punya
satu user pemiliknya dan bisa diisi banyak latihan sekaligus. Atribut
kelasnya ada total_routine buat ngitung jumlah routine yang sudah dibuat,
kategori_valid berisi daftar kategori routine yang boleh dipakai, dan
nama_instansi.

Atribut nama_routine dan user sifatnya public. Daftar latihan yang
disimpan di dalam routine sifatnya private, begitu juga kategori
routine-nya, keduanya cuma bisa diakses lewat property atau method
khusus yang sudah disediakan. Kalau kategori yang dimasukkan gak ada di
daftar kategori_valid, perubahan bakal ditolak dan muncul pesan gagal.

Instance method-nya ada tambah_latihan buat masukin objek Exercise ke
dalam routine, tampilkan_routine buat nampilin seluruh isi routine
beserta total volumenya, dan hitung_total_volume buat ngejumlahin volume
semua latihan yang ada di routine tersebut. Classmethod-nya namanya
tambah_kategori_baru, dipakai buat nambahin pilihan kategori baru ke
daftar kategori_valid. Terus ada staticmethod validasi_jumlah_latihan
yang ngecek apakah jumlah latihan masih dalam batas wajar atau enggak.

## Soal Validasi Data

Semua atribut private di program ini diakses lewat property, jadi ada
fungsi getter buat baca nilainya dan fungsi setter buat ubah nilainya.
Nama fungsi setter sengaja dibuat sama persis dengan nama fungsi
getter-nya, sesuai aturan penulisan Python yang benar.

Tiap kali ada percobaan mengubah data lewat setter, program bakal
mengecek dulu apakah nilainya masuk akal. Kalau enggak, ada dua cara
program menolaknya, bisa dengan mencetak pesan peringatan terus nilai
lama tetap dipakai, atau dengan memunculkan error yang bisa ditangkap
pakai try except.

## Panduan Pengujian

Buat nguji programnya, cukup jalankan file program.py terus perhatikan
output yang muncul secara berurutan.

Bagian pertama nunjukin pembuatan dua objek User, namanya Prabowo dan
Megawati, sekaligus pemanggilan semua jenis method yang ada di class
User, mulai dari instance method, classmethod, sampai staticmethod.

Bagian kedua nunjukin pembuatan dua objek Exercise, yaitu Bench Press dan
Barbell Squat, sekaligus pemanggilan semua method yang ada di class
Exercise.

Bagian ketiga nunjukin pembuatan dua objek WorkoutRoutine yang
masing-masing dihubungkan ke satu user dan satu latihan, jadi kelihatan
jelas kalau class ini memang saling berinteraksi lewat objek, bukan
lewat pewarisan.

Bagian terakhir yang paling penting, di sini diuji coba pengisian setter
pakai data yang valid dan yang tidak valid secara bergantian. Berat badan
Prabowo dicoba diubah jadi angka positif dulu, terus dicoba lagi diisi
angka negatif buat mastiin validasinya jalan. Begitu juga sama berat
beban Bench Press dan kategori routine milik Megawati. Setiap kali data
yang tidak valid dimasukkan, program bakal nolak perubahan itu dan nilai
lama tetap dipertahankan, itu tandanya validasinya berhasil.
