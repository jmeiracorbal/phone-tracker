# Phone tracker

[![Test and Validate](https://github.com/jmeiracorbal/phone-tracker/workflows/Test%20and%20Validate/badge.svg)](https://github.com/jmeiracorbal/phone-tracker/actions/workflows/test.yml)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Poetry](https://img.shields.io/badge/Poetry-1.0%2B-orange.svg)](https://python-poetry.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)](https://github.com/jmeiracorbal/phone-tracker)

A tool to get detailed information about phone numbers. It helps you discover location, carrier, timezone, and other details about any phone number you're curious about.

## What it does

- **Phone number analysis** - Get complete information about any phone number
- **Country and region detection** - Country, region, city, and coordinates
- **Carrier details** - Mobile operator and service provider info
- **Timezone identification** - Automatically finds the right timezone
- **Number validation** - Check if the number is valid and possible
- **Nice interface** - Clean, colored output that's easy to read

## Download executable

1. **Go to [Releases](https://github.com/jmeiracorbal/phone-tracker/releases)**
2. **Download the executable for your platform:**
   - **Linux**: `phone-tracker` (binary)
   - **macOS**: `phone-tracker` (binary)
   - **Windows**: `phone-tracker.exe` (executable)
3. **Run directly** - No installation required!

### Usage

**Linux/macOS:**

```bash
chmod +x phone-tracker
```

```bash
./phone-tracker
```

**Windows:**

```cmd
phone-tracker.exe
```

_Output example_:

```
Enter phone number information:
Country Code Ex [34, 1, 81] : 34
Phone Number Ex [666666666] : xxxxxxxxx

========== SHOW INFORMATION PHONE NUMBERS ==========

Full Number         : +34xxxxxxxxx
Location             : Spanyol
Region Code          : ES
Timezone             : Atlantic/Canary, Europe/Madrid
Operator             : Orange
Valid number         : True
Possible number      : True
International format : +34 xxx xx xx xx
Mobile format        : +34 xxx xx xx xx
Type                 : This is a mobile number
```

## How it works

The tool uses the `phonenumbers` library to:

1. Parse and validate phone numbers
2. Extract country and region information
3. Determine carrier and operator details
4. Identify timezone information
5. Format numbers in various international standards

## Supported formats

- **Country codes**: +1 (US/Canada), +34 (Spain), +81 (Japan), +86 (China), etc.
- **Number types**: Mobile, Fixed-line, Toll-free, Premium rate
- **International standards**: E.164, International, National formats

## For Developers

### Run from source
If you want to run the source code:

```bash
git clone https://github.com/jmeiracorbal/phone-tracker.git
cd phone-tracker
pip install phonenumbers requests
python phone_tracker.py
```

### Build executables
Executables are automatically built and released via GitHub Actions when tags are pushed.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Original author**: [HUNXBYTS](https://github.com/HUNXBYTS)
- **Forked from**: [jmeiracorbal](https://github.com/jmeiracorbal)
- **Based on**: Ghost Tracker tool

## Support

If you run into any issues or have questions:
- Create an issue on GitHub
- Check the [Releases](https://github.com/jmeiracorbal/phone-tracker/releases) page for the latest version

---

**Note**: This tool is for educational and legitimate purposes. Respect privacy and use it responsibly.
