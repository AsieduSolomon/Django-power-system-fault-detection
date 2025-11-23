Power System Fault Detection System
An intelligent web application that uses machine learning to detect electrical faults in three-phase power systems in real-time. The system analyzes voltage and current measurements to identify faults in Phase A, Phase B, Phase C, and ground connections, helping power engineers and technicians quickly diagnose electrical problems.
Show Image
Show Image
Show Image
Show Image
What Does This Project Do?
This application helps detect electrical faults in three-phase power systems by:

Analyzing Real-Time Data: Takes voltage and current readings from all three phases
Detecting Faults: Uses AI to identify if there's a problem in Phase A, B, C, or ground
Visual Reporting: Shows clear, color-coded results indicating healthy or faulty phases
Historical Tracking: Saves all predictions for future reference and analysis

Real-World Application
Power system faults can cause:

Equipment damage and downtime
Safety hazards
Energy losses
Service interruptions

This tool enables quick fault detection, allowing maintenance teams to respond before minor issues become major problems.
Key Features

 Real-Time Fault Detection - Instant analysis of power system measurements
 99% Accuracy - Machine learning model trained on extensive power system data
Beautiful Interface - Modern, responsive design that works on any device
 Clear Visualizations - Color-coded results with fault indicators
 Data Persistence - All predictions saved to database
RESTful API - Separate ML service for scalability
Mobile Friendly - Access from desktop, tablet, or smartphone

 Technology Stack
Frontend & Backend

Django 4.x - Web framework for UI and business logic
HTML5/CSS3 - Modern, animated user interface
JavaScript - Interactive elements and form handling

Machine Learning Service

FastAPI - High-performance API for ML model serving
scikit-learn - Machine learning library
Decision Tree Classifier - Trained fault detection model
StandardScaler - Feature normalization

Data & Storage

SQLite/PostgreSQL - Database for prediction records
Joblib - Model serialization and loading

📋 Prerequisites

Python 3.8 or higher
pip (Python package installer)
Basic understanding of command line/terminal


1. Set Up Python Environment
bash# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
3. Install Dependencies
bash# Install all required packages
pip install django fastapi uvicorn requests joblib scikit-learn numpy
4. Set Up Database
bashcd django_project
python manage.py migrate
5. Start the Application
Open TWO terminal windows:
Terminal 1 - Start ML Service (FastAPI):
bashcd fastapi_project
uvicorn main:app --port 8000 --reload
Terminal 2 - Start Web Application (Django):
bashcd django_project
python manage.py runserver 8080
6. Access the Application
Open your browser and go to:
http://localhost:8080
How to Use
Step 1: Navigate to Prediction Page
Click the "Start Fault Detection" button on the home page.
Step 2: Enter Measurements
Input the voltage (V) and current (A) values for all three phases:

Va, Vb, Vc - Voltage measurements for Phase A, B, and C
Ia, Ib, Ic - Current measurements for Phase A, B, and C

Step 3: Analyze
Click "Analyze & Predict Faults" to get instant results.
Step 4: View Results
The system will display:

✅ Green - No fault detected (Normal operation)
⚠️ Red - Fault detected (Requires attention)

Results show fault status for:

Ground (G)
Phase A
Phase B
Phase C

Example Test Cases
Normal Operation (No Faults)
Va: 230.0 V    Ia: 10.5 A
Vb: 230.0 V    Ib: 10.5 A
Vc: 230.0 V    Ic: 10.5 A

Expected Result: All phases NORMAL ✅
Phase A Ground Fault
Va: 180.0 V    Ia: 25.0 A
Vb: 230.0 V    Ib: 10.5 A
Vc: 230.0 V    Ic: 10.5 A

Expected Result: Phase A FAULT + Ground FAULT ⚠️
Phase B Fault
Va: 230.0 V    Ia: 10.5 A
Vb: 195.0 V    Ib: 18.0 A
Vc: 230.0 V    Ic: 10.5 A

Expected Result: Phase B FAULT ⚠️
📁 Project Structure
power-fault-detection/
│
├── django_project/              # Web application
│   ├── manage.py
│   ├── fault_app/
│   │   ├── models.py           # Database models
│   │   ├── views.py            # Request handlers
│   │   ├── urls.py             # URL routing
│   │   ├── forms.py            # Input forms
│   │   └── templates/
│   │       ├── home.html       # Landing page
│   │       ├── predict.html    # Input form
│   │       └── results.html    # Results display
│   └── settings.py
|
│
└── README.md   



📁
├── ai_module/             # ML service
│   ├── main.py                 # API endpoints
│   ├── decision_tree_model.joblib  # Trained model
│   └── scaler.joblib           # Feature scaler                 # This file
🔌 API Reference
The FastAPI service provides a REST endpoint for predictions:
Endpoint: POST /predict
Request:
json{
    "Va": 230.0,
    "Vb": 230.0,
    "Vc": 230.0,
    "Ia": 10.5,
    "Ib": 10.5,
    "Ic": 10.5
}
Response:
json{
    "G": 0,    // Ground: 0=Normal, 1=Fault
    "A": 0,    // Phase A: 0=Normal, 1=Fault
    "B": 0,    // Phase B: 0=Normal, 1=Fault
    "C": 0     // Phase C: 0=Normal, 1=Fault
}
Test with curl:
bashcurl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"Va":230,"Vb":230,"Vc":230,"Ia":10.5,"Ib":10.5,"Ic":10.5}'
Interactive API Docs:
http://localhost:8000/docs
🤖 Machine Learning Model
Model Details

Algorithm: Decision Tree Classifier
Accuracy: ~99%
Training Data: Historical power system fault data
Input Features: 6 (Va, Vb, Vc, Ia, Ib, Ic)
Output: 4 binary classifications (G, A, B, C)

Fault Types Detected

Ground Fault (G) - Connection to earth/ground
Phase A Fault - Problems in Phase A line
Phase B Fault - Problems in Phase B line
Phase C Fault - Problems in Phase C line

How It Works

Input measurements are collected
Features are normalized using StandardScaler
Decision Tree model predicts fault presence
Results are displayed with visual indicators

🔧 Common Issues & Solutions
Issue: "Connection Refused" Error
Symptom: Django can't connect to FastAPI
Solution:

Make sure FastAPI is running: uvicorn main:app --port 8000
Check if the correct port is used in views.py

Issue: "Template Not Found"
Symptom: Django can't find HTML templates
Solution:

Verify templates are in templates/ folder
Check app is listed in INSTALLED_APPS in settings.py
Ensure APP_DIRS: True in TEMPLATES settings

Issue: "Model File Not Found"
Symptom: FastAPI can't load ML model
Solution:

Ensure decision_tree_model.joblib and scaler.joblib are in the same folder as main.py
Check file names match exactly (case-sensitive)

Issue: Port Already in Use
Solution:
bash# Use different ports
uvicorn main:app --port 8002
python manage.py runserver 8080

# Update FASTAPI_URL in views.py to match
📊 Understanding the Results
Green Results (✅ Normal)

System is operating within normal parameters
No immediate action required
Continue regular monitoring

Red Results (⚠️ Fault)

Abnormal conditions detected
Immediate inspection recommended
Check specific phase indicated
Verify connections and equipment

Multiple Faults
If multiple phases show faults:

Could indicate a multi-phase fault
May suggest upstream issues
Requires comprehensive system check

🎓 Learning Resources
For Developers

Django Documentation
FastAPI Documentation
scikit-learn Guide

For Power Engineers

Understanding three-phase systems
Types of electrical faults
Fault detection methods
Power system protection

🤝 Contributing
Contributions are welcome! Here's how you can help:

Report Bugs - Open an issue describing the problem
Suggest Features - Share ideas for improvements
Submit Pull Requests - Contribute code improvements
Improve Documentation - Help make docs clearer



# Create a feature branch
git checkout -b feature/amazing-feature

# Make changes and commit
git commit -m "Add amazing feature"

# Push to your fork
git push origin feature/amazing-feature

# Open a Pull Request
📜 License
This project is open source and available under the MIT License.
🙏 Acknowledgments

Built with Django and FastAPI frameworks
Machine learning powered by scikit-learn
Inspired by the need for reliable power system monitoring
Thanks to the open-source community

📞 Contact & Support

Issues: GitHub Issues
Discussions: GitHub Discussions
Email: your.email@example.com

🚀 Future Enhancements
Planned features and improvements:

 Real-time data streaming from IoT sensors
 Historical data visualization and analytics
 Email/SMS alerts for critical faults
 Multi-user authentication and roles
 Export reports to PDF
 Integration with SCADA systems
 Mobile app for iOS/Android
 Advanced ML models (Neural Networks, Ensemble methods)

⭐ Show Your Support
If you find this project helpful, please consider:

Starring ⭐ the repository
Sharing with others who might benefit
Contributing improvements
Reporting bugs or suggesting features


Built with ⚡ for reliable power system monitoring
Last Updated: November 2025
