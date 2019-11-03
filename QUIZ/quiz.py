#生成随机的测试
'''假如你是一位地理老师，班上有35 名学生，你希望进行美国各州首府的一个
小测验。不妙的是，班里有几个坏蛋，你无法确信学生不会作弊。你希望随机调整
问题的次序，这样每份试卷都是独一无二的，这让任何人都不能从其他人那里抄袭
答案。当然，手工完成这件事又费时又无聊。好在，你懂一些Python。
下面是程序所做的事：
• 创建 35 份不同的测验试卷。
• 为每份试卷创建50 个多重选择题，次序随机。
• 为每个问题提供一个正确答案和3 个随机的错误答案，次序随机。
• 将测验试卷写到35 个文本文件中。
• 将答案写到35 个文本文件中。'''

import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',\
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',\
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',\
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':\
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':\
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':\
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':\
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':\
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':\
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New\
Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',\
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',\
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',\
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':\
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':\
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West\
Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiznum in range(2):
    point=0
    quizfile = open('captialsquiz%s.text' % (quiznum + 1),'w')
    answerkeyfile = open('captialquiz_answers%s.text' % (quiznum + 1),'w')
    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((''*20) + 'State Capitals Quiz(Form %s)'%(quiznum + 1))
    quizfile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for questionnum in range(50):
        correctanswer = capitals[states[questionnum]]
        wronganswers = list(capitals.values())
        del wronganswers[wronganswers.index(correctanswer)]
        wronganswers = random.sample(wronganswers,3)
        answersoptions = wronganswers+ [correctanswer]
        random.shuffle(answersoptions)
        quizfile.write('%s.What is the capital of %s ?\n'%(questionnum + 1,states[questionnum]))

        for i in range(4):
            quizfile.write('%s.%s\n' % ('ABCD'[i],answersoptions[i]))
        my_answer= random.choice('ABCD')
        quizfile.write('My answer is: %s\n' % (my_answer))
        quizfile.write('\n')
        correct_answer = 'ABCD'[answersoptions.index(correctanswer)]
        if my_answer == correct_answer:
            point+=1
        answerkeyfile.write('%s.%s\n' % (questionnum+1,correct_answer))
    quizfile.write('Score: %s\n\n' % (point))
    quizfile.close()
    answerkeyfile.close()




