
import sys
import math

# Grab the volume of the shipment and the volumes of the two types of bottles
shipment_volume, bottle_one_volume, bottle_two_volume = [int(i) for i in sys.stdin.readline().split()]

# If the shipment volume is greater than the volume of a bottle one or if the
# volume of a bottle one is not greater than the volume of a bottle two it is
# impossible to store the oil
if shipment_volume > bottle_one_volume or bottle_one_volume <= bottle_two_volume:
    print("Impossible")
    sys.exit(0)

# Otherwise, the amount of oil that can be stored in a bottle one is equal to
# the amount of oil that can be stored in a bottle two plus the difference
# between the volume of a bottle one and the volume of a bottle two.
bottle_one_amount = (bottle_two_volume + (bottle_one_volume - bottle_two_volume))

# The number of bottles of size one needed to store the oil is equal to the
# shipment volume divided by the amount of oil that can be stored in a bottle
# one. The number of bottles of size two needed to store the oil is equal to
# the remainder of the shipment volume divided by the amount of oil that can be
# stored in a bottle one divided by the volume of a bottle two.
bottle_one_count = math.floor(shipment_volume / bottle_one_amount)
bottle_two_count = math.floor((shipment_volume % bottle_one_amount) / bottle_two_volume)

# Print the number of bottles of size one and the number of bottles of size two
print(str(bottle_one_count) + " " + str(bottle_two_count))
