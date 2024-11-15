v,c=map(str,input().split())
if((c=='R' and v=='P') or (c=='P' and v=='S') or (c=='S' and v=='R')):
    print("Vignesh")
elif ((v=='R' and c=='P') or (v=='P' and c=='S') or (v=='S' and c=='R')):
    print("Charan")
else:
    print("NULL")
