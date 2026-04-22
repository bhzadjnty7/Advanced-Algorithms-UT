def min_completion_time_greedy(jobs, k):
    # Sort jobs in descending order
    jobs.sort(reverse=True)
    
    # Create workload array for each worker
    workload = [0] * k
    
    # Assign each job to the worker with the smallest load
    for job in jobs:
        # Find the worker with the smallest load
        min_worker_idx = workload.index(min(workload))
        # Assign the job to the worker
        workload[min_worker_idx] += job
    
    # Total time is the maximum workload among workers
    return max(workload)

jobs = [8, 2, 6, 3, 4, 5]
k = 3
print(min_completion_time_greedy(jobs, k))