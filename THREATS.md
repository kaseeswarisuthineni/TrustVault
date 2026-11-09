# TrustVault – Security Threat Model

## 1. Project Overview

TrustVault is a secure document-sharing web application developed using Python, Flask, Flask-Login and SQLite.

The application allows registered users to upload, view and download their documents.

## 2. Assets to Protect

- User account information
- User passwords
- Uploaded documents
- Document ownership information
- Login sessions
- Database records

## 3. Potential Threats and Mitigations

### Threat 1: Unauthorized Access

**Risk:** An unauthenticated user may try to access protected pages.

**Mitigation:** Flask-Login's login_required decorator is used to protect authenticated routes.

**Validation:** Test accessing the dashboard and document pages without logging in.

### Threat 2: Unauthorized Document Download

**Risk:** A user may try to download another user's document.

**Mitigation:** Document ownership is checked before allowing downloads.

**Validation:** Create two test accounts and verify that one account cannot access the other account's documents.

### Threat 3: Malicious File Upload

**Risk:** An attacker may upload executable or unsupported files.

**Mitigation:** Allowed file extensions are restricted and secure_filename is used.

**Validation:** Try uploading an unsupported file type and verify that it is rejected.

### Threat 4: Large File Upload

**Risk:** Very large files may consume server resources.

**Mitigation:** Maximum upload size is restricted to 16 MB.

**Validation:** Upload a file larger than 16 MB and verify that the request is rejected.

### Threat 5: Session and Secret Key Exposure

**Risk:** Weak or exposed secret keys may compromise session security.

**Mitigation:** The Flask SECRET_KEY is loaded from an environment variable during deployment.

**Validation:** Verify that the Render environment contains the SECRET_KEY variable and that the application starts correctly.

### Threat 6: Database and File Storage Failure

**Risk:** Missing storage directories may cause database or upload failures.

**Mitigation:** Database and upload directories are created automatically using os.makedirs().

**Validation:** Deploy the application and verify that the database directory is available.

## 4. Security Testing Checklist

- [ ] Dashboard access without login is rejected.
- [ ] Document pages require authentication.
- [ ] Users cannot download other users' documents.
- [ ] Unsupported file extensions are rejected.
- [ ] Files larger than 16 MB are rejected.
- [ ] Valid PDF and document uploads work.
- [ ] Login and logout work correctly.

## 5. Limitations and Future Improvements

- Add password hashing verification and stronger password policies.
- Implement CSRF protection.
- Add document encryption at rest.
- Implement a persistent production database and file storage.
- Add an audit logging system to record document access and downloads.
- Add automated security tests.

## 6. Conclusion

This threat model identifies important security risks in TrustVault and documents the implemented protections and additional security improvements required for production readiness.