import pandas as pd 
import statistics

df = pd.read_csv("height-weight.csv")

hlist = df["Height(Inches)"].tolist()
wlist = df["Weight(Pounds)"].tolist()

hmean = statistics.mean(hlist)
hmedian = statistics.median(hlist)
hmode = statistics.mode(hlist)
hstd = statistics.stdev(hlist)

wmean = statistics.mean(wlist)
wmedian = statistics.median(wlist)
wmode = statistics.mode(wlist)
wstd = statistics.stdev(wlist)
print("mean median mode is : {},{},{}".format(hmean,hmedian,hmode))
print("mean median mode is : {},{},{}".format(wmean,wmedian,wmode))

hfirst_std_start,hfirst_std_end = hmean-hstd,hmean+hstd
hsecond_std_start,hsecond_std_end = hmean-(2*hstd),hmean+(2*hstd)
hthird_std_start,hthird_std_end = hmean-(3*hstd),hmean+(3*hstd)

wfirst_std_start,wfirst_std_end = wmean-wstd,wmean+wstd
wsecond_std_start,wsecond_std_end = wmean-(2*wstd),wmean+(2*wstd)
wthird_std_start,wthird_std_end = wmean-(3*wstd),wmean+(3*wstd)

hdata_within_1_std = [result for result in hlist if result>hfirst_std_start and result<hfirst_std_end ]
hdata_within_2_std = [result for result in hlist if result>hsecond_std_start and result<hsecond_std_end ]
hdata_within_3_std = [result for result in hlist if result>hthird_std_start and result<hthird_std_end ]

wdata_within_1_std = [result for result in wlist if result>wfirst_std_start and result<wfirst_std_end ]
wdata_within_2_std = [result for result in wlist if result>wsecond_std_start and result<wsecond_std_end ]
wdata_within_3_std = [result for result in wlist if result>wthird_std_start and result<wthird_std_end ]

print("{} % of data for height lies within 1 standard deviation".format(len(hdata_within_1_std)*100.0/len(hlist)))
print("{} % of data for height lies within 2 standard deviation".format(len(hdata_within_2_std)*100.0/len(hlist)))
print("{} % of data for height lies within 3 standard deviation".format(len(hdata_within_3_std)*100.0/len(hlist)))
print("\n\n")
print("{} % of data for weight lies within 1 standard deviation".format(len(wdata_within_1_std)*100.0/len(wlist)))
print("{} % of data for weight lies within 2 standard deviation".format(len(wdata_within_2_std)*100.0/len(wlist)))
print("{} % of data for weight lies within 3 standard deviation".format(len(wdata_within_3_std)*100.0/len(wlist)))
