import time
import os

def digital_clock():
    print("--- My Python Digital Clock ---")
    try:
        while True:
            # Clear screen (Windows ke liye 'cls', Mac/Linux ke liye 'clear')
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Current time format karna
            current_time = time.strftime("%H:%M:%S %p")
            print(f"\n Current Time: {current_time} \n")
            print("Press Ctrl+C to stop.")
            
            time.sleep(1) # Har 1 second baad update hoga
    except KeyboardInterrupt:
        print("\nClock stopped. Bye!")

if __name__ == "__main__":
    digital_clock()
