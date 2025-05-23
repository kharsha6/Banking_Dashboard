# MyBank Dashboard

A simple Django-based banking dashboard UI for displaying user account information in a clean, responsive layout.

## Why Use This Django Banking System?

This Django-based banking dashboard is designed to streamline the management and display of user banking details. It offers:

- 🔒 **Secure Interface**: Built with Django’s robust security features for handling sensitive banking data.
- 🧑‍💻 **Admin Integration**: Easily manage banking records through the Django admin panel—no need for manual database updates.
- 🎨 **User-Friendly UI**: Clean, responsive design to provide users with a pleasant and accessible banking experience.
- ⚙️ **Customizable & Extendable**: Built using Django’s modular structure—easy to extend for additional features like transactions, statements, and analytics.
- 🚀 **Quick Deployment**: Minimal setup and fast integration with existing Django projects.

This system is perfect for learning Django through real-world applications or building a full-featured internal tool for finance-related workflows.

## Features

- Sidebar navigation for Dashboard, Transactions, and Settings
- Welcome section displaying a personalized greeting
- Grid layout to show banking information:
  - Account Holder
  - Account Number
  - Bank Name
  - Branch
  - IFSC Code
  - Account Type
  - Balance (highlighted)
- Responsive and neatly aligned layout using CSS Grid
- Logout functionality with CSRF protection

## How Each Page Works

This Django banking system consists of the following key pages:

### 1. **Dashboard Page (`dashboard.html`)**
- Displays a personalized greeting to the logged-in user.
- Shows detailed banking information such as:
  - Account Holder
  - Account Number
  - Bank Name
  - Branch
  - IFSC Code
  - Account Type
  - Balance
- If no data is found, it shows a warning message.
- Data is passed from the Django view using a context dictionary named `banking_info`.

### 2. **Transactions Page (`transactions.html`)**
- Shows a list of all transactions related to the logged-in user.
- Displays:
  - Recipient or Source
  - Date
  - Description
  - Amount
  - Transaction Type (Credit/Debit)
- Data is fetched securely and rendered using context from the view `transactions_view`.
- Navigation path: `Dashboard > Transactions`.

### 3. **Sidebar Navigation**
- Located on the left side of the dashboard.
- Contains links to:
  - Dashboard
  - Transactions
  - Settings (future requirement)
- Static menu for easy navigation.

### 4. **Logout Button**
- A logout button is present below the banking info section.
- On click, it submits a POST request to the Django `logout` view.
- Logs the user out and redirects them to the login page.

### 5. **Django Admin Panel**
- Accessible at `/admin/`.
- Allows staff/superusers to:
  - Add banking details directly without raw SQL or manual entry.
  - Edit or delete user banking records.
  - Manage other Django models.
- Admin interface is generated automatically by registering models in `admin.py`.

### 6. **Authentication (Handled in Backend)**
- Users must log in to view the dashboard.  
- Django’s built-in authentication system ensures secure access.
- Session-based login maintains user state.

## Technologies Used

- Django (Python)
- HTML & CSS (Vanilla)
- Responsive layout using CSS Grid and Flexbox

## Images

Register :

![image](https://github.com/user-attachments/assets/d839d6d4-7d3f-4953-98fc-2794dd558abf)

Login :

![image](https://github.com/user-attachments/assets/880c38a0-e3d3-4dab-8f2d-e78039ee9096)


Banking Dashboard :

![image](https://github.com/user-attachments/assets/85ac5f9b-e205-4740-ac8e-b56df96f8287)


Transactions :

![image](https://github.com/user-attachments/assets/cca2681d-43ec-4373-b676-4c722ce0daf9)






