# Stat & Food Tracker

**A simple terminal-based stat tracker and food inventory logger built in Python.**

---

## Table of Contents
1. [Description](#description)  
2. [Demo Screenshot](#demo-screenshot)  
3. [Prerequisites](#prerequisites)  
4. [Installation](#installation)  
5. [Usage](#usage)  
   - [Stat Tracker](#stat-tracker)  
   - 7. [Future Features](FUTURE_FEATURES.md)
  
6. [Data Schema (Sample JSON)](#data-schema-sample-json)  
7. [Future Features](#future-features)  
8. [Contributing](#contributing)  
9. [License](#license)

---

## Description
This project helps you track your weight, BMI, body-fat, body-water, muscle mass, and daily calorie intake over time. It also lets you store and manage your food inventory, making it easier to log meals and macros. Ideal for anyone building healthy habits—whether you’re bulking, cutting, or maintaining.

---

## Demo Screenshot
> Below is a placeholder screenshot of the Stat Tracker main menu. Replace `screenshot.png` with your actual image file in the root of this repo.

![Stat Tracker Menu (Placeholder)](screenshot.png)

---

## Prerequisites
- Python 3.7+  
- (Optional) A virtual environment tool (`venv`, `conda`, etc.)

---

## Installation

1. **Clone this repository**  
   ```bash
   git clone git@github.com:rdent8/stat-and-food-tracker-.git
   cd stat-and-food-tracker-
   ```

---

## Usage
*(Your existing Usage section goes here, if not already above)*

---

## Data Schema (Sample JSON)
Below is a sample of what your JSON files look like:

```json
[
    {
        "timestamp": "2025-06-03T14:22:00",
        "date": "2025-06-03",
        "weight": 180.5,
        "bmi": 24.8,
        "body_fat": 18.2,
        "body_water": 55.1,
        "muscle_mass": 40.3,
        "kcal": 2200
    },
    {
        "timestamp": "2025-06-04T07:15:30",
        "date": "2025-06-04",
        "weight": 180.0,
        "bmi": 24.7,
        "body_fat": 18.0,
        "body_water": 55.3,
        "muscle_mass": 40.5,
        "kcal": 2100
    }
]
```

---

## Future Features
See [FUTURE_FEATURES.md](FUTURE_FEATURES.md) for the full roadmap of planned enhancements, including:
1. Export/Import to CSV  
2. Interactive Charts & Visualizations  
3. User Profiles & Authentication  
4. TDEE Estimation & Macro Recommendations  
5. Nutrition API Integration  
6. Responsive Web GUI  
7. Unit Tests & CI/CD  
8. …and more

---

## Contributing
*(Guidelines for contributing to this project)*

## License
*(Your license information here)*
