# Dosya Adı:cpu_scheduler.py
# Yazar: DENİZ EKİZ - 20232013036
# Amac: CPU Zamanlama Algoritmalarinin Simülasyonu

import streamlit as st
import pandas as pd
import copy
from collections import deque
import concurrent.futures 

# SABİT DEĞİŞKENLER VE SÜREÇ SINIFI 

PRIORITY_MAP = {'high': 1, 'normal': 2, 'low': 3}
RR_QUANTUM = 10 
CONTEXT_SWITCH_OVERHEAD = 0.001

class Process:
    def __init__(self, pid, arrival, burst, priority):
        self.pid = pid
        self.arrival = int(arrival)
        self.burst = int(burst)
        self.remaining_time = int(burst)
        self.priority_str = priority.strip().lower()
        self.priority = PRIORITY_MAP.get(self.priority_str, 2)
        
        self.start_time = -1
        self.finish_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        
    def __repr__(self):
        return f"{self.pid}"

# GÖMÜLÜ VERİ SETLERİ

# Case 1 Verisi (200 Süreç)
CASE1_DATA = """Process_ID,Arrival_Time,CPU_Burst_Time,Priority
P001,0,1,high
P002,2,2,normal
P003,4,3,low
P004,6,4,high
P005,8,5,normal
P006,10,6,low
P007,12,7,high
P008,14,8,normal
P009,16,9,low
P010,18,10,high
P011,20,11,normal
P012,22,12,low
P013,24,13,high
P014,26,14,normal
P015,28,15,low
P016,30,16,high
P017,32,17,normal
P018,34,18,low
P019,36,19,high
P020,38,20,normal
P021,40,1,low
P022,42,2,high
P023,44,3,normal
P024,46,4,low
P025,48,5,high
P026,50,6,normal
P027,52,7,low
P028,54,8,high
P029,56,9,normal
P030,58,10,low
P031,60,11,high
P032,62,12,normal
P033,64,13,low
P034,66,14,high
P035,68,15,normal
P036,70,16,low
P037,72,17,high
P038,74,18,normal
P039,76,19,low
P040,78,20,high
P041,80,1,normal
P042,82,2,low
P043,84,3,high
P044,86,4,normal
P045,88,5,low
P046,90,6,high
P047,92,7,normal
P048,94,8,low
P049,96,9,high
P050,98,10,normal
P051,100,11,low
P052,102,12,high
P053,104,13,normal
P054,106,14,low
P055,108,15,high
P056,110,16,normal
P057,112,17,low
P058,114,18,high
P059,116,19,normal
P060,118,20,low
P061,120,1,high
P062,122,2,normal
P063,124,3,low
P064,126,4,high
P065,128,5,normal
P066,130,6,low
P067,132,7,high
P068,134,8,normal
P069,136,9,low
P070,138,10,high
P071,140,11,normal
P072,142,12,low
P073,144,13,high
P074,146,14,normal
P075,148,15,low
P076,150,16,high
P077,152,17,normal
P078,154,18,low
P079,156,19,high
P080,158,20,normal
P081,160,1,low
P082,162,2,high
P083,164,3,normal
P084,166,4,low
P085,168,5,high
P086,170,6,normal
P087,172,7,low
P088,174,8,high
P089,176,9,normal
P090,178,10,low
P091,180,11,high
P092,182,12,normal
P093,184,13,low
P094,186,14,high
P095,188,15,normal
P096,190,16,low
P097,192,17,high
P098,194,18,normal
P099,196,19,low
P100,198,20,high
P101,200,1,normal
P102,202,2,low
P103,204,3,high
P104,206,4,normal
P105,208,5,low
P106,210,6,high
P107,212,7,normal
P108,214,8,low
P109,216,9,high
P110,218,10,normal
P111,220,11,low
P112,222,12,high
P113,224,13,normal
P114,226,14,low
P115,228,15,high
P116,230,16,normal
P117,232,17,low
P118,234,18,high
P119,236,19,normal
P120,238,20,low
P121,240,1,high
P122,242,2,normal
P123,244,3,low
P124,246,4,high
P125,248,5,normal
P126,250,6,low
P127,252,7,high
P128,254,8,normal
P129,256,9,low
P130,258,10,high
P131,260,11,normal
P132,262,12,low
P133,264,13,high
P134,266,14,normal
P135,268,15,low
P136,270,16,high
P137,272,17,normal
P138,274,18,low
P139,276,19,high
P140,278,20,normal
P141,280,1,low
P142,282,2,high
P143,284,3,normal
P144,286,4,low
P145,288,5,high
P146,290,6,normal
P147,292,7,low
P148,294,8,high
P149,296,9,normal
P150,298,10,low
P151,300,11,high
P152,302,12,normal
P153,304,13,low
P154,306,14,high
P155,308,15,normal
P156,310,16,low
P157,312,17,high
P158,314,18,normal
P159,316,19,low
P160,318,20,high
P161,320,1,normal
P162,322,2,low
P163,324,3,high
P164,326,4,normal
P165,328,5,low
P166,330,6,high
P167,332,7,normal
P168,334,8,low
P169,336,9,high
P170,338,10,normal
P171,340,11,low
P172,342,12,high
P173,344,13,normal
P174,346,14,low
P175,348,15,high
P176,350,16,normal
P177,352,17,low
P178,354,18,high
P179,356,19,normal
P180,358,20,low
P181,360,1,high
P182,362,2,normal
P183,364,3,low
P184,366,4,high
P185,368,5,normal
P186,370,6,low
P187,372,7,high
P188,374,8,normal
P189,376,9,low
P190,378,10,high
P191,380,11,normal
P192,382,12,low
P193,384,13,high
P194,386,14,normal
P195,388,15,low
P196,390,16,high
P197,392,17,normal
P198,394,18,low
P199,396,19,high
P200,398,20,normal
"""

# Case 2 Verisi (100 Süreç)
CASE2_DATA = """Process_ID,Arrival_Time,CPU_Burst_Time,Priority
P001,0,4,high
P002,2,7,normal
P003,4,10,low
P004,6,13,high
P005,8,16,normal
P006,10,19,low
P007,12,2,high
P008,14,5,normal
P009,16,8,low
P010,18,11,high
P011,20,14,normal
P012,22,17,low
P013,24,20,high
P014,26,3,normal
P015,28,6,low
P016,30,9,high
P017,32,12,normal
P018,34,15,low
P019,36,18,high
P020,38,1,normal
P021,40,4,low
P022,42,7,high
P023,44,10,normal
P024,46,13,low
P025,48,16,high
P026,50,19,normal
P027,52,2,low
P028,54,5,high
P029,56,8,normal
P030,58,11,low
P031,60,14,high
P032,62,17,normal
P033,64,20,low
P034,66,3,high
P035,68,6,normal
P036,70,9,low
P037,72,12,high
P038,74,15,normal
P039,76,18,low
P040,78,1,high
P041,80,4,normal
P042,82,7,low
P043,84,10,high
P044,86,13,normal
P045,88,16,low
P046,90,19,high
P047,92,2,normal
P048,94,5,low
P049,96,8,high
P050,98,11,normal
P051,100,14,low
P052,102,17,high
P053,104,20,normal
P054,106,3,low
P055,108,6,high
P056,110,9,normal
P057,112,12,low
P058,114,15,high
P059,116,18,normal
P060,118,1,low
P061,120,4,high
P062,122,7,normal
P063,124,10,low
P064,126,13,high
P065,128,16,normal
P066,130,19,low
P067,132,2,high
P068,134,5,normal
P069,136,8,low
P070,138,11,high
P071,140,14,normal
P072,142,17,low
P073,144,20,high
P074,146,3,normal
P075,148,6,low
P076,150,9,high
P077,152,12,normal
P078,154,15,low
P079,156,18,high
P080,158,1,normal
P081,160,4,low
P082,162,7,high
P083,164,10,normal
P084,166,13,low
P085,168,16,high
P086,170,19,normal
P087,172,2,low
P088,174,5,high
P089,176,8,normal
P090,178,11,low
P091,180,14,high
P092,182,17,normal
P093,184,20,low
P094,186,3,high
P095,188,6,normal
P096,190,9,low
P097,192,12,high
P098,194,15,normal
P099,196,18,low
P100,198,1,high
"""

# VERİ YÜKLEME VE METRİK HESAPLAMA FONKSİYONLARI

def load_processes_from_string(data_string):
    processes = []
    lines = data_string.strip().split('\n')
    start_index = 1 if lines and lines[0].startswith("Process_ID") else 0
    
    for line in lines[start_index:]:
        parts = line.strip().split(',')
        if len(parts) >= 4:
            try:
                p = Process(parts[0], parts[1], parts[2], parts[3])
                processes.append(p)
            except ValueError:
                continue
    return processes

def calculate_metrics(completed_processes, timeline, context_switches):
    if not completed_processes:
        return None
        
    total_burst = sum(p.burst for p in completed_processes)
    last_finish_time = max(p.finish_time for p in completed_processes) if completed_processes else 0
    total_time = last_finish_time + (context_switches * CONTEXT_SWITCH_OVERHEAD)

    max_wait = max(p.waiting_time for p in completed_processes)
    avg_wait = sum(p.waiting_time for p in completed_processes) / len(completed_processes)
    max_turnaround = max(p.turnaround_time for p in completed_processes)
    avg_turnaround = sum(p.turnaround_time for p in completed_processes) / len(completed_processes)
    
    throughputs = {}
    time_points = [50, 100, 150, 200]
    for t in time_points:
        count = sum(1 for p in completed_processes if p.finish_time <= t)
        throughputs[t] = count

    efficiency = total_burst / total_time if total_time > 0 else 0
    
    timeline_df = pd.DataFrame(timeline, columns=['Başlangıç', 'Bitiş', 'Süreç ID'])
    timeline_df = timeline_df[timeline_df['Süreç ID'] != 'IDLE'] 
    
    proc_data = {
        'ID': [p.pid for p in completed_processes],
        'Varış': [p.arrival for p in completed_processes],
        'Burst': [p.burst for p in completed_processes],
        'Bitiş Zamanı': [p.finish_time for p in completed_processes],
        'Bekleme Süresi': [p.waiting_time for p in completed_processes],
        'Tamamlanma Süresi': [p.turnaround_time for p in completed_processes],
    }
    metrics_df = pd.DataFrame(proc_data).set_index('ID')

    return {
        'avg_wait': avg_wait, 'max_wait': max_wait,
        'avg_turnaround': avg_turnaround, 'max_turnaround': max_turnaround,
        'throughputs': throughputs,
        'efficiency': efficiency,
        'context_switches': context_switches,
        'timeline_df': timeline_df,
        'metrics_df': metrics_df
    }

# ZAMANLAMA ALGORİTMALARI

def solve_fcfs(processes):
    procs = sorted(processes, key=lambda x: x.arrival)
    current_time = 0
    timeline = []
    context_switches = 0
    last_pid = None
    for p in procs:
        if current_time < p.arrival:
            timeline.append((current_time, p.arrival, "IDLE"))
            current_time = p.arrival
        if last_pid != p.pid and last_pid is not None and current_time > 0:
            context_switches += 1
        start = current_time
        current_time += p.burst
        p.finish_time = current_time
        p.turnaround_time = p.finish_time - p.arrival
        p.waiting_time = p.turnaround_time - p.burst
        timeline.append((start, current_time, p.pid))
        last_pid = p.pid
    return calculate_metrics(procs, timeline, context_switches)

def solve_sjf_non_preemptive(processes):
    pending = sorted(processes, key=lambda x: x.arrival, reverse=True)
    ready_queue = []
    completed = []
    current_time = 0
    timeline = []
    context_switches = 0
    last_pid = None
    while pending or ready_queue:
        while pending and pending[-1].arrival <= current_time:
            ready_queue.append(pending.pop())
        if not ready_queue:
            if pending:
                next_arrival = pending[-1].arrival
                timeline.append((current_time, next_arrival, "IDLE"))
                current_time = next_arrival
            continue
        ready_queue.sort(key=lambda x: x.burst)
        p = ready_queue.pop(0)
        if last_pid != p.pid and last_pid is not None:
            context_switches += 1
        start = current_time
        current_time += p.burst
        p.finish_time = current_time
        p.turnaround_time = p.finish_time - p.arrival
        p.waiting_time = p.turnaround_time - p.burst
        timeline.append((start, current_time, p.pid))
        completed.append(p)
        last_pid = p.pid
    return calculate_metrics(completed, timeline, context_switches)

def solve_priority_non_preemptive(processes):
    pending = sorted(processes, key=lambda x: x.arrival, reverse=True)
    ready_queue = []
    completed = []
    current_time = 0
    timeline = []
    context_switches = 0
    last_pid = None
    while pending or ready_queue:
        while pending and pending[-1].arrival <= current_time:
            ready_queue.append(pending.pop())
        if not ready_queue:
            if pending:
                next_arrival = pending[-1].arrival
                timeline.append((current_time, next_arrival, "IDLE"))
                current_time = next_arrival
            continue
        ready_queue.sort(key=lambda x: x.priority)
        p = ready_queue.pop(0)
        if last_pid != p.pid and last_pid is not None:
            context_switches += 1
        start = current_time
        current_time += p.burst
        p.finish_time = current_time
        p.turnaround_time = p.finish_time - p.arrival
        p.waiting_time = p.turnaround_time - p.burst
        timeline.append((start, current_time, p.pid))
        completed.append(p)
        last_pid = p.pid
    return calculate_metrics(completed, timeline, context_switches)

def solve_preemptive_generic(processes, algo_type):
    procs = processes
    n = len(procs)
    completed = []
    current_time = 0
    timeline = []
    context_switches = 0
    last_pid = None
    while len(completed) < n:
        available = [p for p in procs if p.arrival <= current_time and p.remaining_time > 0]
        if not available:
            future_procs = [p for p in procs if p.arrival > current_time]
            if future_procs:
                next_arr = min(p.arrival for p in future_procs)
                if timeline and timeline[-1][2] == "IDLE":
                    prev_start, _, _ = timeline.pop()
                    timeline.append((prev_start, next_arr, "IDLE"))
                else:
                    timeline.append((current_time, next_arr, "IDLE"))
                current_time = next_arr
                continue
            else:
                break
        if algo_type == 'sjf':
            best_proc = min(available, key=lambda x: x.remaining_time)
        else: 
            best_proc = min(available, key=lambda x: x.priority)
            
        if last_pid != best_proc.pid and last_pid is not None:
            context_switches += 1
            
        best_proc.remaining_time -= 1
        if timeline and timeline[-1][2] == best_proc.pid and timeline[-1][1] == current_time:
            start, _, pid = timeline.pop()
            timeline.append((start, current_time + 1, pid))
        else:
            timeline.append((current_time, current_time + 1, best_proc.pid))
            
        current_time += 1
        last_pid = best_proc.pid
        
        if best_proc.remaining_time == 0:
            best_proc.finish_time = current_time
            best_proc.turnaround_time = best_proc.finish_time - best_proc.arrival
            best_proc.waiting_time = best_proc.turnaround_time - best_proc.burst
            completed.append(best_proc)
    return calculate_metrics(completed, timeline, context_switches)

def solve_round_robin(processes):
    procs_sorted = sorted(processes, key=lambda x: x.arrival)
    n = len(procs_sorted)
    queue = deque()
    current_time = 0
    timeline = []
    completed = []
    context_switches = 0
    last_pid = None
    idx = 0
    
    if procs_sorted and procs_sorted[0].arrival > 0:
        timeline.append((0, procs_sorted[0].arrival, "IDLE"))
        current_time = procs_sorted[0].arrival
        
    while idx < n and procs_sorted[idx].arrival <= current_time:
        queue.append(procs_sorted[idx])
        idx += 1
        
    while queue or idx < n:
        if not queue:
            if idx < n:
                next_proc = procs_sorted[idx]
                timeline.append((current_time, next_proc.arrival, "IDLE"))
                current_time = next_proc.arrival
                while idx < n and procs_sorted[idx].arrival <= current_time:
                    queue.append(procs_sorted[idx])
                    idx += 1
            else:
                break
        
        current_proc = queue.popleft()
        if last_pid != current_proc.pid and last_pid is not None:
            context_switches += 1
            
        run_time = min(current_proc.remaining_time, RR_QUANTUM)
        start_run = current_time
        current_time += run_time
        
        if timeline and timeline[-1][2] == current_proc.pid and timeline[-1][1] == start_run:
            start_prev, _, pid_prev = timeline.pop()
            timeline.append((start_prev, current_time, pid_prev))
        else:
            timeline.append((start_run, current_time, current_proc.pid))
        
        current_proc.remaining_time -= run_time
        last_pid = current_proc.pid
        
        while idx < n and procs_sorted[idx].arrival <= current_time:
            queue.append(procs_sorted[idx])
            idx += 1
            
        if current_proc.remaining_time > 0:
            queue.append(current_proc)
        else:
            current_proc.finish_time = current_time
            current_proc.turnaround_time = current_proc.finish_time - current_proc.arrival
            current_proc.waiting_time = current_proc.turnaround_time - current_proc.burst
            completed.append(current_proc)
            
    return calculate_metrics(completed, timeline, context_switches)

# SARMLAYICI FONKSİYONLAR

def solve_srtf(processes):
    return solve_preemptive_generic(processes, 'sjf')

def solve_preemptive_priority(processes):
    return solve_preemptive_generic(processes, 'priority')

# TÜM ALGORİTMALARIN HARİTALANMASI

ALGO_FUNCTIONS = {
    "FCFS": solve_fcfs,
    "SRTF (Preemptive SJF)": solve_srtf, 
    "Non-Preemptive SJF": solve_sjf_non_preemptive,
    "Round Robin (Q=10)": solve_round_robin,
    "Preemptive Priority": solve_preemptive_priority,
    "Non-Preemptive Priority": solve_priority_non_preemptive,
}

# EŞ ZAMANLI ÇALIŞTIRMA FONKSİYONU (ThreadPoolExecutor ile kararlı)

@st.cache_data
def run_all_algorithms_concurrently(data_string):
    """Veri setini yükler ve tüm algoritmaları eş zamanlı (multithreading) çalıştırır."""
    processes = load_processes_from_string(data_string)
    if not processes:
        return None, None

    results = {}
    
    # ProcessPoolExecutor yerine ThreadPoolExecutor kullanılır.
    # Streamlit ortamında kararlılığı artırır.
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {}
        for algo_name, func in ALGO_FUNCTIONS.items():
            futures[executor.submit(func, copy.deepcopy(processes))] = algo_name
        
        for future in concurrent.futures.as_completed(futures):
            algo_name = futures[future]
            try:
                result = future.result()
                results[algo_name] = result
            except Exception as exc:
                # ThreadPoolExecutor hataları ProcessPool'dan farklıdır
                st.error(f'"{algo_name}" simülasyonu bir hata üretti: {type(exc).__name__}: {exc}')
                results[algo_name] = None
                
    return results, processes 

# WEB ARAYÜZÜ (STREAMLIT)

def run_streamlit_app():
    st.set_page_config(layout="wide")
    st.title("CPU Zamanlama Algoritmaları Karşılaştırmalı Simülasyonu")
    st.markdown("Tüm 6 algoritma, iş yükünü eş zamanlı (multithreading) olarak çalıştırarak karşılaştırılır.")
    
    data_sources = {
        "Case 1 (200 Süreç)": CASE1_DATA,
        "Case 2 (100 Süreç)": CASE2_DATA
    }

    # Yan menü
    st.sidebar.header("Seçim Paneli")
    selected_case_name = st.sidebar.selectbox(
        "1. Veri Durumunu Seçin:",
        list(data_sources.keys())
    )

    st.sidebar.markdown("---")
    st.sidebar.subheader("Simülasyon Ayarları")
    st.sidebar.markdown(f"**Round Robin Quantum:** {RR_QUANTUM}")
    st.sidebar.markdown(f"**Bağlam Değiştirme Süresi:** {CONTEXT_SWITCH_OVERHEAD}")

    # Ana simülasyon ve gösterim
    if selected_case_name:
        
        data_string = data_sources[selected_case_name]
        
        st.info(f"**{selected_case_name}** için {len(ALGO_FUNCTIONS)} algoritma simülasyonu eş zamanlı olarak başlatılıyor...")
        
        results, original_processes = run_all_algorithms_concurrently(data_string)

        if not results or all(r is None for r in results.values()):
            st.error("Simülasyon tamamlanamadı veya süreçler boş. Lütfen konsol çıktısını kontrol edin.")
        else:
            st.success("✅ Tüm Simülasyonlar Eş Zamanlı Olarak Tamamlandı!")
            
            # Karşılaştırma Dataframe'ini oluştur
            comparison_data = []
            for algo_name, res in results.items():
                if res:
                    comparison_data.append({
                        "Algoritma": algo_name,
                        "Ort. Bekleme Süresi": f"{res['avg_wait']:.4f}",
                        "Ort. Tamamlanma Süresi": f"{res['avg_turnaround']:.4f}",
                        "Maks. Bekleme Süresi": f"{res['max_wait']}",
                        "Maks. Tamamlanma Süresi": f"{res['max_turnaround']}",
                        "Verimlilik (Efficiency)": f"{res['efficiency']:.6f}",
                        "Bağlam Değişimi Sayısı": f"{res['context_switches']}",
                        "Throughput (T=200)": f"{res['throughputs'][200]}",
                    })

            comparison_df = pd.DataFrame(comparison_data)

            st.header(f"📊 {selected_case_name} - Algoritma Karşılaştırması")
            
            comparison_df['Ort. Tamamlanma Süresi Sayı'] = comparison_df['Ort. Tamamlanma Süresi'].astype(float)
            comparison_df = comparison_df.sort_values(by='Ort. Tamamlanma Süresi Sayı').drop(columns=['Ort. Tamamlanma Süresi Sayı']).set_index('Algoritma')
            st.dataframe(comparison_df)

            st.markdown("---")
            
            # Detaylı Süreç ve Zaman Çizelgesi Gösterimi
            st.header("🔍 Detaylı Analiz")
            
            valid_algos = [name for name, res in results.items() if res is not None]

            if valid_algos:
                detail_algo_name = st.selectbox(
                    "Detaylarını görmek istediğiniz Algoritmayı seçin:",
                    valid_algos
                )
            
                detail_res = results[detail_algo_name]
                    
                col_tl, col_tp = st.columns([3, 1])

                with col_tl:
                    st.subheader(f" {detail_algo_name} Zaman Çizelgesi")
                    st.markdown("(*IDLE* süreleri ve Bağlam Değişimi yükü gösterilmez.)")
                    st.dataframe(detail_res['timeline_df'])

                with col_tp:
                    st.subheader(f" {detail_algo_name} Throughput Detayı")
                    throughput_data = []
                    for t, count in detail_res['throughputs'].items():
                        throughput_data.append({"Zaman T": t, "İş Tamamlama Sayısı": count})
                    st.table(pd.DataFrame(throughput_data))
                
                st.subheader(f" {detail_algo_name} Süreç Bazlı Metrikler")
                st.dataframe(detail_res['metrics_df'])
            else:
                st.warning("Hiçbir simülasyon geçerli sonuç döndürmedi.")

# Streamlit'in doğru çalışması için bu çağrı, dosyanın en sonunda olmalıdır.
run_streamlit_app()