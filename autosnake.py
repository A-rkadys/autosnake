#!/bin/python

def main():
    import pygame as py
    from gameloop import gameloop
    py.init()
    gameloop()
    py.quit()

if __name__ == "__main__":
    main()

