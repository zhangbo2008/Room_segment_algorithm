# 做一个小鱼的问题


# 切割图形问题.

# 比如这里面的图片,就返回这个3个多边形. 等于把一个大房间,分割成多少个部分
# 然后返回这些部分的各个组成

# 用并查集可以对问题做分类,然后就得到了所有的 小房间内部点的分类结果.
# 合并的规则就是在一个房间内的点就合并成为同一类. 每一个点只需要看他的上下左右像素,如果
# 周围4个点也是内部点,不在线上,那么他们就都是房间内的点.



# 如果要边缘点,只需要找哪些上下左右有一个不在set中的就是边缘点
# 然后边缘点组成边即可.

# 组成边,还是在边缘点中进行搜索,
# 如果房子的墙壁都是水平和数值的,那么就就找哪些水平的左右相邻只有一个,和数值左右相邻只有一个的 点即可!!!!!!!!!111
















import pyclipper

subj = (
    ((180, 200), (260, 200), (260, 150), (180, 150)),
    ((215, 160), (230, 190), (200, 190))
)
clip = ((190, 210), (240, 210), (240, 130), (190, 130))

pc = pyclipper.Pyclipper()
pc.AddPath(clip, pyclipper.PT_CLIP, True)   # 表示添加了一个矩形
pc.AddPaths(subj, pyclipper.PT_SUBJECT, True)  # 表示添加两个一个矩形一个三角

solution = pc.Execute(pyclipper.CT_INTERSECTION, pyclipper.PFT_EVENODD, pyclipper.PFT_EVENODD)

# s
print(solution[0])
print(solution)



