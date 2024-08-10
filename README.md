# Appointment Scheduler

## Overview

**Appointment Scheduler** is a simple and efficient tool designed for managing appointments. It allows users to schedule, reschedule, and cancel appointments with ease. This project is perfect for businesses or individuals who need to manage appointments for services, meetings, or events.

## Features

- **Schedule Appointments**: Easily create new appointments.
- **Reschedule Appointments**: Modify the time or date of existing appointments.
- **Cancel Appointments**: Remove appointments from the schedule.
- **View Calendar**: See all upcoming appointments in a calendar view.
- **Notification System**: Receive reminders and notifications for upcoming appointments (if integrated).
- **User Authentication**: Secure login for users to manage their appointments.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

-python 3.11
-django 
-MySql Server

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/CodeWithTKoS/smartclinic.git
    ```

2. Navigate to the project directory:

    ```bash
    cd SmartClinic
    ```

3. Install the dependencies:

    ```bash
    pip install django
    pip install mysql connector
    ```

4. Configure the database:
    before that we must delete the pycache and migrations.
    ```bash
    python manage.py make migrations
    python manage.py migrate
    ```
    These are the django ORM commands which help us to make tables in a normallised way

5. Start the development server:

    ```bash
    manage.py runserver
    ```

6. Open your browser and navigate to `http://localhost:8000` to view the application.

## Usage

### Scheduling an Appointment

Proccedures run every 5 mins to check if a doctor is waiting or not.

### Rescheduling an Appointment

Checks if any doctor is idol

### Cancelling an Appointment

1. Navigate to your existing appointments.
2. Select the appointment you want to cancel.
3. Click the "Delete" button.

### Environment Variables

- `PORT`: The port the server will run on 8000.
- `MySQL Database`: DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'smartclinic',  
        'USER':'root',  
        'PASSWORD':'1234',  
        'HOST':'localhost',  
        'PORT':'3306'  
    }  
  }

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

### Bug Reports & Feature Requests

Please use the [issue tracker](https://github.com/CodeWithTKoS/smartclinic.git/issues) to report bugs or request features.

## Acknowledgements

- Thanks to the contributors who helped in building this project.
- Special mention to the community for their continuous support.

## Contact

For any questions, feel free to reach out:

- Email: debjitdas50@gmail.com
- GitHub: [@CodeWithTKoS](https://github.com/CodeWithTKoS)

---
