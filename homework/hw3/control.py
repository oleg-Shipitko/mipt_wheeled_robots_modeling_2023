#!/usr/bin/env python

import asyncio
import websockets
import json

from pid import PID

# TODO: Initialize the pid variable.
steering_pid = PID(0.053, 0.0, 0.0)

# Checks if the SocketIO event has JSON data.
# If there is data the JSON object in string format will be returned,
# else the empty string "" will be returned.
def getData(message):
	try:
		start = message.find("[")
		end = message.rfind("]")
		return message[start:end+1]
	except:
		return ""

async def handleTelemetry(websocket, msgJson):
    cte = float(msgJson[1]["cte"])
    speed = float(msgJson[1]["speed"])
    angle = float(msgJson[1]["steering_angle"])

    print("CTE: ", cte, ", speed: ", speed, ", angle: ", angle)

    # TODO: Update the PID controller with the current error
    # 

    # TODO: Calculate steering value here, remember the steering value is [-1, 1].
    #
    #
    
    response = {}

    response["steering_angle"] = steer_value

    # TODO: Play around with throttle value
    response["throttle"] = 0.3

    msg = "42[\"steer\"," + json.dumps(response) + "]"

    await websocket.send(msg)

async def echo(websocket, path):
    try:
        while True:
            message = await websocket.recv()
            if len(message) < 3 or message[0] != '4' or message[1] != '2':
                return

            s = getData(message)
            msgJson = json.loads(s)

            event = msgJson[0]
            if event == "telemetry":
                await handleTelemetry(websocket, msgJson)
            else:
                msg = "42[\"manual\",{}]"
                await websocket.send(msg)
    except websockets.exceptions.ConnectionClosed:
        print("Connection with client closed")


def main():
	start_server = websockets.serve(echo, "localhost", 4567)

	asyncio.get_event_loop().run_until_complete(start_server)
	asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
	main()
