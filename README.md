# 🛡️ Fraud Website Detector

A comprehensive web application that helps users identify potentially fraudulent websites by analyzing multiple security indicators and domain characteristics.

## 🌟 Features

- **Multi-Factor Analysis**: Checks websites for HTTPS protocol, SSL certificates, domain typos, and WHOIS data
- **User Authentication**: Secure login/registration system with password recovery
- **Real-time Detection**: Instant website verification with detailed security reports
- **Results Management**: Save and export scan results to Excel files
- **Intuitive UI**: Clean, responsive interface built with React and Tailwind CSS
- **Comprehensive Database**: Extensive typo detection with 500+ common phishing domains

## 🚀 Technology Stack

### Backend
- **Flask**: Python web framework for API development
- **WHOIS**: Domain registration information lookup
- **SSL**: Certificate validation and security checks
- **CORS**: Cross-origin resource sharing support

### Frontend
- **React 18**: Modern UI library with hooks
- **React Router**: Client-side routing
- **Tailwind CSS**: Utility-first CSS framework
- **Heroicons**: Beautiful SVG icons
- **XLSX**: Excel file generation and export

## 🔍 Security Checks

The application performs four key security validations:

1. **HTTPS Protocol Verification**: Ensures the website uses secure HTTP protocol
2. **SSL Certificate Validation**: Verifies the presence and validity of SSL certificates
3. **Typo Detection**: Scans for common typosquatting patterns and misspelled domains
4. **Domain Information Analysis**: Checks WHOIS data for suspicious domain characteristics

## 📦 Installation

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

### Backend Setup
```bash
cd "mini project/backend"
pip install flask python-whois flask-cors
python app.py
```

### Frontend Setup
```bash
cd "mini project/frontend/fake"
npm install
npm start
```

## 🎯 Usage

1. **Access the Application**: Navigate to `http://localhost:3000`
2. **Login/Register**: Create an account or login with existing credentials
3. **Enter URL**: Input the website URL you want to check
4. **Analyze**: Click "Check Website" to run security analysis
5. **Review Results**: View detailed security assessment
6. **Save Results**: Export findings to Excel for record keeping

## 🛠️ API Endpoints

### POST `/check-website`
Analyzes a website URL for potential fraud indicators.

**Request Body:**
```json
{
  "url": "https://example.com"
}
```

**Response (Legitimate Site):**
```json
{
  "message": "The website is legitimate.",
  "isLegit": true
}
```

**Response (Suspicious Site):**
```json
{
  "message": "The website does not use HTTPS protocol.",
  "isLegit": false
}
```

## 🔧 Configuration

### Backend Configuration
- Default port: `5000`
- Debug mode: Enabled in development
- CORS: Configured for frontend integration

### Frontend Configuration
- Development server: `http://localhost:3000`
- API proxy: `http://localhost:5000`
- Build output: `build/` directory

## 📊 Project Structure

```
fraudwebsite_detector/
├── mini project/
│   ├── backend/
│   │   ├── app.py              # Flask application
│   │   ├── static/             # Static files
│   │   └── templates/          # HTML templates
│   └── frontend/
│       └── fake/
│           ├── src/
│           │   ├── components/ # React components
│           │   ├── App.js      # Main application
│           │   └── index.js    # Entry point
│           ├── public/         # Public assets
│           └── build/          # Production build
└── README.md
```

## 🔐 Security Features

- **Input Validation**: Comprehensive URL format validation
- **SSL Verification**: Real-time certificate checking
- **Typosquatting Detection**: Advanced pattern matching against known fraudulent domains
- **Domain Age Analysis**: WHOIS data verification for suspicious registrations
- **Error Handling**: Graceful failure management with user-friendly messages

## 🎨 User Interface

- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Modern Styling**: Clean interface with Tailwind CSS
- **Interactive Elements**: Real-time feedback and loading states
- **Accessibility**: Screen reader friendly with proper ARIA labels

## 📈 Future Enhancements

- [ ] Machine learning integration for advanced fraud detection
- [ ] Real-time threat intelligence feeds
- [ ] Browser extension for seamless protection
- [ ] Multi-language support
- [ ] Advanced reporting and analytics
- [ ] Integration with external security APIs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**Hassaan1805**
- GitHub: [@Hassaan1805](https://github.com/Hassaan1805)
- Email: zeroc1712@gmail.com

## 🙏 Acknowledgments

- Flask and React communities for excellent frameworks
- Python WHOIS library contributors
- Tailwind CSS team for the utility-first approach
- Security research community for fraud detection insights

---

⭐ **Star this repository if you find it helpful!**
