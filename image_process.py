from PIL import ImageFont, ImageDraw, Image
import json
import random


def burn_id_into_image(image_id):
    image = Image.open(f'./images/{image_id}.png').convert('RGBA')

    id_str = "@id1453"
    f_font = ImageFont.truetype('./Font/Arial Unicode.ttf', 15)  # 自定字体文件和字号大小
    burn = ImageDraw.Draw(image)

    burn.text(
        (80, 230),  # 相对于左上角的位置
        id_str,  # 内容，unicode编码
        fill=(255, 255, 255),  # RGB颜色
        font=f_font,  # 自定义字体
    )

    image.show()
    output_name = "image_with_id.png"
    image.save("./images/" + output_name)

    print('生成的id水印图片保存在./images/image_with_id.png')


def read_json(image_id):

    image_meta = []
    with open('./metadata.json', 'r') as f:
        data = json.load(f)

    for image in data:
        if image["token_id"] == image_id:
            image_meta.append(image)
            break

    with open('./image_meta.json', 'w') as f:
        json.dump(image_meta, f, indent=4)

    print('生成图片的元数据保存在./image_meta.json')


def main():
    token_id = random.randint(0, 30)
    burn_id_into_image(token_id)
    read_json(token_id)


if __name__ == '__main__':
    main()
