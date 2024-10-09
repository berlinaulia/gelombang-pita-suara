# Simulasi Persamaan Gelombang pada Pita Suara
Pita suara adalah lipatan jaringan yang terdapat di laring yang berfungsi untuk menghasilkan suara. Saat udara dari paru-paru mengalir melalui pita suara, lipatan ini bergetar dan menghasilkan gelombang suara. Memahami dinamika gelombang ini penting untuk berbagai aplikasi, mulai dari kesehatan hingga teknologi suara.

Pita suara dianggap sebagai membran persegi dengan panjang dan lebar masing-masing L = 1t . Pada t = 0, diberikan gangguan awal berupa simpangan sinusoidal dengan amplitudo A = 0.1m Tegangan T dan massa per satuan luas o dari membran tersebut menghasilkan gelombang c = 1m / s Simulasikan dinamika getaran pita suara selama t = 2s u(x, y, 0) = A * sin((phi * x) / L) * sin((phi * y) / L). Kondisi awal diberikan sebagai simpangan sinusoidal: du/dt (x, y, 0) = 0

Kondisi batas adalah kondisi batas tetap (dirichlet): c(0, y, t) = u(L, y, t) = u(x, 0, t) = u(x, L, t) = 0 Dengan bantuan python kita akan menggunakan metode perbedaan hingga untuk melakukan simulasinya.

## Pembahasan
![Alt text](https://github.com/berlinaulia/gelombang-pita-suara/blob/main/preview/Screenshot%202024-06-08%20064337.png)
![Alt text](https://github.com/berlinaulia/gelombang-pita-suara/blob/main/preview/Screenshot%202024-06-08%20065817.png)
![Alt text](https://github.com/berlinaulia/gelombang-pita-suara/blob/main/preview/Screenshot%202024-06-08%20065836.png)
![Alt text](https://github.com/berlinaulia/gelombang-pita-suara/blob/main/preview/Screenshot%202024-06-08%20070654.png)


Warna kuning yang terang mewakili amplitudo tinggi gelombang suara, menunjukkan intensitas dan energi yang besar pada titik-titik tertentu di pita suara. Seiring waktu, gelombang ini merambat dan interaksinya dengan batas pita suara menyebabkan energi tersebut menyebar dan amplitudonya menurun, diwakili oleh perubahan warna dari kuning ke hijau. Transisi ini mencerminkan bagaimana energi gelombang suara berkurang dan meredup karena dampak redaman dan penyebaran energi di sepanjang pita

Pergerakan warna dari kuning ke hijau juga menggambarkan dinamika perambatan gelombang suara dalam pita suara sesuai dengan persamaan gelombang dua dimensi. Kondisi batas Dirichlet, yang memaksa gelombang menjadi nol di tepi pita, menghasilkan refleksi gelombang. Refleksi ini, bersama dengan kondisi awal yang ditetapkan, mengarah pada pembentukan pola interferensi yang kompleks di dalam pita suara.
