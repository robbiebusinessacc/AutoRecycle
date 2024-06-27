# AutoRecycle: Building an AI-Driven Automated Recycling Bin Using Vision Transformers

## Introduction
Efficient recycling is essential for sustainable waste management. This project aims to develop an intelligent recycling machine that uses machine learning for automated waste sorting. Leveraging the RealWaste dataset, we train a Vision Transformer (ViT) using the Self-Supervised DINO method to accurately identify and sort various waste types.

## Repository Structure
- **Arduino/**: Contains the Arduino code for controlling the servo motor and proximity sensor.
- **RaspberryPi/**: Contains the Python code for image processing and communication with the Arduino.
- **Notebooks/**: Contains the Jupyter notebook for model training and evaluation.
- **DataSplit/**: Contains scripts for separating data into training and testing sets.
- **Images/**: Contains images of the prototype and setup.
- **LICENSE**: Contains the license for the project.
- **README.md**: Project overview and setup instructions.

## Hardware Setup
- **Camera Module**: High-resolution camera for capturing waste images.
- **Servo Motor**: Mechanically flips a board to direct items into recyclable and non-recyclable categories.
- **Ultrasonic Proximity Sensor**: Detects the presence of objects and triggers the sorting mechanism.
- **Arduino Board**: Processes sensor data and controls the servo motor.
- **Raspberry Pi**: Runs image processing algorithms and communicates with the Arduino.

## Software Setup

### Prerequisites
- Arduino IDE
- Python 3.8+
- Jupyter Notebook
- Fastai
- PyTorch
- TIMM (PyTorch Image Models)
- OpenCV
- Necessary Python libraries: numpy, pandas, matplotlib

### Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/AutoRecycle.git
    cd AutoRecycle
    ```

2. **Set up the Arduino**:
    - Open `Arduino/arduino_code.ino` in the Arduino IDE.
    - Connect your Arduino board and upload the code.

3. **Set up the Raspberry Pi**:
    - Install necessary Python libraries:
      ```sh
      pip install -r RaspberryPi/requirements.txt
      ```
    - Run the Raspberry Pi code:
      ```sh
      python RaspberryPi/raspberry_pi_code.py
      ```

4. **Run the Jupyter Notebook**:
    - Navigate to the `Notebooks` directory and open `AutoRecycle_Model_Training.ipynb` in Jupyter Notebook.
    - Execute the cells to train and evaluate the model.

## Data
The data used in this project is the RealWaste dataset. It is split into raw and processed data for training and evaluation.

## Results
The trained Vision Transformer model achieved a validation accuracy of **95.16%** for detailed waste classification and **98.74%** for binary recyclability classification. These results demonstrate the model's effectiveness in automated waste sorting.

## Discussion and Conclusion
This project demonstrates a significant improvement in recycling efficiency using machine learning. The prototype can be further developed for scalability and integration into real-world recycling systems.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
We would like to thank the creators of the RealWaste dataset for their invaluable resources.

---

For more details, please explore the respective directories.
