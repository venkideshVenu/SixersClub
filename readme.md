# SixersClub Cricket Tournament Platform 🏏

A comprehensive Django-based web platform for managing cricket tournaments, team registrations, player management, and fan engagement. Built with modern web technologies to deliver an exceptional cricket community experience.

## 🌟 Project Overview

**SixersClub** is a full-featured cricket tournament management system that brings together team managers, players, and fans in a unified platform. The application supports multiple cricket formats (T20, ODI, Test) and provides role-based dashboards for different user types.

### ✨ Key Features

#### 🔐 Multi-Role Authentication System

- **Team Managers**: Register and manage teams, add players, oversee team registrations
- **Players**: Individual registration, performance tracking, dashboard access with auto-generated Player IDs
- **Fans**: Follow teams, access news updates, view tournament information

#### 🏆 Tournament Management

- Support for multiple cricket formats (T20, ODI, Test)
- Tournament creation with registration deadlines and fees
- Detailed tournament pages with schedules and information
- Registration status tracking

#### 👥 Team & Player Management

- Team registration with player roster management
- Individual player registration for tournaments
- Unique player ID generation system
- Role-based player categorization (Batsman, Bowler, All-rounder)

#### 📰 News & Content Management

- Article creation and management system
- Image upload support for articles
- Community-driven content sharing
- News categorization and display

#### 🎨 Modern UI/UX

- Responsive Bootstrap-based design
- Interactive dashboards for each user type
- Mobile-friendly interface
- Professional cricket-themed styling

---

## 🛠️ Technology Stack

### Backend

- **Django 5.1.1** - Web framework
- **Python 3.12** - Programming language
- **SQLite** - Database (development)
- **Pillow** - Image processing

### Frontend

- **HTML5/CSS3** - Markup and styling
- **Bootstrap** - Responsive framework
- **JavaScript** - Interactive elements
- **Font Awesome** - Icons

### Development Tools

- **python-dotenv** - Environment variable management
- **Django Admin** - Administrative interface

---

## 📋 Prerequisites

Before setting up the project, ensure you have:

- **Python 3.8+** installed
- **pip** package manager
- **Git** for version control
- **Virtual environment** support (recommended)

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/venkideshVenu/SixersClub.git
cd SixersClub
```

### 2. Create Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_django_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Email Configuration (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
DEFAULT_FROM_EMAIL=your_email@gmail.com
```

Generate a secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Database Setup

```bash
# Apply migrations
python manage.py migrate

# Create superuser account
python manage.py createsuperuser

# (Optional) Load sample data
python manage.py loaddata fixtures/sample_data.json
```

### 6. Static Files

```bash
python manage.py collectstatic
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

---

## 📱 Application Structure

### Apps Overview

```
SixersClub/
├── accounts/          # User management & authentication
├── home/             # Homepage & static pages
├── tournaments/      # Tournament management
├── registrations/    # Team & player registrations
├── news/            # News & articles system
├── static/          # Static files (CSS, JS, images)
├── templates/       # HTML templates
└── media/           # User uploads
```

### Database Models

#### User Management (`accounts`)

- **CustomUser**: Extended user model with role-based access
- User types: Team Manager, Player, Fan
- Auto-generated Player IDs for players

#### Tournament System (`tournaments`)

- **Tournament**: Tournament details with type, dates, fees
- Support for T20, ODI, and Test formats
- Registration deadline management

#### Registration System (`registrations`)

- **TeamRegistration**: Team-based tournament entries
- **PlayerRegistration**: Individual player entries
- Player validation and role management

#### Content Management (`news`)

- **Article**: News articles with image support
- Author attribution and timestamp tracking

---

## 🎯 Usage Guide

### For Team Managers

1. **Register** as a Team Manager
2. **Browse Tournaments** and select desired tournament
3. **Register Team** with team name and motto
4. **Add Players** using their unique Player IDs
5. **Manage Team** through the Team Manager Dashboard

### For Players

1. **Register** as a Player (auto-generates Player ID)
2. **Complete Profile** with role and experience level
3. **Register for Tournaments** individually
4. **Track Performance** through Player Dashboard
5. **View Team Assignments** and match schedules

### For Fans

1. **Register** as a Fan
2. **Follow Tournaments** and teams
3. **Read News** and updates
4. **Access Fan Dashboard** for latest information

### Content Creation

- **All authenticated users** can create news articles
- **Upload images** for articles
- **Share cricket-related content** with the community

---

## 🔧 Admin Interface

Access the Django admin at `http://127.0.0.1:8000/admin/` with superuser credentials:

### Available Admin Features

- **User Management**: View and manage all user accounts
- **Tournament Administration**: Create and manage tournaments
- **Registration Oversight**: Monitor team and player registrations
- **Content Moderation**: Manage news articles and content

---

## 🗂️ Project File Structure

```
SixersClub/
├── manage.py
├── requirements.txt
├── readme.md
├── db.sqlite3
├── .env
│
├── SixersClub/                 # Main project settings
│   ├── __init__.py
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/                   # User management app
│   ├── models.py              # CustomUser model
│   ├── views.py               # Authentication views
│   ├── forms.py               # User registration forms
│   ├── urls.py                # Account URLs
│   └── admin.py
│
├── tournaments/                # Tournament management
│   ├── models.py              # Tournament model
│   ├── views.py               # Tournament views
│   ├── urls.py                # Tournament URLs
│   └── admin.py
│
├── registrations/              # Registration system
│   ├── models.py              # Registration models
│   ├── views.py               # Registration views
│   ├── forms.py               # Registration forms
│   └── urls.py
│
├── news/                       # News/Articles system
│   ├── models.py              # Article model
│   ├── views.py               # News views
│   ├── forms.py               # Article forms
│   └── urls.py
│
├── home/                       # Homepage & static pages
│   ├── views.py               # Home page views
│   ├── forms.py               # Contact forms
│   └── urls.py
│
├── static/                     # Static files
│   ├── home/css/              # Stylesheets
│   ├── home/js/               # JavaScript files
│   ├── home/images/           # Images
│   ├── accounts/images/       # Account-related images
│   ├── article_photos/        # Article images
│   └── tournaments_images/    # Tournament images
│
└── templates/                  # HTML templates
    ├── home/                  # Homepage templates
    ├── accounts/              # User account templates
    ├── tournaments/           # Tournament templates
    ├── registrations/         # Registration templates
    └── news/                  # News templates
```

---

## 🔌 API Endpoints

### Authentication URLs

- `/accounts/login/` - User login
- `/accounts/logout/` - User logout
- `/accounts/register/` - User registration type selection
- `/accounts/register/team_manager/` - Team manager registration
- `/accounts/register/player/` - Player registration
- `/accounts/register/fan/` - Fan registration

### Dashboard URLs

- `/accounts/team_manager_dashboard/` - Team manager dashboard
- `/accounts/player_dashboard/` - Player dashboard
- `/accounts/fan_dashboard/` - Fan dashboard

### Tournament URLs

- `/tournaments/` - Tournament list
- `/tournaments/<int:pk>/` - Tournament detail

### Registration URLs

- `/registrations/team_register/<int:tournament_id>/` - Team registration
- `/registrations/player_register/<int:tournament_id>/` - Player registration

### News URLs

- `/news/` - Article list
- `/news/article/<int:article_id>/` - Article detail
- `/news/create/` - Create article

---

## 🎨 Customization

### Styling

- Modify CSS files in `static/home/css/`
- Update Bootstrap components in templates
- Customize color schemes and fonts

### Templates

- Edit HTML templates in `templates/` directory
- Extend base templates for consistent styling
- Add custom template tags as needed

### Features

- Extend models for additional functionality
- Create custom forms for enhanced user input
- Add new apps for specialized features

---

## 🔍 Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test accounts
python manage.py test tournaments

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 📦 Deployment

### Production Settings

1. Set `DEBUG = False` in settings.py
2. Configure proper database (PostgreSQL recommended)
3. Set up static file serving
4. Configure email backend
5. Update `ALLOWED_HOSTS`

### Environment Variables for Production

```env
SECRET_KEY=production_secret_key
DEBUG=False
DATABASE_URL=postgresql://user:password@localhost/dbname
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

---

## 🤝 Contributing

We welcome contributions to improve SixersClub! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Write comprehensive tests for new features
- Update documentation as needed
- Use meaningful commit messages

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🏆 Acknowledgements

- **Django Framework** - Robust web development framework
- **Bootstrap** - Responsive CSS framework
- **Font Awesome** - Icon library
- **Cricket Community** - Inspiration and feedback
- **Open Source Contributors** - Various libraries and tools

---

## 📞 Support & Contact

For support, feature requests, or bug reports:

- **GitHub Issues**: [Create an issue](https://github.com/venkideshVenu/SixersClub/issues)
- **Email**: Contact the development team
- **Documentation**: Refer to Django documentation for framework-specific questions

---

## 🔄 Version History

- **v1.0.0** - Initial release with core functionality
- **Features**: User management, tournament system, registration, news system
- **Django Version**: 5.1.1
- **Python Version**: 3.12+

---

_Built with ❤️ for the cricket community_
