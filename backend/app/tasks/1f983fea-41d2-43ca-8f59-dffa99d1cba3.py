import time,random,sys

def task(task_id: str, uri: str):
        sys.stdout.write("input -> "+uri)   # inputs to fake task in this S3 bucket
        duration = random.randint(1,10)
        time.sleep(duration)          # Simulate long task
        sys.stdout.write(", processed in "+str(duration)+"s, ") 
        sys.stdout.write("output -> "+uri)   # results of fake task in this S3 bucket

if __name__ == "__main__":
    task(sys.argv[1],sys.argv[2])