class Job:
    
    def __init__(self, weight, time):
        self.weight = weight
        self.time = time
        
    def __repr__(self):
        return repr((self.weight, self.time))


def minWeightedSum(jobs):
    minSum = 0;
    time = 0;
    # Sort jobs in descending order according to wi/ti
    jobs.sort(key=lambda job: float(job.weight)/float(job.time),reverse = True)
    for job in jobs:
        minSum += (job.weight * (job.time + time))  # Ci = wi * (ti + totalTime)
        time += job.time    # Add previous job time
    
    print("Jobs Sequence:",jobs)
    return minSum
 
j1 = Job(4,10) # wi = 4, ti = 10
j2 = Job(10,1) # wi = 10, ti = 1
j3 = Job(2,3)  # wi = 2, ti = 3

jobs = [j1,j2,j3]
print("Minimum Weighted Sum:",minWeightedSum(jobs))
