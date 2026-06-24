

# 📌 Project Name

**YouTube API Basics Extractor**

---

# 📖 Description

A beginner-friendly YouTube Data API project that extracts video and channel information using the YouTube API.

This project demonstrates how to connect with an API, extract raw data, understand JSON responses, parse YouTube URLs to get video IDs, and save extracted data for further analysis.

---

# 🎯 Project Goal

Learn the basics of:

* YouTube Data API
* API authentication using API key
* Extracting video and channel data
* Understanding JSON data structure
* URL parsing
* Building the Extract phase of an ETL pipeline

---

# 🚀 Features

✅ Extract single YouTube video information

✅ Extract YouTube channel information

✅ Convert YouTube URL → Video ID

✅ Fetch data using `googleapiclient.discovery`

✅ Save raw API response as JSON files

---

# 🔄 Project Flow

```
YouTube URL
      ↓
Extract Video ID
      ↓
Call YouTube API
      ↓
Receive JSON Response
      ↓
Save Raw Data
      ↓
video.json / channel.json
```

---

# 📂 Output Files

### video.json

Contains:

* Video title
* Description
* Published date
* Views
* Likes
* Channel ID

### channel.json

Contains:

* Channel name
* Subscribers
* Total videos
* Channel description

---

# 🛠️ Technologies Used

* Python
* YouTube Data API v3
* google-api-python-client
* python-dotenv
* JSON

---

# 📁 Project Structure

```
youtube-api-extractor/
│
├── main.py
├── extract.py
├── config.py
├── utils.py
├── .env.example
│
└── output/
    ├── video.json
    └── channel.json
```

---

# ▶️ How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
YOUTUBE_API_KEY=your_api_key
```

Run:

```bash
python main.py
```

---

# 🧠 Learning Outcome

This project builds the foundation for bigger data engineering projects:

* ETL pipelines
* Data transformation
* Data warehouses
* Analytics dashboards

---

For GitHub repository name, use something like:

```
youtube-api-extractor
```

or

```
youtube-etl-pipeline-beginner
```

This will look like a real data engineering beginner project.
