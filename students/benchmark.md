
### Benchmark Test
B1     | B2
-------- | ---
n = 1000 | n = 1000
c = 100    | c = 10
tpr = 3.322    | tpr = 3.377
failed = 0 | failed = 0
completed = 1000 | completed = 1000


B3     | B4
-------- | ---
n = 1000 | n = 1000
c = 130    | c = 125
tpr = 3.357    | tpr = 3.344
failed = 0 | failed = 0
completed = 1000 | completed = 1000


B1: For this test i began with n = 1000, and c = 100. I chose this numbers cause these were the numbers our teacher began testing his server with. 
B2: I  tested with n = 1000 and c = 10. The reason I chose ten was to see if my time per request would be faster, but it didn't really make a difference. 
B3: After several tests I got to my benchmark point which was n = 1000 and c = 130. In this scenario my server didnt break but anything over 130 and my server would go down. For some reason though the server would crash 1 / 7 times. 
B4: The purpose of this test was to make sure that my benchmark test was 130. Surprisingly I tried this test many times and it was consistently succesful. 