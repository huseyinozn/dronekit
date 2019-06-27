import dronekit_sitl
import time
sitl = dronekit_sitl.start_default()
connecting_string = sitl.connection_string()


from dronekit import connect, VehicleMode

vehicle = connect('tcp:127.0.0.1:5760',wait_ready = True)

def arm_and_takeoff(target_altitude):
	
	print("IHA arm edilebiliyor mu diye kontrol ediliyor")
	while not vehicle.is_armable:
		print("arm edilebilmeyi bekliyor")
		time.sleep(1)
	
	print("motorlar arm ediliyor")
	vehicle.mode = VehicleMode("GUIDED")
	vehicle.mode = VehicleMode("GUIDED")
	vehicle.armed = True
	
	while not vehicle.armed:
		print("arm edilmeyi bekliyor")
		time.sleep(1)


	print("IHA kalkisa geciyor")
	vehicle.simple_takeoff(target_altitude)
	
	while True :
		print ("altitude",vehicle.location.global_relative_frame.alt)
		if vehicle.location.global_relative_frame.alt > 0.95*target_altitude:
			print("hedef yukseklige varildi")
			break
		time.sleep(1)
arm_and_takeoff(10)	

vehicle.close

sitl.stop()
