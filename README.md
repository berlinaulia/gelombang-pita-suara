# Simulasi Persamaan Gelombang pada Pita Suara
Pita suara adalah lipatan jaringan yang terdapat di laring yang berfungsi untuk menghasilkan suara. Saat udara dari paru-paru mengalir melalui pita suara, lipatan ini bergetar dan menghasilkan gelombang suara. Memahami dinamika gelombang ini penting untuk berbagai aplikasi, mulai dari kesehatan hingga teknologi suara.

Pita suara dianggap sebagai membran persegi dengan panjang dan lebar masing-masing L = 1t . Pada t = 0, diberikan gangguan awal berupa simpangan sinusoidal dengan amplitudo A = 0.1m Tegangan T dan massa per satuan luas o dari membran tersebut menghasilkan gelombang c = 1m / s Simulasikan dinamika getaran pita suara selama t = 2s u(x, y, 0) = A * sin((phi * x) / L) * sin((phi * y) / L). Kondisi awal diberikan sebagai simpangan sinusoidal: du/dt (x, y, 0) = 0

Kondisi batas adalah kondisi batas tetap (dirichlet): c(0, y, t) = u(L, y, t) = u(x, 0, t) = u(x, L, t) = 0 Dengan bantuan python kita akan menggunakan metode perbedaan hingga untuk melakukan simulasinya.
