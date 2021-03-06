### quick guide

* 运行 bash setup.sh 安装依赖包并执行，生成的文件在 ./images ，元数据在根目录的json中
* 随机从素材库中选择元素，拼合图片，可以修改生成图片的数量。保证图片的unique
* 素材库尺寸必须一致，这里的尺寸为16*16，可以在 https://www.pixilart.com/ 得到素材，素材命名后可以直接复制进 ./layers/ 对应文件夹。
* 如果加入元素种类，可以直接在 ./layers/ 下新建文件夹

### 生成图片示例: 

![image](./images/0.png)
![image](./images/1.png)
![image](./images/2.png)
![image](./images/3.png)
![image](./images/4.png)
![image](./images/5.png)
![image](./images/6.png)
![image](./images/7.png)
![image](./images/8.png)

[//]: # (![image]&#40;./images/9.png&#41;)

[//]: # ()
[//]: # (![image]&#40;./images/10.png&#41;)

[//]: # (![image]&#40;./images/11.png&#41;)

[//]: # (![image]&#40;./images/12.png&#41;)

[//]: # (![image]&#40;./images/13.png&#41;)

[//]: # (![image]&#40;./images/14.png&#41;)

[//]: # (![image]&#40;./images/15.png&#41;)

[//]: # (![image]&#40;./images/16.png&#41;)

[//]: # (![image]&#40;./images/17.png&#41;)

[//]: # (![image]&#40;./images/18.png&#41;)

[//]: # (![image]&#40;./images/19.png&#41;)

[//]: # ()
[//]: # (![image]&#40;./images/20.png&#41;)

[//]: # (![image]&#40;./images/21.png&#41;)

[//]: # (![image]&#40;./images/22.png&#41;)

[//]: # (![image]&#40;./images/23.png&#41;)

[//]: # (![image]&#40;./images/24.png&#41;)

[//]: # (![image]&#40;./images/25.png&#41;)

[//]: # (![image]&#40;./images/26.png&#41;)

[//]: # (![image]&#40;./images/27.png&#41;)

[//]: # (![image]&#40;./images/28.png&#41;)

[//]: # (![image]&#40;./images/29.png&#41;)
### metadata.json 示例: 
~~~
[{
        "['Ears']": "['Ears/yellow.png']",
        "['Face']": "['Face/orange.png']",
        "['Eyes']": "['Eyes/glasses.png']",
        "['Nose']": "['Nose/orange.png']",
        "['Hair']": "['Hair/red.png']",
        "['Mouth']": "['Mouth/yellow.png']",
        "token_id": 0
    }, ...
]
~~~
