hours_exam = int(input())
minutes_exam = int(input())
hours_arrival = int(input())
minutes_arrival = int(input())

m_exam = hours_exam * 60 + minutes_exam
m_arrival = hours_arrival * 60 + minutes_arrival

diff = abs(m_arrival - m_exam)
hour = diff // 60
minutes = diff % 60

if minutes_arrival == m_exam:
    print("On time")
elif m_exam > m_arrival:
    if diff <= 30:
        print("On time")
        print(f"{diff:02d} minutes before the start")
    elif 30 < diff <= 59:
        print("Early")
        print(f"{diff} minutes before the start")
    else:
        print("Early")
        print(f"{hour}:{minutes:02d} hours before the start")
else:
    print("Late")
    if diff < 60:
        print(f"{diff:02d} minutes after the start")
    else:
        print(f"{hour}:{minutes:02d} hours after the start")




