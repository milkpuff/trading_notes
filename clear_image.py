import os
import re

# 定义文件目录
content_dir = "content/"
static_dir = "assets"

# 查找所有被引用的图片
used_images = set()
for root, _, files in os.walk(content_dir):
    for file in files:
        if file.endswith(('.md', '.html')):
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                content = f.read()
                matches = re.findall(r'!\[.*?\]\((.*?)\)', content)
                matches += re.findall(r'<img.*?src="(.*?)"', content)
                matches = [i.removeprefix('/') for i in matches]
                used_images.update(matches)

# 列出所有实际存在的图片
all_images = set()
for root, _, files in os.walk(static_dir):
    for file in files:
        all_images.add(os.path.relpath(os.path.join(root, file), static_dir))

# 找出未被引用的图片
unused_images = all_images - used_images

# 删除未使用的图片
for image in unused_images:
    # os.remove(os.path.join(static_dir, image))
    print(f"Deleted: {image}")
