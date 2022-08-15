import random, math, time, matplotlib.pyplot as plt

# Timer object to record time
class time_recorder:
  # initialize timer objects
  def __init__(self):
    self.time_arr = {}    # dictionary to store object
    self.start = 0        # start time recorder variable
    self.end = 0          # end time recorder variable
  
  # Start timer function
  def start_timer(self):
    self.start = time.time()
  
  # Function to stop timer and store the recorded time in dictionary object
  def end_timer(self, iter_size):
    self.end = time.time()
    self.time_arr[iter_size] = self.end - self.start

# Insertion sort function
def insertion_sort(A, n):
  for i in range(1, n):
    key = A[i]
    k = i - 1
    while k >= 0 and A[k] > key:
      A[k+1] = A[k]
      k -= 1
    A[k+1] = key

# Merge sort function to recursively call merge sort and merge function for 
# sorting the given array A
def merge_sort(A, p, r):
  if p < r:
    q = math.floor((p+r)/2)
    merge_sort(A, p, q)
    merge_sort(A, q+1, r)
    merge(A, p, q, r)

# Merge function to merge first and second half sorted arrays of given array A 
def merge(A, p, q, r):
  L = A[p: q+1]
  R = A[q+1: r+1]
  L.append(math.inf)
  R.append(math.inf)
  i = 0; j = 0
  for k in range(p, r+1):
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1

# Merge sort function to recursively call merge sort and merge function for 
# sorting the given array A using insertion sort
def merge_ins_sort(A, p, r):
  if p < r:
    if (r-p+1) <= 32:
      insertion_sort(A, r-p+1)
    else:
      q = math.floor((p+r)/2)
      merge_ins_sort(A, p, q)
      merge_ins_sort(A, q+1, r)
      merge_ins(A, p, q, r)


# Merge function to merge first and second half sorted arrays of given array A 
def merge_ins(A, p, q, r):
  L = A[p: q+1]
  R = A[q+1: r+1]
  L.append(math.inf)
  R.append(math.inf)
  i = 0; j = 0
  for k in range(p, r+1):
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1


def main1():
  timerA = time_recorder()
  timerB = time_recorder()
  timerC = time_recorder()

  for j in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 50]:
    arr = []
    for i in range(j):
      arr.append(random.randint(0,20))
    print(f"\nArray size = {j}")
    if j <= 1000:
      print("Random generated array =")
      print(arr)

    arr1 = arr.copy()
    arr2 = arr.copy()
    arr3 = arr.copy()
    
    if j < 20000:
      print("Using insertion sort:")
      
      timerA.start_timer()
      insertion_sort(arr1, len(arr1))
      timerA.end_timer(j)
      if j <= 1000:
        print("Sorted array:", arr1)

    print("Using merge sort:")
    
    timerB.start_timer()
    merge_sort(arr2, 0, len(arr2)-1)
    timerB.end_timer(j)
    if j <= 1000:
      print("Sorted array:", arr2)
    
    print("Using merge - insertion sort:")
    timerC.start_timer()
    merge_ins_sort(arr3, 0, len(arr3)-1)
    timerC.end_timer(j)
    if j <= 1000:
      print("Sorted array:", arr3)
  
  print(timerA.time_arr.keys())
  print(timerA.time_arr.values())
  plt.plot(list(timerA.time_arr.keys()), list(timerA.time_arr.values()), "-b", label = "Insertion sort")

  print(timerB.time_arr.keys())
  print(timerB.time_arr.values())
  plt.plot(list(timerB.time_arr.keys()), list(timerB.time_arr.values()), "-r", label = "Merge sort")

  print(timerC.time_arr.keys())
  print(timerC.time_arr.values())
  plt.plot(list(timerC.time_arr.keys()), list(timerC.time_arr.values()), "-g", label = "Merge-Insertion sort")
  plt.legend(loc="upper left")
  plt.title("Time complexity graphs")
  plt.xlabel("Input size (n)")
  plt.ylabel("Time (ms)")

  plt.show()   

def main2():
  timerA = time_recorder()
  timerB = time_recorder()
  timerC = time_recorder()

  for j in [1, 100, 1000, 10000, 100000]:
    arr = []
    for i in range(j):
      arr.append(random.randint(0,20))
    print(f"\nArray size = {j}")
    if j <= 1000:
      print("Random generated array =")
      print(arr)

    arr1 = arr.copy()
    arr2 = arr.copy()
    arr3 = arr.copy()
    
    if j < 20000:
      print("Using insertion sort:")
      
      timerA.start_timer()
      insertion_sort(arr1, len(arr1))
      timerA.end_timer(j)
      if j <= 1000:
        print("Sorted array:", arr1)

    print("Using merge sort:")
    
    timerB.start_timer()
    merge_sort(arr2, 0, len(arr2)-1)
    timerB.end_timer(j)
    if j <= 1000:
      print("Sorted array:", arr2)
    
    print("Using merge - insertion sort:")
    timerC.start_timer()
    merge_ins_sort(arr3, 0, len(arr3)-1)
    timerC.end_timer(j)
    if j <= 1000:
      print("Sorted array:", arr3)
  
  print(timerA.time_arr.keys())
  print(timerA.time_arr.values())
  plt.plot(list(timerA.time_arr.keys()), list(timerA.time_arr.values()), "-b", label = "Insertion sort")

  print(timerB.time_arr.keys())
  print(timerB.time_arr.values())
  plt.plot(list(timerB.time_arr.keys()), list(timerB.time_arr.values()), "-r", label = "Merge sort")

  print(timerC.time_arr.keys())
  print(timerC.time_arr.values())
  plt.plot(list(timerC.time_arr.keys()), list(timerC.time_arr.values()), "-g", label = "Merge-Insertion sort")
  plt.legend(loc="upper left")
  plt.title("Time complexity graphs")
  plt.xlabel("Input size (n)")
  plt.ylabel("Time (ms)")

  plt.show()

main1()
main2()