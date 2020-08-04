import board
import busio as io
import adafruit_mlx90614
i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)

print("Ambient Temp: ", mlx.ambient_temperature)
print("Object Temp: ", mlx.object_temperature)