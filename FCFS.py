bt=[]
print("Enter the number of process: ")
n=int(input())
print("Enter the burst time of the processes: \n")
bt=list(map(int, input().split()))

at = [int(x) for x in range(n)]
wt=[]
avgwt=0
tat=[]
avgtat=0
tat_2 = []


wt.insert(0,0)
tat.insert(0,bt[0])
tat_2.insert(0,tat[0])

bt_1 = []
for i in range(1,len(bt)):
   #bt_1.insert(bt[i])
   #wt.insert(i,wt[i-1]+bt[i-1])
   tat.insert(i,tat[i-1]+bt[i])
   #tat_2.insert(i,tat[i-1]-at[i])
   #avgwt+=wt[i]
   avgtat+=tat[i]

for j in range(1,len(at)):
    tat_2.insert(i,tat[j]-at[j])
    wt.insert(i,tat_2[j]-bt[j])
    avgwt+=wt[j]

print(tat_2)
avgwt=float(avgwt)/n
avgtat=float(avgtat)/n
print("\n")
print("Process\t  Arrival Time\t Burst Time\t  Completion Time\t Turn Around Time\t Waiting Time\t ")

for i in range(0,n):
   print(str(i)+"\t\t"+str(at[i])+"\t\t"+str(bt[i])+"\t\t"+str(tat[i])+"\t\t\t"+str(tat_2[i])+"\t\t\t"+str(wt[i]))
   print("\n")

print("Average Waiting time is: "+str(avgwt))
print("Average Turn Arount Time is: "+str(avgtat))