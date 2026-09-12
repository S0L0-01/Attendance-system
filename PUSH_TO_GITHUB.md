# Quick Push to GitHub Guide

## You're almost done! Just run these 3 commands in PowerShell:

### Step 1: Open PowerShell and navigate to your project
```powershell
cd "C:\Users\swapn\OneDrive\Desktop\Attendance system\attendance_project"
```

### Step 2: Push to GitHub (this will open a browser for login)
```powershell
git push -u origin main
```

A browser window will pop up asking you to sign in to GitHub. Click "Authorize" and you're done!

---

## Alternative: If the browser doesn't open

Create a Personal Access Token:
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Check the "repo" scope
4. Click "Generate token"
5. Copy the token

Then run:
```powershell
git push -u origin main
```
When prompted:
- Username: S0L0-01
- Password: (paste your token)

---

Your GitHub repository: https://github.com/S0L0-01/Attendance-system
