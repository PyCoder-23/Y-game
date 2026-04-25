import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("board.png")
points = []

fig, ax = plt.subplots()
ax.imshow(img)


def onclick(event):
    if event.xdata and event.ydata:
        points.append((round(event.xdata), round(event.ydata)))
        print(len(points), points[-1])


cid = fig.canvas.mpl_connect("button_press_event", onclick)
plt.show()
print(points)
