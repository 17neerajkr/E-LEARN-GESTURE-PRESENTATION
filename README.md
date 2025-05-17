✋📽️ E-Learn Gesture Presentation

Welcome to E-Learn Gesture Presentation — an innovative, hands-free, gesture-controlled presentation tool built for inclusive education and intuitive interaction. 🚀

🌟 Inspiration

We began this project as a journey into the world of machine learning and computer vision. Along the way, we discovered the power of landmark detection systems like MediaPipe, and realized we could skip the complexity of heavy ML models. This insight led us to design a lightweight, real-time gesture recognition system — making presentations smarter and more accessible, especially for classrooms and educational institutions. 🎓✨

🧠 What It Does

E-Learn Gesture Presentation empowers users to control presentations through hand gestures — no mouse, keyboard, or clicker required! Here's what it can do:

✅ Navigate slides (Next / Previous)✅ Zoom in / out with gestures✅ Pause / Resume presentations✅ Laser pointer mode with fingertip tracking✅ Draw annotations directly with finger✅ Clear annotations with gesture✅ Switch drawing colors✅ Multitasking gesture support✅ Works in real-time with any standard webcam✅ Supports Indian Sign Language (ISL) integration for accessibility

🛠️ How We Built It

We utilized the following technologies and libraries:

🔹 Python🔹 OpenCV — for camera integration and image processing🔹 cvzone — simplifies hand tracking logic🔹 MediaPipe — for real-time hand landmark detection🔹 FastDTW — for matching gesture sequences efficiently🔹 Tkinter / Web / Android (depending on the interface module)

✨ No heavy ML/DL models involved!All gesture recognition is done using normalized landmark keypoints and custom logic, making it incredibly fast and lightweight.

📱 Cross-Platform Support

E-Learn Gesture Presentation is designed for accessibility and scalability:

🌐 Web Interface — For browser-based classroom use📱 Android App — Hands-free ISL-based sentence forming💻 Desktop Module — Control your PC via sign gestures

🚧 Challenges We Faced

🔸 Building a real-time gesture system without CNNs/LSTMs🔸 Normalizing gestures across various angles, lighting, and hand sizes🔸 Designing a user-friendly UI for diverse age groups and abilities🔸 Ensuring real-world usability with field testing in schools

🏆 Accomplishments

🥇 Built a fully working gesture recognition prototype🏫 Successfully tested in collaboration with a government school📢 Received positive academic and community feedback⚡ Created an offline-capable, low-resource solution for rural areas

📚 What We Learned

We discovered that impactful, inclusive tech doesn't always require complex models or big data. With smart logic, real-time interaction, and community-first design, we created a system that is:

❤️ Lightweight🌍 Inclusive📶 Offline-friendly🧠 Educational

🔮 What's Next

📌 Expand support to ASL and other sign languages📌 Collaborate with educators, NGOs, and accessibility advocates📌 Improve recognition under diverse environments📌 Scale outreach to more schools, NGOs, and institutions

🚀 Getting Started

Want to run this project locally? Follow these steps:

🔁 Clone the Repository

# Create virtual environment

python -m venv venv



# Activate it

# On Windows

venv\Scripts\activate



# On macOS/Linux

source venv/bin/activate



git clone https://github.com/17neerajkr/e-learn-gesture-presentation.git
cd e-learn-gesture-presentation
