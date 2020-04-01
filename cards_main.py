#! /usr/bin/env python3
import  cards_tools
# while True 可以无限循环，除非break
while True:
    # 显示功能菜单
    cards_tools.show_menu()
    action_str = input("请输入希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # 1,2,3针对名片的操作
    if action_str in ["1", "2", "3"]:
        # 新建名片
        if action_str == "1":
            cards_tools.add_card()
        # 显示名片
        if action_str == "2":
            cards_tools.show_all()
        #搜索名片
        if action_str == "3":
            cards_tools.search_card()

        pass
    # 0 退出系统
    elif action_str == "0":
        print("欢迎下次再次使用【名片管理系统】")
        break
        # 如果在开发程序时，不希望立刻编写分支内部的代码可以使用pass关键字
        # pass 关键字表示一个占位符，能够保证程序的代码结构正确
        # 程序运行时，pass关键字不会执行任何的操作
        #pass
    else:
        print("输入有误，请重新输入:")
