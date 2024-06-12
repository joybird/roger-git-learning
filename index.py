from images.logo import logo
from style.style import style_one
from js import script

def main():
    print('主函数执行！')
    logo()
    style_one()
    script.run_script()
    print('主程序执行完毕！')


if __name__ == "__main__":
    main()
