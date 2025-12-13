# 📑 CPU-Scheduler: Karşılaştırmalı Performans Raporu (Detaylı)

## Geliştirici ve Proje Bilgileri

* **Geliştiren:** DENİZ EKİZ
* **Öğrenci No:** 20232013036
* **Ders:** İşletim Sistemleri
* **Proje Türü:** Python + Streamlit tabanlı simülasyon arayüzü
* **GitHub:** [https://github.com/denizekiz1201-source/Cpu-Scheduler.git](https://github.com/denizekiz1201-source/Cpu-Scheduler.git)

##  Proje Amacı
Bu proje, modern işletim sistemlerinin temel bileşenlerinden olan CPU zamanlama algoritmalarının performansını iki farklı yoğun iş yükü (veri durumu) altında karşılaştırmalı olarak incelemektedir. Simülasyon, Python ve Streamlit web çatısı kullanılarak interaktif bir arayüz ile sunulmuştur. Algoritmalar, gerçek dünya senaryolarını daha iyi taklit etmek amacıyla eş zamanlı (multithreading) çalıştırılmış ve **bağlam değiştirme yükü (context switch overhead)** dikkate alınmıştır.


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

Senaryolar ve Zaman Çizelgeleri
Simülasyon iki farklı veri setiyle gerçekleştirilmiştir:
Case 1: 200 süreç
Case 2: 100 süreç
Her süreç için geliş zamanı, CPU burst süresi ve öncelik tanımlanmıştır.
Her algoritma için ayrı ayrı zaman çizelgeleri (Gantt benzeri) Streamlit tabanlı web arayüzünde üretilmiştir. Bu çizelgelerde CPU’nun hangi zaman aralığında hangi süreci çalıştırdığı net biçimde gösterilmektedir. IDLE süreleri ve bağlam değişimleri hesaplamalarda dikkate alınmıştır.


Case 1 (200 Süreç) Sonuçları

 Performans Tablosu
 
| Algoritma               | Ort. Bekleme | Maks. Bekleme | Ort. Tamamlama | Maks. Tamamlama | T=50 | T=100 | T=150 | T=200 | Ef.(%) | Bağl. Değişimi |
| ----------------------- | ------------ | ------------- | -------------- | --------------- | ---- | ----- | ----- | ----- | ------ | -------------- |
| **FCFS**                | 813.50       | 1683          | 823.99         | 1703            | 9    | 13    | 16    | 19    | 99.943 | 199            |
| **SRTF (Önceliği SJF)** | 537.00       | 1863          | 547.50         | 1883            | 11   | 22    | 32    | 42    | 99.942 | 212            |
| **NP-SJF**              | 537.42       | 1863          | 547.93         | 1883            | 11   | 22    | 32    | 42    | 99.943 | 199            |
| **Round Robin (Q=10)**  | 1003.49      | 1683          | 1013.99        | 1703            | 9    | 10    | 10    | 18    | 99.938 | 299            |
| **Öncelikli (Preemp.)** | 833.63       | 1689          | 844.13         | 1707            | 6    | 11    | 14    | 20    | 99.943 | 201            |
| **Öncelikli (NP)**      | 824.77       | 1689          | 835.27         | 1707            | 8    | 13    | 16    | 21    | 99.943 | 199            |

Yorum:
Case 1’de en düşük ortalama bekleme ve tamamlanma süreleri SJF tabanlı algoritmalarda elde edilmiştir. Round Robin algoritması ise yüksek bağlam değiştirme sayısı nedeniyle en yüksek bekleme ve tamamlanma sürelerine sahiptir. Throughput açısından en başarılı algoritmalar yine SJF tabanlı yöntemlerdir.


Case 2 (100 Süreç) Sonuçları

Performans Tablosu

| Algoritma                 | Ort. Bekleme | Maks. Bekleme | Ort. TAT | Maks. TAT | T=50 | T=100 | T=150 | T=200 | CPU Verimliliği (%) | Bağlam Değişimi |
| ------------------------- | ------------ | ------------- | -------- | --------- | ---- | ----- | ----- | ----- | ------------------- | --------------- |
| FCFS                      | 418.00       | 851           | 428.50   | 853       | 5    | 10    | 14    | 18    | 99.991              | 99              |
| SRTF (Preemptive SJF)     | 267.86       | 926           | 278.36   | 946       | 10   | 21    | 31    | 42    | 99.989              | 110             |
| Non-Preemptive SJF        | 268.39       | 926           | 278.89   | 946       | 10   | 21    | 30    | 42    | 99.991              | 99              |
| Round Robin (Q=10)        | 511.18       | 836           | 521.68   | 854       | 3    | 6     | 10    | 15    | 99.986              | 149             |
| Priority (Preemptive)     | 411.39       | 836           | 421.89   | 854       | 4    | 8     | 15    | 19    | 99.991              | 100             |
| Priority (Non-Preemptive) | 409.63       | 836           | 420.13   | 854       | 5    | 9     | 15    | 19    | 99.991              | 99              |


Yorum:
Case 2 sonuçları Case 1 ile tutarlıdır. SJF tabanlı algoritmalar en iyi ortalama performansı sunarken, Round Robin algoritması yüksek bağlam değiştirme maliyeti nedeniyle daha düşük throughput ve daha yüksek bekleme süreleri üretmiştir.

Etkileşimli Web Uygulaması 
Proje, Streamlit kullanılarak etkileşimli bir web uygulaması şeklinde geliştirilmiştir. 
Kullanıcılar:
-Case 1 / Case 2 seçebilir.
-6 algoritmayı eş zamanlı çalıştırabilir.
-Karşılaştırma tablolarını inceleyebilir.
-Algoritma bazlı zaman çizelgelerini ve süreç metriklerini görüntüleyebilir.
-Uygulama, çoklu iş parçacığı (ThreadPoolExecutor) kullanarak simülasyonları eş zamanlı çalıştırmaktadır.

Çalıştırmak için
Komut satırı / Terminal = streamlit run cpu_scheduler.py

Sonuç:
Simülasyon sonuçları, SJF tabanlı algoritmaların ortalama bekleme ve tamamlanma süreleri açısından en verimli yöntemler olduğunu göstermiştir. FCFS basit yapısına rağmen uzun işlerin sistem performansını olumsuz etkileyebildiği gözlemlenmiştir. Round Robin algoritması adil ve etkileşimli sistemler için uygun olsa da bağlam değiştirme maliyeti nedeniyle toplam performansı düşürmektedir. Tüm algoritmalarda CPU verimliliğinin %99’un üzerinde olması, sistemin yoğun iş yükü altında etkin çalıştığını göstermektedir.


Kaynakça
1)Silberschatz, A., Galvin, P. B., Gagne, G., Operating System Concepts
2)Tanenbaum, A. S., Modern Operating Systems
3)Stallings, W., Operating Systems: Internals and Design Principles
4)GeeksforGeeks – CPU Scheduling
5)Wikipedia – CPU Scheduling Algorithms















# 📑 CPU-Scheduler: Karşılaştırmalı Performans Raporu (Detaylı)

## Geliştirici ve Proje Bilgileri

* **Geliştiren:** DENİZ EKİZ
* **Öğrenci No:** 20232013036
* **Ders:** İşletim Sistemleri
* **Proje Türü:** Python + Streamlit tabanlı simülasyon arayüzü
* **GitHub:** [https://github.com/denizekiz1201-source/Cpu-Scheduler.git](https://github.com/denizekiz1201-source/Cpu-Scheduler.git)

---

## 🎯 Proje Amacı

Bu proje, modern işletim sistemlerinin temel bileşenlerinden olan CPU zamanlama algoritmalarının performansını iki farklı yoğun iş yükü (veri durumu) altında karşılaştırmalı olarak incelemektedir. Simülasyon, Python ve Streamlit web çatısı kullanılarak interaktif bir arayüz ile sunulmuştur. Algoritmalar, gerçek dünya senaryolarını daha iyi taklit etmek amacıyla eş zamanlı (multithreading) çalıştırılmış ve **bağlam değiştirme yükü (context switch overhead)** dikkate alınmıştır.

## ⚙️ Kullanılan CPU Zamanlama Algoritmaları

1.  **FCFS** (First-Come, First-Served)
2.  **Non-Preemptive SJF** (Shortest Job First - Öncelemeyen)
3.  **SRTF** (Shortest Remaining Time First - Öncelikli SJF)
4.  **Non-Preemptive Priority** (Öncelemeyen Öncelik)
5.  **Preemptive Priority** (Öncelikli Öncelik)
6.  **Round Robin (Q=10)** (Zaman Dilimli, Kuantum = 10ms)

## 📊 Performans Ölçütleri

Simülasyonda kullanılan temel performans metrikleri şunlardır:

* Ortalama Bekleme Süresi (Average Waiting Time)
* Ortalama Tamamlanma Süresi (Average Turnaround Time)
* Maksimum Bekleme / Tamamlanma Süresi (Max Waiting / Turnaround Time)
* CPU Verimliliği (Efficiency)
* Bağlam Değişimi Sayısı (Context Switch Count)
* Belirli Zaman Aralıklarında Üretim Hızı (**Throughput** T = 50, 100, 150, 200)

## 📝 Senaryolar ve Zaman Çizelgeleri

Simülasyon, süreçlerin geliş zamanı, CPU burst süresi ve önceliği tanımlanmış iki farklı veri setiyle gerçekleştirilmiştir:

* **Case 1:** 200 süreç
* **Case 2:** 100 süreç

Her algoritma için ayrı ayrı zaman çizelgeleri (Gantt benzeri) Streamlit arayüzünde üretilmiştir. Bu çizelgelerde CPU’nun hangi zaman aralığında hangi süreci çalıştırdığı net biçimde gösterilmiş; **IDLE süreleri** ve **bağlam değişimleri** hesaplamalarda dikkate alınmıştır.

---

## Case 1 (200 Süreç) Sonuçları

### Performans Tablosu

| Algoritma | Ort. Bekleme | Maks. Bekleme | Ort. Tamamlama | Maks. Tamamlama | T=50 | T=100 | T=150 | T=200 | Ef.(%) | Bağl. Değişimi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FCFS** | 813.50 | 1683 | 823.99 | 1703 | 9 | 13 | 16 | 19 | 99.943 | 199 |
| **SRTF (Önceliği SJF)** | **537.00** | 1863 | **547.50** | 1883 | 11 | **22** | **32** | **42** | 99.942 | 212 |
| **NP-SJF** | 537.42 | 1863 | 547.93 | 1883 | 11 | **22** | **32** | **42** | 99.943 | 199 |
| **Round Robin (Q=10)** | 1003.49 | 1683 | 1013.99 | 1703 | 9 | 10 | 10 | 18 | 99.938 | **299** |
| **Öncelikli (Preemp.)** | 833.63 | 1689 | 844.13 | 1707 | 6 | 11 | 14 | 20 | 99.943 | 201 |
| **Öncelikli (NP)** | 824.77 | 1689 | 835.27 | 1707 | 8 | 13 | 16 | 21 | 99.943 | 199 |

### Yorum

Case 1’de en düşük ortalama bekleme ve tamamlanma süreleri **SJF tabanlı algoritmalar** (SRTF ve NP-SJF) tarafından elde edilmiştir. Bu, kısa işlerin hızlıca tamamlanmasının gecikmeyi önemli ölçüde azalttığını göstermektedir. **Round Robin** algoritması ise yüksek bağlam değiştirme sayısı nedeniyle en yüksek bekleme ve tamamlanma sürelerine sahiptir. Throughput açısından en başarılı algoritmalar yine SJF tabanlı yöntemlerdir.

---

## Case 2 (100 Süreç) Sonuçları

### Performans Tablosu

| Algoritma | Ort. Bekleme | Maks. Bekleme | Ort. TAT | Maks. TAT | T=50 | T=100 | T=150 | T=200 | CPU Verimliliği (%) | Bağlam Değişimi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FCFS** | 418.00 | 851 | 428.50 | 853 | 5 | 10 | 14 | 18 | 99.991 | 99 |
| **SRTF (Preemptive SJF)** | **267.86** | 926 | **278.36** | 946 | 10 | **21** | **31** | **42** | 99.989 | 110 |
| **Non-Preemptive SJF** | 268.39 | 926 | 278.89 | 946 | 10 | **21** | 30 | **42** | 99.991 | 99 |
| **Round Robin (Q=10)** | 511.18 | 836 | 521.68 | 854 | 3 | 6 | 10 | 15 | 99.986 | **149** |
| **Priority (Preemptive)** | 411.39 | 836 | 421.89 | 854 | 4 | 8 | 15 | 19 | 99.991 | 100 |
| **Priority (Non-Preemptive)** | 409.63 | 836 | 420.13 | 854 | 5 | 9 | 15 | 19 | 99.991 | 99 |

### Yorum

Case 2 sonuçları Case 1 ile tutarlıdır. **SJF tabanlı algoritmalar** (özellikle SRTF) en düşük ortalama bekleme ve tamamlanma sürelerini sunarak en iyi performansı göstermiştir. **Round Robin** algoritması, düşük kuantum değeri nedeniyle ortaya çıkan yüksek bağlam değiştirme maliyeti yüzünden daha düşük throughput ve daha yüksek bekleme süreleri üretmiştir.

---

## 🌐 Etkileşimli Web Uygulaması

Proje, **Streamlit** kullanılarak etkileşimli bir web uygulaması şeklinde geliştirilmiştir. Kullanıcılar bu arayüz üzerinden:

* Case 1 / Case 2 seçimi yapabilir.
* 6 algoritmayı eş zamanlı çalıştırabilir.
* Karşılaştırma tablolarını inceleyebilir.
* Algoritma bazlı zaman çizelgelerini (Gantt) ve süreç metriklerini görüntüleyebilir.

Uygulama, çoklu iş parçacığı (`ThreadPoolExecutor`) kullanarak simülasyonları eş zamanlı çalıştırmaktadır.

### Çalıştırmak için

Komut satırı / Terminal = `streamlit run cpu_scheduler.py`

## ✅ Genel Sonuç

Simülasyon sonuçları, **SJF tabanlı algoritmaların** ortalama bekleme ve tamamlanma süreleri açısından en verimli yöntemler olduğunu net bir şekilde göstermiştir.

* **FCFS** basit yapısına rağmen uzun işlerin sistem performansını olumsuz etkileyebildiği (Convoy Effect) gözlemlenmiştir.
* **Round Robin** algoritması adil ve etkileşimli sistemler için uygun olsa da, **bağlam değiştirme maliyeti** nedeniyle toplam sistem performansını düşürmektedir.
* Tüm algoritmalarda CPU verimliliğinin %99’un üzerinde olması, sistemin yoğun iş yükü altında etkin çalıştığını göstermektedir.

---

## 📚 Kaynakça

1.  Silberschatz, A., Galvin, P. B., Gagne, G., *Operating System Concepts*
2.  Tanenbaum, A. S., *Modern Operating Systems*
3.  Stallings, W., *Operating Systems: Internals and Design Principles*
4.  GeeksforGeeks – CPU Scheduling
5.  Wikipedia – CPU Scheduling Algorithms

