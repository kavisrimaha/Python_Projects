# Server Deployment Guide

This Django Todo application can be deployed in several ways. Follow the instructions below based on your deployment target.

## Prerequisites

1. Python 3.8 or higher
2. All dependencies installed (from `requirements.txt`)
3. Database migrations applied

## Quick Start - Local Development Server

### Windows
```bash
run_server.bat
```

### Linux/Mac
```bash
chmod +x run_server.sh
./run_server.sh
```

Or manually:
```bash
python manage.py runserver 0.0.0.0:8000
```

The server will be available at: `http://localhost:8000`

---

## Production Server Deployment

### Option 1: Using Gunicorn (Recommended for Traditional Servers)

Gunicorn is already included in your `requirements.txt`. 

#### Windows
```bash
run_production.bat
```

#### Linux/Mac
```bash
chmod +x run_production.sh
./run_production.sh
```

Or manually:
```bash
# Collect static files
python manage.py collectstatic --noinput

# Run with Gunicorn
gunicorn crudapp.wsgi:application --bind 0.0.0.0:8000 --workers 4
```

**Gunicorn Options:**
- `--bind 0.0.0.0:8000` - Binds to all network interfaces on port 8000
- `--workers 4` - Number of worker processes (adjust based on CPU cores)
- Add `--daemon` to run in background
- Add `--access-logfile access.log --error-logfile error.log` for logging

### Option 2: Deploy to Vercel (Serverless)

You already have `vercel.json` configured! 

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Deploy:
   ```bash
   vercel
   ```

3. For production deployment:
   ```bash
   vercel --prod
   ```

**Note:** SQLite database won't persist on Vercel. Consider using:
- PostgreSQL (via Vercel Postgres)
- Or another cloud database service

### Option 3: Using Systemd (Linux Server)

Create a systemd service file `/etc/systemd/system/todoapp.service`:

```ini
[Unit]
Description=Gunicorn instance to serve Django Todo App
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/Python_Projects
Environment="PATH=/path/to/Python_Projects/venv/bin"
ExecStart=/path/to/Python_Projects/venv/bin/gunicorn --workers 4 --bind unix:/path/to/Python_Projects/todoapp.sock crudapp.wsgi:application

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl start todoapp
sudo systemctl enable todoapp
```

---

## Important Steps Before Production

1. **Set Environment Variables:**
   - Change `SECRET_KEY` in `settings.py` or use environment variable
   - Set `DEBUG = False` (already done)

2. **Collect Static Files:**
   ```bash
   python manage.py collectstatic --noinput
   ```

3. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

5. **Security Settings:**
   - Update `ALLOWED_HOSTS` in `settings.py` with your domain
   - Consider using environment variables for sensitive data
   - Use HTTPS in production

6. **Database:**
   - SQLite is fine for development
   - For production, consider PostgreSQL, MySQL, or another production database

---

## Firewall Configuration

Make sure port 8000 (or your chosen port) is open:

### Windows Firewall
```powershell
New-NetFirewallRule -DisplayName "Django App" -Direction Inbound -LocalPort 8000 -Protocol TCP -Action Allow
```

### Linux (UFW)
```bash
sudo ufw allow 8000/tcp
```

---

## Troubleshooting

- **Port already in use:** Change the port number in the command (e.g., `:8001`)
- **Static files not loading:** Run `python manage.py collectstatic`
- **Database errors:** Run `python manage.py migrate`
- **Module not found:** Ensure virtual environment is activated and dependencies are installed
