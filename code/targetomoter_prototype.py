import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


# =========================
# 1. GOAL PROGRESS SIMULATION
# =========================
def simulate_goal_progress(start_progress, daily_rate, days):
    progress = [start_progress]

    for day in range(1, days + 1):
        progress.append(progress[-1] + daily_rate)

        if progress[-1] >= 100:
            break

    return progress


# =========================
# 2. MOTIVATION SYSTEM
# =========================
def check_progress_for_motivation(current_progress, days_passed, total_days):
    halfway_point = total_days / 2

    if days_passed >= halfway_point and current_progress < 50:
        return "Keep going! You're halfway through — push harder."
    elif current_progress >= 50:
        return "Great job! You're more than halfway there."
    else:
        return "You're on track. Keep it steady."


# =========================
# 3. VISUALISATION
# =========================
def plot_progress(progress):
    plt.figure(figsize=(10, 5))
    plt.plot(progress, label="Progress (%)")
    plt.axhline(100, linestyle='--', label="Goal Achieved")
    plt.title("Simulated Goal Progress")
    plt.xlabel("Days")
    plt.ylabel("Progress (%)")
    plt.legend()
    plt.show()


def generate_sample_progress_data():
    data = {
        'Day': range(1, 31),
        'Progress': np.random.randint(0, 5, 30).cumsum()
    }

    df = pd.DataFrame(data)

    plt.figure(figsize=(10, 5))
    plt.plot(df['Day'], df['Progress'], label="Cumulative Progress")
    plt.xlabel("Day")
    plt.ylabel("Progress (%)")
    plt.title("User Goal Completion Trend")
    plt.legend()
    plt.show()


# =========================
# 4. MOCK BACKEND LOGIC
# =========================
def log_check_in(user_id):
    return {
        "user_id": user_id,
        "check_in_time": datetime.now()
    }


def log_goal_progress(current_progress, increment):
    new_progress = current_progress + increment

    status = "Complete" if new_progress >= 100 else "In Progress"

    return {
        "progress": new_progress,
        "status": status
    }


def log_feedback_response(user_id, message, feedback):
    return {
        "user_id": user_id,
        "message": message,
        "feedback": feedback,
        "timestamp": datetime.now()
    }


# =========================
# 5. MAIN DEMO (RUN THIS)
# =========================
if __name__ == "__main__":
    progress = simulate_goal_progress(10, 3, 30)
    plot_progress(progress)

    message = check_progress_for_motivation(current_progress=40, days_passed=15, total_days=30)
    print("Motivation:", message)

    generate_sample_progress_data()