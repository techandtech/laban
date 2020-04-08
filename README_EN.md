Pygame Installation

```bash
pip3 install pygame
```

Table with codes for the combination

0 - body parts, 1 - type of movement, 2 - duration of movement, 3 - quality of movement, 4 - space, 5 - mode of movement, 6 - figure

|      |                                                              |
| ---- | ------------------------------------------------------------ |
| 0    | 30 body parts                                                |
| 1    | stopping, unbalancing, falling, turning, jumping, opening, free movement, squeezing, twisting, changing support |
| 2    | long-term, instantaneous                                     |
| 3    | swing, touch, wiggle, slip, kick, whiplash                   |
| 4    | single focus, moving focus                                   |
| 5    | impact, impulse, continuous movement, rebound, swing.        |
| 6    | circle, line, broken line, point, triangle, quadrangle       |

## How the program works

1. The user enters the interval between repetitions of the combination in seconds, for example **5**.
2. Next, enter the combination consisting of numbers from 0 to 6, for example **6125**.
3. Then enter the number of times the combination is repeated, for example **3**.

![img](https://lh6.googleusercontent.com/49jLRMphIfYsjpMgDK4TINFBZmzVBh9_8Q5ec_bl5nd-Uq3NGS3J3kQb5MOW8g4VsD_UiSy9b3bo2KLKqz3Cb7ktNFW7bTqV71x0BbdncQUU4ETLdFagk1Sh8CUnCMMwej0Seo-f)

Video demonstration of the program: https://youtu.be/D2S3VfFqfTY

Text demonstration:

- random figure(6) - random mode of motion(1) - random duration of motion(2) - random mode of motion(5)
- **...5 seconds of silence…**
- random figure(6) - random mode of motion(1) - random duration of motion(2) - random mode of motion(5)
- **...4 seconds of silence…**
- random figure(6) - random mode of motion(1) - random duration of motion(2) - random mode of motion(5)
- **...3 seconds of silence…**

If the number of repetitions (e.g. 10) is greater than the pause length (e.g. 5), the pause will decrease to one: 5, 4, 3, 2, 1, 1, 1, 1, 1, 1
