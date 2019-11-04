from __future__ import print_function

import time

from dronekit import connect, VehicleMode, LocationGlobalRelative


vehicle = connect("udp:127.0.0.1:14551", wait_ready=True)

def arm_and_takeoff(aTargetAltitude):
    
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto
    #  (otherwise the command after Vehicle.simple_takeoff will execute
    #   immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)


arm_and_takeoff(20)

vehicle.airspeed = 3

print("ilk wp gidiliyor")
point1 = LocationGlobalRelative(40.9863167, 29.0548226, 20)
vehicle.simple_goto(point1)

time.sleep(0.2)
point1 = LocationGlobalRelative(40.9863167, 29.0548226, 20)
vehicle.simple_goto(point1)
time.sleep(25)


print("ikinci wp gidiliyor")
point2 = LocationGlobalRelative(40.9865010, 29.0548870, 20)
vehicle.simple_goto(point2)
time.sleep(0.2)
point2 = LocationGlobalRelative(40.9865010, 29.0548870, 20)
vehicle.simple_goto(point2)
time.sleep(25)


print("geri donuluyor")
point3= LocationGlobalRelative(40.9864463, 29.0545973, 20)
vehicle.simple_goto(point3)
time.sleep(0.2)
point3= LocationGlobalRelative(40.9864463, 29.0545973, 20)
vehicle.simple_goto(point3)
time.sleep(25)

vehicle.mode = VehicleMode("LAND")
vehicle.mode = VehicleMode("LAND")
vehicle.close()

