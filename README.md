# Task Manager - Modern Todo List Application

A beautiful, modern todo list application built with Django and Bootstrap. Features a clean, professional UI with pastel colors, smooth animations, and a responsive design.

## Features

- ✨ Modern, clean UI design
- 🎨 Beautiful pastel color theme
- 📱 Fully responsive design
- ✅ Task management (Create, Read, Update, Delete)
- 🔐 User authentication (Login, Signup, Logout)
- 📊 Task statistics dashboard
- 🎯 Status tracking (Pending/Completed)
- 💫 Smooth animations and transitions

## Tech Stack

- **Backend**: Django 5.2.7
- **Frontend**: Bootstrap 5.3.2, Bootstrap Icons
- **Database**: SQLite (development)
- **Deployment**: Vercel (serverless)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Python_Projects
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

## Deployment

### Deploy to Vercel

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy:
```bash
vercel
```

3. Set environment variables in Vercel dashboard:
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: Set to `False` for production

4. For production deployment:
```bash
vercel --prod
```

## Project Structure

```
Python_Projects/
├── api/
│   └── index.py          # Vercel serverless function
├── crudapp/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todoapp/              # Main application
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── templates/
│   └── static/
├── manage.py
├── requirements.txt
└── vercel.json           # Vercel configuration
```

## Environment Variables

For production, set these environment variables:

- `SECRET_KEY`: Django secret key (required)
- `DEBUG`: Set to `False` for production

## License

MIT License

## Author

Built with ❤️ using Django and Bootstrap
