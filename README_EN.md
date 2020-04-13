Pygame Installation

```bash
pip3 install pygame
```

Table with codes for the combination

| Number | Category                  | Possible options                                           |
| ----- | -------------------------- | ------------------------------------------------------------ |
| 1     | body parts               | 28 body parts                                               |
| 2     | type of movement              | stopping, unbalancing, falling, turning, jumping, opening, free movement, squeezing, twisting, changing support |
| 3     | duration of movement | long-term, instantaneous                                         |
| 4     | quality of movement         | swing, touch, wiggle, slip, kick, whiplash |
| 5     | space             | single focus, moving focus                        |
| 6     | mode of movement | impact, impulse, continuous movement, rebound           |
| 7     | figure                     | circle, line, broken line, point, triangle, quadrangle  |

## How the program works

1. The user enters the interval between repetitions of the combination in seconds, for example **5**.
2. Next, enter the combination consisting of numbers from 1 to 7, for example **7236**.
3. Then enter the number of times the combination is repeated, for example **3**.

Video demonstration of the program: https://youtu.be/TWnkuZWifd8

Text demonstration:

- random figure(7) - random mode of motion(2) - random duration of motion(3) - random mode of motion(6)
- **...5 seconds of silence…**
- random figure(7) - random mode of motion(2) - random duration of motion(3) - random mode of motion(6)
- **...4 seconds of silence…**
- random figure(7) - random mode of motion(2) - random duration of motion(3) - random mode of motion(6)
- **...3 seconds of silence…**

If the number of repetitions (e.g. 10) is greater than the pause length (e.g. 5), the pause will decrease to one: 5, 4, 3, 2, 1, 1, 1, 1, 1, 1
