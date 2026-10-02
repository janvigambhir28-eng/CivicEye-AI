[README (2).md](https://github.com/user-attachments/files/32969481/README.2.md)
# 🛡️ CivicEye AI: Hyperlocal Problem Solver

CivicEye AI turns a photo of a community issue (a pothole, a broken streetlight, overflowing trash, a water leak) into an instant triage report. Upload an image and the app uses Google's Gemini model to classify the problem, rate how urgent it is, and write a short summary that a repair crew can act on.

## Features

- **Photo upload**: accepts `.jpg`, `.jpeg` and `.png` images.
- **Category detection**: classifies the issue, e.g. Road Damage, Waste Management, Public Lighting, Water Leakage.
- **Urgency score**: rates the issue from 1 (low) to 5 (critical hazard) based on danger to citizens.
- **Actionable summary**: a two-sentence description of what needs fixing, written for dispatch crews.
- **Simple web UI**: built with Streamlit, so it runs in the browser with no front-end code.

## How It Works

1. The user uploads an image through the Streamlit file uploader.
2. The image is opened with Pillow and displayed on the page.
3. The image and a structured prompt are sent to `gemini-2.5-flash` through the `google-genai` SDK.
4. The model's response (category, urgency, summary) is rendered on the page as the "Official AI Dispatch Report".

## Tech Stack

| Component | Purpose |
|-----------|---------|
| [Streamlit](https://streamlit.io) | Web interface |
| [google-genai](https://pypi.org/project/google-genai/) | Gemini API client |
| [Pillow](https://pypi.org/project/pillow/) | Image handling |
| Gemini 2.5 Flash | Image understanding and report generation |

## Getting Started

### Prerequisites

- Python 3.9 or newer
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)

### Installation

```bash
git clone <your-repo-url>
cd <your-repo-folder>
pip install streamlit google-genai pillow
```

Or, with a `requirements.txt`:

```
streamlit
google-genai
pillow
```

```bash
pip install -r requirements.txt
```

### Set Your API Key

The app calls `genai.Client()` with no arguments, so it reads the key from an environment variable. Do not hard-code the key in the source file.

**macOS / Linux**

```bash
export GEMINI_API_KEY="your-api-key-here"
```

**Windows (PowerShell)**

```powershell
$env:GEMINI_API_KEY="your-api-key-here"
```

If you deploy on Streamlit Community Cloud, add `GEMINI_API_KEY` under **App settings → Secrets** instead.

### Run the App

```bash
streamlit run app.py
```

Replace `app.py` with the name of your file. Streamlit opens the app at `http://localhost:8501`.

## Usage

1. Open the app in your browser.
2. Click **Browse files** and choose a photo of the issue.
3. Wait a few seconds while the model analyses the image.
4. Read the generated report under **Official AI Dispatch Report**.

### Example Output

```
**Category**: Road Damage
**Urgency Score**: 4 / 5
**Actionable Summary**: A large pothole spans most of the left lane and poses a risk to two-wheelers and cars. The crew should cone off the area and fill and compact the pothole with asphalt.
```

(Output varies with the image and the model.)

## Project Structure

```
.
├── app.py            # Streamlit app
├── requirements.txt  # Python dependencies
└── README.md
```

## Troubleshooting

| Problem | Likely cause and fix |
|---------|----------------------|
| `Something went wrong: ... API key ...` | `GEMINI_API_KEY` is not set in the terminal where you run Streamlit. Set it and restart the app. |
| `429` / quota errors | The free tier rate limit was reached. Wait a minute and retry. |
| Model not found | The model name may have been retired. Update the `model=` value in the code. |
| Blank or irrelevant report | The image may be unclear. Use a well-lit, close-up photo of the issue. |

## Limitations

- The report is AI-generated and should be reviewed by a person before work is dispatched.
- Urgency scores are an estimate from a single photo and do not account for location, traffic or surrounding context.
- The app does not yet store reports or send them to any authority.

## Future Improvements

- Add GPS or address capture so reports include the location.
- Save reports to a database and show them on a map.
- Let citizens submit reports directly to the local municipal body.
- Support multiple languages.

## License

Add your preferred license here (for example, MIT).
