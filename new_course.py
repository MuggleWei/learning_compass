import datetime
import os
import sys

if __name__ == "__main__":
    # 需要至少输入一个课程
    if len(sys.argv) < 2:
        print("please input at least 1 course name")
        sys.exit(1)

    # 判断当前目录是否正确
    course_base_dir = os.path.join("content", "posts", "course")
    if not os.path.exists(course_base_dir):
        print("failed find course director: {}".format(course_base_dir))
        sys.exit(1)

    # 生成课程
    tzinfo = datetime.timezone(datetime.timedelta(hours=8))
    for course in sys.argv[1:]:
        course_dir = os.path.join(course_base_dir, course)
        if os.path.exists(course_dir):
            print("{} already exists, ignore".format(course))
            continue

        os.makedirs(course_dir, exist_ok=True)

        course_path = os.path.join(course_dir, "index.md")
        with open(course_path, "w", encoding="utf-8") as f:
            dt = datetime.datetime.now(tz=tzinfo)
            date_str = dt.strftime("%Y-%m-%dT%H:%M:%S+08:00")

            f.write("---\n")
            f.write("title: \"{}\"\n".format(course))
            f.write("date: {}\n".format(date_str))
            f.write("draft: false\n")
            f.write("---\n")

            f.write("\n")
            f.write("## 课程资源\n")
            f.write("| 名称 | 大学/机构 | 公开课视频链接 | 课件链接 | 备注 |\n")
            f.write("| ---- | ---- | ---- | ---- | ---- |\n")

            f.write("\n")
            f.write("## 教材习题用书\n")
            f.write("| 书名 | 书号 | 作者 | 出版社 | 备注 |\n")
            f.write("| ---- | ---- | ---- | ---- | ---- |\n")

            f.write("\n")
            f.write("## 依赖课程\n")
            f.write("| 课程 | 备注 |\n")
            f.write("| ---- | ---- |\n")

            print("Generate Course {} completed, path: {}".format(
                course, course_path))