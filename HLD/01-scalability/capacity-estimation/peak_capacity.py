# peak capacity
# supppose peak traffic is 5x average traffic

daily_request = 1_000_000
seconds_per_day = 24*60*60
average_rps = daily_request/seconds_per_day

peak_multiplier = 5

peak_rps = average_rps * peak_multiplier

print("Average RPS:", round(average_rps,2))
print("Peak RPS:", round(peak_rps,2))


# Average RPS: 11.57
# Peak RPS: 57.87