# 基于Opencv 的图片生成器
* 使用json文件配置，生成图片， 目前仅仅支持直线 和 矩形

## 依赖
* python
* opencv-python

## json 文件格式
* 导出的坐标系约定：原点在左上角，x正轴往右， y正轴往下
```json
{
    width: 图片宽度,
    heigh: 图片高度,
    title: 图片标题,
    
    lines: [
        {
            color : 颜色(可选){r:?, g:?, b:?}，
            points : [
                x1,
                y1,
                x2,
                y2,
                ...
            ]
        },
        ...
    ],
    rects: [
        {
            color : 颜色(可选){r:?, g:?, b:?}，
            x : x,
            y : y,
            w : width,
            h : heigh,
            id: 矩形id（string), 会在矩形左上角显示
        },
        ...
    ]
}
```

## Getting started
* 基本用法
```sh
    python3 generate.py <json文件路径或目录>
```

* 测试, 将test_res 目录的所有json文件生成对应的图片
```sh
    python3 generate.py ./test_res
```