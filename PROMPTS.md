# TrustVault – AI Prompt Documentation

## Project: Secure Document Sharing

### Entry 1 – 03 November 2026
**Prompt:** Help me create a secure document-sharing web application using Python Flask.

**AI Output:** Suggested Flask project structure with routes, templates, models and database.

**Error:** Flask module was missing.

**Correction:** Installed Flask and required dependencies.

**Commit:** Initial project setup.

### Entry 2 – 04 November 2026
**Prompt:** Help me implement user registration and login using Flask and SQLite.

**AI Output:** Generated registration, login and password authentication code.

**Error:** Login and registration configuration issues.

**Correction:** Corrected routes, database models and Flask-Login configuration.

**Commit:** 6d016ff – Complete Day 2 registration and login.

### Entry 3 – 05 November 2026
**Prompt:** How can I restrict users to view and download only their own documents?

**AI Output:** Suggested login_required protection and filtering documents by owner_id.

**Security Focus:** Authorization and access control.

**Error:** Document access needed ownership verification.

**Correction:** Added owner-based filtering and download authorization checks.

**Commit:** 707ce07 – Complete Day 5 view and download documents.

### Entry 4 – 06 November 2026
**Prompt:** Help me secure document uploads against unsafe file types and large files.

**AI Output:** Suggested secure_filename, allowed extensions, UUID filenames and file-size validation.

**Security Focus:** Upload security and access control.

**Error:** Large files exceeded the configured upload limit.

**Correction:** Configured a 16 MB upload limit and file type validation.

**Commit:** 4a60c54 – Complete Day 6 document security.

### Entry 5 – 09 November 2026
**Prompt:** Help me deploy my Flask application on Render and fix the SQLite database directory error.

**AI Output:** Suggested environment-based SECRET_KEY and automatic database and upload directory creation.

**Error:** SQLite OperationalError – unable to open database file.

**Correction:** Added os.makedirs() for database and uploads directories.

**Commit:** 5425292 – Fix database directory for deployment.

## Conclusion

AI tools were used to understand errors, improve security, implement features and deploy TrustVault. All generated suggestions were reviewed and tested during development.s