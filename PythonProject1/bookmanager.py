
class Cat:
    def __init__(self, cat_id, name, color, character):
        self.cat_id = cat_id
        self.name = name
        self.color = color
        self.character = character
    def __str__(self):
        return f"小猫编号:{self.cat_id}, 小猫名字:{self.name}, 小猫颜色:{self.color}, 小猫性格:{self.character}"


class CatManager:
    def __init__(self):
        self.cats = {}

    def add_cat(self, cat):
        if cat.cat_id in self.cats:
            print("错误：这个小猫编号已经存在")

        else:
            self.cats[cat.cat_id] = cat
            print(f"已添加：{cat}")

    def remove_cat(self, cat_id):
        if cat_id in self.cats:
            del self.cats[cat_id] #小猫名字索引的小猫对象
            print(f"已删除小猫编号{cat_id}")
        else:
            print("错误：小猫编号未找到")
    def show_all_cats(self):
        for cat in self.cats.values():
            print(cat)

    def find_cat(self, cat_id):
        if cat_id in self.cats:
            print(f"找到小猫：{self.cats[cat_id]}")
        else:
            print("未找到小猫")


def main():
    cat_manager = CatManager()
    while True:
        print("\n小猫管理菜单：")
        print("1.添加小猫")
        print("2.删除小猫")
        print("3.显示所有小猫")
        print("4.查询小猫")
        print("5.退出")
        choice = input("请输入选项：")

        if choice == '1':
            cat_id = input("请输入小猫编号：")
            name = input("请输入小猫名字：")
            color = input("请输入小猫颜色：")
            character= input("请输入小猫性格：")
            cat_manager.add_cat(Cat(cat_id, name, color, character))
        elif choice == '2':
            cat_id = input("请输入要删除的小猫编号：")
            cat_manager.remove_cat(cat_id)
        elif choice == '3':
            cat_manager.show_all_cats()
        elif choice == '4':
            cat_id = input("请输入要查询的小猫编号：")
            cat_manager.find_cat(cat_id)
        elif choice == '5':
            print("正在退出。。。")
            break
        else:
            print("无效选项，请输入1-5之间的数字：")


if __name__ == "__main__":
    main()