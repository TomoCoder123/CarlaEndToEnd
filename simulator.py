import carla
import random
client = carla.Client('localhost')
world = client.get_world()
print(world)
print(client.get_available_maps())

client.load_world('Town12')

print("Switching")

# Retrieve the spectator object
spectator = world.get_spectator()

# Get the location and rotation of the spectator through its transform
transform = spectator.get_transform()

location = transform.location
rotation = transform.rotation

# Set the spectator with an empty transform
spectator.set_transform(carla.Transform())
# This will set the spectator at the origin of the map, with 0 degrees
# pitch, yaw and roll - a good way to orient yourself in the map
