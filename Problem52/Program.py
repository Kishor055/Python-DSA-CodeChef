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
