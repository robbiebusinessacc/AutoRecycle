# AutoRecycle: Building an AI-Driven Automated Recycling Bin Using Vision Transformers

## Repository Structure
- **Arduino/**: Contains the Arduino code for controlling the servo motor and proximity sensor.
- **RaspberryPi/**: Contains the Python code for image processing and communication with the Arduino.
- **Notebooks/**: Contains the Jupyter notebook for model training and evaluation.
- **DataSplit/**: Contains scripts for separating data into training and testing sets.
- **Images/**: Contains images of the prototype and setup.
- **LICENSE**: Contains the license for the project.
- **README.md**: Project overview and setup instructions.


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
The data used in this project is the RealWaste dataset. 

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
We would like to thank the creators of the RealWaste dataset for their invaluable resources.

---

For more details, please explore the respective directories.
