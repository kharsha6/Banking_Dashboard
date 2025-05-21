## Setup Instructions

Follow these steps to run the MyBank Dashboard on your local machine:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/mybank-dashboard.git
   cd mybank-dashboard
   ```

2. **Create and Activate a Virtual Environment (optional but recommended)**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install Django**
   ```bash
   pip install django
   ```

4. **Create Django Project (if not already included)**
   ```bash
   django-admin startproject myproject .
   ```

5. **Add Your App**
   ```bash
   python manage.py startapp dashboard
   ```

6. **Register the App and Static Files**
   - In `myproject/settings.py`, add your app to `INSTALLED_APPS`:
     ```python
     INSTALLED_APPS = [
         ...
         'dashboard',
     ]
     ```
   - Add this for static files:
     ```python
     STATIC_URL = '/static/'
     STATICFILES_DIRS = [BASE_DIR / "static"]
     ```

7. **Create Templates and Static Folders**
   - Create a folder structure like:
     ```
     dashboard/
     ├── templates/
     │   └── dashboard.html
     └── static/
         └── css/
             └── style.css
     ```

8. **Add URL Configuration**
   - In `dashboard/urls.py`:
     ```python
     from django.urls import path
     from . import views

     urlpatterns = [
         path('', views.dashboard_view, name='dashboard'),
     ]
     ```
   - In `myproject/urls.py`:
     ```python
     from django.contrib import admin
     from django.urls import path, include

     urlpatterns = [
         path('admin/', admin.site.urls),
         path('', include('dashboard.urls')),
     ]
     ```

9. **Create a View**
   - In `dashboard/views.py`:
     ```python
     from django.shortcuts import render

     def dashboard_view(request):
         banking_info = {
             'account_holder': 'John Doe',
             'account_number': '1234567890',
             'bank_name': 'MyBank',
             'branch_name': 'Main Branch',
             'ifsc_code': 'MYBK0001234',
             'account_type': 'Savings',
             'balance': 15000
         }
         return render(request, 'dashboard.html', {'banking_info': banking_info})
     ```

10. **Run Migrations**
    ```bash
    python manage.py migrate
    ```

11. **Create a Superuser (to use Django Admin)**
    ```bash
    python manage.py createsuperuser
    ```

12. **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

13. **Visit the Dashboard**
    Open your browser and go to:  
    `http://127.0.0.1:8000/`

---
Now your MyBank dashboard should be running successfully with dummy banking info.
