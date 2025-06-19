# Django Authentication Backend

A robust Django REST API backend providing comprehensive user authentication, authorization, and profile management features. Built with Django REST Framework and JWT authentication.

## 🚀 Features

### Authentication & Authorization
- **JWT Token Authentication** with refresh token support
- **User Registration** with optional admin privileges
- **Secure Login/Logout** with token blacklisting
- **Password Management** (change password, forgot password)
- **Role-based Access Control** (Admin-only endpoints)

### User Management
- **User Profile Management** with CRUD operations
- **Advanced User Filtering** (username, email, staff status)
- **Paginated User Lists** with search capabilities
- **Profile Image Upload** via Cloudinary integration

### API Documentation
- **Interactive Swagger UI** for API exploration
- **ReDoc Documentation** for detailed API reference
- **OpenAPI 3.0 Schema** generation

## 🛠️ Tech Stack

- **Backend Framework:** Django 5.2.3
- **API Framework:** Django REST Framework
- **Authentication:** Simple JWT
- **Database:** PostgreSQL (production), configurable for development
- **Image Storage:** Cloudinary
- **Documentation:** drf-spectacular
- **Filtering:** django-filter
- **CORS:** django-cors-headers

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL (for production)
- Cloudinary account (for image uploads)

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd backend_auth
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the root directory:

```env
# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/database_name

# Cloudinary Configuration
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# Deployment (set to TRUE for production)
RENDER=FALSE
```

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## 📚 API Endpoints

### Authentication Endpoints
| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| POST | `/api/register/` | User registration | None |
| POST | `/api/login/` | User login | None |
| POST | `/api/login/refresh/` | Refresh JWT token | None |
| POST | `/api/logout/` | User logout | None |
| POST | `/api/forgot-password/` | Reset password | None |
| POST | `/api/change-password/` | Change password | Required |

### User Management Endpoints
| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| GET | `/api/hello/` | Protected hello message | Required |
| GET/PUT | `/api/user-profile/` | Get/Update user profile | Required |
| GET | `/api/userlist/` | List all users (with filters) | Required |
| GET | `/api/admin-only/` | Admin-only endpoint | Admin Required |

### Profile Management Endpoints
| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| POST | `/api/profile-register/` | Create new profile | None |
| GET | `/api/profile/` | List all profiles | None |
| GET/PUT/DELETE | `/api/profile/<id>/` | Profile detail operations | None |

### Documentation Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/schema/` | OpenAPI schema |
| GET | `/api/docs/swagger/` | Swagger UI |
| GET | `/api/docs/redoc/` | ReDoc documentation |

## 🔧 API Usage Examples

### User Registration
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "email": "user@example.com",
    "password": "securepassword123",
    "admin_code": "make-me-admin"
  }'
```

### User Login
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "password": "securepassword123"
  }'
```

### Access Protected Endpoint
```bash
curl -X GET http://localhost:8000/api/hello/ \
  -H "Authorization: Bearer <your-access-token>"
```

### Create Profile with Image
```bash
curl -X POST http://localhost:8000/api/profile-register/ \
  -H "Authorization: Bearer <your-access-token>" \
  -F "name=John Doe" \
  -F "age=25" \
  -F "image=@profile.jpg"
```

## 🔍 Advanced Features

### User Filtering
The `/api/userlist/` endpoint supports advanced filtering:
- `?username=john` - Filter by username (contains)
- `?email=@gmail.com` - Filter by email (contains)
- `?is_staff=true` - Filter by staff status
- `?is_superuser=false` - Filter by superuser status

### Admin Privileges
Users can be granted admin privileges during registration or profile update using the special code `make-me-admin`.

### Profile Validation
- Age validation ensures users are 18 or older
- Image uploads are handled via Cloudinary with automatic URL generation

## 🚀 Deployment

### Environment Variables for Production
```env
RENDER=TRUE
DATABASE_URL=postgresql://prod_user:prod_pass@prod_host:5432/prod_db
CLOUDINARY_CLOUD_NAME=prod_cloud_name
CLOUDINARY_API_KEY=prod_api_key
CLOUDINARY_API_SECRET=prod_api_secret
```

### Production Considerations
- Set `DEBUG = False` in production
- Configure proper `ALLOWED_HOSTS`
- Use environment variables for sensitive data
- Enable HTTPS
- Configure proper CORS settings

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

## 📁 Project Structure

```
backend_auth/
├── accounts/                 # Main app directory
│   ├── migrations/          # Database migrations
│   ├── admin.py            # Admin configuration
│   ├── filters.py          # Custom filters
│   ├── models.py           # Database models
│   ├── permissions.py      # Custom permissions
│   ├── serializers.py      # API serializers
│   ├── validators.py       # Custom validators
│   ├── views.py            # API views
│   └── urls.py             # App URL patterns
├── backend_auth/            # Project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
└── manage.py               # Django management script
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the API documentation at `/api/docs/swagger/`
- Review the test cases for usage examples

## 🔗 Related Links

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Simple JWT Documentation](https://django-rest-framework-simplejwt.readthedocs.io/)
- [Cloudinary Documentation](https://cloudinary.com/documentation/django_integration)
