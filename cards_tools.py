# 定义一个空的列表，用来针对名片的管理,列表保存名字信息应该是一个字典类型的值
card_list = []

def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】 v 1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*" * 50)

def add_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 提示用户输入名片信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话号码：")
    qq_str = input("请输入qq号码：")
    email_str = input("请输入邮箱：")

    # 根据用户输入的信息建立名片字典
    card_dic = {"name": name_str,
                "phone": phone_str,
                "qq": qq_str,
                "email": email_str}
    # 把输入的用户信息添加到列表中
    card_list.append(card_dic)
    #添加完成之后提示用户已经添加成功
    print("名片 %s 已经添加完成" % name_str )

def show_all():
    """显示全部名片"""
    print("-" * 50)
    print("显示所有名片")
    # 判断列表是否为空，可以使用len函数
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用新增功能添加名片")

        # return 返回一个函数的执行结果
        # return下发的代码不会被执行，如果return 后面没有任何的内容，表示返回到调用函数的位置
        #并且不会返回任何的结果
        return
    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")
    # 打印分割线
    print("=" * 50)

    # 遍历名片列表 依次输出字典信息
    for card_dic in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dic["name"],
                                        card_dic["phone"],
                                        card_dic["qq"],
                                        card_dic["email"]))




def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    # 提示用户输入要查找的姓名
    find_name = input("请输入要查找的姓名: ")
    # 遍历列表，查询用户输入的姓名是否在列表中存在，如果存在就线上，如果不存在就退出
    for card_dic in card_list:
        if card_dic["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dic["name"],
                                            card_dic["phone"],
                                            card_dic["qq"],
                                            card_dic["email"]))
            deal_card(card_dic)
            break
    else:
        print("抱歉没有找到 %s" % find_name)

def deal_card(find_card):
    """  处理查找到的名片

    :param find_card: 查找到的名片
    """
    print("=" * 50)
    #print(find_card)
    action_str = input("请选择要执行的操作"
                       "【1】修改，【2】删除， 【0】 返回上级菜单: ")

    if action_str == "1":
        print("修改名片")
        find_card["name"] = input_card_info(find_card["name"], "姓名：")
        find_card["phone"] = input_card_info(find_card["phone"], "电话：")
        find_card["qq"] = input_card_info(find_card["qq"], "QQ：")
        find_card["email"] = input_card_info(find_card["email"], "邮箱：")
    elif action_str == "2":
        print("删除成功 %s" % find_card)
        card_list.remove(find_card["name"])
        # print("删除名片")

def input_card_info(dict_value, tip_message):
    """ 定义两个参数，名片信息

    :param dict_value: 字典中原有的值
    :param tip_message: 用户输入的值
    :return: 如果用户输入了内容，就返回内容，否则返回资源原有的值
    """
    # 1、提示用户输入内容
    str = input(tip_message)
    # 2、针对用户的输入进行判断，如果用户输入了内容直接返回结果
    if len(str) > 0:
        return  str
    else:
        return dict_value
    # 3、如果用户没有输入内容，则直接返回原来的值

