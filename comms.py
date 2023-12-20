import robot
import paho.mqtt.client as mqtt
Robot=None

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc) )
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    global Robot
    if Robot is not None:
        print("Robot created.")
    else:
        print(f"Received message: {msg.payload.decode()} {msg.retain}")
        print(f"create Robot with missiong {msg.payload.decode()}.")
        Robot = robot.Robot(msg.payload.decode())
        Robot.start()


if __name__ == "__main__":
    try:
        client = mqtt.Client(client_id ="robot", protocol=mqtt.MQTTv311, clean_session=True)
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("192.168.0.222", 1883, 3)
        client.loop_forever()
        print("end of script")
        robot.controller.GPIO.cleanup()
    except KeyboardInterrupt:
        robot.controller.GPIO.cleanup()
