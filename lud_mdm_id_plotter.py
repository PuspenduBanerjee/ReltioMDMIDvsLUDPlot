from typing import Any

import matplotlib
from dateutil import tz
from jsonpath_ng import jsonpath, parse
import json
import pandas as pd
import matplotlib.dates as mdates
import glob
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
import mplcursors
#from mpldatacursor import datacursor




def process_raw_input(fname):
    # fname = "./resources/sej05t7phwdm1h3_01-20_entities_b09e.json"
    # fname = "./resources/sej05t7phwdm1h3_20-03_entities_b82e_20200403.json"
    lud_ex = parse("crosswalks[*].reltioLoadDate")
    with open(fname + "_lud.csv", "w+") as f1:
        f1.writelines("mdm_id,lud\n")
        with open(fname, "r") as f:
            for line in f:
                line = line.strip()
                if len(line) > 1:
                    line = line[:-1] if line.endswith(",") else line
                    o = json.loads(line)
                    mdm_id = o["attributes"]["MDMCustomerID"][0]["value"]
                    lud = max([match.value for match in lud_ex.find(o)])
                    f1.writelines(mdm_id + "," + lud + "\n")
                    # print(mdm_id,lud)
    return f1.name


def plot_it(data_file_name: str,ax:Any,ax3:Any,color):
    tz_str='America/New_York'
    report_date=data_file_name.split(".json_lud.csv")[0].split("_")[-1]
    df = pd.read_csv(data_file_name, parse_dates=['lud'])
    # df_dt_range=pd.date_range(start_date, end_date, freq='W')
    df['lud'] = df.lud.dt.tz_convert(tz=tz_str)
    df2 = df.groupby(df.lud.dt.ceil('12H')).count()
    df3 = df2.add_suffix('_count').reset_index()
    print(df3)
    # r=[pd.to_datetime('2020-03-01 00:00:01'), pd.to_datetime('2020-04-05 00:15:00')]
    ax3=df3.plot(x='lud',y='mdm_id_count',kind='scatter',color=color, \
                rot=30,xticks=df3['lud'],grid=True, logy=False, \
                title="Records Mismatched Count vs Last updated date", \
                 ax=ax3,  label=f"Reported: {report_date}")
    #ax3.set_xscale('symlog')
    ax3.set(xlabel="Last Updated")
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%m/%dT%H',tz=tz.gettz(tz_str)))
    # ax3.ticklabel_format(style='plain',axis='y')
    ax3.legend()
    mplcursors.cursor(hover=True)
    ax = df.plot(x='lud', y='mdm_id', kind='scatter', color=color, \
                 rot=30, grid=True, xticks=df3['lud'], logy=False, \
                 title="Records Mismatched vs Last updated date", \
                 ax=ax,   label=f"Reported: {report_date}")
    #ax.set_xscale('symlog')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%dT%H',tz=tz.gettz(tz_str)))
    ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), '')))
    ax.legend()
    mplcursors.cursor(hover=True)
    #datacursor()
    return ax,ax3


if __name__ == "__main__":
    ax=None
    ax3=None
    plt.rcParams['ytick.labelsize'] = "small"
    plt.ioff()
    for f1_name in  list(glob.glob("./resources/*.json")):
        f1_name = process_raw_input(f1_name)
        hex_number="#{:06x}".format(random.randint(0, 0xFFFFFF))
        print('A  Random Hex Color Code is :',hex_number)
        plt.style.use('ggplot')
        ax,ax3=plot_it(f1_name,ax,ax3,color=hex_number)
    plt.show()
