x = int(input("Enter an amount to deposit: "))

print("Here is the breakdown of your deposit.")

t = x // 1000
print(t, "\t - \t1000")
x = x - t * 1000

h = x // 500
print(h, "\t - \t500")
x = x - h * 500

h2 = x // 200
print(h2, "\t - \t200")
x = x - h2 * 200

h = x // 100
print(h, "\t - \t100")
x = x - h * 100

f = x // 50
print(f, "\t - \t50")
x = x - f * 50

ts = x // 20
print(ts, "\t - \t20")
x = x - ts * 20

t2 = x // 10
print(t2, "\t - \t10")
x = x - t2 * 10

o = x // 1
print(o, "\t - \t1")
x = x - o * 1