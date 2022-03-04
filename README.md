# Solar System ☀️

<p align="center">
    <img alt="Solar System Demo" src="https://media.giphy.com/media/4lxGPRiKNo96ylV5hw/giphy.gif">
</p>

The Solar System recreation made with Python using PyOpenGL and PyGame.

**📢 DISCLAIMER: I tried to make axis rotation and translational movement more nearest from reality that I could. Both of them are based on Earth params for the other orbs.
The distance between orbs and them scale was changed for a better visualization, in this way, they don't try to respect reality measurement.**

## Technologies 🐍

This project was maded with [PyOpenGL](http://pyopengl.sourceforge.net/) `v3.1.6`, [PyGame](https://www.pygame.org/) `v2.1.2` and Python `v3.9.7`. Developed in Windows `x64` using wheels who's there isn't in PIP. You can download those wheels [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl) (based on your machine architeture and yours Python version). And then install them manually with PIP.

## Motivation 🎓

This idea was given by a professor in my university. In this moment, here in 2022, I'm start having computer graphics lessons and this subject always interested me. So, given that context I decided to try my best, considering which before this project I hadn't any knowledge about computer graphics.

## Challenges 📐

Below I try to point all of the challenges I fought with to achieve this result, in time order.

1. How create an 3D sphere
2. How use 2D textures in 3D objects
3. How rotate an object on own axis
4. How correctly positionate objects based on XYZ coordinates
5. How to scale an object
6. How to make objects do translational movement

<p align="center">
    <a title="Lucas Vieira, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Circle_cos_sin.gif">
        <img width="256" alt="Circle cos sin" src="https://upload.wikimedia.org/wikipedia/commons/3/3b/Circle_cos_sin.gif">
    </a>
</p>

7. How to change translational movement speed, depending on orb distance from Sun
8. How to render movement line paths of orbs in a performatic way
9. How create lights
10. How create a light spot who's affect the entire orbs
11. How to apply "shadows" to all orbs except the Sun

## Running Locally 🛠️

1. You will need to have the graphics libraries installed as commented before
2. Be sure you has NumPy installed (version used here is `v1.20.3`)
3. Go to project folder and run
```
python .\src\main.py
```
4. The program should open in your screen

## License 💼

MIT