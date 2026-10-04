# daily request -> average RPS
# RPS -> request per second

daily_request = 1_000_000
seconds_per_day = 24*60*60

average_rps = daily_request / seconds_per_day

print("Average RPS: ",round(average_rps,2))

# Average RPS:  11.57
