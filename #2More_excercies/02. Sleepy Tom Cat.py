number_off_days = int(input())
norm_of_play_time = 30000
year_days = 365
work_m_play = 63
off_m_play = 127

working_days = year_days - number_off_days

working_play_time = working_days * work_m_play
off_play_time = number_off_days * off_m_play

total_play_time = working_play_time + off_play_time

diff = abs(norm_of_play_time - total_play_time)

total_h = diff // 60
total_m = diff % 60

if total_play_time > norm_of_play_time:
    print("Tom will run away")
    print(f"{total_h} hours and {total_m} minutes more for play")
else:
    total = abs(norm_of_play_time - total_play_time)
    minutes = total % 60
    hours = total //60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
