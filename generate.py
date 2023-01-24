
import sys, os
import json
import numpy as np
import cv2 as cv

COLOR_WHITE = (255, 255, 255)

def parse_color(json_color):
    return (json_color['b'], json_color['g'], json_color['r'])

def draw_lines(img, lines):
    for line in lines:
        for k in range(0, len(line['points']), 4):
            pt_a = (line['points'][k], line['points'][k+1])
            pt_b = (line['points'][k+2], line['points'][k+3])
            cv.line(img, pt_a, pt_b, COLOR_WHITE)

def draw_rects(img, rects):
    for rect in rects:
        pt_start = (rect['x'], rect['y'])
        pt_end = (rect['x'] + rect['w'], rect['y']+rect['h'])
        color = COLOR_WHITE
        if 'color' in rect:
            color = parse_color(rect['color'])
            print("color:", color)
        cv.rectangle(img, pt_start, pt_end, color, 1)

def handle_file(path):
    print("handling path:", path)
    file_obj = open(path, 'r')
    try:
        content = file_obj.read()
        data = json.loads(content)
        print("data:", data)
        img = np.zeros((data['heigh'], data['width'], 3), np.uint8)
        if "lines" in data:
            draw_lines(img, data['lines'])
        if "rects" in data:
            draw_rects(img, data['rects'])    
        cv.imwrite(os.path.splitext(path)[0]+".jpg", img)            
    finally:
        file_obj:close()

def handle_directory(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == ".json":
                handle_file(os.path.join(root, file))

def show_usage():
    print("========================================")
    print("Usage:")
    print("python generate.py <file or directory>")
    print("========================================")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_usage()
        exit(1)
    path = sys.argv[1]
    if os.path.isdir(path):
        handle_directory(path)
    elif os.path.isfile(path):
        if os.path.splitext(path)[1] == ".json":
            handle_file(path)
        else:
            print("invalid json file")
            exit(1)
    else:
        print("unknown path:", path)
        exit(1)
