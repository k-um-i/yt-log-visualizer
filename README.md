# yt-log-visualizer
Python script for generating an overview.html file that provides an overview of Youtube data logged with the アリス -discord bot.

## Usage Instructions
1. Clone the repo
```
git clone https://github.com/k-um-i/yt-log-visualizer.git
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Inside the main.py file, change the string inside 'parse_log()' to point to your exported .csv file.
4. Run the script
```
python main.py
```

### Things to note
1. The script may take a while to run depending on how many Youtube videos you have logged, since it requests each videos metadata.
2. Only log entries that are 'Listening Time' and have a Youtube link inside the 'Comment' column will be parsed.
3. The visuals and overall execution is still horrendous, I'll probably update it at somepoint.

## Examples
![image](https://github.com/user-attachments/assets/7eef8eff-689f-4a4f-a86c-6fd11ddf75bc)
![image](https://github.com/user-attachments/assets/d43f8e57-1e0e-4782-b667-5c2a4231fba9)
