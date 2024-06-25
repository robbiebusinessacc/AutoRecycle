import RPi.GPIO as GPIO
import time
import os
from PIL import Image as PILImage
from fastai.vision import *
from pathlib import Path
import serial

# Set up GPIO pins for the ultrasonic sensor
GPIO.setmode(GPIO.BCM)
TRIG = 6  # TRIG pin
ECHO = 5  # ECHO pin
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Set up the serial communication with Arduino
arduino = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)  # Give some time for the serial connection to initialize

# Move servo to 90 degrees initially
arduino.write(b'90\n')
print("Servo initialized to: 90 degrees (Neutral Position)")
time.sleep(2)  # Allow time for the servo to move

def measure_distance():
    # Ensure the trigger pin is set to low initially
    GPIO.output(TRIG, False)
    time.sleep(2)  # Allow sensor to settle

    # Send a 10us pulse to the trigger pin
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    print("Pulse sent")

    pulse_start = time.time()

    # Wait for the echo pin to go high
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        if time.time() - pulse_start > 1:
            print("Error: Echo pin didn't go high")
            return -1
    print("Echo pin went high")

    pulse_end = time.time()

    # Wait for the echo pin to go low
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        if time.time() - pulse_start > 1:  # Timeout after 1 second
            print("Error: Echo pin didn't go low")
            return -1
    print("Echo pin went low")

    # Calculate the pulse duration
    pulse_duration = pulse_end - pulse_start
    print(f"Pulse duration: {pulse_duration} seconds")

    # Calculate the distance
    distance = pulse_duration * 17150  # Speed of sound in air (34300 cm/s) divided by 2
    print(f"Calculated distance: {distance} cm")

    return round(distance, 2)

def take_picture(filename):
    os.system(f"libcamera-still -o {filename}")

def crop_board_area(image_path, output_path):
    image = PILImage.open(image_path)
    width, height = image.size
    
    # Define crop parameters based on the scaled dimensions
    left = 1051
    top = 351
    right = 2648
    bottom = 1755

    # Make it a square based on the smallest dimension
    crop_width = right - left
    crop_height = bottom - top
    crop_size = min(crop_width, crop_height)

    # Adjust right and bottom to make the crop area square
    right = left + crop_size
    bottom = top + crop_size

    # Crop the area
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(output_path)

def predict_image(image_path):
    # Define the directory and the model file
    model_dir = Path(".")  # The directory containing the model file
    model_file = model_dir / "export.pkl"

    # Print the paths to ensure correctness
    print(f"Model file: {model_file}")

    # Load the Fastai learner
    try:
        learn = load_learner(model_dir, model_file.name)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

    # Perform prediction using the Fastai learner
    try:
        img_fastai = open_image(image_path)
        pred_class, pred_idx, outputs = learn.predict(img_fastai)
        pred_label = str(pred_class)
        print("Prediction performed successfully.")
        return pred_label
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None

def map_to_recyclable(prediction):
    recyclable_labels = ['Metal', 'Plastic', 'Glass', 'Paper', 'Cardboard']
    return 'Recyclable' if prediction in recyclable_labels else 'Non-Recyclable'

try:
    while True:
        print("Starting measurement...")
        dist = measure_distance()
        if dist == -1:
            print("Measurement error. Check the sensor connections and try again.")
        elif dist <= 30:
            print(f"Measured Distance = {dist} cm - Object detected within 30 cm")
            # Take a picture and save it to pic.jpg
            take_picture("pic.jpg")
            print("Picture taken and saved to pic.jpg")
            # Crop the board area and save it to cropped_pic.jpg
            crop_board_area("pic.jpg", "cropped_pic.jpg")
            print("Cropped picture saved to cropped_pic.jpg")
            # Perform prediction on the cropped image
            pred_label = predict_image("cropped_pic.jpg")
            if pred_label:
                mapped_pred = map_to_recyclable(pred_label)
                print(f'Predicted Class: {pred_label}')
                print(f'Mapped Prediction: {mapped_pred}')
                # Control servo motor based on prediction
                if mapped_pred == 'Recyclable':
                    arduino.write(b'1\n')
                    print("Servo moved to: 1 degree (Recyclable)")
                else:
                    arduino.write(b'180\n')
                    print("Servo moved to: 180 degrees (Non-Recyclable)")
                time.sleep(2)
                arduino.write(b'90\n')
                print("Servo moved to: 90 degrees (Neutral Position)")
            else:
                print("Prediction could not be made due to previous errors.")
        else:
            print(f"Measured Distance = {dist} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
    arduino.close()
