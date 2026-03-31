# 🚀 SmartCommerce | MarketFlow

## Intelligent E-commerce Platform with Advanced Analytics & Admin Dashboard

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-2.0+-red.svg)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/sqlite-3-blue.svg)](https://www.sqlite.org/)
[![JWT](https://img.shields.io/badge/JWT-auth-orange.svg)](https://jwt.io/)

---

## 📖 About The Project

**SmartCommerce** is a complete, production-ready e-commerce platform developed as a portfolio showcase. It combines a modern shopping experience with powerful administrative tools and advanced analytics capabilities.

### 🏪 The Store: **MarketFlow**

MarketFlow is the customer-facing brand of the SmartCommerce platform, offering a seamless and intuitive shopping experience inspired by major e-commerce platforms like Shopee, Mercado Libre, and TikTok Shop.

### ✨ Key Features

#### 🛍️ Customer Experience (MarketFlow Store)
- **Secure Authentication** - JWT-based login and registration system
- **Smart Product Discovery** - Real-time search, category filtering, and price sorting
- **Interactive Shopping Cart** - Dynamic quantity controls and real-time price updates
- **Simulated Checkout** - Multiple payment methods (Credit Card, PIX, Boleto)
- **Password Recovery** - Three-step verification flow with code simulation
- **Responsive Design** - Perfect experience across desktop, tablet, and mobile devices

#### 👑 Admin Dashboard (SmartCommerce Admin)
- **Product Management** - Full CRUD operations for product catalog
- **User Overview** - View all registered users with registration dates
- **Order Management** - Track all customer orders with detailed information
- **Analytics Dashboard** - Real-time metrics and visual insights
- **Data Export** - Export analytics data to JSON and CSV formats

#### 📊 Analytics Center (SmartCommerce Analytics)
- **Interactive Charts** - Product category distribution and payment method analysis
- **Key Metrics** - Total products, users, orders, and revenue
- **Advanced Filtering** - Search across all tables in real-time
- **Export Functionality** - Download reports in multiple formats
- **Business Intelligence** - Data-driven insights for decision making

---

## 🛠️ Technology Stack

### Backend
| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **Flask** | Web framework and API development |
| **SQLAlchemy** | Object-Relational Mapping (ORM) |
| **JWT** | Authentication and authorization |
| **Werkzeug** | Password hashing and security |
| **SQLite** | Lightweight database management |

### Frontend
| Technology | Purpose |
|------------|---------|
| **HTML5/CSS3** | Structure and styling |
| **JavaScript (Vanilla)** | Interactivity and API integration |
| **Chart.js** | Data visualization and charts |
| **Font Awesome 6** | Icon library |
| **Google Fonts** | Typography (Inter font family) |

---

## 📁 Project Structure
SmartCommerce/
├── backend/
│ ├── app.py # Main Flask application with all API routes
│ ├── models.py # Database models (User, Product, Order)
│ ├── database.py # Database configuration and session management
│ ├── seed_fixed.py # Database seeder with initial data
│ ├── store.db # SQLite database (generated after seeding)
│ └── requirements.txt # Python dependencies
│
├── frontend/
│ ├── login.html # Authentication page (login/register)
│ ├── forgot_password.html # Password recovery flow
│ ├── e-commerce-frontend.html # Main store interface (MarketFlow)
│ ├── admin.html # Administrative panel
│ ├── analytics.html # Analytics dashboard
│ └── payment.html # Checkout simulation page
│
├── printscreen/
│ ├── admin.png # Admin panel screenshot
│ ├── admin2.png # Admin panel alternative view
│ ├── analyticsPRTSC.png # Analytics dashboard screenshot
│ ├── analyticsPRTSC2.png # Analytics dashboard alternative view
│ ├── inicial.png # Store homepage screenshot
│ ├── inicial2.png # Store homepage alternative view
│ ├── payment.png # Payment page screenshot
│ ├── payment2.png # Payment page alternative view
│ ├── payment3.png # Payment page confirmation view
│ ├── forgoytpassword.png # Forgot password page
│ └── forgotpassword2.png # Forgot password alternative view
│
└── README.md # This file

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8** or higher
- **pip** package manager
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation & Setup

#### 1. Clone the repository
```bash
git clone https://github.com/yourusername/smartcommerce-marketflow.git
cd smartcommerce-marketflow
2. Set up the backend environment
bash
cd backend
pip install -r requirements.txt
3. Create and populate the database
bash
python seed_fixed.py
This will create the SQLite database with:

Admin user (admin/1234)

Demo user (demo/demo123)

Sample products across 4 categories

4. Start the backend server
bash
python app.py
The API will be available at: http://127.0.0.1:5000

5. Start the frontend server (in a new terminal)
bash
cd ../frontend
python -m http.server 5500
6. Access the application
Open your browser and navigate to:

text
http://localhost:5500/login.html
🔐 Authentication & Test Credentials
Role	Username	Password	Access Level
👑 Administrator	admin	1234	Full system access, Admin Panel, Analytics
👤 Regular User	demo	demo123	Store access only
🎯 Application Workflow
Customer Journey (MarketFlow)
Register/Login → Create account or sign in

Browse Products → Search, filter by category, sort by price

Add to Cart → Select products and manage quantities

Checkout → Fill shipping details and choose payment method

Order Confirmation → Receive simulated payment confirmation

Admin Journey (SmartCommerce)
Login as Admin → Use admin credentials

Access Admin Panel → Click "Admin" button in header

Manage Products → Add, view, or delete products

View Analytics → Access dashboard with charts and metrics

Export Data → Download reports in JSON/CSV format

📊 API Endpoints
Method	Endpoint	Description	Auth Required
POST	/register	Create new user account	❌
POST	/login	Authenticate and get JWT token	❌
GET	/profile	Get current user profile	✅
GET	/products	Retrieve all products	❌
POST	/admin/products	Add new product	✅ (admin only)
DELETE	/admin/products/<id>	Delete product	✅ (admin only)
POST	/orders	Create new order	✅
GET	/admin/analytics	Get analytics data	✅ (admin only)
🎨 Design Features
Modern Gradient UI - Eye-catching gradients and smooth transitions

Glassmorphism Effects - Subtle backdrop filters and shadows

Responsive Layout - Fully responsive from 320px to 4K displays

Interactive Elements - Hover effects, loading states, and toast notifications

Accessibility - Semantic HTML and keyboard navigation support

📈 Analytics Dashboard Features
Key Metrics Display
Total Products Count

Total Registered Users

Total Orders Processed

Total Revenue Generated

Visualizations
Bar Chart - Products distribution by category

Pie Chart - Payment method popularity

Data Management
Real-time search across all tables

CSV export for spreadsheet software (Excel, Google Sheets, LibreOffice)

JSON export for developers and API integration

Complete data export functionality

🔒 Security Features
Password Hashing - All passwords hashed using Werkzeug security

JWT Authentication - Token-based authorization for protected routes

Role-Based Access - Separate permissions for admin and regular users

CORS Protection - Configured to accept requests only from trusted origins

Input Validation - All user inputs validated before processing

📸 Screenshots
🏠 Store Interface (MarketFlow)
Store Homepage	Store Homepage Alternative
https://printscreen/inicial.png	https://printscreen/inicial2.png
🔐 Authentication Pages
Login Page	Password Recovery
Login interface with credentials	Password recovery flow
Coming soon	https://printscreen/forgoytpassword.png
Forgot Password Alternative
https://printscreen/forgotpassword2.png

👑 Admin Panel
Admin Dashboard	Admin Dashboard Alternative
https://printscreen/admin.png	https://printscreen/admin2.png
📊 Analytics Dashboard
Analytics Dashboard	Analytics Dashboard Alternative
https://printscreen/analyticsPRTSC.png	https://printscreen/analyticsPRTSC2.png
💳 Checkout & Payment
Payment Page	Payment Page Alternative	Payment Confirmation
https://printscreen/payment.png	https://printscreen/payment2.png	https://printscreen/payment3.png
🚧 Future Enhancements
Payment Gateway Integration - Real payment processing (Stripe, PagSeguro)

Email Notifications - Order confirmations and password recovery emails

Product Reviews - Rating and review system with comments

Image Upload - Product image upload functionality

Discount Coupons - Promotional codes and special offers

Wishlist - Save favorite products for later

Order Tracking - Real-time order status updates

Multi-language Support - Internationalization (i18n)

🤝 Contributing
Contributions are welcome! Here's how you can help:

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

Development Guidelines
Follow PEP 8 for Python code

Use semantic HTML5 elements

Write clear commit messages

Test all changes before submitting

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
Your Name

🌐 Portfolio: your-portfolio.com

🐙 GitHub: @yourusername

💼 LinkedIn: Your LinkedIn Profile

📧 Email: your.email@example.com

🙏 Acknowledgments
Inspired by modern e-commerce platforms (Shopee, Mercado Libre, TikTok Shop)

Chart.js for beautiful data visualizations

Font Awesome for comprehensive icon library

The Flask and Python communities for excellent documentation

📊 Project Statistics
Metric	Value
Total Lines of Code	~3,500
API Endpoints	8
Database Tables	3
Frontend Pages	6
Screenshots	11
JavaScript Functions	25+
CSS Properties	400+
🏆 Key Achievements
✅ Full-Stack Implementation - Complete e-commerce solution from database to UI

✅ Professional UI/UX - Modern design matching industry standards

✅ Data Analytics - Built-in business intelligence features

✅ Secure Authentication - JWT-based auth with role-based access

✅ Export Functionality - Data export in multiple formats

✅ Responsive Design - Works seamlessly across all devices

✅ Portfolio Ready - Production-quality code with documentation

⭐ Show Your Support
If this project helped you or inspired you, please give it a ⭐ on GitHub!

