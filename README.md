# 基于Opencv 的图片生成器
* 使用json文件配置，生成图片

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
            color : 颜色(可选)，
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
            color : 颜色(可选)，
            x : x,
            y : y,
            w : width,
            h : heigh,
        },
        ...
    ]
}
```

## Getting started
```sh
    python3 generate.py <json文件路径或目录>
```