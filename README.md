# CPU Zamanlama Algoritmaları Simülasyonu

**Yazar:** Deniz Ekiz  
**Öğrenci No:** 20232013036  
**Dosya:** `cpu_scheduler.py`  

Bu proje, işletim sistemlerinde kullanılan **CPU zamanlama algoritmalarını** karşılaştırmalı olarak simüle etmek amacıyla geliştirilmiştir.  
Uygulama, **Streamlit** tabanlı bir web arayüzü üzerinden çalışır ve tüm algoritmaları **eş zamanlı (multithreading)** olarak simüle eder.

---

##  Amaç

- CPU zamanlama algoritmalarının performanslarını karşılaştırmak  
- Bekleme süresi, tamamlanma süresi, verimlilik ve throughput gibi metrikleri analiz etmek  
- Farklı iş yükleri (100 ve 200 süreç) altında algoritmaların davranışını gözlemlemek  

---

##  Kullanılan Teknolojiler

- **Python 3**
- **Streamlit**
- **Pandas**
- **Concurrent Futures (ThreadPoolExecutor)**

---

##  Simüle Edilen Zamanlama Algoritmaları

Toplam **6 farklı CPU zamanlama algoritması** uygulanmıştır:

1. **FCFS (First Come First Served)**
2. **SRTF (Preemptive Shortest Job First)**
3. **Non-Preemptive SJF**
4. **Round Robin (Quantum = 10)**
5. **Preemptive Priority Scheduling**
6. **Non-Preemptive Priority Scheduling**

---

##  Kullanılan Veri Setleri

### Case 1
- **200 süreç**
- Artan arrival time
- Burst time: 1 – 20
- Öncelik: high / normal / low

### Case 2
- **100 süreç**
- Değişken burst süreleri
- Karışık öncelik dağılımı

Veri setleri **kod içine gömülü (embedded)** olarak tanımlanmıştır.

---

##  Simülasyon Varsayımları

| Parametre | Değer |
|---------|------|
| Round Robin Quantum | `10` |
| Context Switch Overhead | `0.001` |
| Öncelik Haritası | high = 1, normal = 2, low = 3 |

---

##  Hesaplanan Performans Metrikleri

Her algoritma için aşağıdaki metrikler hesaplanır:

- Ortalama Bekleme Süresi
- Maksimum Bekleme Süresi
- Ortalama Tamamlanma (Turnaround) Süresi
- Maksimum Tamamlanma Süresi
- CPU Verimliliği (Efficiency)
- Bağlam Değişimi (Context Switch) Sayısı
- Throughput (T = 50, 100, 150, 200)
- Süreç bazlı detaylı metrik tablosu
- Zaman çizelgesi (Gantt benzeri)

---

##  Uygulama Arayüzü

Streamlit arayüzü şu özellikleri sunar:

- Veri seti seçimi (Case 1 / Case 2)
- Tüm algoritmaların **eş zamanlı çalıştırılması**
- Karşılaştırmalı sonuç tablosu
- Seçilen algoritma için:
  - Zaman çizelgesi
  - Throughput tablosu
  - Süreç bazlı detaylı metrikler

---

##  Çalıştırma Talimatları

### 1️.Gerekli Kütüphaneleri Kurun

```bash
pip install streamlit pandas
```

---

### 2. Uygulamayı Başlatın

```bash
streamlit run cpu_scheduler.py
```

---

### 3️.Tarayıcıdan Görüntüleyin

```text
http://localhost:8501
```
## 🔄 Eş Zamanlı Çalışma Yapısı

- Tüm CPU zamanlama algoritmaları **ThreadPoolExecutor** kullanılarak paralel (eş zamanlı) şekilde çalıştırılır.
- Bu yaklaşım, Streamlit ortamı için **kararlı ve güvenli** bir çalışma yapısı sağlar.
- Her algoritma için süreç listesi `deepcopy` kullanılarak **tamamen izole edilir**.
- Böylece algoritmalar birbirlerinin sonuçlarını etkilemeden bağımsız olarak simüle edilir.

---

## 📌 Notlar

- **IDLE** (boşta kalma) süreleri zaman çizelgesinde gösterilmez.
- **Context switch (bağlam değiştirme) süresi**, toplam simülasyon süresi hesabına dahil edilir.
- Simülasyon sonuçları **akademik analiz ve eğitim amaçlıdır**.

