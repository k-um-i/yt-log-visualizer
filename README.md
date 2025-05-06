# yt-log-visualizer
Python script for generating an overview.html file that provides an overview of Youtube data logged in a .csv file.

## Usage Instructions
1. Clone the repo
```
git clone https://github.com/k-um-i/yt-log-visualizer.git
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Run the script with your .csv file path as the argument
```
python main.py <.csv filepath>
```

### Things to note
- The script may take a while to run depending on how many Youtube videos you have logged, since it requests each videos metadata.
- Only log entries that are 'Listening Time' and have a Youtube link inside the 'Comment' column will be parsed.
- The visuals and overall execution is still horrendous, I'll probably update it at somepoint.

### CSV File format
Required Columns: [Media Type, Comment, Amount Logged, Log Date] \
Media Type value must be "Listening Time". \
Comment value must be a Youtube link. \
Amount Logged value must be an int representing minutes. \
Log Date format: 2025-05-05 19:39:57

### Planned Features
- View data between specified dates only.
- More visualizations of data.
- Cleaner UI.
- Filters/Searching (e.g. showing only data for specified channel)

## Examples
![image](https://github.com/user-attachments/assets/53bc27b0-a556-442d-ab87-c346562153f1)
![image](https://github.com/user-attachments/assets/2c41da5d-624b-485e-9adf-cc2eb24c48e9)
![image](https://github.com/user-attachments/assets/38c00024-3616-46ec-9e0d-3e9bf3e2b8e6)
![image](https://github.com/user-attachments/assets/af9b399a-44f6-4adb-ad19-c02edc0a58bc)
