print("疯狂填词游戏")
print("请根据提示输入相应的内容\n")

# 询问用户语言偏好
language = input("请选择语言 (中文/english): ").lower().strip()

if language in ["english", "en", "eng"]:
    # 英文版本
    print("\nMAD LIB GAME")
    print("Enter answers to the following prompts\n")
    
    # Python的input()，其中括号内是输入前的内容
    guy = input("Name of a famous man: ")
    girl = input("Name of a famous woman: ")
    food = input("Your favorite food (plural): ")
    ship = input("Name of a space ship: ")
    job = input("Name of a profession (plural): ")
    planet = input("Name of a planet: ")
    drink = input("Your favorite drink: ")
    number = input("A number from 1 to 10: ")

    story = "\nA famous married couple, GUY and GIRL, went on\n" +\
            "vacation to the planet PLANET. It took NUMBER\n" +\
            "weeks to get there travelling by SHIP. They\n" +\
            "enjoyed a luxurious candlelight dinner over-\n" +\
            "looking a DRINK ocean while eating FOOD. But,\n" +\
            "since they were both JOB, they had to cut their\n" +\
            "vacation short."

else:
    # 中文版本 - 加入中国元素和梗
    print("\n请根据提示输入内容，我们会生成一个有趣的故事!\n")
    
    guy = input("一位著名男明星的名字: ")
    girl = input("一位著名女明星的名字: ")
    food = input("你喜欢的小吃(复数，如:煎饼果子): ")
    ship = input("一个飞船的名字: ")
    job = input("一种职业(复数，如:程序员): ")
    planet = input("一个星球的名字: ")
    drink = input("你喜欢的饮料: ")
    number = input("1到10之间的一个数字: ")

    # 中文故事模板，加入中国元素和梗
    story = "\n著名夫妻GUY和GIRL，乘坐着SHIP号飞船前往PLANET度假。\n" +\
            "他们花了NUMBER周时间才到达目的地。在欣赏着DRINK色的星空同时，\n" +\
            "他们享受着豪华的烛光晚餐，吃着地道的FOOD。但是，\n" +\
            "由于他们都是苦逼的JOB，老板突然打电话要求加班，\n" +\
            "不得不提前结束假期，匆匆返回地球搬砖。"

# 替换故事中的占位符
story = story.replace("GUY", guy)
story = story.replace("GIRL", girl)
story = story.replace("FOOD", food)
story = story.replace("SHIP", ship)
story = story.replace("JOB", job)
story = story.replace("PLANET", planet)
story = story.replace("DRINK", drink)
story = story.replace("NUMBER", number)

print(story)