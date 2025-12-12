# Cpu-Scheduler

CPU Zamanlama Algoritmaları Karşılaştırmalı Simülasyonu
Geliştiren: DENİZ EKİZ
Öğrenci No: 20232013036
Ders: İşletim Sistemleri
Proje Türü: Python + Streamlit tabanlı simülasyon arayüzü

Proje Amacı
Bu proje, modern işletim sistemlerinin temel bileşenlerinden olan CPU zamanlama algoritmalarının performansını iki farklı yoğun iş yükü (veri durumu) altında karşılaştırmalı olarak incelemektedir. Simülasyon, Python ve Streamlit web çatısı kullanılarak interaktif bir arayüz ile sunulur. Algoritmalar, gerçek dünya senaryolarını daha iyi taklit etmek amacıyla eş zamanlı (multithreading) çalıştırılmış ve bağlam değiştirme yükü (context switch overhead) dikkate alınmıştır.

Kullanılan CPU Zamanlama Algoritmaları:
1)FCFS (First-Come, First-Served)
2)Non-Preemptive SJF (Shortest Job First - Öncelemeyen)
3)SRTF (Shortest Remaining Time First - Öncelikli SJF)
4)Non-Preemptive Priority (Öncelemeyen Öncelik)
5)Preemptive Priority (Öncelikli Öncelik)
6)Round Robin (Q=10) (Zaman Dilimli, Kuantum = 10ms)

Performans Ölçütleri:
-Ortalama Bekleme Süresi (Average Waiting Time)
-Ortalama Tamamlanma Süresi (Average Turnaround Time)
-Maksimum Bekleme / Tamamlanma Süresi (Max Waiting / Turnaround Time)
-CPU Verimliliği (Efficiency
-Bağlam Değişimi Sayısı (Context Switch Count)
-Belirli Zaman Aralıklarında Üretim Hızı (Throughput @ T = 50, 100, 150, 200)

