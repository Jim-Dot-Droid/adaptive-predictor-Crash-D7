## Streamlit Cloud Deployment

1. **Create new repository** on GitHub
2. **Add these exact files**:
   - `app.py`
   - `requirements.txt` (must contain plotly==5.22.0)
3. **Deploy to Streamlit**:
   - Go to [share.streamlit.io](https://share.streamlit.io/)
   - New App → From existing repo
   - Set Python version to 3.10
   - No advanced settings needed
4. **Wait 3-5 minutes** for first build

## Verification Steps

After deployment:
1. Click "Manage App"
2. Check logs for:
   - "Successfully installed plotly-5.22.0"
3. If errors persist:
   - Delete and redeploy
   - Try Python 3.9 instead of 3.10