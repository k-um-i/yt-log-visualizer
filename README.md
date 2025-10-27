# yt-log-visualizer
Python app built with [streamlit](https://github.com/streamlit/streamlit) that provides an overview of Youtube data logged in a .csv file.

## Usage Instructions
1. Clone the repo
```
git clone https://github.com/k-um-i/yt-log-visualizer.git
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Start the streamlit application
```
streamlit run app.py
```
4. Open the app at ``` localhost:8501 ``` by default and follow the instructions.

### Things to note
- The first run when loading your .csv file may take a while to run depending on how many Youtube videos you have logged, since it requests each videos metadata. On subsequent runs this process should be faster thanks to the metadata caching implementation.
- Only log entries that have a Youtube link inside the 'Comment' column will be parsed.

### CSV File format
Required Columns: [Comment, Amount Logged, Log Date] \
Comment value must be a Youtube link. \
Amount Logged value must be an int representing minutes. \
Log Date format: 2025-05-05 19:39:57

## Examples
<img width="2506" height="973" alt="image" src="https://github.com/user-attachments/assets/326b3133-7b46-4aca-9c80-d2451f9075d4" />
<img width="2209" height="560" alt="image" src="https://github.com/user-attachments/assets/d9d9eea6-8fcb-4181-b4e0-92a6c391735b" />
<img width="2484" height="753" alt="image" src="https://github.com/user-attachments/assets/43f6e5c2-1b7c-44cf-9774-a01bf6e3dd2b" />
