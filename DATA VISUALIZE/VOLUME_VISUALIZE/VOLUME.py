import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
df = pd.read_excel('province_volume.xlsx')
fig,ax= plt.subplots(figsize=(15,8))
colors = dict(zip(['Guangdong','Anhui','Shanghai','Zhejiang','Jiangsu',
              'Jiangxi','Guangxi','Shandong','Fujian','Hunan'],
             ['#BCBCBC','#adb0ff', '#ffb3ff', '#90d595', '#e48381',
             '#aafbff', '#f7bb5f', '#eafb50','#89C479','#6B6B6B']))
def draw_barchart(month):
    dff = df[df['MONTH'].eq(month)].sort_values(by='VOL', ascending=True).tail(10)
    ax.clear()
    ax.barh(dff['Province'],dff['VOL'],color=[colors[x] for x in dff['Province']])
    for i,(vol,province) in enumerate(zip(dff['VOL'],dff['Province'])):
        ax.text(vol+1, i,     f'{vol:,.2f}',  size=12, ha='left',  va='center')
    ax.text(0.8, 0.4, month,transform=ax.transAxes,color='#777777', size=46, ha='left', weight=800)
    ax.text(0, 1.06, 'VOL',transform=ax.transAxes, size=12, color='#777777',weight=800)
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12) #x轴字体颜色
    ax.margins(0, 0.01)
    ax.set_axisbelow(True)
    ax.text(0.25, 1.1, 'SHIPMENT VOLUME FROM JAN TO SEP,2019',
                transform=ax.transAxes, size=18, weight=600, ha='left')
    plt.box(False)


animator = animation.FuncAnimation(fig, draw_barchart, frames=range(1, 10),interval=1000)

animator.save('VOL.gif',writer='pillow')


