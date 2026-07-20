import sys

print("Python:", sys.version)
print("Executável:", sys.executable)

try:
    import pygame
    print("Pygame:", pygame.__version__)
except Exception as e:
    print("Erro:", e)