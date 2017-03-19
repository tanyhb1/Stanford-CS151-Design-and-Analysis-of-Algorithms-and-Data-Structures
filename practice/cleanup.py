def main():
    number_testcases = int(input())
    j = 0

    while(j < number_testcases):
        jobs_remaining_array = []
        chef_jobs = []
        assistant_jobs = []
        jobs_total, jobs_completed = input().split()
        jobs_completed_indices = input().split()
        
        jobs_completed_indices = list(map(int,jobs_completed_indices))
        jobs_total = int(jobs_total)
        jobs_completed = int(jobs_completed)      
        
        for i in range(jobs_total):
            x = i + 1
            if not x in jobs_completed_indices:
                jobs_remaining_array.append(x)   
        for i in range(len(jobs_remaining_array)):
            if i%2 == 0:
                chef_jobs.append(jobs_remaining_array[i])
            else:
                assistant_jobs.append(jobs_remaining_array[i])
        
        for i in range(len(chef_jobs)):
            if i == len(chef_jobs)-1:
                print(chef_jobs[i])
            else:
                print(chef_jobs[i], end=' ')
        for i in range(len(assistant_jobs)):
            if i == len(assistant_jobs)-1:
                print(assistant_jobs[i])
            else:
                print(assistant_jobs[i], end=' ')
        j = j + 1

if __name__ == "__main__":
    main()