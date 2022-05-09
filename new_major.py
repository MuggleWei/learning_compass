import datetime
import os
import sys

if __name__ == "__main__":
    # 需要至少输入一个专业
    if len(sys.argv) < 2:
        print("please input at least 1 major name")
        sys.exit(1)

    # 判断当前目录是否正确
    major_base_dir = os.path.join("content", "posts", "major")
    if not os.path.exists(major_base_dir):
        print("failed find major director: {}".format(major_base_dir))
        sys.exit(1)

    # 生成专业
    tzinfo = datetime.timezone(datetime.timedelta(hours=8))
    for major in sys.argv[1:]:
        major_dir = os.path.join(major_base_dir, major)
        if os.path.exists(major_dir):
            print("Major {} already exists, ignore".format(major))
            continue

        os.makedirs(major_dir, exist_ok=True)

        major_path = os.path.join(major_dir, "index.md")
        with open(major_path, "w", encoding="utf-8") as f:
            dt = datetime.datetime.now(tz=tzinfo)
            date_str = dt.strftime("%Y-%m-%dT%H:%M:%S+08:00")

            f.write("---\n")
            f.write("title: \"{}\"\n".format(major))
            f.write("date: {}\n".format(date_str))
            f.write("draft: false\n")
            f.write("---\n")

            f.write("\n")
            f.write("## 学科编码\n")
            f.write("| 学科体系 | 编码 | 备注 |\n")
            f.write("| ---- | ---- | ---- |\n")

            f.write("\n")
            f.write("## 课程列表与路线图\n")

            f.write("\n")
            f.write("### 某校课程列表\n")
            f.write("| 编号 | 课程名称 | 类别 | 备注 |\n")
            f.write("| ---- | ---- | ---- | ---- |\n")

            f.write("\n")
            f.write("### 某校课程路线图\n")
            f.write("```graphviz\n")
            f.write("digraph {}\n")
            f.write("```\n")

            print("Generate Major {} completed, path: {}".format(
                major, major_path))