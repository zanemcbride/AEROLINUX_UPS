f= open("UPS_SHUTDOWN_THRESHOLD.txt", "r")
threshold=int((f.readline()))
num_two=70
ans=threshold-50
print(ans)