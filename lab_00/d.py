w1,h1,w2,h2 = map(int,input().strip().split())
p1 = 2*((w1+w2)+max(h1, h2))
p2 = 2*(max(w1,w2)+(h1+h2))
print(min(p1,p2))
