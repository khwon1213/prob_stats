import thinkstats.thinkstats as ts
from thinkstats import Cdf
from thinkstats import myplot

birthday_arrival = [114	,
153	,
151	,
17	,
79	,
71	,
16	,
33	,
28	,
34	,
2	,
0	,
20	,
14	,
9	,
101	,
6	,
29	,
23	,
39	,
4	,
49	,
17	,
70	,
57	,
24	,
0	,
26	,
4	,
14	,
14	,
11	,
39	,
13	,
26	,
23	,
14	,
101	,
125	,
0	,
53	,
10	,
56	,
165	,
46	,
5	,
0	,
38	,
29	,
4	,
30	,
89	,
14	,
                    ]

cdf = Cdf.MakeCdfFromList(birthday_arrival)
print 'Mean:', cdf.Mean()
myplot.Clf()
myplot.Cdf(cdf)
myplot.Save('birthday_cdf')
myplot.Clf()
myplot.Cdf(cdf, complement=True)
myplot.Save('birthday_ccdf', yscale='log')
myplot.Close()
