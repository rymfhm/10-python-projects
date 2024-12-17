import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time is up")

def main():
    print("Countdown Timer")
    try:
        total_time = int(input("Enter the countdown time in seconds: "))
        if total_time > 0:
            countdown_timer(total_time)
        else:
            print("Please enter a positive number for time.")
    except ValueError:
        print("Invalid input. Please enter an integer value for time.")

if __name__ == "__main__":
    main()