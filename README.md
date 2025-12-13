# CPU-Scheduler
CPU Zamanlama Algoritmaları Karşılaştırmalı Simülasyonu
Geliştiren: DENİZ EKİZ
Öğrenci No: 20232013036
Ders: İşletim Sistemleri
Proje Türü: Python + Streamlit tabanlı simülasyon arayüzü
GitHub: https://github.com/denizekiz1201-source/Cpu-Scheduler.git

Proje Amacı
Bu proje, modern işletim sistemlerinin temel bileşenlerinden olan CPU zamanlama algoritmalarının performansını iki farklı yoğun iş yükü (veri durumu) altında karşılaştırmalı olarak incelemektedir. Simülasyon, Python ve Streamlit web çatısı kullanılarak interaktif bir arayüz ile sunulur. Algoritmalar, gerçek dünya senaryolarını daha iyi taklit etmek amacıyla eş zamanlı (multithreading) çalıştırılmış ve bağlam değiştirme yükü (context switch overhead) dikkate alınmıştır.

Kullanılan CPU Zamanlama Algoritmaları:
1-FCFS (First-Come, First-Served)
2-Non-Preemptive SJF (Shortest Job First - Öncelemeyen)
3-SRTF (Shortest Remaining Time First - Öncelikli SJF)
4-Non-Preemptive Priority (Öncelemeyen Öncelik)
5-Preemptive Priority (Öncelikli Öncelik)
6-Round Robin (Q=10) (Zaman Dilimli, Kuantum = 10ms)

Performans Ölçütleri:
-Ortalama Bekleme Süresi (Average Waiting Time)
-Ortalama Tamamlanma Süresi (Average Turnaround Time)
-Maksimum Bekleme / Tamamlanma Süresi (Max Waiting / Turnaround Time)
-CPU Verimliliği (Efficiency)
-Bağlam Değişimi Sayısı (Context Switch Count)
-Belirli Zaman Aralıklarında Üretim Hızı (Throughput  T = 50, 100, 150, 200)

Kurulum ve Çalıştırma:
Bu simülasyon bir Python web uygulama çatısı olan Streamlit kullanılarak geliştirilmiştir.


Kurulum ve Çalıştırma:
Python 3.x
Gerekli Kütüphaneler: streamlit, pandas, copy, collections, concurrent.futures
Bu simülasyon bir Python web uygulama çatısı olan Streamlit kullanılarak geliştirilmiştir.

1.Ön Gereksinimler:
Projenin çalışması için bilgisayarınızda Python kurulu olmalıdır.
2.Bağımlılıkların Kurulumu:
Proje, streamlit ve pandas kütüphanelerine ihtiyaç duyar. Bu kütüphaneleri terminal/komut istemcisi üzerinden aşağıdaki komutla kurabilirsiniz:
pip install streamlit pandas

Uygulamayı Çalıştırma:
cpu_scheduler.py dosyasını indirdikten veya klonladıktan sonra, terminalinizde dosyanın bulunduğu dizine gidin ve aşağıdaki komutu çalıştırın:  streamlit run cpu_scheduler.py 
Bu komut, uygulamayı varsayılan web tarayıcınızda açacaktır (Genellikle http://localhost:8501).

Kullanım ve Analiz
Uygulama arayüzü iki ana bölümden oluşur:
1.Seçim Paneli (Sidebar)
Veri Durumunu Seçin: Simülasyonu çalıştırmak istediğiniz ön tanımlı veri setini seçin (Case 1 veya Case 2).
Simülasyon Ayarları: Sabit olarak tanımlanmış Round Robin Quantum ve Bağlam Değiştirme Süresi (Context Switch Overhead) değerlerini görebilirsiniz.

2.Algoritma Karşılaştırması
Tüm algoritmalar seçilen veri seti üzerinde eş zamanlı olarak çalıştırılır ve aşağıdaki metrikler karşılaştırmalı bir tabloda sunulur:
-Ort. Bekleme Süresi: Süreçlerin ortalama ne kadar beklediği.
-Ort. Tamamlanma Süresi: Süreçlerin başlangıcından bitişine kadar geçen ortalama süre.
-Maks. Bekleme/Tamamlanma Süresi: Açlık (starvation) riskini ve en uzun süren işleri gösterir.
-Verimlilik (Efficiency): CPU'nun iş yapmakla geçirdiği sürenin toplam süreye oranı.
-Bağlam Değişimi Sayısı: Algoritmanın Overhead (Ek Yük) miktarını gösterir.Throughput (T=200): Belirli bir zaman (örneğin $T=200$ birim zaman) içinde tamamlanan iş sayısı

3.Detaylı Analiz
Bu bölümde, açılır menüden seçtiğiniz algoritmaya ait detaylı verileri inceleyebilirsiniz:
-Zaman Çizelgesi (Gantt Chart Verisi): Hangi süreçlerin hangi zaman aralıklarında CPU'yu kullandığını gösterir.
-Throughput Detayı: $T=50, 100, 150, 200$ zaman noktalarındaki tamamlanan iş sayısını gösterir.
-Süreç Bazlı Metrikler: Her bir sürecin (P001, P002, ...) kendi Bekleme Süresi, Tamamlanma Süresi ve Bitiş Zamanı verilerini listeler.

Ek Notlar:
Projeye yeni algoritmalar veya farklı veri setleri eklemek kolaylıkla mümkündür.
concurrent.futures.ThreadPoolExecutor kullanımı, Streamlit'in yapısı gereği arayüzün kilitlenmemesi ve simülasyonların eş zamanlı olarak stabil çalışması için tercih edilmiştir.
Bağlam değiştirme yükü (Context Switch Overhead), sadece preemptive (öncelikli) ve Round Robin algoritmalarında, süreç değişimi sırasında zaman çizelgesine dahil edilmiştir.
