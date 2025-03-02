import threading
import time
import subprocess

class NvidiaSmiMonitor(threading.Thread):
    def __init__(self, interval=2):
        super().__init__()
        self.interval = interval  # 몇 초마다 실행할지
        self.running = True       # 실행 플래그

    def run(self):
        """백그라운드 스레드에서 nvidia-smi 실행"""
        while self.running:
            self.print_gpu_status()
            time.sleep(self.interval)  # interval 간격으로 실행

    def print_gpu_status(self):
        """nvidia-smi 실행 후 Colab에 출력"""
        try:
            result = subprocess.run(["nvidia-smi"], capture_output=True, text=True)
            print(result.stdout)  # 결과 출력
        except Exception as e:
            print(f"Error running nvidia-smi: {e}")

    def stop(self):
        """스레드 종료"""
        self.running = False

