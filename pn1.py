from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(20)
    left(17)
    if abs(pos()) < 1:
        break
end_fill()
done()
