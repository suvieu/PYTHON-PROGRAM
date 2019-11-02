# 掷色子 模拟掷两颗色子，统计两颗色子点数的和分布
from random import randint
import pygal
class Die():
    def __init__(self,num_sides=6):
        self.num_sides=num_sides
    def roll(self):
        return randint(1,self.num_sides)
die1=Die()
die2=Die()
results=[]
frequencies=[]
for roll_num in range(1000):
    result=die1.roll()+die2.roll()
    results.append(result)
for value in range(2,die1.num_sides+die2.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)
hist=pygal.Bar()
hist.title='result of rolling two D6 1000 times'
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title="result"
hist.y_title="frequency"
hist.add('D6+D6',frequencies)
hist.render_to_file('die_visual.svg')
