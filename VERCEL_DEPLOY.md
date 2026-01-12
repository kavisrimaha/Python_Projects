# Vercel Deployment Guide

## Quick Deploy Steps

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. **Go to [Vercel Dashboard](https://vercel.com/dashboard)**
   - Sign in with GitHub
   - Click "Add New Project"

2. **Import Your Repository**
   - Select your GitHub repository: `kavisrimaha/Python_Projects`
   - Click "Import"

3. **Configure Project Settings**
   - **Framework Preset**: Other
   - **Root Directory**: `./` (leave as default)
   - **Build Command**: Leave empty (Vercel will auto-detect)
   - **Output Directory**: Leave empty

4. **Set Environment Variables**
   Click "Environment Variables" and add:
   - `SECRET_KEY`: Your Django secret key (generate a new one for production)
   - `DEBUG`: `False`

5. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete

### Option 2: Deploy via Vercel CLI

1. **Install Vercel CLI** (if not already installed):
```bash
npm install -g vercel
```

2. **Login to Vercel**:
```bash
vercel login
```

3. **Deploy**:
```bash
vercel
```

4. **Set Environment Variables**:
```bash
vercel env add SECRET_KEY
vercel env add DEBUG
```

5. **Deploy to Production**:
```bash
vercel --prod
```

## Important Notes

### Database Considerations

⚠️ **SQLite won't work on Vercel** - Vercel is serverless and doesn't persist files.

**Options:**
1. **Use Vercel Postgres** (Recommended)
   - Add Vercel Postgres in your Vercel dashboard
   - Update `settings.py` to use PostgreSQL
   - Connection string will be provided by Vercel

2. **Use External Database**
   - PostgreSQL (Supabase, Railway, etc.)
   - MongoDB Atlas
   - Any cloud database service

### Update Settings for PostgreSQL

If using Vercel Postgres, update `crudapp/settings.py`:

```python
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DATABASE'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}
```

### Generate New Secret Key

For production, generate a new secret key:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Or use:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Troubleshooting

### Static Files Not Loading
- Vercel automatically handles static files with WhiteNoise
- Make sure `STATIC_ROOT` and `STATICFILES_STORAGE` are set correctly

### Database Errors
- SQLite won't work - use PostgreSQL or another cloud database
- Make sure database connection strings are set in environment variables

### Build Errors
- Check that all dependencies are in `requirements.txt`
- Ensure Python version is compatible (Vercel uses Python 3.9+)

## Post-Deployment

1. **Run Migrations**:
   - You may need to run migrations manually via Vercel CLI or add a build command

2. **Create Superuser**:
   - Use Django admin or create via Vercel CLI

3. **Test Your Application**:
   - Visit your Vercel deployment URL
   - Test all features (login, signup, create tasks, etc.)

## Useful Commands

```bash
# View deployment logs
vercel logs

# View environment variables
vercel env ls

# Remove deployment
vercel remove

# List all deployments
vercel ls
```

## Support

- [Vercel Documentation](https://vercel.com/docs)
- [Django on Vercel](https://vercel.com/guides/deploying-django-to-vercel)
