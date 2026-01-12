# Database Setup for Vercel Deployment

## Current Situation
You're in the Vercel Storage section. For Django, you need **PostgreSQL**.

## Step-by-Step Instructions

### Option 1: Use Vercel Marketplace (Recommended)

1. **Click "Cancel"** on the current modal (if it's still open)

2. **Look for "Marketplace"** in the Storage section
   - You should see a link or section mentioning "Marketplace Database Providers"
   - Click on it or look for Postgres options

3. **Select PostgreSQL**
   - In the Marketplace, find and select **PostgreSQL**
   - Click "Create" or "Add"

4. **Configure Database**
   - Name your database (e.g., "todoapp-db")
   - Select a region (choose closest to you)
   - Click "Create"

5. **Vercel will automatically:**
   - Add environment variables to your project
   - Variables will be named like:
     - `POSTGRES_URL`
     - `POSTGRES_PRISMA_URL`
     - `POSTGRES_URL_NON_POOLING`
     - `POSTGRES_USER`
     - `POSTGRES_HOST`
     - `POSTGRES_PASSWORD`
     - `POSTGRES_DATABASE`

### Option 2: Use External Database (If Marketplace Not Available)

If you can't find Postgres in the Marketplace, use an external service:

#### A. Supabase (Free & Easy)
1. Go to https://supabase.com
2. Sign up for free
3. Create a new project
4. Go to Settings → Database
5. Copy the connection string
6. Add to Vercel as environment variables

#### B. Railway (Free Tier)
1. Go to https://railway.app
2. Sign up with GitHub
3. Create new project → Add PostgreSQL
4. Copy connection details
5. Add to Vercel environment variables

## After Database is Created

You'll need to update your Django settings to use PostgreSQL. The connection details will be in your Vercel environment variables.
