import numpy as np
import pandas as pd
from tabulate import tabulate
# import matplotlib.pyplot as plt

df = pd.read_csv("/Users/tsekii/Downloads/analyticsAdmin.clusterB-06@ccepdemo.com_Webex_Attendee_analytics-clusterb_2019-10-09_2019-11-08.csv", true_values=["Y"],false_values=["N"])

is_sharing = df[["CONFERENCE_ID", "USER_NAME","IS_SHARING"]].query('IS_SHARING == True') 
sharing_result = tabulate(is_sharing, tablefmt="grid", headers="keys")

print(sharing_result)

