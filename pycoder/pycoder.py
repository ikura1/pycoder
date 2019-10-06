
import pendulum
# import argparse

def show_age(birthday):
    age = pendulum.parse(birthday).age
    print(f"あなたは現在{age}歳です。")


if __name__ == "__main__":
    main()
