alpha=0.00001
m,c=0,0

x=[2,4,6]
y=[4,8,12]


m=len(x)

max_it=int(input("Enter the maximum number of iterations: "))

l=0
for _ in range(max_it):

    dm,dc=0,0
    for i in range(int(m)):
        yp = m * x[i] + c

        dm+=(yp-y[i])*x[i]
        dc=(yp-y[i])

        dm/=m
        dc/=m

        m-=alpha * dm
        c-=alpha * dc

cost = (1 / m) * sum([(m * x[i] + c - y[i]) ** 2 for i in range(int(m))])
print("Cost:",c)

print(f"final values: m: {m:6f},c:{c:6f}")
