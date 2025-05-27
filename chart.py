import matplotlib.pyplot as plt
from profile_manager import get_user_profile 

def plot_user_profile(username):
    profile = get_user_profile(username)

    if not profile: 
        print("No profile found")
        return 
    
    total = profile.get("total_choices", {})
    labels= list(total.keys())
    sizes=list(total.values())


    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90 )
    plt.title(f"{username} - Most Preferred Coffees")

    history=profile.get("history",[])
    time_counts={}
    for entry in history:
        time=entry["time"]
        time_counts[time] = time_counts.get(time,0) + 1
    
    times = sorted(time_counts.keys())
    frequency = [time_counts[s] for s in times]

    plt.subplot(1,2,2)
    plt.bar(times,frequency, color='sienna')
    plt.xlabel("Hour")
    plt.ylabel("Coffee Count")
    plt.title(f"{username} - Coffee Time Trends")

    plt.tight_layout()
    plt.show()





