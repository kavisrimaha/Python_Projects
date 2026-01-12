# Vercel Setup Configuration Guide

## Framework Preset Selection

When deploying your Django app to Vercel, use these settings:

### Framework Preset
**Select: "Other"** or **"No Framework"**

Vercel doesn't have a specific Django preset, so "Other" is the correct choice. Your `vercel.json` file will handle the configuration automatically.

### Complete Configuration Settings

When setting up your project in Vercel, use these exact settings:

```
Framework Preset: Other
Root Directory: ./
Build Command: (leave empty)
Output Directory: (leave empty)
Install Command: (leave empty)
```

### Why "Other"?

- Django is a Python framework, not a JavaScript framework
- Vercel's auto-detection works best for JS frameworks (Next.js, React, etc.)
- Your `vercel.json` file already configures everything needed
- The `api/index.py` file serves as the serverless function handler

### What Happens Next?

1. Vercel will detect your `vercel.json` configuration
2. It will use the `@vercel/python` builder
3. All routes will be handled by `api/index.py`
4. Your Django app will run as a serverless function

### Important Notes

- ✅ Don't change the Root Directory (keep it as `./`)
- ✅ Don't add a Build Command (Django doesn't need building)
- ✅ Don't add an Output Directory
- ✅ Your `vercel.json` handles everything automatically

---

**TL;DR: Select "Other" for Framework Preset and leave everything else as default!**
