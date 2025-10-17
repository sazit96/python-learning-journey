def line (n, s):
    if len(s) == 1:
      print(n * s)
    elif len(s) > 1:
       print(n * s[0])
    else: print(n * "*")

line(7, "%")
line(5, "xsazit")
line(7, "")