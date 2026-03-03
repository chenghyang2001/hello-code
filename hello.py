from datetime import datetime


def get_current_time(fmt: str = "%Y/%m/%d %H:%M") -> str:
    """取得格式化的當前時間"""
    return datetime.now().strftime(fmt)


def greet(name: str) -> str:
    """產生問候語"""
    return f"Hello, {name}!"


def main():
    print(f"現在時間：{get_current_time()}")
    for name in ["World", "Peter", "Peter Yang"]:
        print(greet(name))


if __name__ == "__main__":
    main()
