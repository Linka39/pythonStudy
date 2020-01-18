import sys

import easygui as g

while 1:
    print(g.msgbox('嘿，你好'))
    msg='这段时间你学到了什么？'
    title='互动选项'
    choices = ['编程','谈恋爱','玩游戏']
    choice = g.choicebox(msg,title,choices)
    g.msgbox('你选择的是'+str(choice),'结果')

    if g.ccbox(msg,title):
        pass
    else:
        sys.exit(0)