# Modern Calculator

A beautiful and easy-to-use calculator with both web and desktop versions. Features a modern UI, keyboard support, and advanced calculation capabilities.

![Calculator Preview](website/images/preview.png)

## Features

- 🎨 Modern, gradient-based design
- ⌨️ Full keyboard support
- 📱 Responsive layout for all devices
- 🧮 Advanced calculation features
- 💾 Available for Windows and Android
- 🌐 Web version accessible anywhere

## Try It Online

Visit our website to try the calculator online: [Modern Calculator Web](https://yourusername.github.io/modern-calculator)

## Downloads

- [Windows Version](https://github.com/yourusername/modern-calculator/releases/latest/download/ModernCalculator-Windows.zip)
- [Android Version](https://github.com/yourusername/modern-calculator/releases/latest/download/ModernCalculator.apk)

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Node.js 14+ (for web development)
- Android Studio (for Android development)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/modern-calculator.git
   cd modern-calculator
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the web version locally:
   ```bash
   python -m http.server 8000 --directory website
   ```

4. Build packages:
   ```bash
   ./create_packages.bat  # Windows
   ./create_packages.sh   # Linux/Mac
   ```

### Building Mobile Version

1. Open the project in Android Studio:
   ```bash
   cd android
   ./gradlew assembleDebug
   ```

2. The APK will be generated in `android/app/build/outputs/apk/debug/`

## Project Structure

```
modern-calculator/
├── website/              # Web version
│   ├── css/             # Stylesheets
│   ├── js/              # JavaScript files
│   ├── images/          # Icons and images
│   └── downloads/       # Application packages
├── android/             # Android app source
├── calculator.py        # Desktop version
└── create_packages.bat  # Build script
```

## Keyboard Shortcuts

- `0-9`: Number input
- `.`: Decimal point
- `+`, `-`, `*`, `/`: Operators
- `Enter` or `=`: Calculate
- `Escape`: Clear
- `Backspace`: Delete last digit

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Icons and gradients inspired by modern design trends
- Built with love for the open-source community

## Contact

Your Name - [@yourusername](https://twitter.com/yourusername)

Project Link: [https://github.com/yourusername/modern-calculator](https://github.com/yourusername/modern-calculator)