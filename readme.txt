### delivery_rj_ongkir v1.0
### module ini masih tahap development di odoo versi 11. Odoo versi lain belum dilakukan pengetesan.

### next version: 
###    1. Account Starter
###        - penambahan feature : Pengecekan daftar profinsi
###        - type field nama kurrier akan diganti (untuk scalelabiltiy)
###    1. Account Basic
###        - penambahan feature : Lacaak Paket(Resi) JNE
###
###    2. Account Pro


User documentation:

Cara menggunakan module delivery_rj_ongkir:
- install module/feature delivery_rj_ongkir
- setelah terinstall, masuk ke setting: inventory-> configuration -> delivery method. Pilih setting untuk Raja Onkir yang sudah tercreate otomatis saat penginstalan.
- dibagian token silahkan copy paste token yang anda dapatkan dari raja ongkir dan url conn : api.rajaongkir.com kemudian save.
- setelah semua tersetting dengan baik, kini module featurenya sudah bisa dipakai dari aplikasi sales

Settingan penggunaan:
- Pastikan city dari company sudah diisi dengan id kota yang ada di indonesia (untuk melihatnya, bisa dilihat melalui feature check profinsi (next version) melalui api check profinsi)
- Pastikan city dari partner/customer di isi dengan id kota yang ada di indonesia

nb: jika ada terjadi error(bug) saat pemakaian module, silahkan email: henrotanjung@gmail.com


Developer documentations:

