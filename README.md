# Miles Delivery Chatbot

A last-mile delivery chatbot built with Python, Streamlit, and Groq API. This project includes three versions of the chatbot with different personalities for research evaluation purposes.

## Overview

Miles is a delivery assistant chatbot that helps customers reschedule parcel deliveries. The project explores how different chatbot behaviors affect user experience.

### Three Versions

| Version | Description | Behavior |
|---------|-------------|----------|
| **Good Miles** | Helpful and efficient | Follows the delivery script, offers relevant alternatives, confirms bookings |
| **Dumb Miles** | Unhelpful and repetitive | Doesn't listen, keeps suggesting home delivery even when customer says they're not home |
| **Curious Miles** | Nosy and personal | Asks personal questions about work, living situation, what they ordered |

## Live Demo Links

- Good Miles: [[click here!]](https://chatbot-z9q4sbned6qxid7q6ivavb.streamlit.app/)
- Dumb Miles: [[click here!]](https://chatbot-hw2nakyrqwbyxrr7mjdzhz.streamlit.app/)
- Curious Miles: [[click here!]](https://chatbot-jiqb9xbauqsiyptfulzecm.streamlit.app/)

## Installation

### Requirements
- Python 3.8+
- Groq API key (free at https://console.groq.com)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/miles-chatbot.git
cd miles-chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your API key:

Create a `.streamlit/secrets.toml` file:
```toml
GROQ_API_KEY = "your-api-key-here"
```

## How to Run

### Run locally:
```bash
# Good Miles
streamlit run miles_app.py

# Dumb Miles
streamlit run miles_dumb.py

# Curious Miles
streamlit run miles_curious.py
```

The app will open in your browser at `http://localhost:8501`

## Project Structure

```
miles-chatbot/
├── miles_app.py        # Good Miles - helpful version
├── miles_dumb.py       # Dumb Miles - unhelpful version
├── miles_curious.py    # Curious Miles - nosy version
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Conversation Flow (Good Miles)

1. Miles greets customer and mentions their delivery
2. Offers early delivery option
3. If YES → Offers home delivery (14:00-17:00)
4. If NO → Asks for preferences and suggests alternatives:
   - Home: 14:00-18:00
   - Workplace: 15:00-21:00
   - Parcel locker: 400m away, 24/7 access
   - Supermarket pickup: 500m away, 07:00-22:00
5. Confirms booking and offers reminder
6. Ends conversation politely

## Delivery Options

| Location | Time Availability |
|----------|------------------|
| Home | 14:00 - 18:00 |
| Workplace | 15:00 - 21:00 |
| Parcel Locker | After 15:00, 24/7 pickup |
| Supermarket | After 15:00, open 07:00-22:00 |

## Technologies Used

- **Python** - Programming language
- **Streamlit** - Web interface
- **Groq API** - LLM provider (using llama-3.1-8b-instant)
- **LLM** - Large Language Model for natural conversation

## Author

Tassneem Altaf  
Data Science & AI Student, BUAS

## Acknowledgments

- Breda University of Applied Sciences (BUAS)
- Groq for free API access