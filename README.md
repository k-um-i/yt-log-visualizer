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
Required Columns: [Media Type, Comment, Log Date] \
Media Type value must be "Listening Time". \
Comment value must be a Youtube link. \
Log Date format: 2025-05-05 19:39:57

### Planned Features
- View data between specified dates only.
- More visualizations of data.
- Cleaner UI.
- Filters/Searching (e.g. showing only data for specified channel)

## Examples
![image](https://github.com/user-attachments/assets/68054e91-5fed-4585-bae5-a4690ac8df59)
![image](https://github.com/user-attachments/assets/58adc059-4a0d-4dd2-ab06-0113a208e981)

