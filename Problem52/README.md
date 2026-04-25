# 📅 Meeting Assistant — Earliest Free Time Finder

A simple yet efficient scheduling utility that finds the **earliest available time slot** where all participants are free for a given meeting duration.

---

## 🚀 Problem Statement

Given:

* A list of events in the format:

  ```
  "<name> <action> <start_time> <end_time>"
  ```
* An integer `k` representing the **meeting duration (in minutes)**

### 🎯 Goal:

* Find the **earliest time** when all participants are free for at least `k` continuous minutes
* If no such time exists, return `-1`

---

## 🧠 Example

### Input:

```bash
events = [
  "sam sleep 12:00 18:59",
  "alex gaming 00:00 11:00"
]
k = 60
```

### Output:

```bash
19:00
```

---

## ⚙️ Approach

1. Convert time from `HH:MM` format to **minutes**
2. Create a timeline array of size `1440` (total minutes in a day)
3. Mark all **busy time slots**
4. Scan the timeline to find **k consecutive free minutes**
5. Convert result back to `HH:MM` format

---

## 💻 Implementation (Python)

```python
def getEarliestMeetTime(events, k):
    def to_minutes(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    busy = [0] * 1440

    # Mark busy times
    for event in events:
        parts = event.split()
        start = to_minutes(parts[2])
        end = to_minutes(parts[3])

        for t in range(start, end + 1):
            busy[t] = 1

    free_count = 0

    # Find earliest free slot
    for i in range(1440):
        if busy[i] == 0:
            free_count += 1
            if free_count == k:
                start = i - k + 1
                h = start // 60
                m = start % 60
                return f"{h:02d}:{m:02d}"
        else:
            free_count = 0

    return "-1"
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(1440 + n)`
* **Space Complexity:** `O(1440)`

---

## 📌 Key Highlights

* Efficient **timeline-based interval marking**
* Uses **sliding window technique** to detect free slots
* Handles **overlapping schedules seamlessly**
* Works within fixed daily bounds (24 hours)

---

## 🧩 Edge Cases Considered

* Fully occupied day → returns `-1`
* Multiple overlapping events
* Free slot at start or end of the day
* Minimum duration (`k = 1`)

---

## 🔮 Future Improvements

* Support multi-day scheduling
* Optimize using interval merging (instead of full timeline)
* Add user-specific availability tracking
* Build a UI or API for real-world use

---

## 👨‍💻 Author

**Kishor Kakde Patil**
Electronics & Communication Engineering
AI | ML | Cloud Enthusiast 🚀

---

## ⭐ Support

If you found this useful, consider giving it a ⭐ on GitHub!

---
