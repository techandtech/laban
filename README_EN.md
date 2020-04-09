Pygame Installation

```bash
pip3 install pygame
```

Table with codes for the combination

| Number | Category                  | Possible options                                           |
| ----- | -------------------------- | ------------------------------------------------------------ |
| 0     | body parts               | 28 body parts                                               |
| 1     | type of movement              | stopping, unbalancing, falling, turning, jumping, opening, free movement, squeezing, twisting, changing support |
| 2     | duration of movement | long-term, instantaneous                                         |
| 3     | quality of movement         | swing, touch, wiggle, slip, kick, whiplash |
| 4     | space             | single focus, moving focus                        |
| 5     | mode of movement | impact, impulse, continuous movement, rebound, swing           |
| 6     | figure                     | circle, line, broken line, point, triangle, quadrangle  |

## How the program works

1. The user enters the interval between repetitions of the combination in seconds, for example **5**.
2. Next, enter the combination consisting of numbers from 0 to 6, for example **6125**.
3. Then enter the number of times the combination is repeated, for example **3**.

![img](https://lh6.googleusercontent.com/KtaKPcylF72q4Vgujmacd8RV5AXLGQOgK5fRpkGLTnIOLLcQeuztzuqGQToT3dQj9uo0AkDed-_fgrI7uFInPe8-b7vXBRVpV3m5ujuy_lFrLoQmMKF7paFGPZYWhUQAxCc4muvM)

Video demonstration of the program: https://youtu.be/TWnkuZWifd8

Text demonstration:

- random figure(6) - random mode of motion(1) - random duration of motion(2) - random mode of motion(5)
- **...5 seconds of silence…**
- random figure(6) - random mode of motion(1) - random duration of motion(2) - random mode of motion(5)
- **...4 seconds of silence…**
- random figure(6) - random mode of motion(1) - random duration of motion(2) - random mode of motion(5)
- **...3 seconds of silence…**

If the number of repetitions (e.g. 10) is greater than the pause length (e.g. 5), the pause will decrease to one: 5, 4, 3, 2, 1, 1, 1, 1, 1, 1
