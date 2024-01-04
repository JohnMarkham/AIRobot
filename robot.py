import os
import time
import io
import controller
from openai import OpenAI
import base64
import json
from picamera import PiCamera


class Robot():
    context = """Context: You will control a robot by issuing simple instructions based on images that you are fed, and a mission you are given.
    Your instructions are in the set (forward, backward, stop, left, right, found).
    Your response is limited to values in that instruction set, you cannot respond with any other word."""
    limits = """ When you can't see the object you are looking for you need to turn in a consistent direction until you find the object.
    so for example, if you decide to turn left, then you should continue to turn left until you are given an image of the object that you are seeking."""
    instruction_timer = 0.15

    def __init__(self, objective: str):
        self.encoded_image = ""
        self.complete = False
        self.objective = objective
        self.mission = Robot.context + self.objective + Robot.limits
        # Set up an initial conversation with ChatGPT (Change the information below to match your OpenAI account information, (organization, api_key, etc).
        self.client= OpenAI()
        self.organization = "organization"
        self.org = os.environ.get(self.organization)
        self.thekey = "OPENAI_API_KEY"
        self.openkey = os.environ.get(self.thekey)
        self.client = OpenAI()


    def start(self):
        self.pic_count = 0
        while not self.complete:
            self.pic_count += 1
            instruction = self.take_picture()
            self.execute(instruction)

    def execute(self, instruction: str):
        """
        User getattr on the parameter instruction to execute method.

        """
        getattr(self,instruction)()
        time.sleep(Robot.instruction_timer)
        self.stop()

    #Define Functions:
    def forward(self):
        controller.motor_forward()

    def backward(self):
        controller.motor_backward()

    def stop(self):
        controller.motor_stop()

    def left(self):
        controller.motor_spin_left()

    def right(self):
        controller.motor_spin_right()

    def found(self):
        self.complete = True

    def take_picture(self) -> str:
        """

        """
        self.encoded_image = self.snap()
        response = self.client.chat.completions.create(
            #If you receive an error message make sure you have access to this model: https://help.openai.com/en/articles/7102672-how-can-i-access-gpt-4 
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": self.mission},
                        {
                            "type": "image/jpeg",
                            "image": self.encoded_image
                        },
                    ],
                }
            ],
            max_tokens=300,
        )
        r=response.model_dump()
        instruction = r['choices'][0]['message']['content']
        print(f"The instruction from ChatGPT is {instruction}")
        return instruction

    def snap(self):
        my_stream = io.BytesIO()
        with PiCamera() as camera:
            camera.rotation = 180
            camera.start_preview()
            camera.capture(my_stream,'jpeg')
        my_stream.seek(0)
        file_path = '/home/pi/Pictures/captured_image' + str(self.pic_count) + '.jpg'
        with open(file_path,'wb') as file:
            image_data = my_stream.read()
            file.write(image_data)
        encoded_image = base64.b64encode(image_data).decode("utf-8")
        return encoded_image



if __name__ == "__main__":
    try:
        x = Robot("Find and approach the blue gym ball when it appears. When you complete this mission, issue the command 'found'")
        x.start()
        controller.GPIO.cleanup()
    except KeyboardInterrupt:
        controller.GPIO.cleanup()

