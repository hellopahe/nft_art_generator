from PIL import Image
import re
import json
import os
import random

# 素材路径
paths = {
    './layers/Face',
    './layers/Ears',
    './layers/Nose',
    './layers/Hair',
    './layers/Mouth',
    './layers/Eyes'
}

# 全局变量，保存素材信息，素材权重，生成图片的数量，生成图片的特征集
component = {}
component_weights = {}

image_num = 30  # 可修改，超过生成图片的理论最大值会报错

image_id = 0
token_id = 0
output_images = []


def find_file(folder):
    for root, ds, fs in os.walk(folder):
        for f in fs:
            yield f


def read_file():

    # 遍历layers文件夹
    for path in paths:
        temp = []
        for i in find_file(path):
            temp.append(path + "/" + i)
        component[path] = temp

        # 生成权重
        weights = []
        generate_weights(weights, len(temp), 100)
        component_weights[path] = weights

        print('%s的路径下共有%d个素材，它们的权重为:' % (path, len(temp)))
        print(component_weights[path])


def generate_weights(weights, length, total_sum):

    # 根据元素数量，生成length长度的随机权重序列
    if length == 1:
        weights.append(total_sum)
        return

    x = random.randint(0, int(total_sum / length))
    weights.append(x)
    generate_weights(weights, length - 1, total_sum - x)


def generate():

    # 递归生成图片
    if len(output_images) >= image_num:
        return

    new_image = {}
    for key, value in component.items():
        new_image[key] = random.choices(value, component_weights[key])[0]

    if new_image in output_images:
        return generate()
    else:
        output_images.append(new_image)
        generate_png(new_image)
        return generate()


def generate_png(new_image):
    global image_id
    temp = []

    # 确保将face存入待处理图像的队列头部，优先堆叠
    for k in new_image:
        if "Face" in k:
            temp.append(Image.open(f'{new_image[k]}').convert('RGBA'))

    for k in new_image:
        if "Face" in k:
            continue
        temp.append(Image.open(f'{new_image[k]}').convert('RGBA'))

    # 按照队列顺序合成图像
    for i in range(0, len(temp) - 1):
        temp[i + 1] = Image.alpha_composite(temp[i], temp[i + 1])

    # 保存
    output_rgb = temp[-1].convert('RGB')
    output_name = str(image_id) + ".png"
    image_id += 1
    output_rgb.save("./images/" + output_name)


def generate_metadata():

    # 生成图片元数据, 用output_image中的数据经正则过滤后放入json
    data = []
    global token_id
    for im in output_images:
        temp = {}
        for k, v in im.items():
            str1 = str(re.findall('(?<=./layers/).*$', k))
            str2 = str(re.findall('(?<=./layers/).*$', v))
            temp[str1] = str2
        temp["token_id"] = token_id
        token_id += 1
        data.append(temp)

    with open('./metadata.json', 'w') as f:
        json.dump(data, f, indent=4)

    print('已生成图片的元数据，存储路径为./metadata.json\n已生成的图片存储路径为./images/')


def main():
    read_file()
    generate()
    generate_metadata()


if __name__ == '__main__':
    main()

